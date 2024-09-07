import pickle


import csv


def csv_to_dict(file_path):
    cnt = 0
    word_dict = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            cnt += 1
            print(row)
            if len(row) == 2:
                german, english = row
                # Remove quotes if present
                german = german.strip('"')
                english = english.strip('"')
                word_dict[german] = english

    print(cnt, len(word_dict))
    return word_dict


# Usage
file_path = 'german_english_words.csv'  # Replace with your CSV file path
german_english_dict = csv_to_dict(file_path)

# Print the first 5 items to verify
print("First 5 items in the dictionary:")
for i, (german, english) in enumerate(list(german_english_dict.items())[:5]):
    print(f"{german}: {english}")

# Print the total number of words
print(f"\nTotal words in dictionary: {len(german_english_dict)}")


s = open('dictinary', 'wb')
pickle.dump(german_english_dict, s)
s.close()
