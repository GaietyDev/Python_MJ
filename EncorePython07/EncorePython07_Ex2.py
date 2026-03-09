import random
from random import randint

replacements = {'I':'you', 'me':'you', 'my':'your',
                'we':'you', 'us':'you', 'mine':'yours'}

def changePerson(sentence):
    s = sentence.split()
    replyWords = []
    #print(s)
    for word in s:
        replacement = replacements.get(word, word)
        #print(f"{word:8} {replacement}")
        replyWords.append(replacement)
    #print(replyWords)
    newSentence = " ".join(replyWords)
    #print(newSentence)
    return newSentence

changePerson("I left my house today.")

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")
qualifiers = ("Why do you say that",
              "You seem to think that",
              "Can you explain why")

def reply(sentence):
    number = randint(1, 4)
    #for numbers in range(10):
    #   print(number, end = " ")
    if number == 1:
        return random.choice(hedges)
    else:
        qualifier = random.choice(qualifiers)+ " "
        personChange = changePerson(sentence)
        return qualifier + personChange
    
#for numbers in range(10):
#   print(reply("I left my house today."))

def main():
    print("Hello! I hope you've had a pleasant day so far")
    print("What do you want help with?")
    print()

    inputSentence = ""
    while inputSentence != "QUIT":
        inputSentence = input(">>>")
        print(reply(inputSentence))
        print()
    print("Goodbye and enjoy your day!")

main()
