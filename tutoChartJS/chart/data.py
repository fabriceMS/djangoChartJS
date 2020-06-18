import os
import pandas as pd
from datetime import datetime, timedelta


# Global variable
PIE_PATH="/Users/fabrice/Documents/chartJS/tutoChartJS/chart/datas"


# Get Pie data
def get_data(path=PIE_PATH, filename="sample-pie-data.csv", separator=','):
    csv_path = os.path.join(path, filename)
    
    return pd.read_csv(csv_path, sep=separator)






#####################
#       MAIN        #
#####################
if __name__ == "__main__":
    data = get_data(filename='sample-bar-data.csv', separator=";")
    print(data.head())

    # Convert the Date field into a python DateTime and sort it (instead of string)
    data['Date'] = pd.to_datetime(data['Date'])
    data.sort_values('Date', inplace=True)

    print (data["HTTP server time"].tolist())

    #print(data['Nombre total de transactions'].str.replace(',', '.').astype(float))