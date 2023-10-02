import json

def extract_data(json_data, output_file):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == "description":
                output_file.write(f"Description: {value}\n")
            elif key == "images":
                if "orig" in value:
                    output_file.write(f"Image URL (orig): {value['orig']['url']}\n")
            elif key == "pinner":
                pinner_data = value
                username = pinner_data.get("username", "N/A")
                full_name = pinner_data.get("full_name", "N/A")
                follower_count = pinner_data.get("follower_count", "N/A")
                output_file.write(f"Pinner Username: {username}\n")
                output_file.write(f"Pinner Full Name: {full_name}\n")
                output_file.write(f"Pinner Follower Count: {follower_count}\n")
            elif key == "grid_title":
                output_file.write(f"Grid Title: {value}\n")
            elif key == "domain":
                output_file.write(f"Domain: {value}\n")
            elif key == "display_description":
                output_file.write(f"Display Description: {value}\n")
            elif key == "reaction_counts":
                for reaction_key, reaction_count in value.items():
                    output_file.write(f"Reaction {reaction_key}: {reaction_count}\n")
            elif key == "link":
                output_file.write(f"Link: {value}\n")
            elif key == "id":
                output_file.write(f"ID: {value}\n")
            extract_data(value, output_file)
    elif isinstance(json_data, list):
        for item in json_data:
            extract_data(item, output_file)

# Specify the path to the JSON file containing your data
json_file_path = 'pinterest_data_158.json'

# Open the JSON file for reading
with open(json_file_path, 'r') as json_file:
    # Load the JSON data from the file into a Python data structure
    json_data = json.load(json_file)

# Open a file for writing the extracted data
output_file_path = 'extracted_data.txt'
with open(output_file_path, 'w') as output_file:
    # Call the extract_data function to parse and extract data, and write it to the output file
    extract_data(json_data, output_file)

print(f"Extracted data has been written to {output_file_path}")