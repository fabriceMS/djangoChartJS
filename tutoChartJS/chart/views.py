from django.shortcuts import render
from chart import data

# Display home page
def home(request):

    csv_data = data.get_pie_data()



    context = {
        'title': "Population (millions)",
        'labels': csv_data["Countries"].tolist(),
        'data': csv_data["Value"].tolist(),
        'backgroundColor': ["#a8d8ea", "#aa96da","#fcbad3","#ffffd2","#c45850"],
  
    }

    return render(request, 'chart/index.html', context)

