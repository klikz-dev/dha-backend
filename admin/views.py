import csv
from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path

from membersuite.models import Membership


BASE_DIR = Path(__file__).resolve().parent.parent


def index(request):
    context = {}
    return render(request, BASE_DIR / 'templates/admin/home.html', context)


def exportcsv(request):
    memberships = Membership.objects.all()
    response = HttpResponse('text/csv')

    response['Content-Disposition'] = 'attachment; filename=memberships.csv'
    writer = csv.writer(response)

    writer.writerow(['Email', 'Membership', 'Acute',
                    'Ambulatory', 'LTPAC', 'Organization Name'])

    rows = memberships.values_list(
        'email', 'membership', 'acute', 'ambulatory', 'ltpac', 'organization_name')

    for row in rows:
        writer.writerow(row)
    return response
