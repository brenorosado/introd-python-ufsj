from datetime import datetime

def convertMetersToCentimeters():
    metersString = input("Insert the value in meters to be converted (ex.: 1.74):")
    metersValue = float(metersString);
    centimetersValue = metersValue * 100
    print("Value converted: ", round(centimetersValue, 2), " cm");
    return centimetersValue

def getCurrentDatetime():
    now = datetime.now()
    print("datetime: ", now);
    formattedDatetime = now.strftime("%m/%d/%Y %H:%M:%S")
    print("formatted datetime: ", formattedDatetime);

def checkTypeOfChar():
    vowels = list("AaEeIiOoUu")
    charToCheck = input("Insert the char: ");

    if(charToCheck.isnumeric()):
        print("Number inserted.");
        return;

    if(charToCheck in vowels):
        print("The char is a vowel.")    
    else:
        print("The char is a consoant.")

    return; 

def invertWord():
    word = input("Insert the word to be inverted: ")
    invertedWord = '';
    for i in range(len(word) -1, -1, -1):
        invertedWord += word[i];

    print("Inverted word: ", invertedWord)

# convertMetersToCentimeters()
# getCurrentDatetime()
# checkTypeOfChar()
# invertWord()