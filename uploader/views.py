import csv
from django.shortcuts import render
from .models import Record


def upload_csv(request):
    message = ""

    if request.method == 'POST':
        file = request.FILES.get('file')

        # ❌ No file selected
        if not file:
            return render(request, 'upload.html', {'message': 'Please select a file ❌'})

        # ❌ Only CSV allowed
        if not file.name.endswith('.csv'):
            return render(request, 'upload.html', {'message': 'Only CSV file allowed ❌'})

        try:
            data = file.read().decode('utf-8').splitlines()
            reader = csv.reader(data)

            next(reader)  # skip header

            for row in reader:
                # ❌ skip empty rows
                if not row:
                    continue

                # ✅ avoid duplicates
                Record.objects.get_or_create(
                    name=row[0],
                    email=row[1],
                    age=row[2]
                )

            message = "File Uploaded Successfully ✅"

        except Exception as e:
            message = f"Error: {str(e)} ❌"

    return render(request, 'upload.html', {'message': message})


def show_data(request):
    data = Record.objects.all()
    return render(request, 'data.html', {'data': data})