def vigenere_encrypt(content, key):

    encrypt_arr = []
    for i in range(len(content)):                                                           # for every element given the length of input
        char = content[i]                                                                   # assign index of input to char
        if char.isupper():                                                                  # handle A-Z
            encrypt_char = chr(((ord(char) - 65) + ord(key[i % len(key)])) % 26 + 65)
            encrypt_arr.append(encrypt_char)
        elif char.islower():                                                                # handle a-z
            encrypt_char = chr(((ord(char) - 97) + ord(key[i % len(key)])) % 26 + 97)
            encrypt_arr.append(encrypt_char)
        elif char.isnumeric():                                                              # handle 0-9
            encrypt_char = chr(((ord(char) - 48) + ord(key[i % len(key)])) % 10 + 48)
            encrypt_arr.append(encrypt_char)
        else:                                                                               # handle special characters                                                
            encrypt_char = char
            encrypt_arr.append(encrypt_char)
    encrypt_string = "".join(str(x) for x in encrypt_arr)
    print(f"\nThe encrypted test is as follows: \n\n{encrypt_string}")
    return encrypt_string

def vigenere_decrypt(content, key):   
                                                                 
    decrypt_arr = []
    for i in range(len(content)):                                                           # for every element given the length of input
        char = content[i]                                                                   # assign index of input to char
        if char.isupper():                                                                  # handle A-Z
            decrypt_char = chr(((ord(char) - 65) - ord(key[i % len(key)])) % 26 + 65)
            decrypt_arr.append(decrypt_char)
        elif char.islower():                                                                # handle a-z
            decrypt_char = chr(((ord(char) - 97) - ord(key[i % len(key)])) % 26 + 97)
            decrypt_arr.append(decrypt_char)
        elif char.isnumeric():                                                              # handle 0-9
            decrypt_char = chr(((ord(char) - 48) - ord(key[i % len(key)])) % 10 + 48)
            decrypt_arr.append(decrypt_char)
        else:                                                                               # handle special characters                                                
            decrypt_char = char
            decrypt_arr.append(decrypt_char)
    decrypt_string = "".join(str(x) for x in decrypt_arr)
    print(f"\nThe decrypted test is as follows: \n\n{decrypt_string}")
    return decrypt_string

def result(txt_file,mode):                                                                  # assign mode for determining wether the method/result was encrypt or decrypt

    option = input("Save result to text file (Y/N): ")
    remove = ".txt"                                                                         # used by replace() to clean the txt file name of the new txt file

    if option.upper() == "Y":
        with open(f"{txt_file.replace(remove,"")}_cipher.txt", "w") as file:                # create new file to store cipher content
            file.write(mode)
        print(f"Result written to {txt_file.replace(remove,"")}_cipher.txt")                # show path to the created txt file
    elif option.upper() == "N": 
        pass                                                                                # exit program
    else:
        print("Invalid input, please try again.")

def get_input():

    txt_file = input("file name: ")                                                         # ask user input for txt file

    with open(txt_file, "r") as file:                                                   
        content = file.read()                                                               # read the text file and store to content

    key = input("key: ")                                                                    

    option = input("encrypt (E) or decrypt (D): ")

    if option.upper() == "E":
        result(txt_file,mode=vigenere_encrypt(content, key))
    elif option.upper() == "D":
        result(txt_file,mode=vigenere_decrypt(content, key))
    else:
        print("Invalid input, please try again.")

get_input()





