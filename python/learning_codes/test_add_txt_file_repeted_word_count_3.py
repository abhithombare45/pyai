import re

def get_words(filename):
    with open(filename, "r") as file:
        text = file.read()
    words = re.findall(r'\b\w+\b', text)  # Extracts words
    return words

def main ():
	words = get_words("address.txt")
	print("words", "\n\n\n")
	
	# Convert words to lowercase and filter words with 3 or more characters
	lowercase_words = [word.lower() for word in words if len(word) >= 3]

	# Count occurrences of each word using a dictionary
	counts = {}

	for word in lowercase_words:
    		if word in counts:
        		counts[word] += 1  # Increment count if word already exists
    		else:
        		counts[word] = 1  # Initialize count if word is seen for the first time
	print("Word : it's count")
	for word, count in counts.items():
		if count >=3:
			print(f"{word}:  {count}")

main()
