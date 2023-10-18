from config.db import db, ma, app

class solicitud(db.Model):
    __tablename__ = "tablasolicitud"

    id = db.Column(db.Integer, primary_key=True)
    idpasajero = db.Column(db.Integer, db.ForeignKey('tablapasajero.id'))
    hora = db.Column(db.String(50))
    punto_final = db.Column(db.String(50))

    def __init__(self, idpasajero, hora, punto_final):
        self.idpasajero = idpasajero
        self.hora = hora
        self.punto_final = punto_final

with app.app_context():
    db.create_all()

class solicitudschema(ma.Schema):
    class Meta:
        fields = ('id','idpasajero', 'hora', 'punto_final')