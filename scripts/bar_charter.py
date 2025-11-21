# Using 2 input tsv files, make a bar chart showing the relative abundance of each of the 7 set categories under the column "coding", contrasting the 2 files.


import pandas as pd
import matplotlib.pyplot as plt
import argparse

def load_data(file_path):
    """Load data from a TSV file into a pandas DataFrame."""
    return pd.read_csv(file_path, sep='\t')

def prepare_data(df, all_categories):
    """Prepare data for plotting by calculating relative abundances."""
    category_counts = df['coding'].value_counts(normalize=True)
    # Create a complete series with all categories, filling missing ones with 0
    category_counts = category_counts.reindex(all_categories, fill_value=0)
    # Convert to DataFrame and rename columns properly
    return pd.DataFrame({
        'category': category_counts.index,
        'relative_abundance': category_counts.values
    })

def plot_bar_chart(data1, data2, label1, label2):
    """Plot a bar chart comparing the relative abundances from two datasets."""
    merged_data = pd.merge(data1, data2, on='category', suffixes=(f'_{label1}', f'_{label2}'), how='outer')
    
    # Set up the bar chart
    x = merged_data['category']
    bar_width = 0.35
    index = range(len(x))
    
    plt.bar(index, merged_data[f'relative_abundance_{label1}'], bar_width, label=label1)
    plt.bar([i + bar_width for i in index], merged_data[f'relative_abundance_{label2}'], bar_width, label=label2)
    
    plt.xlabel('Category')
    plt.ylabel('Relative Abundance')
    plt.title('Relative Abundance of Categories')
    plt.xticks([i + bar_width / 2 for i in index], x, rotation=45, ha='right')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('/home/laurier/repos/COMP370_HW10/data/results.png')

def main():
    parser = argparse.ArgumentParser(description='Generate a bar chart comparing relative abundances from two TSV files.')
    parser.add_argument('file1', help='Path to the first TSV file')
    parser.add_argument('file2', help='Path to the second TSV file')
    parser.add_argument('--label1', default='File 1', help='Label for the first dataset')
    parser.add_argument('--label2', default='File 2', help='Label for the second dataset')
    
    args = parser.parse_args()
    
    # Load data
    df1 = load_data(args.file1)
    df2 = load_data(args.file2)
    
    # Define all possible categories
    all_categories = ['Course question/advice', 'Program question/advice', 'Logistics question/advice', 'General question/advice', 'Complaint', 'Event/Announcement/Advertisment', 'Meme/Funny Post']
    
    # Prepare data
    data1 = prepare_data(df1, all_categories)
    data2 = prepare_data(df2, all_categories)
    
    # Plot bar chart
    plot_bar_chart(data1, data2, args.label1, args.label2)

if __name__ == '__main__':
    main()