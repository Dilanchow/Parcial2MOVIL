from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pasajero import pasajero, pasajeroschema
# from models.pasajero import Pasajero, PasajerosSchema

ruta_pasajero = Blueprint("ruta_pasajero",__name__)

pasajero_schema = pasajeroschema()
pasajeros_schema = pasajeroschema(many=True)

@ruta_pasajero.route('/pasajero', methods=['GET'])
def pagos():
    resultall = pasajero.query.all() # Select * from Pasajeros
    resultado_pago = pasajeros_schema.dump(resultall)
    return jsonify(resultado_pago)

@ruta_pasajero.route('/savepasajero', methods=['POST'])
def save():
    idPasajero = request.json['idpasajero']
    nombrepasajero = request.json['nombre']
    telefonopasajero = request.json['telefono']
    ubicacionpasajero = request.json['ubicacion']
    apellidopasajero = request.json['apellido']
    new_pago = pasajero(
        idPasajero,
        nombrepasajero,
        telefonopasajero,
        ubicacionpasajero,
        apellidopasajero
    )
    db.session.add(new_pago)
    db.session.commit()
    return "Datos guardados con éxito"

@ruta_pasajero.route('/updatepasajero', methods=['PUT'])
def Update():
    id = request.json['id']
    idPasajero = request.json['idpasajero']
    nombrepasajero = request.json['nombre']
    telefonopasajero = request.json['telefono']
    ubicacionpasajero = request.json['ubicacion']
    apellidopasajero = request.json['apellido']
    
    pagos = pasajero.query.get(id)
    if pagos:
        print(pagos)
        pagos.idpasajero = idPasajero
        pagos.nombre = nombrepasajero
        pagos.telefono = telefonopasajero
        pagos.ubicacion = ubicacionpasajero
        pagos.apellido = apellidopasajero
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_pasajero.route("/deletepasajero/<id>", methods=["DELETE"])
def eliminar(id):
    pasajeros = pasajero.query.get(id)
    db.session.delete(pasajeros)
    db.session.commit()
    return jsonify(
        pasajero_schema.dump(pasajeros),
    )