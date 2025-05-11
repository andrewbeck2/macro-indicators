from fredapi import Fred
import pandas as pd
import matplotlib.pyplot as plt

# Add your API key here
FRED_API_KEY = '03ba0d7fd7fc4014e5de737ad375fc21'
fred = Fred(api_key=FRED_API_KEY)

# Indicator mapping
INDICATORS = {
    1: ('US GDP (Quarterly)', 'GDP'),
    2: ('Unemployment Rate', 'UNRATE'),
    3: ('CPI All Urban Consumers', 'CPIAUCSL')
}

def main():
    print("Available Indicators:")
    for k, v in INDICATORS.items():
        print(f"{k}: {v[0]}")
    
    try:
        choice = int(input("Enter the number of the indicator you want to graph: "))
        start = input("Enter start date (YYYY-MM-DD): ")
        end = input("Enter end date (YYYY-MM-DD): ")

        if choice not in INDICATORS:
            print("Invalid choice.")
            return

        name, code = INDICATORS[choice]
        data = fred.get_series(code, observation_start=start, observation_end=end)

        data.plot(title=name)
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.grid(False)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
