from cProfile import label
from multiprocessing import context
from turtle import title
from django.shortcuts import render
from core.models import avgTemp
from core.models import avgRain
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

    rain = avgRain.objects.all()

    fig2 = px.line(
        x=[t.date for t in rain],
        y=[t.average for t in rain],
        title='Kenya Yearly Rainfall Avarage',
        labels= {'x':'Date', 'y': 'Rainfall (mm)'}
    )

    chart2 = fig2.to_html()


    context = {'chart': chart+chart2}
    return render(request, 'core/chart.html', context)


def chart2(request):
    rain = avgRain.objects.all()

    fig = px.line(
        x=[t.date for t in rain],
        y=[t.average for t in rain],
        title='Kenya Yearly Rainfall Avarage',
        labels= {'x':'Date', 'y': 'Rainfall (mm)'}
    )

    chart2 = fig.to_html()

    context = {'chart': chart2}
    return render(request, 'core/chart.html', context)