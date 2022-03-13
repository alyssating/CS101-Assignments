'''
@author: alyssa ting
netID: at341
'''

def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''

    with open('data/books.txt', "r") as file:
        firstLine = file.readline()

    ret = []
    for i in range(1,len(firstLine.split(",")),2):
        ret.append(firstLine.split(",")[i])

    file.close()

    dict = {}
    newFile = open('data/books.txt', 'r')

    for line in newFile:
        line = line.strip()
        lst = line.split(",")
        student = lst[0]
        if student not in dict:
            dict[student] = [0 for i in ret]
        for i in range(1,len(lst)-1,2):
            book = line.split(",")[i]
            dex = ret.index(book)
            dict[student][dex] = int(line.split(",")[line.split(",").index(book) + 1])
    return (ret,dict)

if __name__ == '__main__':
    print (getdata())