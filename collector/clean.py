import re

# Read the text file
with open('your_text_file.txt', 'r') as file:
    text = file.read()

# Remove timestamps (various formats)
cleaned_text = re.sub(r'\d{1,2}:\d{1,2}(?::\d{1,2})?\s*(?:[APap][Mm])?\s*', '', text)

# Remove extra line breaks
cleaned_text = re.sub(r'\n+', ' ', cleaned_text)

# Remove extra spaces
cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

# Save the cleaned text to a new file
with open('cleaned_text.txt', 'w') as output_file:
    output_file.write(cleaned_text)

print("Cleaned text has been saved to 'cleaned_text.txt'")
