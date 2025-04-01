import re
import argparse
from collections import Counter


bad_words = {"from", "is", "and", "a", "an", "in", "on", "to", "of", "for", "with", "at", "by", "the", "that", "this", "it"}

def clean_text_func(text):
    return re.sub(r"[^\w\s]", "", text.lower())

def analyze_text_func(file_path):
 
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
       

        words = clean_text_func(text).split()
        filtered_words = [word for word in words if word not in bad_words]
        total_words = len(filtered_words)

        word_counts = Counter(filtered_words)
        most_common_words = word_counts.most_common(5)

        total_chars = sum(len(word) for word in filtered_words)
        avg_word_length = total_chars / total_words if total_words > 0 else 0

        sentences = re.split(r'[.!?]', text)
        total_sentences = len([s for s in sentences if s.strip()])

        
        print("\n File Analysis Report ")
        print(f"Total Words (excluding stop words): {total_words}")
        print("Top 5 Most Frequent Words:")
        for word, count in most_common_words:
            print(f"  - {word}: {count} times")
        print(f"Average Word Length: {avg_word_length:.2f} characters")
        print(f"Total Sentences: {total_sentences}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="File Analyzer CLI Tool")
    parser.add_argument("file", help="Path to the .txt file")
    
    args = parser.parse_args()
    analyze_text_func(args.file)

if __name__ == "__main__":
    main()
