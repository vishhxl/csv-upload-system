import csv
from django.shortcuts import render
from .models import Record

def upload_csv(request):
    message = ""

    if request.method == 'POST':
        file = request.FILES['file']
        data = file.read().decode('utf-8').splitlines()
        reader = csv.reader(data)

        next(reader)

        for row in reader:
            Record.objects.get_or_create(
                name=row[0],
                email=row[1],
                age=row[2]
            )

        message = "File Uploaded Successfully ✅"

    return render(request, 'upload.html', {'message': message})


def show_data(request):
    data = Record.objects.all()
    return render(request, 'data.html', {'data': data})