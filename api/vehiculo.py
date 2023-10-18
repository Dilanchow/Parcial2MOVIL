from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vehiculo import vehiculo, vehiculochema
from models.viaje import viaje, viajeschema

ruta_vehiculo = Blueprint("ruta_vehiculo",__name__)

vehiculo_schema = vehiculochema()
vehiculos_schema = vehiculochema(many=True)

@ruta_vehiculo.route('/vehiculo', methods=['GET'])
def Vehiculos():
    resultall = vehiculo.query.all() # Select * from Pasajeros
    resultado_vehiculo = vehiculos_schema.dump(resultall)
    return jsonify(resultado_vehiculo)

@ruta_vehiculo.route('/savevehiculo', methods=['POST'])
def save():
    placa = request.json['placa']
    capacidad = request.json['capacidad']
    new_vehiculo = vehiculo(
        placa,
        capacidad
    )
    db.session.add(new_vehiculo)
    db.session.commit()
    return "Datos guardados con éxito"

@ruta_vehiculo.route('/updatevehiculo', methods=['PUT'])
def Update():
    id = request.json["id"]
    placa = request.json['placa']
    capacidad = request.json['capacidad']
    vehiculos = vehiculo.query.get(id)
    if vehiculos:
        print(vehiculos)
        vehiculos.placa = placa
        vehiculos.capacidad = capacidad

        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"
    
@ruta_vehiculo.route("/deletevehiculo/<id>", methods=["DELETE"])
def eliminar(id):
    solicitud = vehiculo.query.get(id)
    db.session.delete(solicitud)
    db.session.commit()
    return jsonify(
        vehiculo_schema.dump(solicitud),
    )

# ---------------- Relación Vehiculo/Viaje ----------------------------------------------------------------
@ruta_vehiculo.route('/relacion', methods=['POST'])
def dostabla():
    datos = {}
    resultadorelacion = db.session.query(vehiculo,viaje). \
        select_from(vehiculo).join(viaje).all()
    i=0
    for vehiculos, viajes in resultadorelacion:
        i+=1
        datos[i]={
            'vehiculo':vehiculos.id,
            'viaje': viajes.id, 
        }
    return datos