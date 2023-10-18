from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.solicitud import solicitud, solicitudschema
from models.pasajero import pasajero, pasajeroschema

ruta_solicitud = Blueprint("ruta_solicitud",__name__)

solicitud_schema = solicitudschema()
solicitudes_schema = solicitudschema(many=True)

@ruta_solicitud.route('/solicitud', methods=['GET'])
def Solicitudes():
    resultall = solicitud.query.all()
    resultado_solicitud = solicitudes_schema.dump(resultall)
    return jsonify(resultado_solicitud)

@ruta_solicitud.route('/savesolicitud', methods=['POST'])
def save():
    idPasajero = request.json['idpasajero']
    hora = request.json['hora']
    punto_final = request.json['punto_final']
    new_solicitud = solicitud(
        idPasajero,
        hora,
        punto_final,
    )
    db.session.add(new_solicitud)
    db.session.commit()
    return "Datos guardados con éxito"

@ruta_solicitud.route('/updatesolicitud', methods=['PUT'])
def Update():
    id = request.json['id']
    idPasajero = request.json['idpasajero']
    hora = request.json['hora']
    punto_final = request.json['punto_final']
    solicitudes = solicitud.query.get(id)
    if solicitudes:
        print(solicitudes)
        solicitudes.idpasajero = idPasajero
        solicitudes.hora = hora
        solicitudes.punto_final = punto_final
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"
    
@ruta_solicitud.route("/deletesolicitud/<id>", methods=["DELETE"])
def eliminar(id):
    soli = solicitud.query.get(id)
    db.session.delete(soli)
    db.session.commit()
    return jsonify(
        solicitud_schema.dump(soli),
    )

# ---------------- Relación pasajero/solicitud ----------------------------------------------------------------
@ruta_solicitud.route('/relacionsolicitud', methods=['POST'])
def dostabla():
    datos = {}
    resultadorelacion = db.session.query(pasajero,solicitud). \
        select_from(pasajero).join(solicitud).all()
    i=0
    for vehiculos, viajes in resultadorelacion:
        i+=1
        datos[i]={
            'vehiculo':vehiculos.id,
            'viaje': viajes.id, 
        }
    return datos