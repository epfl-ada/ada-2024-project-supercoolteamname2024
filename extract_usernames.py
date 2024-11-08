import re

# Replace 'filename.txt' with the path to your text file
filename = 'wiki-RfA.txt'
output_file = 'usernames.txt'

# Define a list to store all SRC values
src_entries = []

# Open and read the input file
with open(filename, 'r') as file:
    for line in file:
        # Use regex to match lines that start with SRC
        match = re.match(r'SRC:(\S+)', line)
        if match:
            src_entries.append(match.group(1))

# Write all SRC entries to the output file
with open(output_file, 'w') as file:
    for src in src_entries:
        file.write(src + '\n')

print(f"Extracted SRC entries have been written to {output_file}")
