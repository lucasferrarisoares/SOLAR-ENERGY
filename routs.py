from flask import render_template
from Data.DataController import DataController

controller = DataController()

def register_routes(app):

    @app.route('/')
    def home():
        return render_template('index.html')
    
    app.add_url_rule('/api/data', view_func=controller.getAllDatajson)

    @app.route('/api/filtertemp/<temp>')
    def filter_temp(temp):
        return controller.filterbytempjson(temp)
    
    @app.route('/api/filterdate/<date>')
    def filter_date(date):
        return controller.filterbydatejson(date)