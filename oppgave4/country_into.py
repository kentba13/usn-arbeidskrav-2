"""
DEL A
Oppretter og returnerer en dictionary med informasjon om hovedstand og antall innbyggere
"""
def create_country_info_dictionary():
    data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873],
    }
    return data

#Henter informasjon om et gitt land fra dictionary.
def get_country_info(dict, country):
    return dict.get(country)

def add_country_info(data):
    country_input = input("Skriv inn navnet på det nye landet: ")
    country_capitalized = country_input.capitalize()
    
    #Verifiserer om landet fins i dictionary fra før eller ikke
    if country_capitalized in data:
        print(f"{country_capitalized} finnes allerede i databasen.")
        return
    
    hovedstad = input(f"Skriv inn hovedstaden i {country_capitalized}: ")
    try:
        innbyggere = float(input(f"Skriv inn antall innbyggere i {hovedstad} (i millioner): "))
        if innbyggere < 0:
            print("Antall innbyggere kan ikke være negativt.")
            return
    except ValueError:
        print("Det skjedde en feil, vennligst prøv igjen.")
        return
    
    data[country_capitalized] = [hovedstad, innbyggere]
    print(f"{country_capitalized} har blitt lagt til i databasen.")

#Lesbar utskrift av dictionary.
def print_dictionary(dict):
    print("\nOppdatert Dictionary:")
    for land, info in dict.items():
        hovedstad, innbyggere = info
        print(f"{land}: Hovedstad - {hovedstad}, Innbyggere - {innbyggere} mill.")

def main():

    countryInfo = create_country_info_dictionary()  

    """
    Del B 
    Hente informasjon basert på brukerinput
    """
    input_country = input("Skriv inn et land: ")
    
    # Stor forbokstav
    input_country_capilatized = input_country.capitalize()
    
    #Hent informasjon av landet og skriv ut til konsoll
    info = get_country_info(countryInfo, input_country_capilatized)
    
    if info:
        hovedstad, innbyggere = info
        print(f"{hovedstad} er hovedstaden i {input_country_capilatized} og det er {innbyggere} mill. innbyggere i {hovedstad}.")
    else:
        print(f"{input_country_capilatized} finnes ikke i databasen.")

    """
    DEL C
    Ber brukeren legge til informasjon om et nytt land og oppdaterer dictionary.
    """
    print("\nLegg til nytt land")
    add_country_info(countryInfo)  
    # Skrive ut oppdatert dictionary
    print_dictionary(countryInfo)

if __name__ == "__main__":
    main()