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

    f = open('data/movies.txt')
    lst = []
    for line in f:
        line = line.strip()
        movie = line.split(",")[1]
        if movie not in lst:
            lst.append(movie)
    lst = sorted(lst)

    f.close()

    dict = {}
    newF = open('data/movies.txt')
    for line in newF:
        line = line.strip()
        movie = line.split(",")[1]
        student = line.split(",")[0]
        rating = line.split(",")[-1]
        if student not in dict:
            dict[student] = [0 for i in lst]
        dict[student][lst.index(movie)] = int(rating)

    return (lst,dict)

if __name__ == '__main__':
    print (getdata())