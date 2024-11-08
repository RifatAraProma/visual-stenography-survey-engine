import sqlite3
from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
import os
import random
import json
import datetime

app = Flask(__name__)

# Dictionary to store user data
user_data = {}

# Initialize the SQLite database and table if it doesn’t already exist
def init_db():
    conn = sqlite3.connect('tracker.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rotation_tracker (
                        page_number INTEGER,
                        subfolder TEXT,
                        rotation_index INTEGER,
                        PRIMARY KEY (page_number, subfolder)
                    )''')
    conn.commit()
    conn.close()

# Helper function to get current timestamp
def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Load rotation indexes from the database
def load_rotation_tracker():
    conn = sqlite3.connect('tracker.db')
    cursor = conn.cursor()
    cursor.execute("SELECT page_number, subfolder, rotation_index FROM rotation_tracker")
    tracker = {(row[0], row[1]): row[2] for row in cursor.fetchall()}
    conn.close()

    # Initialize tracker for each page and subfolder if not already in DB
    for page in range(1, 10):  # Pages 1 through 9
        for subfolder in ['trend keeper', 'replicator', 'de-noiser']:
            if (page, subfolder) not in tracker:
                tracker[(page, subfolder)] = 0
    return tracker


# Update rotation index in the database
def update_rotation_index(page_number, subfolder, index):
    conn = sqlite3.connect('tracker.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO rotation_tracker (page_number, subfolder, rotation_index) VALUES (?, ?, ?)",
                   (page_number, subfolder, index))
    conn.commit()
    conn.close()


# Initialize the database and load rotation tracker
init_db()
image_rotation_tracker = load_rotation_tracker()

# Function to retrieve images for each page
def get_images(page_number):
    base_path = os.path.join('static', 'images', f'page{page_number}')
    images = {}

    subdirs = ['reference', 'trend keeper', 'replicator', 'de-noiser']
    subdirs.remove('reference')
    random.shuffle(subdirs)
    subdirs.insert(0, 'reference')

    for subfolder in subdirs:
        image_path = os.path.join(base_path, subfolder)
        if os.path.isdir(image_path):
            image_files = [file for file in os.listdir(image_path) if file.endswith(('.svg', '.png', '.jpg', '.jpeg'))]
            if subfolder == 'reference' and image_files:
                images[subfolder] = os.path.join('images', f'page{page_number}', subfolder, image_files[0]).replace('\\', '/')
            elif image_files:
                # Get current index from the tracker, using (page_number, subfolder) as the key
                image_index = image_rotation_tracker[(page_number, subfolder)] % len(image_files)
                images[subfolder] = os.path.join('images', f'page{page_number}', subfolder, image_files[image_index]).replace('\\', '/')

                # Update rotation index for next use
                image_rotation_tracker[(page_number, subfolder)] = (image_rotation_tracker[(page_number, subfolder)] + 1) % len(image_files)
                update_rotation_index(page_number, subfolder, image_rotation_tracker[(page_number, subfolder)])

    return images


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_data['timestamps'] = {'name_entered': get_timestamp()}  # Save timestamp
        return redirect(url_for('page', page_number=1))
    return render_template('base.html')

@app.route('/page/<int:page_number>', methods=['GET', 'POST'])
def page(page_number):
    if request.method == 'POST':
        user_data[f'page_{page_number}'] = request.form.to_dict()
        if 'timestamps' not in user_data:
            user_data['timestamps'] = {}
        user_data['timestamps'][f'page_{page_number}_submitted'] = get_timestamp()

        if page_number < 9:
            return redirect(url_for('page', page_number=page_number + 1))
        else:
            return redirect(url_for('feature_rank'))
    
    images = get_images(page_number)
    return render_template('page.html', page_number=page_number, images=images)

@app.route('/feature_rank', methods=['GET', 'POST'])
def feature_rank():
    if request.method == 'POST':
        # Save the feature ranking and additional comments from the form
        user_data['feature_ranking'] = request.form.get('ranked_features')
        user_data['other_features'] = request.form.get('other_features')
        
        user_data['timestamps']['feature_rank_submitted'] = get_timestamp()
        return redirect(url_for('complete'))
    
    return render_template('feature_rank.html')

@app.route('/complete', methods=['GET', 'POST'])
def complete():
    if request.method == 'POST':
        user_data['timestamps']['complete_downloaded'] = get_timestamp()
        return save_and_download_json(user_data)

    return render_template('complete.html')

def save_and_download_json(data):
    response = Response(json.dumps(data, indent=4), mimetype='application/json')
    response.headers.set('Content-Disposition', 'attachment', filename='user_data.json')
    return response

if __name__ == '__main__':
    app.run(debug=True)
