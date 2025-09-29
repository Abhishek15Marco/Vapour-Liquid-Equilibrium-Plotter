import sys, os

# Add project root to Python path so it can find "src"
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.vle_plotter import plot_vle #, plot_multiple_vle

def main():
    print("Ethanol-Water VLE Visualization")

    # Example A : Single curve at 78 °C
    print("Plotting at 78 °C.")
    plot_vle(T=78)

    # Example B : Comparing at multiple temperatures
    # print("Plotting at 60 °C, 78 °C, 90 °C.")
    # plot_multiple_vle([60, 78, 90])

if __name__ == "__main__":
    main()
