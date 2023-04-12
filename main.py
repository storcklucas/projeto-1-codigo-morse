# unicode para retirar a acentuacao #
from unidecode import unidecode

morse_table = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}
key_list = list(morse_table.keys())
val_list = list(morse_table.values())
cont = True


while cont:
    choice = input("Entre '1' para converter codigo morse para frase e '2' para converter frase para codigo morse.")

    if choice == "1":
        morse_code = input("Digite o codigo morse para converter para frase.")
        split_morse = morse_code.split(" ")
        list_2 = []
        for symbol in split_morse:
            position = val_list.index(symbol)
            list_2.append(key_list[position])
        print("".join(list_2))
        cont = False


    elif choice == "2":
        phrase = unidecode(input("Digite a frase para converter para codigo morse.").upper())
        list = []

        for letter in phrase:
            list.append(morse_table[letter])

        print(" ".join(list))
        cont = False


    else:
        print("Digite a opcao correta.")


