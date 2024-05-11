from flask import Flask
from flask_restful import Resource, Api

App = Flask(__name__)

api = Api(App)

fakeDatabase = {
    1:{'name':'Clean car'},
    2:{'name':'Write blog'},
    3:{'name':'Start stream'},
}

class Items(Resource):
    def get(self):
        return fakeDatabase
    
    def post(input_dict):
        fakeDatabase[len(fakeDatabase.keys())+1] = input_dict

api.add_resource(Items, '/')

if __name__ == "__main__":
    App.run(debug=True)

