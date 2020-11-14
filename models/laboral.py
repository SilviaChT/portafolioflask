from base_datos import db
from datetime import datetime

class LaboralModel(db.Model):
    __tablename__="t_laboral"
    id = db.Column("lab_id", db.Integer, primary_key=True)
    descripcion = db.Column("lab_descripcion", db.String(100))
    fecini = db.Column("lab_fecini", db.Date)
    fecfin = db.Column("lab_fecfin", db.Date)
    contacnombre = db.Column("lab_contacnombre", db.String(100))
    contaccelular = db.Column("lab_contaccelular", db.String(15))    
    observacion = db.Column("lab_observacion", db.String(100))    
    estado = db.Column("lab_estado",db.Boolean, default=True)
    fecreg = db.Column("lab_fecreg",db.DateTime,default=datetime.now)   
    #RELACIONES
    per_id = db.Column(db.Integer, db.ForeignKey('t_persona.per_id'), nullable=False)
        
    def __init__(self,descripcion, fecini, fecfin, contacnombre, contaccelular,observacion,estado,per_id):
        self.descripcion = descripcion
        self.fecini = fecini
        self.fecfin = fecfin
        self.contacnombre = contacnombre
        self.contaccelular = contaccelular        
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
            'contacnombre': self.contacnombre,
            'contaccelular': self.contaccelular,            
            'observacion':self.observacion,
            'estado':self.estado,            
            'fecreg':self.fecreg.strftime("%m-%d-%Y %H:%M:%S"),
        }