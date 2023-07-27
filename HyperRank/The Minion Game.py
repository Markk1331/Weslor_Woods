def minion_game(string):
    vowel = 0
    consonant = 0
    for i in range(len(string)):
        if string[i] in ['A','E','I','O','U','a','e','i','o','u']:
            vowel = vowel + len(string)-i
        else:
            consonant = consonant + len(string)-i
    if consonant > vowel:
        print("Stuart", consonant)
    elif consonant == vowel:
        print("Draw")
    else:
        print("Kevin", vowel)

if __name__ == '__main__':
    s = input()
    minion_game(s)