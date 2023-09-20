if __name__ == "__main__":

    def calcPow():
        numberString = input("Insira o numero a ser elevado: ")
        number = int(numberString);

        elevationString = input("Insira a potencia: ")
        elevation = int(elevationString);
        result = number;

        for i in range(1, elevation):
            result = result * number;

        print("Resultado: ", result);
        return;

    def printTenToOne(): 
        number = 10;
        while number >= 1:
            print(number);
            number -= 1;

        return;

    def printListOfNames():

        listOfNames = [];
        for i in range(0, 4):
            newName = input("Insira o nome da pessoa a ser inserida na lista: ");
            listOfNames.append(newName);

        for name in listOfNames:
            print(name);

        return

# calcPow();
# printTenToOne()
printListOfNames();