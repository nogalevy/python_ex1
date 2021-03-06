'''
Written by: Noga Levy (ID: 315260927, login: levyno)
             and Tali Kalev (ID: 208629691, login: talikal)

Goal of the Program: The program gets from user an integer between 1 to 4.
                    The program then runs the function associated with the
                    number.
                    1: gets 2 numbers from user
                        and prints the number of times the first number's digits appear
                        in the second number
                    2: Program acts as a stack with the following operations:
                        i = insert new
                        e = the last item- list[-1]
                        p = print
                        else = exit
                        input: one of the above operations
                        output: if p is chosen, the program prints the contents
                        of the stack in a numbered column
                    3: receives list of genes and prints list of
                        genes where the last number is less than 0.1
                    4: gets encrypted message and prints the decoded message after
                        applying ROT-13 algorithm
'''

########################################################################

def question1():
    '''question 1: gets 2 numbers from user
        and prints the number of times the first number's digits appear
        in the second number'''
    counter = 0
    n1, n2 = input("Please enter 2 numbers: ").split()
    n1 = [int(x) for x in n1]
    n2 = [int(x) for x in n2]
    for x in n1:
        if x in n2:
            counter += 1

    print(counter)

########################################################################

def question2():
    ''' Program acts as a stack with the following operations:
        i = insert new
        e = the last item- list[-1]
        p = print
        else = exit
    '''
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

########################################################################

def question3():
    '''question 3: receives list of genes and prints list of
        genes where the last number is less than 0.1'''
    geneList = input("Please enter list of genes: ").split()
    bestGenes = []
    for i in range(0, len(geneList)):
        temp = geneList[i]
        temp = temp.split(',')
        if float(temp[-1]) < 0.1:
            for j in range(0, len(temp) - 2):
                bestGenes.append(temp[j])

    bestGenes = list(dict.fromkeys(bestGenes))
    print(bestGenes)

########################################################################

def question4():
    '''gets encrypted message and prints the decoded message after
        applying ROT-13'''
    inp = input("Enter message to decode: ")
    inp = [calc_letter(x) for x in inp]
    inp = "".join(inp)
    print(inp)

def calc_letter(x):
    '''gets char - if the char is a letter A-Z or a-z: rotate 13'''
    output = 0
    if not x.isalpha():
        return x
    if x.isupper():
        output += (ord("A") + ((ord(x) - ord("A") + 13) % 26))
    elif x.islower():
        output += (ord("a") + ((ord(x) - ord("a") + 13) % 26))
    return chr(output)

########################  MAIN LOOP ################################

lst_f = [question1, question2, question3, question4]
option = input("Please enter request: ")
while option.isdigit() and int(option) in range(1,5):
    lst_f[int(option) - 1]()
    option = input("Please enter request: ")
