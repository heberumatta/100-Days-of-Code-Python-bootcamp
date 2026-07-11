from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_flag = True

def cipher(text, shift, selection):
    output_text = ""
    if selection == 'd':
        shift *= -1
    for char in text:
        if char in alphabet:
            index = (alphabet.index(char) + shift)%27
            output_text += alphabet[index]
        else:
            output_text += char
    print(f"The result is: {output_text}")

print(logo)
input("Press Enter to continue...")

while continue_flag:
    
    while selection := input("Enter 'd' for decode or 'e' for encode: ") not in ['e', 'd']:
        print("Please enter one of the following options!!")
    text = input("Enter the text to be encrypted: ").lower()
    shift = int(input("Enter the shift number: "))

    cipher(text, shift, selection)

    if input("Do you want to encode or decode again?(y)") == "y":
        continue_flag = True
    else:
        continue_flag = False
