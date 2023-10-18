from flask import Flask, jsonify,json
from config.db import  db, ma, app

from api.vehiculo import vehiculo, ruta_vehiculo
from api.pasajero import pasajero, ruta_pasajero
from api.reporte import reporte, ruta_reporte
from api.pagos import pago, ruta_pago
from api.solicitud import solicitud, ruta_solicitud
from api.viaje import viaje, ruta_viaje

app.register_blueprint(ruta_vehiculo,url_prefix = '/api')
app.register_blueprint(ruta_pasajero, url_prefix = '/api')
app.register_blueprint(ruta_viaje, url_prefix = '/api')
app.register_blueprint(ruta_solicitud, url_prefix = '/api')
app.register_blueprint(ruta_pago, url_prefix = '/api')
app.register_blueprint(ruta_reporte, url_prefix = '/api')

@app.route('/')
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')