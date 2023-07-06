
import pathlib
import random
from string import ascii_letters
import requests
import keys #.py file containing the API key (hidden)

from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

word = ""
length = 0

def get_random_word(length):
    url = f"https://random-word-api.herokuapp.com/word?length={str(length)}"
    response = requests.get(url)
    data = response.json()  # Convert the response to JSON

    word = "".join(data).upper()  # Convert the list to a string, and then to uppercase 
    
    return word

def check_if_word(guess): #some problem with this
    #url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={keys.DICTIONARY_KEY}"
    #response = requests.get(url)
    #data = response.json()
    
    #if isinstance(data, list):
        # Check if the response contains alternative words
    #    for item in data:
    #        if 'meta' in item and item['meta'].get('id', '') == word:
    #            return True
    #    return False
    #else:
        # The response does not contain alternative words
    #    return False
    return True
    


def show_guesses(guesses, word):
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")

        console.print("".join(styled_guess), justify="center")

def game_end(word):
    print(f"The word was:{word}\n")



def main():
# Pre-process
  #get length from user
  length = int(input("\nWhat length would you like your word to be? "))                               

  #get a random word through function + API
  word = get_random_word(length)

  #for checking purposes 
  #print(word)  # Output: some {length} letter string

# Process (main loop)
  for guess_num in range(1, length+2):
    guess = input(f"\nGuess {guess_num}: ").upper()

    while not check_if_word(guess):
      guess = input(f"Invalid guess, not a word. Guess {guess_num}: ").upper() #uses an API to check if the guess is a word 
        

    if guess == word:
        print("\nCorrect\n\n")
        break

    show_guesses(guess,word)

# Post-process
  else:
    game_end(word)


if __name__ == "__main__":
    main()
    
