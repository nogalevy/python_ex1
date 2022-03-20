def question4():
    '''gets input and print it after ROT-13'''
    inp = input("enter...: ")
    inp = [calc_letter(x) for x in inp]
    inp = "".join(inp)
    print(inp)

def calc_letter(x):
    '''gets char - if the char is a letter A-Z or a-z: rotate 13'''
    output = 0
    if not x.isalpha(): return x
    if x.isupper(): output += (ord("A") + ((ord(x) - ord("A") + 13) % 26))
    elif x.islower(): output += (ord("a") + ((ord(x) - ord("a") + 13) % 26))
    return chr(output)

question4()

# Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
