import random

def grades():
    # scores = random_num
    print "Scores and Grades"
    grade = ""
    for r in range(10):
        scr = random.randint(60,101)
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
