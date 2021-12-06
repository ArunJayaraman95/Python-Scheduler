from tkinter import *


#region Calculation

class Course:
    def __init__(self, name, start, end, days):
        """Days is a list with values from 1-5 for M-F"""
        self.name = name.ljust(12)
        self.start = start
        self.end = end
        self.days = days
        self.dayOfWeek = {1:"M", 2:"T", 3: "W", 4:"Th", 5:"F"}

    def getName(self):
        return self.name

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getDays(self):
        return self.days

    def __repr__(self):
        return f'{self.name}:\t {intToTime(self.start)} - {intToTime(self.end)} \ton {"-".join([self.dayOfWeek[x] for x in self.days])}'

def intToTime(t):
    return f'{str(t)[:-2] if t < 1200 else str(t-1200)[:-2]}:{str(t)[-2:]}{["AM","PM"][t >= 1200]}'

courses = [
    Course("Stats", 1030, 1120, [1, 3, 5]),
    Course("Algorithms", 1730, 1845, [2, 4]),
    Course("Game Design", 1730, 1845, [1, 3]),
    Course("Numerical", 1600, 1715, [2,4]),
    Course("Game Lab", 1900, 2040, [1,3]),
    Course("AI", 1600, 1715, [1,3]),
    Course("Automata", 1630, 1720, [1,3]),
    Course("Fake", 1715, 1745, [2,4])
]

numCourses = len(courses)
limit = 2**numCourses
possibleSchedules = []

def conflict(A: Course, B: Course):
    """Checks if there's a conflict between 2 classes. In other words, if 2 classes overlap in times on the same days"""

    if A == B:
        return False

    conflictDay = False
    for aDays in A.getDays():
        if aDays in B.getDays():
            conflictDay = True

    conflictTimes = (A.getStart() <= B.getStart() <= A.getEnd()) or (B.getStart() <= A.getStart() <= B.getEnd())
    return conflictTimes and conflictDay

# Check conflicts
for inc in range(limit):
    t = bin(inc)[2:].zfill(numCourses)
    tempCourses = []

    for i,b in enumerate(t):
        if b == '1':
            tempCourses.append(courses[i])
    poss = True
    for x in range(0, len(tempCourses)):
        for y in range(x, len(tempCourses)):
            if conflict(tempCourses[x], tempCourses[y]):
                poss = False
            else:
                pass
    if poss:
        print(tempCourses)
        print("SUCCESS")
        possibleSchedules.append(tempCourses)
        pass

mostClasses = max([len(schedule) for schedule in possibleSchedules])


print('\n\n\nCourse Combos\n=========\n')

testCourse = None
for schedule in possibleSchedules:
    if len(schedule) >= mostClasses - 1:
        if len(schedule) == mostClasses:
            if not testCourse:
                testCourse = schedule
            print("Optimal:\n")
        # print(p, "\n")
        for course in schedule:
            print(course)
        print('===========================')
#endregion




print('<><><><><><><><><><><><><><><><><>')
root = Tk()
root.geometry("1900x1080")
# Create windows for each possible schedule
# Be able to go back and forth on each

increment = 30
for i in range(800, 2200, increment):
    timeStamp = Label(root, bg = "#AAA", text = intToTime(i))
    timeStamp.grid(row = i, column = 1, rowspan = increment,columnspan = 2, sticky='news')
for course in testCourse:
    print(course)
    start = course.getStart()
    span = course.getEnd() - course.getStart()
    # TODO ~ Convert to actual spanning time for correct scale visually
    print(start, span)
    for day in course.getDays():
        t = Label(root, bg = "#FF0", text = course.getName())
        t.grid(row = start, column = day + 2, rowspan = span, sticky='nesw')



#Create a label Widgetf
# titleLabel1 = Label(root, text = "HI")
# titleLabel2 = Label(root, text = "New guy")
# titleLabel3 = Label(root, text = "Super cool dudee")
# titleLabel1.grid(row = 0, column = 0)
# titleLabel2.grid(row = 1, column = 5)
# titleLabel3.grid(row = 1, column = 1)
root.mainloop()