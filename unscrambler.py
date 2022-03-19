from requests import get
from itertools import permutations
from time import sleep

print("--UNSCRAMBLER--")

#wordlist_whole = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
#wordlist = wordlist_whole.text.split('\n')

def again():
    chc = input("Again [y/n]? ")
    
    if chc.lower().strip() == "y":
        main()
    elif chc.lower().strip() == "n":
        exit()
    else:
        print("Please enter valid option. Retry in 5 seconds.")
        sleep(5)
        again()

def main():
    scrambled_word = input("Enter scrambled word: ")

    combinations = [comb for comb in permutations(scrambled_word, len(scrambled_word))]

    wordList = []

    for i in combinations:
        word = ''.join(i)
        response = get(f'https://en.wiktionary.org/wiki/{word}')
        if response.status_code == 200:
            wordList.append(word)

    #wordList = set(wordList)

    for j in set(wordList):
        print(j)
        
    again()

main()
