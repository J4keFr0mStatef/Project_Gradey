
import pickle

class Quarter:
    def __init__(self):
        pass

class Class:
    def __init__(self, hours):
        assignments = {}
        grade = None
        self.hours = hours
    
    # Setters and mutators
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if(grade.isalpha()):
            self._grade = grade
        else:
            print("Please input a character, or update your grade with '[object].update()'")

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, val):
        if(1 <= val < 4):
            self._hours = val
        else:
            print("Make sure the number of hours is correct...")

    # adds an assignment to the class
    def addAssignment(self, name, weight=None, possible=100, earned=None):
        self.assignments[f"{name}"] = Assignment(weight, possible, earned)
        
    # calculate and return the letter and the numerical grade
    def giveGrade(self):
        tot = 0
        for i in self.assignList:
            tot += self.assignList[i].weighted

        # calculate letter grade on a 10-pt scale
        grade = 'F'
        if(tot >= 90):
            grade = 'A'
        elif(tot >= 80):
            grade = 'B'
        elif(tot >= 70):
            grade = 'C'
        elif(tot >= 60):
            grade = 'D'

        return grade, tot

    def __str__(self):
        pass
        
class Assignment:
    def __init__(self, weight=None, possible=100, earned=None):
        self.weight = weight
        self.earned = earned
        self.possible = possible

    # accessors and mutators
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, val):
        self._weight = val

    @property
    def earned(self):
        return self._earned

    @earned.setter
    def earned(self, val):
        self._earned = val

    @property
    def possible(self):
        return self._possible

    @possible.setter
    def possible(self, val):
        self._possible = val

    # assignment methods
    def percentage(self):
        return (self.earned / self.possible) * 100

    def weighted(self):
        return self.percentage * self.weight/100

    def __str__(self):
        return f"{self}:\t{self.earned}/{self.possible}\t{self.earned/self.possible * 100}%"

# function to save the current state to a pickle file
def save(tracker):
    pickle.dump(tracker, open("saved.p", "wb"))

# main program
def main():
    # try to load the save, if there is none, instantiate it
    try:
        tracker = pickle.load(open("saved.p", "rb"))
    except:
        tracker = {}

    # when program runs, need a quarter and a year
    year = input("What year do you want to access? [E.g. 'Y1, Y2, ... ']\n")
    quarter = input("Quarter? \n[E.g. 'Q1, Q2, ... '")
    print("-" * 10, end="\n")

    if(not year in tracker):
        tracker[year][quarter] = Quarter()

    # primary part of the program
    while(True):
        pass

if(__name__ == "__main__"):
    main()
