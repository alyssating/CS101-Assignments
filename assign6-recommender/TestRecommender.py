'''
@author: alyssa ting
netID: at341
'''

import SmallDukeEatsReader
import RecommenderEngine


def driver():
    '''
    Tests values returned by functions averages, similarities, and recommendations
    in the RecommenderEngine module by comparing it by correct provided values.
    '''

    (items,ratings) = SmallDukeEatsReader.getdata()
    print("items = ",items)
    print("ratings = ", ratings)

    avg = RecommenderEngine.averages(items,ratings)

    correctAvgList = [('DivinityCafe', 4.0), ('TheCommons', 3.0),
                      ('Tandoor', 2.4285714285714284), ('IlForno', 1.8),
                      ('Farmstead',1.4), ('LoopPizzaGrill',1.0),
                      ('TheSkillet',0.0), ('PandaExpress',-0.2),
                      ('McDonalds', -0.3333333333333333)]
    correctAvgVals = [i[1] for i in correctAvgList]

    myAvgVals = [i[1] for i in RecommenderEngine.averages(items,ratings)]

    # testing averages function
    flag = True

    for i in range(len(myAvgVals)):
        x = abs(correctAvgVals[i]-myAvgVals[i])
        if x > 0.001:
            flag = False

    print("average",avg)

    if flag:
        print ("averages works")
    else:
        print ("averages fails")

    for key in ratings:
        slist = RecommenderEngine.similarities(key,ratings)
        if key == "Sung-Hoon":
            mySimilarityVals = [x[1] for x in slist]
        print(key, slist)
        r3 = RecommenderEngine.recommendations(key,items,ratings,3)
        if key == 'Sarah Lee':
            myRecommendationVals = [x[1] for x in r3]
        print("top", r3)

    # testing similarities function
    correctSimilaritiesList = [('Wei', 1), ('Sly One', -1), ('Melanie', -2),
                               ('Sarah Lee', -6), ('J J', -14), ('Harry', -24),
                               ('Nana Grace', -29)]
    correctSimilaritiesVals = [i[1] for i in correctSimilaritiesList]

    flag2 = True
    for i in range(len(mySimilarityVals)):
        x = abs(correctSimilaritiesVals[i]-mySimilarityVals[i])
        if x > 0.001:
            flag2 = False

    if flag2:
        print("similarities works")
    else:
        print("similarities fails")

    # testing recommender function

    correctRecommendationsList = [('Tandoor', 149.5), ('TheCommons', 128.0),
                                  ('DivinityCafe', 123.33333333333333),
                                  ('Farmstead', 69.5), ('TheSkillet', 66.0),
                                  ('LoopPizzaGrill', 62.0), ('IlForno', 33.0),
                                  ('McDonalds', -69.5), ('PandaExpress', -165.0)]
    correctRecommendationsVals = [x[1] for x in correctRecommendationsList]

    flag3 = True
    for i in range(len(myRecommendationVals)):
        x = abs(correctRecommendationsVals[i]-myRecommendationVals[i])
        if x > 0.001:
            flag3 = False

    if flag3:
        print("recommendations works")
    else:
        print("recommendations fails")

if __name__ == '__main__':
    driver()