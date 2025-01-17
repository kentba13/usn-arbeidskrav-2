import numpy as np
import matplotlib.pyplot as plt

def calculate_plots(x):
    """
    Beregner verdiene av funksjonen f(x) = -x^2 - 5.
    """
    return -x**2 - 5

#Plot funksjon
def plot_function(x, y):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label = r'$f(x) = -x^2 - 5$')
    plt.title('Graf av funksjonen f(x) = -x² - 5')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)  # X-akse
    plt.axvline(0, color='black', linewidth=0.5)  # Y-akse
    plt.show()

def main():
    try:
        # Definer intervallet [-10, 10] med 200 jevnt fordelte punkter
        x = np.linspace(-10, 10, 200)
        
        # Beregn f(x) for hver x
        y = calculate_plots(x)
        
        # Plot funksjonen
        plot_function(x, y)
    
    except Exception as e:
        print(f"En feil oppstod: {e}")

if __name__ == "__main__":
    main()