print "x",
for i in range(1,13):
    print i,
print "\n"
for x in range(1,13):
    y = 0
    print x,
    while y < 12 * x:
        y += x
        print y,
    print "\n"
