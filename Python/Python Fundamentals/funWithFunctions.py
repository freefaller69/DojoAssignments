# def odd_even():
#     for num in range(1,2001):
#         if num % 2 == 0:
#             print "Number is", str(num) + ". This is an even number."
#         elif num % 2 != 0:
#             print "Number is", str(num) + ". This is an odd number."
#
# odd_even()

def multiply(lst, mult):
    newList = []
    for num in lst:
        newList.append(num * mult)
    return newList

a = [2,4,10,16,20]
b = 5
multiply(a,b)

def layered_multiples(arr):
    new_array = []
    for idx in arr:
        new_list = []
        while idx > 0:
            new_list.append(1)
            idx -= 1
        new_array.append(new_list)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
