from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import random

app = Flask(__name__)

# Dictionary to store user data
user_data = {}

def get_images(page_number):
    base_path = os.path.join('static', 'images', f'page{page_number}')
    images = {}

    subdirs = ['reference', 'overwhelmed', 'replicator', 'trend keeper']

    # Shuffle the subdirectories except for 'reference'
    subdirs.remove('reference')
    random.shuffle(subdirs)
    subdirs.insert(0, 'reference')  # Ensure 'reference' is always first

    for subfolder in subdirs:
        image_path = os.path.join(base_path, subfolder)
        if os.path.isdir(image_path):
            for file in os.listdir(image_path):
                if file.endswith(('.svg', '.png', '.jpg', '.jpeg')):
                    # Normalize path to use forward slashes
                    images[subfolder] = os.path.join('images', f'page{page_number}', subfolder, file).replace('\\', '/')
                    break
    print(images)
    return images

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        user_data['name'] = name
        return redirect(url_for('page', page_number=1))
    return render_template('base.html')

@app.route('/page/<int:page_number>', methods=['GET', 'POST'])
def page(page_number):
    if request.method == 'POST':
        user_data[f'page_{page_number}'] = request.form.to_dict()

        if page_number < 9:
            return redirect(url_for('page', page_number=page_number + 1))
        else:
            return redirect(url_for('complete'))
    
    images = get_images(page_number)
    return render_template('page.html', page_number=page_number, images=images)

@app.route('/complete', methods=['GET', 'POST'])
def complete():
    if request.method == 'POST':
        return save_and_download_json(user_data)

    return render_template('complete.html')

def save_and_download_json(data):
    import json
    from flask import Response

    response = Response(json.dumps(data, indent=4), mimetype='application/json')
    response.headers.set('Content-Disposition', 'attachment', filename='user_data.json')
    return response

if __name__ == '__main__':
    app.run(debug=True)
