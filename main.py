import pandas as pd
from flask import Flask
from Data.DataModel import DataModel
from Data.DataController import DataController 
from routs import register_routes

app = Flask(__name__)
controller = DataController()
register_routes(app)

def readData():
    return dataProcessing(pd.read_excel('DataModel.xlsx'))

def dataProcessing(data):
    models = []
    for _, row in data.iterrows():
        model = DataModel(
            date=row.get('data'),
            energy_generation=row.get('geração_energetica_kwh'),
            temperature=row.get('temperatura_inversor'),
            performance=row.get('rendimento_inversor')
        )
        models.append(model)
    return models

def main():
    listData = controller.getAllData()
    if listData == []:
        listData = readData()
        for model in listData:
            controller.saveData(model)
    app.run()

if __name__ == "__main__":
    main()
        
        