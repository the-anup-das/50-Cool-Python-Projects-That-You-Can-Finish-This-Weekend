alphabet = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f"Here's the {direction}d result: {end_text}")

def encode(message, shift):
    encoded_text = ""
    for i in message:

        if i in alphabet:
            position = alphabet.index(i)
            encode_position = position + shift
            encoded_text += alphabet[encode_position]
        else:
            encoded_text += i    
    return encoded_text

def decode(message, shift):
    decoded_text = ""
    for i in message:
        if i in alphabet:
            encode_position = alphabet.index(i)
            actual_position = encode_position - shift
            decoded_text += alphabet[actual_position]
        else:
            decoded_text += i
    
    return decoded_text

print(logo)

FLAG_END = False

while not FLAG_END:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    message = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    
    #if the user enters the shift number more than 45 
    shift = shift % 26

    if choice == "encode":
        print(f"The encoded text is '{encode(message,shift)}'")
    elif choice == "decode":
        print(f"The decoded text is '{decode(message,shift)}'")
    else:
        print("Check your input")

    user_response = input("Type 'yes' if you want to restart. Otherwise type 'no'. \n").lower()
    if user_response == "no":
        FLAG_END = True
        print("bye")
