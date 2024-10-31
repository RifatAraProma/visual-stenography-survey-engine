import os

# Directories to process (page1 to page9)
base_dir = 'C:/Users/rifat/OneDrive/Documents/Research/Temporal data/Visual Stenography Survey/survey-engine/static/images'  # Adjust this path to your actual output directory
pages = [f'page{i}' for i in range(1, 10)]

# The SVG replacement tag
new_svg_tag = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" class="marks" width="1012" height="385" viewBox="0 0 1012 385"><rect width="1012" height="385" fill="white"/>'

# Function to replace the first <svg> tag in a file
def replace_svg_tag(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace the first occurrence of the <svg ...> tag
        if content.startswith('<svg'):
            start_index = content.find('>') + 1
            if start_index > 0:
                # Replace the first <svg> tag
                content = new_svg_tag + content[start_index:]

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated SVG file: {file_path}")

    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

# Iterate through page directories
for page in pages:
    page_dir = os.path.join(base_dir, page)
    
    # Iterate through subdirectories (except reference)
    for subfolder in ['overwhelmed', 'replicator', 'trend keeper']:
        subfolder_path = os.path.join(page_dir, subfolder)

        if os.path.isdir(subfolder_path):
            # Iterate over all SVG files in the subdirectory
            for file_name in os.listdir(subfolder_path):
                if file_name.endswith('.png'):
                    file_path = os.path.join(subfolder_path, file_name)
                    replace_svg_tag(file_path)

print("Processing complete.")
