import numpy as np
# using numpy library
import matplotlib.pyplot as plt
# using matplot to plot

# Taking binary system of Water and Ethanol
# Antoine equation to find P_sat
# Antoine eq: log10(P_sat) = A - B / (C + T)
# P in mmHg, T in deg C

antoine_constants = {
    "water": {"A": 8.07131, "B": 1730.63, "C": 233.426},
    "ethanol": {"A": 8.20417, "B": 1642.89, "C": 230.3}
}

def antoine_pressure(A, B, C, T):
    # For finding P_sat
    return 10 ** (A - (B / (C + T)))

def vle_curve(T=78):

    # Calculating VLE curve for water-ethanol at constant temperature
    # Pure component vapor pressures

    P_water   = antoine_pressure(**antoine_constants["water"], T=T)
    P_ethanol = antoine_pressure(**antoine_constants["ethanol"], T=T)
        
    x1 = np.linspace(0, 1, 100)   # mole fraction ethanol in liquid
    y1 = (x1 * P_ethanol) / (x1 * P_ethanol + (1 - x1) * P_water)
    x2 = 1 - x1
    y2 = 1 - y1
    z1 = P_water
    z2 = P_ethanol
    
    return x1, y1, x2, y2, z1, z2

def plot_vle(T=78):
    # Plotting x-y VLE curve
    x1, y1, x2, y2, z1, z2= vle_curve(T)

    plt.figure(figsize=(8,6))
    plt.plot(x1, y1, label=f"T = {T} °C (Vapor Pressure Ethanol)")
    plt.plot(x1, (x1*z1), 'k--', label="y = x (Liquid Pressure Ethanol)")
    plt.plot(x1, y2, label=f"T = {T} °C (Vapor Pressure Water)")
    plt.plot([x1,(x1*z2), 'k--', label="y = -x (Liquid Pressure Ethanol)")
    
    plt.xlabel("Liquid Mole Fraction Ethanol (x1)")
    plt.ylabel("Vapor Mole Fraction Ethanol (y1)")
    plt.title("VLE Diagram: Ethanol-Water (Raoult's Law)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_vle()
