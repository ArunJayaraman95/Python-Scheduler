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
        return f'{self.name}:\t {badIntToTime(self.start)} - {badIntToTime(self.end)} \ton {"-".join([self.dayOfWeek[x] for x in self.days])}'


def badIntToTime(t) -> str:
    return f'{str(t)[:-2] if t < 1200 else str(t-1200)[:-2]}:{str(t)[-2:]}{["AM","PM"][t >= 1200]}'


def MidToTime(t) -> str:
    minutes = t % 60
    hours = int((t-minutes)/60)
    #print(hours,minutes)
    if hours == 0: hours = 12
    res = f'{hours-12 if hours > 12 else hours}:{str(minutes).zfill(2)}{["AM","PM"][t > 719]}'
    return res


def minutesSinceMidnight(timeString) -> int:
    digits = [x for x in timeString if x.isdigit()]
    digits = int(''.join(digits))
    if 1200 <= digits <= 1259:
        digits -= 1200
    if 'PM' in timeString: 
        digits += 1200
    minutes = digits % 100
    hours = (digits - minutes)/100
    return int(60 * hours + minutes)

courses = [
    Course("Stats", 1030, 1120, [1, 3, 5]),
    Course("Stats", 1050, 1120, [1, 3, 5]),
    Course("Stats", 930, 1020, [1, 3, 5]),
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

    # If the same object, return no conflict
    if A == B:
        return False
    # If objects aren't the same but have the same name, return a conflict
    if A.getName() == B.getName():
        return True

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
        #print(tempCourses)
        #print("SUCCESS")
        possibleSchedules.append(tempCourses)
        pass

mostClasses = max([len(schedule) for schedule in possibleSchedules])


print('\n\n\nCourse Combos\n=========\n')

testCourse = None
accepted = []
notLookingForMost = False
for schedule in possibleSchedules:
    if notLookingForMost:
        mostClasses -= 1
    if len(schedule) >= mostClasses:
        accepted.append(schedule)
        if len(schedule) == mostClasses:
            if not testCourse:
                testCourse = schedule
            # print("Optimal:\n")
        # print(p, "\n")
        for course in schedule:
            #print(course)
            pass
        # print('===========================')
#endregion




# print('<><><><><><><><><><><><><><><><><>')
# print('<><><><><><><><><><><><><><><><><>')
# print('<><><><><><><><><><><><><><><><><>')
# print('<><><><><><><><><><><><><><><><><>')
# print('<><><><><><><><><><><><><><><><><>')
# print('<><><><><><><><><><><><><><><><><>')

root = Tk()
root.state("zoomed")
SW = root.winfo_screenwidth()
SH = root.winfo_screenheight()

# Fonts

font1 = ('Arial', 15)


# CONFIGURING LABELS (INDEPENDENT)

# Create time labels
timeLabel = Label(root, bg = "#D44", text = "Time\Day")
timeLabel.grid(row = 0, column = 0, sticky = 'news')
for i in range(31):
    c = "#DEE2F0" if i % 2 else "#D3D3F0"
    timeStamp = Label(root, bg = c, text = MidToTime(420 + 30*i), font = font1, pady = 1)
    timeStamp.grid(row = 30*i + 1, rowspan = 30, column = 0,columnspan = 1, sticky = "news")
    # print(i)
    for j in range(7):
        if i % 2:
            c = "#DEE2E1" if j % 2 else "#DFE0E0"
        else:
            c = "#D3D3D3" if j % 2 else "#C8C8C8"
        dummy = Label(root, bg = c, text = '.', fg = c)
        dummy.grid(row = 30*i+1, column = j + 1, rowspan = 30, sticky = 'news')

# Create weekday labels
for i, day in enumerate(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']):
    dayLabel = Label(root, bg = "#999", text = day, font = font1)
    dayLabel.grid(row = 0, column = i + 1, sticky = 'news')



colorList = [
    "#d62d5e",
    "#e77b55",
    "#fade9c",
    "#4ddbb9",
    "#8e8beb",
    "#f9b8b8",
    "#f3f5c8",
    "#abf8f2",
    "#cad4f3",
    "#fad8fb"]

# DEPENDENT
labels = []
sIndex = 0

# for i in accepted:
#     for j in i:
#         print(j)
# print()
# print(len(accepted))
# Add courses into schedule
def generate():
    global sIndex
    for c, course in enumerate(accepted[sIndex]):
        if c > len(colorList):
            color = "#DDD"
        color = colorList[c]
        # print(course)
        start = minutesSinceMidnight(badIntToTime(course.getStart()))
        span = minutesSinceMidnight(badIntToTime(course.getEnd())) - start

        for day in course.getDays():
            t = Label(root, bg = color, text = course.getName(),borderwidth = 3, relief="ridge", font = ("Times New Roman", 15))
            t.grid(row = start - 420, column = day + 1, columnspan=1, rowspan = span, sticky='nesw')
            labels.append(t)
    # Descriptive Labels
    nameLabel = Label(root, text = f'Schedule #{sIndex + 1} of {len(accepted)}', font = ('Arial', 20))
    nameLabel.grid(row = 0, column = 9, columnspan = 1, pady = 10)
    
# Generate first schedule  
generate()


# Sidebars

# Button to clear label
def clearSchedule():
    for label in labels:
        label.destroy()

def prevCombo():
    global sIndex

    clearSchedule()

    if sIndex != 0:
        sIndex -= 1

    generate()

def nextCombo():
    global sIndex

    clearSchedule()

    if sIndex != len(accepted) - 1:
        sIndex += 1

    generate()

prevB = Button(root, text = "Prev", command = prevCombo, pady = 5, bg = "lightblue", font = font1, padx = 10)
nextB = Button(root, text = "Next", command = nextCombo, pady = 5, bg = "lightblue", font = font1, padx = 10)

prevB.grid(row = 0, column = 8)
nextB.grid(row = 0, column = 10)

for i in range(8):
    root.columnconfigure(i, minsize = (3/4)*(1/8)*SW)

root.rowconfigure(0, minsize = SH/100)
root.columnconfigure(8, minsize = (3/4)*(1/12)*SW)
root.columnconfigure(9, minsize = (3/4)*(1/8)*SW)
root.columnconfigure(10, minsize = (3/4)*(1/12)*SW)

root.mainloop()

# x = minutesSinceMidnight("12:59AM")
# print(x)
# x = MidToTime(x)
# print(x)