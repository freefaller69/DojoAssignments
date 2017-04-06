#input
l1 = ['magical unicorns',19,'hello',98.98,'world']
#output
# "The array you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"

# input
l2 = [2,3,1,7,4,12]
#output
# "The array you entered is of integer type"
# "Sum: 29"

# input
l3 = ['magical','unicorns']
#output
# "The array you entered is of string type"
# "String: magical unicorns"

# newStr = ''
# mySum = 0
# for x in data:
#     if isinstance(x, int):
#         mySum += x
#     if isinstance(x, str):
#         newStr += x + ' '
#
myList = l3
mySum = 0
newStr = ""
for items in myList:
    if isinstance(items, int) or isinstance(items, float):
        mySum += items
    if isinstance(items, str):
        newStr += items + " "
if all(isinstance(items, int) for items in myList):
    print "The array you entered is of integer type"
    print "Sum:", mySum
elif all(isinstance(items, str) for items in myList):
    print "The array you entered is of string type"
    print "String: " + newStr
else:
    print "The array you entered is of mixed type"
    print "String: " + newStr
    print "Sum:", mySum
