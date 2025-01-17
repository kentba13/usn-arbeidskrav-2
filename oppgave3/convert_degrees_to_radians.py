import numpy as np

#Convert degrees to radians.
def degrees_to_radians(degrees):
    return degrees * np.pi / 180

def main():
    try:
        degrees = float(input('Skriv inn grader: '))
        radians = degrees_to_radians(degrees)
        print(f"Radian tallet er {radians}.")
    except ValueError:
        print("Det skjedde en feil, vennligst prøv igjen.")

if __name__ == "__main__":
    main()