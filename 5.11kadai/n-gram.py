import re

sentence = "I am an NLPer"


def word_n_gram(sentence, N):

    words = sentence.split()
    result = []
    for it, c in enumerate(words):
        if it + N > len(words):
            return result
        result.append(words[it : it + N])


print(word_n_gram(sentence, N=2))


def char_n_gram(sentence, N):
    result2 = []
    for it in range(len(sentence)):
        if it + N > len(sentence):
            return result2
        result2.append(sentence[it : it + N])


print(char_n_gram(sentence, N=2))
