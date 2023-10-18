from config.db import db, ma, app

class pago(db.Model):
    __tablename__ = "tablapago"

    id = db.Column(db.Integer, primary_key=True)
    idpasajero = db.Column(db.Integer, db.ForeignKey('tablapasajero.id'))
    fecha = db.Column(db.String(50))
    monto = db.Column(db.String(50))
    formapago = db.Column(db.String(50))

    def __init__(self,idpasajero, fecha, monto, formapago):
        self.idpasajero = idpasajero
        self.fecha = fecha
        self.monto = monto
        self.formapago = formapago

with app.app_context():
    db.create_all()

class pagoschema(ma.Schema):
    class Meta:
        fields = ('id','idpasajero', 'fecha', 'monto','formapago')