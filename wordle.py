import pandas as pd
import emoji

def loadwordle():
    wordlist = pd.read_csv("./wordlelist.csv", header = None, names = ["Word"])
    wordlist = wordlist["Word"].str.lower()
    wordlist = pd.DataFrame(wordlist)
    return wordlist

def getcurrentword(wordlist):
    now = pd.Timestamp.today()
    start = pd.Timestamp(2022, 3, 14) # start of s1 wk3
    # want to do 'if n multiple of x hours has passed, use wordlist[n]'
    nowhours = now.day_of_year * 24 + now.hour
    starthours = start.day_of_year * 24 + start.hour
    hourspassed = nowhours - starthours
    wordindex = (hourspassed // 6) % len(wordlist)
    currentword = wordlist["Word"][wordindex]
    return currentword

def checkguess(currentword, input):
    guess = str(input).lower()
    if len(guess) != 5:
        return "Your guess doesn't have the right number of letters! The mystery word has five letters."
    wordletters = []
    output = []
    for i in range(len(currentword)):
        wordletters.append(currentword[i])
    for i in range(len(guess)):
        if any(letter in guess[i] for letter in wordletters[i]):
            output.append(emoji.emojize(":green_square:"))
        elif any(letter in guess[i] for letter in wordletters):
            output.append(emoji.emojize(":yellow_square:"))
        else:
            output.append(emoji.emojize(":black_large_square:"))
    output = " ".join(output)
    if output == emoji.emojize(":green_square: :green_square: :green_square: :green_square: :green_square:"):
        return "You did it! The word refreshes every six hours - see you again soon!"
    return output
