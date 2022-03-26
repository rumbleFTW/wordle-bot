#importing stuff 

from data import *


def frequency(dB):                                                                      #calculating the frequency of letters
        freq = {'a': 0,
                'b': 0,
                'c': 0,
                'd': 0,
                'e': 0,
                'f': 0,
                'g': 0,
                'h': 0,
                'i': 0,
                'j': 0,
                'k': 0,
                'l': 0,
                'm': 0,
                'n': 0,
                'o': 0,
                'p': 0,
                'q': 0,
                'r': 0,
                's': 0,
                't': 0,
                'u': 0,
                'v': 0,
                'w': 0,
                'x': 0,
                'y': 0,
                'z': 0,}
        for word in dB:
                for letter in word:
                        freq[letter] += 1
        return freq

def evaluate(f):                                                                        #assigning weights to letters
        ev = {'a': 0,
                'b': 0,
                'c': 0,
                'd': 0,
                'e': 0,
                'f': 0,
                'g': 0,
                'h': 0,
                'i': 0,
                'j': 0,
                'k': 0,
                'l': 0,
                'm': 0,
                'n': 0,
                'o': 0,
                'p': 0,
                'q': 0,
                'r': 0,
                's': 0,
                't': 0,
                'u': 0,
                'v': 0,
                'w': 0,
                'x': 0,
                'y': 0,
                'z': 0,}
        total = sum(f.values())
        for letter in ev:
                ev[letter] = f[letter]/total
        return ev

def bestChoice(dB, e):                                                                  #finding the most probable word
        maxScore = 0
        bestStr = ''
        for item in dB:
                score = 0
                wrd = set(i for i in item)
                for letter in wrd:
                        score += e[letter]
                if(score > maxScore):
                        maxScore = score
                        bestStr = item
        return bestStr