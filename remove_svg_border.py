import os

# Directories to process (page1 to page9)
base_dir = 'C:/Users/rifat/OneDrive/Documents/Research/Temporal data/Visual Stenography Survey/survey-engine/static/images'  # Adjust this path to your actual output directory
pages = [f'page{i}' for i in range(1, 10)]

# The stroke patterns to remove
strokes_to_remove = ['stroke="#ddd"', 'stroke="#888"']

# Function to remove stroke attributes from a file
def remove_stroke(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove each stroke pattern from the file content
        for stroke in strokes_to_remove:
            content = content.replace(stroke, '')

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated SVG file: {file_path}")

    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

# Iterate through page directories
for page in pages:
    reference_dir = os.path.join(base_dir, page, 'reference')

    if os.path.isdir(reference_dir):
        # Iterate over all SVG files in the reference subdirectory
        for file_name in os.listdir(reference_dir):
            if file_name.endswith('.svg'):
                file_path = os.path.join(reference_dir, file_name)
                remove_stroke(file_path)

print("Processing complete.")
