from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.reporte import reporte, reporteschema
from models.viaje import viaje, viajeschema

ruta_reporte = Blueprint("ruta_reporte",__name__)

reporte_schema = reporteschema()
reportes_schema = reporteschema(many=True)

@ruta_reporte.route('/reporte', methods=['GET'])
def pagos():
    resultall = reporte.query.all() # Select * from Pasajeros
    resultado_pago = reportes_schema.dump(resultall)
    return jsonify(resultado_pago)

@ruta_reporte.route('/savereporte', methods=['POST'])
def save():
    idPasajero = request.json['idviaje']
    nombrepasajero = request.json['fecha']
    telefonopasajero = request.json['reclamo']
    new_pago = reporte(
        idPasajero,
        nombrepasajero,
        telefonopasajero,
    )
    db.session.add(new_pago)
    db.session.commit()
    return "Datos guardados con éxito"

@ruta_reporte.route('/updatereporte', methods=['PUT'])
def Update():
    id = request.json['id']
    idPasajero = request.json['idviaje']
    nombrepasajero = request.json['fecha']
    telefonopasajero = request.json['reclamo']
    
    pagos = reporte.query.get(id)
    if pagos:
        print(pagos)
        pagos.idviaje = idPasajero
        pagos.fecha = nombrepasajero
        pagos.reclamo = telefonopasajero
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_reporte.route("/deletereporte/<id>", methods=["DELETE"])
def eliminar(id):
    reportes = reporte.query.get(id)
    db.session.delete(reportes)
    db.session.commit()
    return jsonify(
        reporte_schema.dump(reportes),
    )

# ---------------- Relación reporte/viaje ----------------------------------------------------------------
@ruta_reporte.route('/relacionviaje', methods=['POST'])
def dostabla():
    datos = {}
    resultadorelacion = db.session.query(viaje,reporte). \
        select_from(viaje).join(reporte).all()
    i=0
    for reportes, viajes in resultadorelacion:
        i+=1
        datos[i]={
            'reporte':reportes.id,
            'viaje': viajes.id, 
        }
    return datos