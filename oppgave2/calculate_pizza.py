import math
from utils.constants import PIZZA_PER_STUDENT

#Kalkulerer pizzaer basert på antall elever
def calculate_pizzas(number_of_students):
    # Runder opp til heltall
    return math.ceil(number_of_students * PIZZA_PER_STUDENT)

def main():
    try:
        student_amount = int(input('Antall elever: '))
        if student_amount < 0:
            print("Antall elever kan ikke være negativt.")
            return
        
        pizza_amount = calculate_pizzas(student_amount)
        #f-string literal for uttrykk i streng
        print(f"{pizza_amount} pizza(er) må kjøpes til festen.")
    except ValueError:
        print("Det skjedde en feil, vennligst prøv igjen.")

if __name__ == "__main__":
    main()
