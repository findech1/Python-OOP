import json
import difflib

# Load JSON data into a Python dictionary
with open('data.json', 'r') as f:
    data = json.load(f)

# Function to get definition of a word
def get_definition(word):
    word = word.lower()  # Convert input word to lowercase
    if word in data:
        return data[word]
    else:
        suggestions = difflib.get_close_matches(word, data.keys(), n=3, cutoff=0.7)
        if suggestions:
            suggestion = suggestions[0]  # Take the most similar word as suggestion
            return f"Word not found. Did you mean '{suggestion}'?"
        else:
            return "Word not found."

# Test the function
word = input("Enter a word to get its definition: ")
definition = get_definition(word)
print(definition)
