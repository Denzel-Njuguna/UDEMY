logo = '''
      _       _               
     (_)     | |              
 ___ _ _ __  | |__   ___ _ __  
/  __| | '_ \| '_ \ / _ \ '__| 
| (__| | |_) | | | |  __/ |    
 \___|_| .__/|_| |_|\___|_|    
        | |                    
        |_|
    
        '''
encoded_data = []
decoded_data = []
letters= [chr(i) for i in range(ord('a'),ord("z")+1)]
Letters = letters
def encode():
    encode_info = input("please enter the information you would like to encode \n").lower()
    times_over = int(input("enter the encoding value\n"))
    for each in encode_info:
        if each in letters:
            each_index = [index for index, letter in enumerate(letters) if letter == each]
            encoded_index = (each_index[0] + times_over)% 26
            encoded_letter = letters[encoded_index]
            encoded_data.append(encoded_letter)
        else:
            encoded_data.append(each)
    return ''.join(encoded_data)
        

def decode():
    decode_info = input("please enter the information you would like to decode \n").lower()
    times_under = int(input("enter the decoding value \n"))
    for each in decode_info:
        if each in letters:
            #enumerate gives the letter and its index in list letters so the first index finds the index of the letter(each) that matches to the value of letter
            each_index = [index for index, letter in enumerate(letters) if letter == each]
            decoded_index = (each_index[0]-times_under)
            if decoded_index == 0:
                decoded_index = 26
            elif decoded_index < 0:
                decoded_index = 26- abs(decoded_index)
            decoded_value = letters[decoded_index]
            decoded_data.append(decoded_value)
        else:
            decoded_data.append(each)
    return ''.join(decoded_data)
def action(logo,):
    user_choice = input(f"welcome to a ceaser's\n {logo}\n would you like to \"encode\" or would you like to \"decode\" \n").lower()
    if user_choice == "encode":
        encoded_message = encode()
        print(encoded_message)
    elif user_choice == "decode":
        decoded_message = decode()
        print(decoded_message)
    else:
        print("invalid choice")
        
if __name__ =="__main__":
    try:
        action(logo)
    except KeyboardInterrupt:
        print("the user has opted out")