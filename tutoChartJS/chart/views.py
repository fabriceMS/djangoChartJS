from django.shortcuts import render
from chart import data
import pandas as pd
from datetime import datetime, timedelta

# Display home page
def home(request):

    csv_data = data.get_data()

    csv_data_bar = data.get_data(filename='sample-bar-data.csv', separator=";")


    csv_data_bar['Date'] = pd.to_datetime(csv_data_bar['Date'])
    csv_data_bar.sort_values('Date', inplace=True)


    context = {
        'title': "Population (millions)",
        'labels': csv_data["Countries"].tolist(),
        'data': csv_data["Value"].tolist(),
        'backgroundColor': ["#a8d8ea", "#aa96da","#fcbad3","#ffffd2","#c45850"],
        'Date': csv_data_bar['Date'].astype(str).tolist(),
        #'trans': csv_data_bar['Nombre total de transactions'].str.replace(',', '.').astype(float),
        'srv_time': csv_data_bar["HTTP server time"].tolist(),
  
    }
    

    return render(request, 'chart/index.html', context)

