import random,string

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxz'
alphabets = string.ascii_lowercase

word_length = int(input("Please enter word length : "))
print()
number_suggestions = int(input("Please enter the number of suggestions : "))
print()

def generator():
    type_letter = []
    for i in range(word_length):
        choice = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter : ")
        type_letter.append(choice)
        print()

    for i in range(number_suggestions):
        word_suggested = []
        for letter in type_letter:
            if letter == 'v':
                word_suggested.append(random.choice(vowels))
            elif letter == 'c':
                word_suggested.append(random.choice(consonants))
            elif letter == 'l':
                word_suggested.append(random.choice(alphabets))
            else:
                word_suggested.append(letter)

        word_suggested = "".join(map(str,word_suggested))

        print(word_suggested)

generator()
