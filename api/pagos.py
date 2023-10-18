from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pagos import pago, pagoschema
# from models.pasajero import Pasajero, PasajerosSchema

ruta_pago = Blueprint("ruta_pago",__name__)

pago_schema = pagoschema()
pagos_schema = pagoschema(many=True)

@ruta_pago.route('/pago', methods=['GET'])
def pagos():
    resultall = pago.query.all() # Select * from Pasajeros
    resultado_pago = pagos_schema.dump(resultall)
    return jsonify(resultado_pago)

@ruta_pago.route('/savepago', methods=['POST'])
def save():
    id_pasajero = request.json['idpasajero']
    fecha_pago = request.json['fecha']
    monto_pago = request.json['monto']
    formapago_pago = request.json['formapago']
    new_pago = pago(
        id_pasajero,
        fecha_pago,
        monto_pago,
        formapago_pago,
        
    )
    db.session.add(new_pago)
    db.session.commit()
    return "Datos guardados con éxito"

@ruta_pago.route('/updatepago', methods=['PUT'])
def Update():
    id = request.json['id']
    id_pasajero = request.json['idpasajero']
    fecha_pago = request.json['fecha']
    monto_pago = request.json['monto']
    formapago_pago = request.json['formapago']
    
    pagos = pago.query.get(id)
    if pagos:
        print(pagos)
        pagos.id_pasajero = id_pasajero
        pagos.fecha_pago = fecha_pago
        pagos.monto_pago = monto_pago
        pagos.formapago_pago = formapago_pago
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_pago.route("/deletepago/<id>", methods=["DELETE"])
def eliminar(id):
    pagos = pago.query.get(id)
    db.session.delete(pagos)
    db.session.commit()
    return jsonify(
        pago_schema.dump(pagos),
    )