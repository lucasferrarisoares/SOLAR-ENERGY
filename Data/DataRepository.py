from conectionDataBase import conection
from Data.DataModel import DataModel

class DataRepository:
    def __init__(self):
        self.db_connection = conection


    def saveData(self, dataModel):
        cursor = self.db_connection.cursor()
        cursor.execute(
            """
            INSERT INTO DataModel (date, energy_generation, temperature, performance)
            VALUES (%s, %s, %s, %s)
            """,
            (dataModel.date, dataModel.energy_generation, dataModel.temperature, dataModel.performance)
        )
        self.db_connection.commit()
        cursor.close()

    def updateData(self, dataModel):
        cursor = self.db_connection.cursor()
        cursor.execute(
            """
            UPDATE DataModel
            SET energy_generation = %s, temperature = %s, performance = %s
            WHERE date = %s
            """,
            (dataModel.energy_generation, dataModel.temperature, dataModel.performance, dataModel.date)
        )
        self.db_connection.commit()
        cursor.close()

    def deleteData(self, date):
        cursor = self.db_connection.cursor()
        cursor.execute(
            """
            DELETE FROM DataModel
            WHERE date = %s
            """,
            (date,)
        )
        self.db_connection.commit()
        cursor.close()

    def getDataModels(self, where_clause=None, params=None):
        cursor = self.db_connection.cursor()

        query = "SELECT * FROM DataModel"
        if where_clause:
            query += f" {where_clause}"

        cursor.execute(query, params or ())
        rows = cursor.fetchall()
        cursor.close()

        return [
            DataModel(
                id=row[0],
                date=row[1].strftime("%d/%m/%Y"),
                energy_generation=row[2],
                temperature=row[3],
                performance=row[4] * 100
            )
            for row in rows
        ]

    
    def getDataModelsJson(self, function):
        result = [
            {
                "date": dm.date,
                "energy_generation": dm.energy_generation,
                "temperature": dm.temperature,
                "performance": dm.performance
            }
            for dm in function
        ]
        return result
    
    
    def getDataModelByDate(self, date):
        cursor = self.db_connection.cursor()
        cursor.execute(
            """
            SELECT * FROM DataModel
            WHERE date = %s
            """,
            (date,)
        )
        data_model = cursor.fetchone()
        cursor.close()

        if data_model:
            return DataModel(
                id=row[0],
                date=row[1].strftime("%d/%m/%Y"),
                energy_generation=row[2],
                temperature=row[3],
                performance=row[4] * 100
            )
        return None