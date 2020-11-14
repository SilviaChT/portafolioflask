from base_datos import db
from datetime import datetime

class HabilidadModel(db.Model):
    __tablename__="t_habilidad"
    id = db.Column("hab_id", db.Integer, primary_key=True)
    descripcion = db.Column("hab_descripcion", db.String(200))    
    observacion = db.Column("hab_observacion", db.String(100))    
    estado = db.Column("hab_estado",db.Boolean, default=True)
    fecreg = db.Column("hab_fecreg",db.DateTime,default=datetime.now)   
    #RELACIONES
    per_id = db.Column(db.Integer, db.ForeignKey('t_persona.per_id'), nullable=False)
        
    def __init__(self,descripcion, observacion,estado,per_id):
        self.descripcion = descripcion        
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
            'observacion':self.observacion,
            'estado':self.estado,            
            'fecreg':self.fecreg.strftime("%m-%d-%Y %H:%M:%S"),
        }