from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesarCipher(text, shift, direction):
    resultText = ""
    for letter in text:
        if letter in alphabet:
            textIndex = alphabet.index(letter)
            if direction == "encode":
                resultPosition = textIndex+shift
                if resultPosition >= len(alphabet):
                    resultPosition -= len(alphabet)
                resultText += alphabet[resultPosition]
            elif direction == "decode":
                resultPosition = textIndex-shift
                if resultPosition <= -1:
                    resultPosition += len(alphabet)
                resultText += alphabet[resultPosition]
        else:
            resultText += letter
    print(f"The {direction}d text is {resultText}")

continueProgram = True
while continueProgram:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesarCipher(text, shift, direction)

    wantToContinue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if wantToContinue == "no":
        continueProgram = False
        print("Goodbye")