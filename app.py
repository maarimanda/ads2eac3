import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def sequencia_fibonacci():
   proximo = 1
   anterior = 0
   limite = 100
   found = 0
   resposta = "0,"
   while (found < limite):
       found=found+1 
       if (found):
           tmp = proximo
           proximo = proximo + anterior
           anterior = tmp
           resposta+= str(proximo) + ","
           if (found % 5 == 0):
               resposta = resposta + "<br>" 

   return resposta

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
