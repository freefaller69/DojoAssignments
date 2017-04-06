import random
random_num = random.sample(xrange(60,101), 10)

# print random_num

def grades():
    scores = random_num
    print "Scores and Grades"
    for scr in scores:
        if scr >= 90:
            grade = "A"
        elif scr >= 80:
            grade = "B"
        elif scr >= 70:
            grade = "C"
        elif scr >= 60:
            grade = "D"
        print "Score:", str(scr) + "; Your grade is " + grade
    print "End of the program.  Bye!"
grades()
