#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
placeholder = '[name]'
with open(r'C:\Users\Bertha\Documents\UDEMY\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt') as invited_names:
    names = invited_names.readlines()
with open(r'C:\Users\Bertha\Documents\UDEMY\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt') as starting_letter:
    letter_contents = starting_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_file = letter_contents.replace(placeholder, stripped_name)
        with open(fr'C:\Users\Bertha\Documents\UDEMY\Mail+Merge+Project+Start\Mail Merge Project Start\Output\ReadyToSend\letter_for_{stripped_name}.txt',mode="w") as completed_letter:
            completed_letter.write(new_file)