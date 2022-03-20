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

def question3():
    '''question 3: receives list of genes and returns list of
        genes where the last number is less than 0.1'''
    geneList = input("Please enter list of genes: ").split()
    bestGenes = []
    for i in range(0, len(geneList)):
        temp = geneList[i]
        temp = temp.split(',')
        if float(temp[-1]) < 0.1:
            for j in range(0, len(temp) - 1):
                bestGenes.append(temp[j])

    bestGenes = list(dict.fromkeys(bestGenes))
    return bestGenes

l1 = question3()
print(l1)
