#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def read_names():
    with open("./Input/Names/invited_names.txt", "r") as file:
        return file.readlines()

def read_starting_letter():
    with open("./Input/Letters/starting_letter.txt", "r") as letter_template:
        content = letter_template.read()
        return content

def update_letter(content, guest):
    return content.replace("[name]", guest)

def send_letter(message, guest):
    with open(f"./Output/ReadyToSend/letter_for_{guest}.txt", "w") as invite:
        invite.write(message)


all_names = read_names()

for name in all_names:
    name = name.strip()
    old_message = read_starting_letter()
    new_message = update_letter(old_message, name)
    send_letter(new_message, name)
    print(f"Invitation sent to {name}")
