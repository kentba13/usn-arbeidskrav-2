from oppgave1.calculate_age import main as oppg1_main
from oppgave2.calculate_pizza import main as oppg2_main
from oppgave3.convert_degrees_to_radians import main as oppg3_main
from oppgave4.country_into import main as oppg4_main
from oppgave5.calculate_area import main as oppg5_main
from oppgave6.function_plotter import main as oppg6_main

def main():
    print("Python Arbeidskrav2")
    while True:
        print("\nVelg en oppgave å kjøre:")
        print("1. Oppgave 1: Beregn Alder")
        print("2. Oppgave 2: Beregn antall Pizzaer")
        print("3. Oppgave 3: Konverter grader til radianer")
        print("4. Oppgave 4: Informasjon av land og bruk av dictionary")
        print("5. Oppgave 5: Beregn areal og ytre Omkrets")
        print("6. Oppgave 6: Plotting av Funksjon")
        print("0. Avslutt")
        
        valg = input("Skriv inn ditt valg (0-6): ")
        
        if valg == '1':
            oppg1_main()
        elif valg == '2':
            oppg2_main()
        elif valg == '3':
            oppg3_main()
        elif valg == '4':
            oppg4_main()
        elif valg == '5':
            oppg5_main()
        elif valg == '6':
            oppg6_main()
        elif valg == '0':
            print("Avslutter programmet")
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

if __name__ == "__main__":
    main()