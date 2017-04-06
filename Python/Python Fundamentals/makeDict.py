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
    i = 0
    newList = []
    newDict = {}
    for items in arr1:
        newList += "(" + arr1[i] + ":" + arr2[i] + ")",
        # newList += "(" + arr1[i], arr2[i] + ")",
        i += 1
    print newList
    newDict = dict(newList)
    print newDict
makeDictv2(name,favorite_animal)
