def str_n_gram(text, n):
    result = []
    for i in range(len(text) - n + 1):
        result.append(text[i : i + n : 1])
    return set(result)


sentence = "paraparaparadise"
sentence2 = "paragraph"

X = str_n_gram(sentence, 2)
Y = str_n_gram(sentence2, 2)

print(X | Y)
print(X & Y)
print(X - Y)
print("se" in X.union(Y))
