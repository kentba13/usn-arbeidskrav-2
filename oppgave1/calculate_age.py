#Importer TARGET_YEAR fra utils mappe
from utils.constants import TARGET_YEAR

#Kalkulerer alder basert på input og konstant deklarert i constants filen i utils mappen.
def calculateAge(baselineYear):
    return baselineYear - TARGET_YEAR

#Kunne også kalkulert alder baser på nåværende år ved å bruke datetime modulen. 
def main():
    try:
        birthYear = int(input('Hvilket år er du født? '))
        age = calculateAge(birthYear)
        #f-string for å sette uttrykk direkte i string.
        print(f'Du ble {age} år i løpet av {TARGET_YEAR}.')
    except ValueError:
        print("Det skjedde en feil, vennligst prøv igjen.")

if __name__ == "__main__":
    main()