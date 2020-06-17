import os
import pandas as pd


#get data from CSV file
PIE_PATH="/Users/fabrice/Documents/chartJS/tutoChartJS/chart/datas"

def get_pie_data(path=PIE_PATH, filename="sample-pie-data.csv"):
    csv_path = os.path.join(path, filename)
    
    return pd.read_csv(csv_path)


if __name__ == "__main__":
    data = get_pie_data()
    print(data.head())

    print(type(data["Value"]))