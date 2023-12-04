from flask import Flask, render_template, flash, request, Response, jsonify, redirect, url_for
from database import app, db, EstudianteSchema
from personaje import Personaje

student_schema = EstudianteSchema()
students_schema = EstudianteSchema(many=True)

@app.route('/')
def home():
    personaje = Personaje.query.all()
    estudiantesLeidos = students_schema.dump(personaje)
    return render_template('index.html', personaje = estudiantesLeidos)

@app.route('/agregar', methods=['POST'])
def addEstudiante():
    nombre = request.form['nombre']
    alterego = request.form['alterego']
    tipo = request.form['tipo']

    if nombre and alterego and tipo:
        nuevo_estudiante = Personaje(nombre, alterego, tipo)
        db.session.add(nuevo_estudiante)
        db.session.commit()
        response = jsonify({
            'nombre' : nombre,
            'alterego' : alterego,
            'tipo' : tipo
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete
@app.route('/eliminar/<id>')
def deleteEstudiante(id):
     personaje = Personaje.query.get(id)
     db.session.delete(personaje)
     db.session.commit()
    
     flash('Personaje ' + id + ' eliminado correctamente')
     return redirect(url_for('home'))

# #Method Put
@app.route('/actualizar/<id>', methods=['POST'])
def editEstudiante(id):    
    
    nombre = request.form['nombre']
    alterego = request.form['alterego']
    tipo = request.form['tipo']

    if nombre and alterego and tipo:
        personaje = Personaje.query.get(id)
        # return student_schema.jsonify(personaje)
        personaje.nombre = nombre
        personaje.alterego = alterego
        personaje.tipo = tipo
        
        db.session.commit()
        
#         response = jsonify({'message' : 'Estudiante ' + id + ' actualizado correctamente'})
        flash('Personaje ' + id + ' modificado correctamente')
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
