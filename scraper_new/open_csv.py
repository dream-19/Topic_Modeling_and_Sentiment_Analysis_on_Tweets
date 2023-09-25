import os
import csv
import re

def read_csv(relative_path):
    all_files = []
    tot_tweets = 0
    tot_tweets_without_repost = 0
    num_files = 0
    # Iterate through all files in the directory
    for filename in os.listdir(relative_path):
        # Construct the full file path
        file_path = os.path.join(relative_path, filename)
        all_files.append(file_path)
        
        # Check if the file is a regular file (not a subdirectory)
        if os.path.isfile(file_path):
            # Determine the file type based on the file extension
            file_extension = os.path.splitext(filename)[1].lower()
                    
            if file_extension == '.csv':
                row_count = 0
                row_without_repost = 0
                with open(file_path, 'r') as csv_file:
                    first_row = None
                    last_row = None
                    csv_file.readline() #index
                    csv_reader = csv.reader(csv_file)
                    
                    for row in csv_reader:
                        text = row[2]
                        #conto le righe senza repost doppi
                        if not(re.match(r'^RT', text)):
                            row_without_repost += 1
                            
                        if first_row is None:
                            first_row = row
                        row_count += 1
                        last_row = row
                    print("Dimensione file",filename, ":  ", row_count, ", senza repost:",row_without_repost,"date da: ", last_row[1].split()[0], "a: ", first_row[1].split()[0])
                    tot_tweets += row_count
                    tot_tweets_without_repost += row_without_repost
                    num_files += 1
                    
    print("\nTotale tweet: ", tot_tweets, "per totale file: ", num_files)
    print("Totale tweet senza repost: ", tot_tweets_without_repost, "per totale file: ", num_files)
    return all_files

if __name__ == '__main__':
    read_csv('./files')