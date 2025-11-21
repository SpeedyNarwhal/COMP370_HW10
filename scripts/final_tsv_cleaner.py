# keep only columns 1, 2 and 8 from input tsv file and save it to the same file

import argparse
import csv
import os

def clean_tsv(input_file):
    temp_file = input_file + '.tmp'
    
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(temp_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile, delimiter='\t')
        
        for row in reader:
            if len(row) >= 8:
                new_row = [row[0], row[1], row[7]]
                writer.writerow(new_row)

def main():
    parser = argparse.ArgumentParser(description='Clean TSV file by keeping only specific columns.')
    parser.add_argument('input_file', type=str, help='Path to the input TSV file')
    
    args = parser.parse_args()
    
    clean_tsv(args.input_file)
    
    # Replace original file with cleaned file
    os.replace(args.input_file + '.tmp', args.input_file)

if __name__ == '__main__':
    main()