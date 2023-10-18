from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.viaje import viaje, viajeschema
from models.pasajero import pasajero, pasajeroschema

ruta_viaje = Blueprint("ruta_viaje",__name__)

viaje_schema = viajeschema()
viajes_schema = viajeschema(many=True)

@ruta_viaje.route('/viaje', methods=['GET'])
def Viajes():
    resultall = viaje.query.all() # Select * from Pasajeros
    resultado_pago = viajes_schema.dump(resultall)
    return jsonify(resultado_pago)

@ruta_viaje.route('/saveviaje', methods=['POST'])
def save():
    idPasajero = request.json['idpasajero']
    hr = request.json['hr']
    trayecto = request.json['trayecto']
    new_viaje = viaje(
        idPasajero,
        hr,
        trayecto
    )
    db.session.add(new_viaje)
    db.session.commit()
    return "Datos guardados con éxito"

@ruta_viaje.route('/updateviaje', methods=['PUT'])
def Update():
    id = request.json['id']
    idPasajero = request.json['idpasajero']
    hr = request.json['hr']
    trayecto = request.json['trayecto']
    viajes = viaje.query.get(id)
    if viajes:
        print(viajes)
        viajes.idpasajero = idPasajero
        viajes.hr = hr
        viajes.trayecto = trayecto
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"
    
@ruta_viaje.route("/deleteviaje/<id>", methods=["DELETE"])
def eliminar(id):
    viaj = viaje.query.get(id)
    db.session.delete(viaj)
    db.session.commit()
    return jsonify(
        viaje_schema.dump(viaj),
    )

# ---------------- Relación viajes/pasajero ----------------------------------------------------------------
@ruta_viaje.route('/relacionviaje', methods=['POST'])
def dostabla():
    datos = {}
    resultadorelacion = db.session.query(pasajero,viaje). \
        select_from(pasajero).join(viaje).all()
    i=0
    for pasajeros, viajes in resultadorelacion:
        i+=1
        datos[i]={
            'pasajero':pasajeros.id,
            'viaje': viajes.id, 
        }
    return datos