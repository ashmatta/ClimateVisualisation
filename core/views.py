from cProfile import label
from multiprocessing import context
from turtle import color, title
from django.shortcuts import render
from core.models import avgTemp
from core.models import avgRain
import plotly.express as px
from core.forms import DateForm


# Create your views here.
def chart(request):
    temp = avgTemp.objects.all()

    fig = px.scatter(
        x=[t.date for t in temp],
        y=[t.average for t in temp],
        color =[t.average for t in temp],
        color_continuous_scale='Inferno', 
        title='Kenya Yearly Temperature Avarage',
        labels= {'x':'Date', 'y': 'Temp (Celceius)'}
    )

    fig.update_layout(title={
        'font_size': 22,
        'xanchor': 'center',
        'x': 0.5
    })

    chart = fig.to_html()



    rain = avgRain.objects.all()

    fig2 = px.bar(
        x=[t.date for t in rain],
        y=[t.average for t in rain],
        color =[t.average for t in rain],
        color_continuous_scale='pubu',
        title='Kenya Yearly Rainfall Avarage',
        labels= {'x':'Date', 'y': 'Rainfall (mm)'}
    )

    fig2.update_layout(title={
        'font_size': 22,
        'xanchor': 'center',
        'x': 0.5
    })

    chart2 = fig2.to_html()


    context = {'chart': chart+chart2, 'form': DateForm()}
    return render(request, 'core/chart.html', context)


