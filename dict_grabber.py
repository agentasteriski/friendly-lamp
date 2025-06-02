import pandas as pd

# Step 1: Read transcriptions.csv
csv_file_path = 'transcriptions.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Extract unique values from the ph_seq column
unique_values_set = set()  # Using a set to ensure uniqueness
for value in df['ph_seq']:
    unique_values_set.update(value.split())
unique_values = sorted(unique_values_set)

# Step 3: Write the unique values to a text file
output_file_path = 'unique_phonemes.txt'
with open(output_file_path, 'w') as f:
    for value in unique_values:
        f.write(value + '\n')

print(f"Phonemes have been written to {output_file_path}")
