def ringTheBell(numberofAttempts, secondsBetweenAttempts):
    totalTimeSpent=numberofAttempts*secondsBetweenAttempts
    return totalTimeSpent

#from myFunction import ringTheBell
def main():
    myAttempts=int(input("Please enter your number of attempts :"))
    mySecondsBetweenAttempts=int(input("Please enter the seconds between attempts :"))
    myTimeSpent=ringTheBell(myAttempts, mySecondsBetweenAttempts)
    return myTimeSpent
print("The value returned by main is :", main())
    