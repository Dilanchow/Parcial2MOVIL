from config.db import db, ma, app

class reporte(db.Model):
    __tablename__ = "tablareporte"

    id = db.Column(db.Integer, primary_key=True)
    idviaje = db.Column(db.Integer, db.ForeignKey('tablaviaje.id'))
    fecha = db.Column(db.String(50))
    reclamo = db.Column(db.String(50))

    def __init__(self,idviaje, fecha, reclamo):
        self.idviaje = idviaje
        self.fecha = fecha
        self.reclamo = reclamo

with app.app_context():
    db.create_all()

class reporteschema(ma.Schema):
    class Meta:
        fields = ('id','idviaje', 'fecha', 'reclamo')