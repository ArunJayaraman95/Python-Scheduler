class Course:
    def __init__(self, name, start, end, days):
        """Days is a list with values from 1-5 for M-F"""
        self.name = name
        self.start = start
        self.end = end
        self.days = days

    def getName(self):
        return self.name

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getDays(self):
        return self.days

    def __repr__(self):
        return self.name

courses = [
    Course("Stats", 1030, 1120, [1, 3, 5]),
    Course("Algorithms", 1730, 1845, [2, 4]),
    Course("Game Design", 1730, 1845, [1, 3]),
    Course("Game Lab", 1900, 2040, [1,3]),
    Course("AI", 1600, 1715, [1,3]),
    Course("Automata", 1600, 1715, [1,3]),
    Course("Fake", 1715, 1745, [2,4])
]

print(courses[0].getName())
print(courses)
count = len(courses)

switch = [0 for _ in courses]
print(switch)

inc = "0" * count
print(f'{inc=}')

limit = 2**count

def conflict(A: Course, B: Course):
    """Checks if there's a conflict between 2 classes. In other words, if 2 classes overlap in times on the same days"""
    # print(A.getStart(), A.getEnd())
    # print(B.getStart(), B.getEnd())

    conflictDay = False
    for aDays in A.getDays():
        if aDays in B.getDays():
            conflictDay = True
    conflictTimes = (A.getStart() <= B.getStart() <= A.getEnd()) or (B.getStart() <= A.getStart() <= B.getEnd())
    # print(conflictTimes and conflictDay)

for i in range(limit):
    t = bin(i)[2:].zfill(count)
    temporaryHolder = []
    for i,b in enumerate(t):
        if b == '1':
            temporaryHolder.append(courses[i])
    print(temporaryHolder)

conflict(courses[-1], courses[-2])