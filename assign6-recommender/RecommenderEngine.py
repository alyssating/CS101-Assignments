'''
@author: alyssa ting
netID: at341
'''

def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    ret = []
    for i in range(len(items)):
        item = items[i]
        totalItems = sum([1 for x in list(ratings.items()) if x[1][i] != 0])
        total = sum([x[1][i] for x in list(ratings.items()) if x[1][i] != 0])
        if totalItems != 0:
            ret.append((item,total/totalItems))
        else:
            tpl = (item,0.0)
            ret.append(tpl)
    return sorted(sorted(ret), key = lambda x: x[1], reverse = True)

def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    ret = []
    for i in list(ratings.items()):
        if name != i[0]:
            dotProduct = sum([ratings[name][x] * i[1][x] for x in range(len(i[1]))])
            ret.append((i[0], dotProduct))
    return sorted(sorted(ret), key=lambda x: x[1], reverse=True)

def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''

    similaritiesList = similarities(name, ratings)
    similaritiesList = similaritiesList[:numUsers]

    newRatings = {}
    for i in similaritiesList:
        num = i[1]
        for x in ratings:
            if x == i[0]:
                lst = [y * num for y in ratings[i[0]]]
                newRatings[i[0]] = lst
    avg = averages(items, newRatings)
    return avg

if __name__ == '__main__':

    items = ["DivinityCafe","Farmstead", "IlForno", "Loop", "McDonalds"]
    ratings = {"Sarah Lee": [3,3,3,3,0],
               "Melanie": [5,0,3,0,1],
               "JJ": [0,1,0,-1,1],
               "Sly one": [5,0,1,3,0],
               "Sung-Hoon": [0,-1,-1,5,1]}
    print (similarities("Melanie", ratings))
    print (recommendations("Melanie", items, ratings, 2))

