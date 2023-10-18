from config.db import db, ma, app

class pasajero(db.Model):
    __tablename__ = "tablapasajero"

    id = db.Column(db.Integer, primary_key=True)
    idvehiculo = db.Column(db.Integer, db.ForeignKey('tablavehiculo.id'))
    nombre = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    ubicacion = db.Column(db.String(50))
    apellido = db.Column(db.String(50))

    def __init__(self,idvehiculo, nombre,telefono,ubicacion,apellido):
        self.idvehiculo = idvehiculo
        self.nombre = nombre
        self.telefono = telefono
        self.ubicacion = ubicacion
        self.apellido = apellido

with app.app_context():
    db.create_all()

class pasajeroschema(ma.Schema):
    class Meta:
        fields = ('id', "idvehiculo", "nombre", "telefono", "ubicacion", "apellido")