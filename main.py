alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo

print(logo) # print caeser cipher ascii text logo from file "art.py"


def caeser(text, shift, direction):
    if direction == "encode": # determining whether the program shoud encode or decode
        encode= True 
        
    elif direction == "decode":
        encode = False

    final_message=""
    for letter in text: # for every character in given message
        
        if not letter.isalpha() : # if character is alphabetic continue to encode/decoding process
            final_message +=letter # if character is not part of the alphabet add it to final message and continue to next char
            continue
            
        ind = alphabet.index(letter) # find the index of the letter in the alphabet
        if encode:
            if ind + shift >25: # if shift given is over 25
                 ind = (ind +shift) %26 # find index of encrypted letter
                
            else: 
                ind+=shift # find index of encrypted letter
                
        else: # if decode
            shift%=26 # make sure shift given is under 26
            ind-=shift # find index of decrypted letter
            
        final_message +=alphabet[ind] # add encrypted/decrypted letter to final message
        
    print(f"The {direction}d text is {final_message}.") # when loop is finished iterating through every character print completed final message

def direction_check(direct): # a method to make sure the direction being inputted is "encode" or "decode"
    while (direct != 'encode') and (direct != 'decode'): # enter the loop and remain in it if direct is not 'encode' or 'decode'
        print(f"\nSorry, we did not understand your message '{direct}'. Please try again.\n")
        direct = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  
    return direct

def shift_check(shaft): # a method to ensure the shift being inputted is valid
    while not shaft.isnumeric(): # enter and remain in loop if shift is not valid
        print("\nSorry, your inputted shift was not a number. Please try again.\n")
        shaft = input("Type the shift number:\n") # take the desired shift from input
    return int(shaft) # return the shift as an integer when given shift is valid

question = 'yes' # enter in to while loop 

while question == 'yes': # while loop to repeat process as long as user desires

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") # get direction from input
    start_direction = direction_check(direction) # confirm given direction is valid and assign it to start_direction
    
    start_text = input("Type your message:\n").lower() # take the desired message from input
    
    shift = input("Type the shift number:\n") # take the desired shift from input
    start_shift = shift_check(shaft = shift) # assign start_shift to a shift that is a verified number (the return of shift_check)
        
    caeser(text = start_text, shift = start_shift, direction = start_direction) # call caeser once the text shift and direction are known
    question = input("Type 'yes' if you want to encode or decode again. Otherwise type 'no' or anything else.\n") 
