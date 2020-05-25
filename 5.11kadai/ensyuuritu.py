moji = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

moji2 = moji.strip(".")
moji3 = moji2.replace(",", "")
risuto = moji3.split()

numlist = []
for lis in risuto:
    num = len(lis)
    numlist.append(num)

print(numlist)
