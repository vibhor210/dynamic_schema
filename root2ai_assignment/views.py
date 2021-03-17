from django.shortcuts import render
from django.db import connection

def index(request):
    if request.method == "POST":
        if request.POST.get("table_name"):
            column = ""
            no_of_column = request.POST.get("no_of_column")
            data_type = (request.POST.get("data_type")).split(",")
            for i in range(1,int(no_of_column)+1):
                if i <= len(data_type):
                    column = column + f''' "column{i}" {data_type[i-1]}'''
                else:
                    column = column + f''' "column{i}" varchar(200)'''

                if i != int(no_of_column):
                    column = column + ",\n"    
            cursor = connection.cursor()
            cursor.execute(f''' CREATE SCHEMA IF NOT EXISTS {request.POST.get("schema_name")};

            CREATE TABLE {request.POST.get("schema_name")}.{request.POST.get("table_name")} 
            ({column}); ''')
        
        return render(request, "index.html")

    return render(request, "index.html")
