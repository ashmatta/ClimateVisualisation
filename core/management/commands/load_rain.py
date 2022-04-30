import csv
from datetime import date
from itertools import islice
import pathlib
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import avgRain


class Command(BaseCommand):
    help = 'Load data from Rain file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / 'rain.csv'

        with open(datafile, newline='') as csvfile:
            reader = csv.DictReader(islice(csvfile, 0, None))
            for row in reader:
                dt = date(
                    year=int(row['Year']),
                    month=int(row['Month']),
                    day=1
                )
                avgRain.objects.get_or_create(date=dt, average=row['Rainfall'])