#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Paths
names_path = BASE_DIR / "Input" / "Names" / "invited_names.txt"
letter_path = BASE_DIR / "Input" / "Letters" / "starting_letter.txt"
output_path = BASE_DIR / "Output" / "ReadyToSend"

# Read the letter template
with open(letter_path) as letter_file:
    letter_contents = letter_file.read()

# Read all names
with open(names_path) as names_file:
    names = names_file.readlines()

# Create personalised letters
for name in names:
    stripped_name = name.strip()

    new_letter = letter_contents.replace("[name]", stripped_name)

    with open(output_path / f"letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)