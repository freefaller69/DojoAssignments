name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
#
# def makeDict(arr1,arr2):
#     newDict = {}
#     newList = zip(arr1,arr2)
#     newDict = dict(newList)
#     print newDict
# makeDict(name,favorite_animal)

def makeDictv2(arr1,arr2):
    newDict = {}
    if len(arr1) >= len(arr2):
        length = len(arr1)
        big = arr1
        small = arr2
    else:
        length = len(arr2)
        big = arr2
        small = arr1

    for index in range(length):
    # for items in arr1:
        # print index
        # print arr1[index]
        # print arr2[index]
        try:
            newDict[big[index]] = small[index]
        except IndexError:
            newDict[big[index]] = None
        # newList += "(" + arr1[i] + ":" + arr2[i] + ")",
        # newList += "(" + arr1[i], arr2[i] + ")",
        # i += 1
    print newDict
makeDictv2(name,favorite_animal)
