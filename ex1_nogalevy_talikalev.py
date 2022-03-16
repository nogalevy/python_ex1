def question1():
    '''question 1: gets 2 numbers from user
        and return the number of digits they have in common'''
    counter = 0
    n1, n2 = input("Please enter 2 numbers: ").split()
    n1 = [int(x) for x in n1]
    n2 = [int(x) for x in n2]
    for x in n1:
        if x in n2:
            counter += 1

    print(counter)

question1()

#option = input("Please enter request: ")

#while isinstance(option, int) and int(option) in range(1,5):


#    option = input("Please enter request: ")
