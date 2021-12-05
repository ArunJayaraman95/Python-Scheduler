class Course:
    def __init__(self, name, start, end, days):
        """Days is a list with values from 1-5 for M-W"""
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

testData = [
    Course("Stats", 1030, 1120, [1, 3, 5]),
    Course("Algorithms", 1730, 1845, [2, 4]),
    Course("Game Design", 1730, 1845, [1, 3]),
    Course("Game Lab", 1900, 2040, [1,3]),
    Course("AI", 1600, 1715, [1,3]),
    Course("Automata", 1600, 1715, [1,3]),
]

print(testData[0].getName())