from base_datos import db
from datetime import datetime
import time
class PersonaModel(db.Model):
    __tablename__="t_persona"
    id = db.Column("per_id", db.Integer, primary_key=True)
    dni = db.Column("per_dni", db.String(8))
    nombres = db.Column("per_nombres", db.String(50))
    apellidos = db.Column("per_apellidos", db.String(50))
    fecnac = db.Column("per_fecnac", db.Date)
    sexo = db.Column("per_sexo", db.String(1))
    correo = db.Column("per_correo", db.String(30))
    celular = db.Column("per_celular",db.String(15))    
    observacion = db.Column("per_observacion", db.String(100))
    estado = db.Column("per_estado", db.Boolean, default=True)    
    fecreg = db.Column("per_fecreg", db.DateTime, default=datetime.now)        
    # RELACIONES    
    # Voy a crear mi relacion inversa
    # sirve para hacer la relacion inversa (traer todos la experiencia laboral que pertenecen a esa persona) y nos ayuda demasiado para la logica
    laborales = db.relationship('LaboralModel', backref='persona')
    conocimientos = db.relationship('ConocimientoModel', backref='persona')
    hobbies = db.relationship('HobbieModel', backref='persona')
    habilidades = db.relationship('HabilidadModel', backref='persona')
    academicos = db.relationship('AcademicoModel', backref='persona')

    def __init__(self, dni, nombres, apellidos, fecnac, sexo, correo, celular, observacion, estado):
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecnac = fecnac
        self.sexo = sexo
        self.correo = correo
        self.celular = celular
        self.observacion = observacion        
        if estado is not None:
            self.estado = estado

    def guardar_bd(self):
        db.session.add(self)
        db.session.commit()

    def mostrar_json(self):
        # print (self.fecnac.strftime("%m/%d/%Y, %H:%M:%S"))

        return {
            'id':self.id,
            'dni':self.dni,
            'nombres':self.nombres,
            'apellidos': self.apellidos,
            'fecnac': self.fecnac.strftime("%m-%d-%Y"),
            'sexo': self.sexo,
            'correo':self.correo,
            'celular':self.celular,            
            'observacion':self.observacion,
            'estado':self.estado,            
            'fecreg':self.fecreg.strftime("%m-%d-%Y %H:%M:%S")
        }
    def __str__(self):
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'%(self.id, self.dni, self.nombres,self.apellidos,self.fecnac,self.sexo,self.correo,self.celular,self.observacion,self.estado,self.fecreg)

