import os
import shutil

# Base input directories (adjust paths as needed)
clusters_dir = 'C:/Users/rifat/OneDrive/Documents/Research/Temporal data/What Do People see in Line Charts GitHub/Follow Up User Evaluation Design/Qualitative Analysis/Clusters/Combined'
input_dir = 'C:/Users/rifat/OneDrive/Documents/Research/Temporal data/What Do People see in Line Charts GitHub/User Evaluation Results'  # Directory with original datasets
output_dir = 'C:/Users/rifat/OneDrive/Documents/Research/Temporal data/Visual Stenography Survey/vsse/static/images'  # Directory with page1..page9

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

# Dictionary to map dataset names (for handling variations in naming)
dataset_name_mapping = {
    'Apple': 'apple',
    'Astro': 'astro',
    'Chi Homicide Monthly': 'chi',
    'Climate': 'climate',
    'Doge': 'doge',
    'EEG': 'eeg',
    'Flights Weekly': 'flights',
    'NZ Tourist Monthly': 'nz',
    'Unemployment': 'unemployment'
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

# List of cluster types
cluster_types = ['replicator', 'de-noiser', 'trend keeper']

# Function to find matching PNG and copy corresponding SVG
def process_clusters_for_dataset(dataset, dataset_dir_name):
    for cluster in cluster_types:
        cluster_path = os.path.join(clusters_dir, cluster)

        # Loop through the PNG files in the cluster folder
        for png_file in os.listdir(cluster_path):
            if png_file.endswith('.png') and dataset_name_mapping[dataset] in png_file and noise_levels[dataset] in png_file:
                # Extract noise level and round number from PNG file name
                parts = png_file.split('_')
                if len(parts) >= 4:
                    round_number = parts[3].replace('.png', '')  # Round number (e.g., 1)
                    source_svg_dir = os.path.join(input_dir, f'User Evaluation Round {round_number}', 'Drawings Categorize by dataset', f'{dataset}')
                    matching_svg_file = None

                    # Search for the corresponding SVG file with the same noise level and round number
                    for svg_file in os.listdir(source_svg_dir):
                        if noise_levels[dataset] in svg_file and svg_file.endswith('.svg'):
                            matching_svg_file = svg_file
                            break

                    if matching_svg_file:
                        # Construct the output path
                        output_cluster_dir = os.path.join(output_dir, dataset_to_page[dataset], cluster)
                        os.makedirs(output_cluster_dir, exist_ok=True)  # Ensure the output directory exists
                        file_name = matching_svg_file.replace('.svg', '')
                        output_file_path = os.path.join(output_cluster_dir, f'{file_name}_{round_number}.svg')

                        # Copy the SVG file to the output directory
                        shutil.copy(os.path.join(source_svg_dir, matching_svg_file), output_file_path)
                        print(f"Copied {matching_svg_file} to {output_file_path}")
                    else:
                        print(f"No matching SVG found for {png_file} in dataset {dataset}")
                else:
                    print(f"Invalid PNG file format: {png_file}")

# Process each dataset
for dataset, dataset_dir_name in dataset_name_mapping.items():
    process_clusters_for_dataset(dataset, dataset_dir_name)

print("Processing completed.")
