import csv
from datetime import date
from itertools import islice
import pathlib
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import avgTemp


class Command(BaseCommand):
    help = 'Load data from Temp file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / 'temp.csv'

        with open(datafile, newline='') as csvfile:
            reader = csv.DictReader(islice(csvfile, 0, None))
            for row in reader:
                dt = date(
                    year=int(row['Year']),
                    month=int(row['Month']),
                    day=1
                )
                avgTemp.objects.get_or_create(date=dt, average=row['Temperature'])