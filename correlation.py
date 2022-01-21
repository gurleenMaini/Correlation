import numpy as np 
import csv
import pandas as pd 
import plotly.express as px

with open("data.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
    fig.show()
def getDataSource(data_path):
    coffeeInMl= []
    sleepInHrs= []
    with open(data_path) as csvFile:
        csvReader= csv.DictReader(csvFile)
        for row in csvReader:
            coffeeInMl.append(float(row["Coffee in ml"]))
            sleepInHrs.append(float(row["sleep in hours"]))
    return {"x": coffeeInMl, "y": sleepInHrs}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print("Correlation between coffee in ml vs sleep in hours ")
    print(correlation)

def setUp():
    data_path= "data.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
setUp()