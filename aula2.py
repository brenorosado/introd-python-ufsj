if __name__ == "__main__":

    def getTimeFromSeconds(secondsString):
        if(secondsString == ''):
           print("Invalid input.")
           return
        
        seconds = int(secondsString)
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 3600) % 60
        print(hours, "hours,", minutes, "minutes e", seconds, "seconds.")
        return

    def calcWageWithAdjustment(wageString):
        if(wageString == ''):
            print("Invalid input.")
            return
        
        wage = float(wageString)

        if(wage < 280):
            wage = wage + wage * 0.2
        elif(wage < 700):
            wage = wage + wage * 0.15
        elif(wage < 1500):
            wage = wage + wage * 0.01
        elif(wage >= 1500):
            wage = wage + wage * 0.05
        
        print("Wage before adjustment: ", wageString);
        print("Applied adjustment: ", 100 * (wage - float(wageString)) / float(wageString), "%")
        print("Wage raised in: ", wage - float(wageString))
        print("Ajusted salary: ", wage)
        return
        
# getTimeFromSeconds(input("Insert value in seconds:"))
calcWageWithAdjustment(input("Insert wage to calculate adjustment: "))