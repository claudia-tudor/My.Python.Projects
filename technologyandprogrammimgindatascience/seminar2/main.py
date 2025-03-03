def ringTheBell(numberofAttempts, secondsBetweenAttempts=5):
    totalTimeSpent=numberofAttempts*secondsBetweenAttempts
    return totalTimeSpent

#from myFunction import ringTheBell
def main():
    myAttempts=int(input("Please enter your number of attempts :"))
    myTimeSpent=ringTheBell(myAttempts)
    return myTimeSpent
print("The value returned by main is :", main())
    