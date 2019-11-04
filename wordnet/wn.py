import  nltk
from nltk.corpus import wordnet
import collections

class WN:

   def get_synonyms(self,synsets):
       synonyms = []

       for syn in synsets:
           for l in syn.lemmas():
               synonyms.append(l.name())

       return list(set(synonyms))

   def get_synsets(self,word):
       synsets = []

       for syn in wordnet.synsets(word):
           synsets.append(syn)

       return synsets
#main
if __name__ == '__main__':
    #nltk.download('stopwords')
    #nltk.download('wordnet')
    #first = wordnet.synset('hound.n.02')
    #second = wordnet.synset('dog.n.01')
    #print(first.path_similarity(second))
    wn = WN()
    synsets = wn.get_synsets("study")
    synonyms = wn.get_synonyms(synsets)
    bed = wordnet.synset('bed.n.01')
    #hyp = bed.hyponyms()
    #hyp = bed.hypernyms()
    #synsets = wn.get_synsets("university")
    #for synset in synsets:
    #    print('%s : %s' % ( synset, synset._definition))

    #print(synonyms)

    #animal is a hypernym of elephant
    #hypernyms = wn.get_hypernyms("elephant")
    #print(hypernyms)


    # poker, roulette, and craps are hyponyms of game
    #hyponyms = wn.get_hyponyms("bed")
    #print(hyponyms)