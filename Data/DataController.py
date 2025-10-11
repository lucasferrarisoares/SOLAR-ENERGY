from Data.DataRepository import DataRepository
from flask import jsonify

class DataController:
    def __init__(self):
        self.repository = DataRepository()


    def saveData(self, dataModel):
        return self.repository.saveData(dataModel)

    def updateData(self, dataModel):
        return self.repository.updateData(dataModel)

    def deleteData(self, data):
        return self.repository.deleteData(data)

    def getAllDatajson(self):
        return jsonify(self.repository.getDataModelsJson(self.repository.getDataModels()))
    
    def getAllData(self):
        return self.repository.getDataModels()
    
    def filterbytempjson(self, temp):
        return jsonify(self.repository.getDataModelsJson(self.repository.getDataModels("WHERE temperature = %s", (temp,))))
    
    def filterbydatejson(self, date):
        return jsonify(self.repository.getDataModelsJson(self.repository.getDataModels("WHERE date = %s", (date,))))