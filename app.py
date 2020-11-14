from flask import Flask
# pip install flask-restful
from flask_restful import Api
# pip install flask-sqlalchemy
from base_datos import db
# from models.estante import EstanteModel
from controllers.persona import PersonasController, PersonaController
from controllers.laboral import LaboralesController, LaboralController, EncontrarLaboralController
from controllers.conocimiento import ConocimientosController, ConocimientoController, EncontrarConocimientoController
from controllers.hobbie import HobbiesController, HobbieController, EncontrarHobbieController
from controllers.habilidad import HabilidadesController, HabilidadController, EncontrarHabilidadController
from controllers.academico import AcademicosController, AcademicoController, EncontrarAcademicoController

app = Flask(__name__)
# dialect+driver://username:password@host:port/database
# es compatible con MySQL, Oracle, PostgreSQL, SQLite
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/portafolioo'
api = Api(app=app)
@app.before_first_request
def iniciador():
    # Aca se conecta al servidor
    db.init_app(app)
    # Eliminacion de los modelos, x defecto elimina todos
    # db.drop_all(app=app)
    # Creacion de los Modelos
    db.create_all(app=app)

@app.route("/")
def inicio():
    return 'El servidor funciona correctamente'

# DEFINIR MIS RUTAS
api.add_resource(PersonasController,'/persona')
api.add_resource(PersonaController, '/persona/<int:per_id>')

api.add_resource(LaboralesController, '/laboral')
api.add_resource(LaboralController, '/laboral/<int:lab_id>')
api.add_resource(EncontrarLaboralController,'/laboral/<string:palabra>')

api.add_resource(ConocimientosController, '/conocimiento')
api.add_resource(ConocimientoController, '/conocimiento/<int:conoci_id>')
api.add_resource(EncontrarConocimientoController,'/conocimiento/<string:palabra>')

api.add_resource(HobbiesController, '/hobbie')
api.add_resource(HobbieController, '/hobbie/<int:hob_id>')
api.add_resource(EncontrarHobbieController,'/hobbie/<string:palabra>')

api.add_resource(HabilidadesController, '/habilidad')
api.add_resource(HabilidadController, '/habilidad/<int:hab_id>')
api.add_resource(EncontrarHabilidadController,'/habilidad/<string:palabra>')

api.add_resource(AcademicosController, '/academico')
api.add_resource(AcademicoController, '/academico/<int:acad_id>')
api.add_resource(EncontrarAcademicoController,'/academico/<string:palabra>')

if __name__ == '__main__':
    app.run(debug=True)