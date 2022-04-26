from multiprocessing import context
from django.shortcuts import render
from core.models import avgTemp
import plotly.express as px


# Create your views here.
def chart(request):
    temp = avgTemp.objects.all()

    fig = px.line(
        x=[t.date for t in avgTemp],
        y=[t.average for t in avgTemp]
    )

    chart = fig.to_html()

    context = {'chart': chart}
    return render(request, 'core/chart.html', context)
