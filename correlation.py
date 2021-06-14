import numpy as np
import plotly.express as px
import csv

def get_data_source(data_path):
    days_present = []
    marks_in_percent = []

    with open(data_path) as file:
        reader = csv.DictReader(file)

        for row in reader:
            days_present.append(float(row["Days Present"]))
            marks_in_percent.append(float(row["Marks In Percentage"]))

        return {"x" : days_present, "y" : marks_in_percent}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between number of days present and marks is" , correlation[0,1])

def setup():
    data_path = "marks-dayspresent.csv"

    data_source = get_data_source(data_path)
    find_correlation(data_source)

setup()