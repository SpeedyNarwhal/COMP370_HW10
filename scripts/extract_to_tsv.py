# python3 extract_to_tsv.py -o <output_file> <json file> <num_posts_to_output>
# Outputs a TSV file with the specified number of posts from the input JSON file.

import json
import argparse
import csv

def extract_to_tsv(json_file, output_file, num_posts):
    with open(json_file, 'r') as jf:
        data = json.load(jf)

    with open(output_file, 'w', newline='') as tf:
        tsv_writer = csv.writer(tf, delimiter='\t')
        tsv_writer.writerow(['name', 'title', 'coding'])  # Header row

        posts = data['data']['children']
        for i, post in enumerate(posts):
            if i >= num_posts:
                break
            post_data = post['data']
            name = post_data.get('name', '')
            title = post_data.get('title', '')
            tsv_writer.writerow([name, title, ''])

def main():
    parser = argparse.ArgumentParser(description='Extract posts from JSON to TSV.')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output TSV file')
    parser.add_argument('json_file', type=str, help='Input JSON file')
    parser.add_argument('num_posts', type=int, help='Number of posts to output')

    args = parser.parse_args()
    extract_to_tsv(args.json_file, args.output, args.num_posts)

if __name__ == '__main__':
    main()