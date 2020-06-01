bun = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

jisyo = {}

for i, word in enumerate(bun.split(), 1):
    if i in (1, 5, 6, 7, 8, 9, 15, 16, 19):
        jisyo[word.strip(".")[:1]] = i
    else:
        jisyo[word.strip(".")[:2]] = i

print(jisyo)
