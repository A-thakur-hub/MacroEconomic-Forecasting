from fredapi import Fred
import pandas as pd


fred = Fred(api_key='API_KEY')


indicators = {
    'GDP': 'Gross Domestic Product (current $)',
    'UNRATE': 'Unemployment Rate',
    'CPIAUCSL': 'Consumer Price Index',
    'FEDFUNDS': 'Federal Funds Rate',
    'INDPRO': 'Industrial Production Index',
    'RSXFS': 'Advance Retail Sales: Retail Trade'
}


def fetch_2023_data(fred, indicators):
    
    data_2023 = {}
    start_date = '2013-01-01'
    end_date = '2023-12-31'
    
    for code, name in indicators.items():
        try:
            
            series = fred.get_series(code, start_date=start_date, end_date=end_date)
            if not series.empty:  # Check if series is not empty
                series_2023 = series[series.index.year == 2023]
                if not series_2023.empty:
                    data_2023[name] = series_2023
                else:
                    print(f"No data available for {name} ({code}) for the year 2023.")
            else:
                print(f"No data available for {name} ({code}) for the year 2023.")
        except Exception as e:
            print(f"Could not retrieve data for {name} ({code}): {e}")

    # Convert to a DataFrame
    if data_2023:
        data_2023_df = pd.DataFrame(data_2023)
        return data_2023_df
    else:
        return None

data_2023 = fetch_2023_data(fred, indicators)

if data_2023 is not None:
    csv_filename = 'economic_indicators_2023.csv'
    data_2023.to_csv(csv_filename)
    
    print(f"Data saved to {csv_filename}")
else:
    print("No data was retrieved for the specified indicators.")