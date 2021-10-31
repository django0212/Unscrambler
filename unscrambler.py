import requests
import itertools
import time

print("--UNSCRAMBLER--")

#wordlist_whole = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
#wordlist = wordlist_whole.text.split('\n')

def again():
    chc = input("Again [Y/n]? ")
    
    if chc.lower() == "y":
        main()
    elif chc.lower() == "n":
        exit()
    else:
        print("Please enter valid option. Retry in 5 seconds.")
        time.sleep(5)
        again()

def main():
    scrambled_word = input("Enter scrambled word: ")

    combinations = [comb for comb in itertools.permutations(scrambled_word, len(scrambled_word))]

    wordList = []

    for i in combinations:
        word = ''.join(i)
        response = requests.get(f'https://en.wiktionary.org/wiki/{word}')
        if response.status_code == 200:
            wordList.append(word)

    #wordList = set(wordList)

    for j in set(wordList):
        print(j)
        
    again()

main()
