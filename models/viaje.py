from config.db import db, ma, app

class viaje(db.Model):
    __tablename__ = "tablaviaje"

    id = db.Column(db.Integer, primary_key=True)
    idpasajero = db.Column(db.Integer, db.ForeignKey('tablapasajero.id'))
    hr = db.Column(db.String(50))
    trayecto = db.Column(db.String(50))
    

    def __init__(self,idpasajero, hr,trayecto):
        self.idpasajero = idpasajero
        self.hr = hr
        self.trayecto = trayecto

with app.app_context():
    db.create_all()

class viajeschema(ma.Schema):
    class Meta:
        fields = ('id', "idpasajero", "hr", "trayecto")