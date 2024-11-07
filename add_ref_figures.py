import os
import shutil

# Define the base input directory (where your folders like 'Apple', 'Astro', etc. are located)
input_dir = 'C:/Users/rifat/OneDrive/Documents/Research/Temporal data/What Do People see in Line Charts GitHub/User Evaluation Design/stimuli organized by dataset'

# Define the base output directory (where 'page1', 'page2', etc. are located)
output_dir = './static/images'

# Define noise level selection for each dataset
noise_levels = {
    'Apple': 'mid',
    'Astro': 'high',
    'Chi Homicide Monthly': 'high',
    'Climate': 'max',
    'Doge': 'high',
    'EEG': 'low',
    'Flights Weekly': 'mid',
    'NZ Tourist Monthly': 'max', 
    'Unemployment': 'max'    
}

# Define the mapping of datasets to pages (Apple -> page1, Astro -> page2, etc.)
dataset_to_page = {
    'Apple': 'page1',
    'Astro': 'page2',
    'Chi Homicide Monthly': 'page3',
    'Climate': 'page4',
    'Doge': 'page5',
    'EEG': 'page6',
    'Flights Weekly': 'page7',
    'NZ Tourist Monthly': 'page8',
    'Unemployment': 'page9'
}

# Loop through each dataset
for dataset, noise_level in noise_levels.items():
    # Define the directory where the files are located for the current dataset
    dataset_dir = os.path.join(input_dir, dataset)

    # Check if the dataset directory exists
    if not os.path.exists(dataset_dir):
        print(f"Directory not found: {dataset_dir}")
        continue

    # Look for the file with the correct noise level
    selected_file = None
    for file_name in os.listdir(dataset_dir):
        # Check if the noise level is part of the file name and the file ends with .svg
        if noise_level in file_name and file_name.endswith('.svg'):
            selected_file = file_name
            break

    # If no file was found, continue to the next dataset
    if not selected_file:
        print(f"No file found with noise level '{noise_level}' in {dataset}")
        continue

    # Construct the full path to the selected input file
    input_file_path = os.path.join(dataset_dir, selected_file)

    # Get the corresponding page directory
    page_dir = os.path.join(output_dir, dataset_to_page[dataset], 'reference')

    # Create the output directory if it doesn't exist
    os.makedirs(page_dir, exist_ok=True)

    # Construct the full path for the output file
    output_file_path = os.path.join(page_dir, selected_file)

    # Copy the file to the output directory
    shutil.copy(input_file_path, output_file_path)
    print(f"Copied {input_file_path} to {output_file_path}")

print("File copying completed.")
