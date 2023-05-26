from morse_dict import decode

def translate(word: str) -> list:
    morse_list = []
    for letter in word:
        for key, val in decode.items(): 
            if val == letter: morse_list.append(key)
    return morse_list
    
    
if __name__ == '__main__':
    word_to_morse = input("Enter a word to translate: ").upper()
    morse_code = translate(word_to_morse)

    for i in range(len(morse_code)):
        print(f"{word_to_morse[i]} is {morse_code[i]}")