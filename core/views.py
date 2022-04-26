from cProfile import label
from multiprocessing import context
from turtle import title
from django.shortcuts import render
from core.models import avgTemp
import plotly.express as px


# Create your views here.
def chart(request):
    temp = avgTemp.objects.all()

    fig = px.line(
        x=[t.date for t in temp],
        y=[t.average for t in temp],
        title='Kenya Yearly Temperature Avarage',
        labels= {'x':'Date', 'y': 'Temp (Celceius)'}
    )

    chart = fig.to_html()

    context = {'chart': chart}
    return render(request, 'core/chart.html', context)
