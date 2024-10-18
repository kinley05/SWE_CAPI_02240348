import re



with open('C:/Users/tsher/Desktop/csf Assignment/dictionary.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize an empty dictionary to store words
dictionary = {}

# Step 2: Process each line to extract only Dzongkha words
for line in lines:
    # Strip leading/trailing spaces or newlines
    line = line.strip()
    
    # Use regex to keep only lines that contain Dzongkha (Tibetan script)
    # The Dzongkha words are in the Unicode range \u0F00-\u0FFF
    dzongkha_words = re.findall(r'[\u0F00-\u0FFF]+', line)

    # Skip lines with no Dzongkha words
    if dzongkha_words:
        # Join the Dzongkha words to form a clean line
        dzongkha_text = ' '.join(dzongkha_words)
        split_words = dzongkha_text.split("།")
        for word in split_words:
            word = word.strip()
            if word:
                dictionary[word] = word
 # Store the cleaned line in the dictionary as both key and value for now
        dictionary[dzongkha_text] = dzongkha_text  # Storing Dzongkha words temporarily as values

# Step 3: Save only Dzongkha words into a new file
with open('C:/Users/tsher/Desktop/csf assignment/dictionary_cleaned.txt', 'w', encoding='utf-8') as file:
    for word in dictionary.keys():
        file.write(word + '\n')

print(f"Processed {len(dictionary)} Dzongkha_word_entries.")