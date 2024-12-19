import re
from collections import defaultdict
import matplotlib.pyplot as plt

# change 'filename.txt' to where ur text file is
filename = '../../data/wiki-RfA.txt'
output_file_stats = '../../data/user_votes_stats.txt'
output_file_usernames = '../../data/usernames.txt'

# keep track of votes per user and unique usernames
vote_counts = defaultdict(int)
unique_src_entries = set()

# temp storage for the current user and votes
current_user = None
current_votes = None

print("Ok, let's start reading the file...\n")

# open the file and read it line by line
with open(filename, 'r', encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        # strip extra spaces or whatever
        line = line.strip()
        
        # look for SRC and get the username
        src_match = re.search(r'SRC:(\S+)', line)
        if src_match:
            current_user = src_match.group(1)
            unique_src_entries.add(current_user)  # add to the list of usernames
            
        # look for VOT and get the votes
        vot_match = re.search(r'VOT:(\d+)', line)
        if vot_match:
            current_votes = int(vot_match.group(1))

        # when we have both user and votes, count it
        if current_user and current_votes is not None:
            vote_counts[current_user] += current_votes

            # clear the vars for the next round
            current_user = None
            current_votes = None

# total up all the votes
total_votes = sum(vote_counts.values())
print(f"\nTotal votes cast: {total_votes}")

# sort votes biggest to smallest
sorted_votes = sorted(vote_counts.values(), reverse=True)

# write vote counts to a file
with open(output_file_stats, 'w', encoding="utf-8") as file:
    for user, votes in vote_counts.items():
        file.write(f"{user}: {votes} votes\n")

# write unique SRC usernames to another file
with open(output_file_usernames, 'w', encoding="utf-8") as file:
    for src in sorted(unique_src_entries):  # sorting not needed
        file.write(src + '\n')

print(f"\nSaved all SRC usernames to {output_file_usernames}")
print(f"Wrote user vote stats to {output_file_stats}")

# show a histogram for the votes
plt.figure(figsize=(10, 6))
plt.hist(sorted_votes, bins=20, edgecolor='black', alpha=0.7)
plt.xlabel("Number of votes")
plt.ylabel("How often it happened")
plt.title("Histogram of votes cast by users (sorted)")

plt.show()
