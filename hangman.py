import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        
        print("Você tem", lives, " vidas restantes e você já usou essas letras: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("Essa letra não contém na palavra.")

        elif user_letter in used_letters:
                print("Você já usou esse caractere. Por favor tente novamente.")
        else:
            print("Caracter inválido. Por favor tente novamente.")
    
    if lives == 0:
        print("Você morreu, desculpe. A palavra era", word)
    else:
        print("Você adivinhou a palavra", word, '!!')


if __name__ == '__main__':
    hangman()
