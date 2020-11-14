from base_datos import db
from datetime import datetime

class ConocimientoModel(db.Model):
    __tablename__="t_conocimiento"
    id = db.Column("conoci_id", db.Integer, primary_key=True)
    descripcion = db.Column("conoci_descripcion", db.String(200))
    fecini = db.Column("conoci_fecini", db.Date)
    fecfin = db.Column("conoci_fecfin", db.Date)
    cestudios = db.Column("conoci_cestudios", db.String(100))    
    observacion = db.Column("conoci_observacion", db.String(100))    
    estado = db.Column("conoci_estado",db.Boolean, default=True)
    fecreg = db.Column("conoci_fecreg",db.DateTime,default=datetime.now)   
    #RELACIONES
    per_id = db.Column(db.Integer, db.ForeignKey('t_persona.per_id'), nullable=False)
        
    def __init__(self,descripcion, fecini, fecfin, cestudios,observacion,estado,per_id):
        self.descripcion = descripcion
        self.fecini = fecini
        self.fecfin = fecfin
        self.cestudios = cestudios        
        self.observacion= observacion
        self.estado = estado 
        self.per_id=per_id       

    def guardar_bd(self):
        db.session.add(self)
        db.session.commit()

    def mostrar_json(self):
        return {
            'id':self.id,
            'descripcion':self.descripcion,
            'fecini':self.fecini.strftime("%m-%d-%Y"),
            'fecfin': self.fecfin.strftime("%m-%d-%Y"),
            'cestudios': self.cestudios,            
            'observacion':self.observacion,
            'estado':self.estado,            
            'fecreg':self.fecreg.strftime("%m-%d-%Y %H:%M:%S"),
        }