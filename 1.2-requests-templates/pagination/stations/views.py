from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from csv import DictReader
from pagination.settings import BUS_STATION_CSV

PAGE_COUNT = 10
DEFUALT_PAGE_COUNT = 1


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stations = []
    with open(BUS_STATION_CSV, 'r', encoding='utf-8') as csv_file:
        file_object = DictReader(csv_file)
        line_count = 0
        for row in file_object:
            if line_count == 0:
                line_count += 1
            else:
                bus_stations.append(row)
    page_number = int(request.GET.get('page', DEFUALT_PAGE_COUNT))
    paginator = Paginator(bus_stations, PAGE_COUNT)
    page = paginator.page(page_number)
    context = {
         'bus_stations': page.object_list,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
