from config.db import db, ma, app

class vehiculo(db.Model):
    __tablename__ = "tablavehiculo"

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(255))
    capacidad = db.Column(db.String(255))

    def __init__(self,placa, capacidad):
        self.placa = placa
        self.capacidad = capacidad

with app.app_context():
    db.create_all()

class vehiculochema(ma.Schema):
    class Meta:
        fields = ('id', "placa", "capacidad")