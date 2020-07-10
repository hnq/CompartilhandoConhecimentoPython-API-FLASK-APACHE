#EXEMPLO WebService Simples com GET
#DESENVOLVEDOR: HENRIQUE MANOEL DE CAMPOS
#LINKEDIN: https://www.linkedin.com/in/henrique-manoel-de-campos-962248143/
#EMAIL: hnq_campos@hotmail.com
#Premissas:
#	Python: https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe 
#	PIP: https://pip.pypa.io/en/stable/installing/
#	VSCode: https://code.visualstudio.com/
#	Postman: https://www.postman.com/downloads/
#	Apache: https://httpd.apache.org/download.cgi#apache24
#          Lembrando coloquei um ZIP do Apache junto com esse projeto
 
# dando imports de libs no Python
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from datetime import date

objFlaskApp = Flask(__name__)
objAPI = Api(objFlaskApp)

class Relogio(Resource):
    def get(self):
        dDataHoje = date.today()
        print(dDataHoje)    
        result= dDataHoje 
        return jsonify({"DataHoje:":result})

objAPI.add_resource(Relogio, '/datahoje') 

if __name__ == '__main__':
    objFlaskApp.run()        