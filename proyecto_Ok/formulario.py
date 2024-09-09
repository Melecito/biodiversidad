from flask import Flask, request, render_template, url_for, redirect

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def contactanos():
    return render_template('contactanos.html')

@app.route("/guardar_datos",  methods=["POST"])

def guardar_datos():
    Nombres = request.form['Nombre'];
    print('aaaa', Nombres)
    Apellidos = request.form['Apellido'];
    Correo = request.form['Correo'];
    Celular = request.form['Celular'];
    Comentarios = request.form['Comentario'];
    fecha_hora = datetime.now().strftime("%Y-%M-%D, %H:%M:%S");
    print(fecha_hora)
    
    with open('registro_personas.csv', 'a') as archivo:
        archivo.write(f"{Nombres},{Apellidos},{Correo},{Celular},{Comentarios},{fecha_hora}\n")

    return redirect(url_for('confirmacion', nombre=Nombres))

@app.route("/confirmacion")
def confirmacion():
    nombre = request.args.get('nombre'),
    return render_template('confirmacion.html', nombre=nombre) 

@app.route('/Ecosistemas')
def Ecosistemas():
    return render_template('Ecosistemas.html')

@app.route('/Fauna')
def Fauna():
    return render_template('Fauna.html')

@app.route('/index_biodiversidad')
def index_biodiversidad():
    return render_template('index_biodiversidad.html') 

@app.route('/Flora_Boyaca_y_Cundinamarca')
def Flora_Boyaca_y_Cundinamarca():
    return render_template('Flora_Boyaca_y_Cundinamarca.html')

@app.route('/introduccion')
def introduccion():
    return render_template('introduccion.html') 

@app.route('/mapa_interactivo')
def mapa_interactivo():
    return render_template('mapa_interactivo.html')

@app.route('/REFERENCIAS')
def REFERENCIAS():
    return render_template('REFERENCIAS.html') 


if(__name__ == '__main__'):
    app.run(debug=True)