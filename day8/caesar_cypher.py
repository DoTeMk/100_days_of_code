from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)



def caesar_cypher(direction, text, shift):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift 
            end_text += alphabet[new_position]
    print(f"The {direction}d text is {end_text}")


answer_continue = False
while not answer_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)
    
    caesar_cypher(direction=direction, text=text, shift=shift)

    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if answer == "no":
        answer_continue = True
        print("Goodbye")