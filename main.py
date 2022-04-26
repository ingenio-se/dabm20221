# -*- coding: utf-8 -*-

from flask import Flask, render_template,request
import os
import random

app = Flask(__name__)

@app.route('/login')
def inicio():
    return render_template('inicio.html')

@app.route('/componentes')
def componentes():
    return render_template('login.html')

@app.route('/validar',methods=["POST"])
def validar():
    if request.method == "POST": 
        usuario = request.form['usuario']
        password = request.form['password']
        accion = request.form['accion']
        print("Accion:",accion)
        
        return render_template('menu.html',title='SISTEMA DE MONITOREO')

@app.route('/monitoreo')
def monitoreo():
    datos = getParametros()
    print(datos)
    
    #lectura = random.randint(0,50)
    #color=0
    
    lecturas =[]
    for i in range(0,100):
        lectura = random.randint(0,50)
        lecturas.append(lectura)
    
    colores=[]
    for lectura in lecturas:
        color=0
        '''
        condicionales
        '''
        if int(datos[0][1]) <= lectura and int(datos[0][2]) >= lectura:
            color=1
        if int(datos[1][1]) <= lectura and int(datos[1][2]) >= lectura:
            color=2
        if int(datos[2][1]) <= lectura and int(datos[2][2]) >= lectura:
            color=3
        
        colores.append(color)
    
    return render_template('monitor.html',datos=datos,lecturas=lecturas,colores=colores)
    
        
def getParametros():
    directorio = os.path.dirname(__file__)
    archivo = 'static/parametros.csv'
    ruta = os.path.join(directorio,archivo)
    
    f = open(ruta,'r')
    lineas = f.readlines()
    f.close()
    
    datos=[]
    for l in lineas:
        l=l.replace("\n","")
        l=l.split(";")
        datos.append(l)
        
    return datos    

if __name__ == "__main__":
    app.run(debug=True)