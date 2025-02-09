import re

def get_words(filename):
    with open(filename, "r") as file:
        text = file.read()
    words = re.findall(r'\b\w+\b', text)  # Extracts words
    return words

def main():
	words = get_words("address.txt")
	print(words)
	#lowercase_words = [words.lower() for word in words if len(word) >= 4]
	lowercase_words = [word.lower() for word in words if len(word) >= 4]
	counts = {word: words.count(word) for word in words}
	
	for key, value in counts.item(): 
		print(key, value )

main()
