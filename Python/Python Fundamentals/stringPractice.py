str = "It's thanksgiving day. It's my birthday,too!"
str.find("day")
str.replace("day", "month")
print str

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
start = x[0]
end = x[len(x)-1]
y = [start,end]
print y

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y = x[0:len(x)/2]
z = x[len(x)/2:]
z.insert(0, y)
print z
