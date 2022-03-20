def question2():
    lst = []
    while True:
        req = input("enter your request: ")
        if req == "i":
            str = input("Enter string: ")
            str = str[1:]
            lst.append(str)
        elif req == "e" and lst:
            lst.pop()
        elif req == "p":
            for i, s in enumerate(lst):
                print("{} {}".format(i, s))

        else:
            return


question2()
# Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
