import math

def calculate_area_and_perimeter(a, b):
    # Hypotenus
    c = math.sqrt(a**2 + b**2)
    
    # Areal av trekanten
    area_triangle = (a * b) / 2
    
    # Areal av halvsirkelen
    radius = (a * b) / 2
    area_semicircle = (math.pi * radius**2) / 2 #** er "power of" operator
    
    # Totalt areal
    total_area = area_triangle + area_semicircle
    
    # Ytre omkrets
    circumference = a + b + (math.pi * radius)
    
    return total_area, circumference

def main():
    try:
        # Input for a og b
        a = float(input('Skriv inn lengden av katet a: '))
        b = float(input('Skriv inn lengden av katet b: '))
        
        if a <= 0 or b <= 0:
            print("Lengdene må være positive tall.")
            return
        
        # Beregn areal og omkrets
        area, circumference = calculate_area_and_perimeter(a, b)
        #:.3f er en format specifier for å oppgi 3 desimaler
        print(f"Arealet av figuren er {area:.3f} kvadratmeter.")
        print(f"Den ytre omkretsen av figuren er {circumference:.3f} meter.")    
    except ValueError:
        print("Det skjedde en feil, vennligst prøv igjen.")

if __name__ == "__main__":
    main()