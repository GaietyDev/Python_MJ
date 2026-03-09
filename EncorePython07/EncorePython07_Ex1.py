import random

f = open("prepositions.txt")
s = f.read()
prepositions = s.split()
f1 = open("articles.txt")
s1 = f1.read()
articles = s1.split()
f2 = open("verbs.txt")
s2 = f2.read()
verbs = s2.split()
f3 = open("nouns.txt")
s3 = f3.read()
nouns = s3.split()

#print("Nouns:")
#print(nouns)
#print()
#print("Prepositions:")
#print(prepositions)
#print
#print("Verbs:")
#print(verbs)
#print()
#print("Articles:")
#print(articles)
#print()

def nounPhrase():
   article = random.choice(articles) + " " 
   noun = random.choice(nouns)
   noun_phrase = article + noun
   return noun_phrase

#for noun_phrases in range(5):
#   print(nounPhrase())

def prepositionalPhrase():
    preposition = random.choice(prepositions) + " "
    prepositional_phrase = preposition + nounPhrase()
    return prepositional_phrase

#for prepositional_phrases in range(5):
#    print(prepositionalPhrase())

def verbPhrase():
    verb = random.choice(verbs) + " "
    noun_phrase = nounPhrase() + " "
    prepositional_phrase = prepositionalPhrase() + " "
    verb_phrase = verb + noun_phrase + prepositional_phrase
    return verb_phrase

#for verb_phrases in range(5):
#    print(verbPhrase())

def sentence():
    verb_phrase = verbPhrase() + " "
    noun_phrase = nounPhrase() + " "
    sentence = noun_phrase + verb_phrase
    return sentence

for sentences in range(20):
    print(sentence())
