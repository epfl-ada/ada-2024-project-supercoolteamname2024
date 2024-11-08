import re
from collections import defaultdict
import matplotlib.pyplot as plt

# Replace 'filename.txt' with the path to your text file
filename = 'wiki-RfA.txt'
output_file_stats = 'user_votes_stats.txt'
output_file_usernames = 'usernames.txt'

# Dictionary to store vote counts for each user and a set for unique usernames
vote_counts = defaultdict(int)
unique_src_entries = set()

# Temporary storage for current entry data
current_user = None
current_votes = None

print("Starting to read and parse the file...\n")

# Open and read the input file line by line
with open(filename, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        # Strip any extra whitespace from the line
        line = line.strip()
        
        # Check if line contains SRC and capture the user
        src_match = re.search(r'SRC:(\S+)', line)
        if src_match:
            current_user = src_match.group(1)
            unique_src_entries.add(current_user)  # Add user to the set of unique usernames
            
        # Check if line contains VOT and capture the votes
        vot_match = re.search(r'VOT:(\d+)', line)
        if vot_match:
            current_votes = int(vot_match.group(1))

        # If we have both current_user and current_votes, add to vote counts
        if current_user and current_votes is not None:
            vote_counts[current_user] += current_votes

            # Reset for next entry
            current_user = None
            current_votes = None

# Calculate the total number of votes
total_votes = sum(vote_counts.values())
print(f"\nTotal number of votes cast: {total_votes}")

# Sort vote counts in descending order
sorted_votes = sorted(vote_counts.values(), reverse=True)

# Write vote counts for each user to the stats output file
with open(output_file_stats, 'w') as file:
    for user, votes in vote_counts.items():
        file.write(f"{user}: {votes} votes\n")

# Write all unique SRC entries to the usernames output file
with open(output_file_usernames, 'w') as file:
    for src in sorted(unique_src_entries):  # Optional: sort usernames alphabetically
        file.write(src + '\n')

print(f"\nUnique SRC entries have been written to {output_file_usernames}")
print(f"Vote statistics have been written to {output_file_stats}")

# Plot as histogram
plt.figure(figsize=(10, 6))
plt.hist(sorted_votes, bins=20, edgecolor='black', alpha=0.7)
plt.xlabel("Number of Votes Cast")
plt.ylabel("Frequency")
plt.title("Histogram of Votes Cast by Users (Sorted)")

plt.show()

