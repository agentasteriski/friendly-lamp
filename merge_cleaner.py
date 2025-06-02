import yaml

# Load the content of the YAML file
with open('merged.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)

# Define the prefixes you want to remove
prefixes_to_remove = ['es/', 'zh/', 'fr/', 'ko/', 'th/']

# Filter out entries beginning with the specified prefixes
filtered_data = []
for phoneme_group in data['merged_phoneme_groups']:
    filtered_group = [phoneme for phoneme in phoneme_group if not any(phoneme.startswith(prefix) for prefix in prefixes_to_remove)]
    # Only add the group if it has more than one entry after filtering
    if len(filtered_group) > 1:
        filtered_data.append(filtered_group)

# Update the data with the filtered entries
data['merged_phoneme_groups'] = filtered_data

# Save the updated content to a new YAML file
with open('merge_updated.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data, file, default_flow_style=False)
