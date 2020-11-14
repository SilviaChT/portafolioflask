from base_datos import db
from datetime import datetime

class AcademicoModel(db.Model):
    __tablename__="t_academico"
    id = db.Column("acad_id", db.Integer, primary_key=True)
    nivel = db.Column("acad_nivel", db.String(100))
    cestudios = db.Column("acad_cestudios", db.String(200))    
    carrera = db.Column("acad_carrera", db.String(200))    
    observacion = db.Column("acad_observacion", db.String(100))    
    estado = db.Column("acad_estado",db.Boolean, default=True)
    fecreg = db.Column("acad_fecreg",db.DateTime,default=datetime.now)   
    #RELACIONES
    per_id = db.Column(db.Integer, db.ForeignKey('t_persona.per_id'), nullable=False)
        
    def __init__(self,nivel, cestudios, carrera,observacion,estado,per_id):
        self.nivel = nivel
        self.cestudios = cestudios
        self.carrera = carrera        
        self.observacion= observacion
        self.estado = estado 
        self.per_id=per_id       

    def guardar_bd(self):
        db.session.add(self)
        db.session.commit()

    def mostrar_json(self):
        return {
            'id':self.id,
            'nivel':self.nivel,
            'cestudios':self.cestudios,
            'carrera': self.carrera,            
            'observacion':self.observacion,
            'estado':self.estado,            
            'fecreg':self.fecreg.strftime("%m-%d-%Y %H:%M:%S"),
        }