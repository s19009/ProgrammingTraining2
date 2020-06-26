def cipher(t):
    result = ""
    for c in t:
        if c.islower():
            result += chr(219 - chr(c))
        else:
            result += c
    return result


t = "helloworld"

coded = cipher(t)
print(coded)

cecoded = cipher(coded)
print(decoded)
