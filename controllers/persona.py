from flask_restful import Resource, reqparse
from models.persona import PersonaModel
from datetime import datetime
# @app.route("/persona",methods=["get","post"])
class PersonasController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "dni",
        type=str,
        required=True,
        help="Falta ingresar el N° DNI"
    )
    parser.add_argument(
        "nombres",
        type=str,
        required=True,
        help="Falta ingresar los Nombres"
    )
    parser.add_argument(
        "apellidos",
        type=str,
        required=True,
        help="Falta ingresar los Apellidos"
    )
    parser.add_argument(
        "fecnac",
        type = str,
        required=True,
        help="Falta ingresar la Fecha de Nacimiento"
    )    
    parser.add_argument(
        "sexo",
        type=str,
        required=False,
        help='Falta ingresar el sexo de la Persona'
    )
    parser.add_argument(
        "correo",
        type=str,
        required=False,
        help='Falta ingrsar el Correo Electrónico'
    )
    parser.add_argument(
        "celular",
        type=str,
        required=False,
        help='Falta ingrsar el Celular'
    )
    parser.add_argument(
        "observacion",
        type=str,
        required=False,
        help='Falta ingresar la Observacion'
    )
    parser.add_argument(
        "estado",
        type=bool,
        required=False,
        help='Falta ingresar el estado de la Persona'
    )
    def get(self):
        personas = PersonaModel.query.all()
        # print(personas)
        resultado = []
        for persona in personas:
            print(persona.laborales)
            laborales=[]
            for laboral in persona.laborales:
                print(laboral.mostrar_json())
                laborales.append(laboral.mostrar_json())
            temporal = persona.mostrar_json()
            temporal['laborales'] = laborales
            resultado.append(temporal)
        return {
            'ok':True,
            'content': resultado,
            'message': None
        }
    
    def post(self):
        data = self.parser.parse_args()
        print(data)
        persona = PersonaModel(data['dni'],data['nombres'],data['apellidos'],data['fecnac'],data['sexo'],data['correo'],data['celular'],data['observacion'], data['estado'])
        persona.guardar_bd()
        persona.mostrar_json()
        try:
            
            print(persona)
            return {
                'ok':True,
                'message':'Se guardo exitosamente el registro personal',
                'content': persona.mostrar_json()
            }
        except:
            return {
                'ok':False,
                'message':'No se pudo guardar el registro personal en la bd'
            },500

class PersonaController(Resource):
    def get(self, per_id):
        persona = PersonaModel.query.filter_by(id=per_id).first()
        print(persona.laborales)
        if persona:
            return {
                'ok':True,
                'content':persona.mostrar_json(),
                'message': None
            }
        else:
            return {
                'ok': False,
                'content': None,
                'message': 'No existe el registro personal con id: '+str(per_id)
            }, 404
    def put(self, per_id):
        persona = PersonaModel.query.filter_by(id=per_id).first()
        if persona:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "dni",
                type=str,
                required=True,
                help="Falta ingresar el N° DNI"
            )
            parser.add_argument(
                "nombres",
                type=str,
                required=True,
                help="Falta ingresar los Nombres"
            )
            parser.add_argument(
                "apellidos",
                type=str,
                required=True,
                help="Falta ingresar los Apellidos"
            )
            parser.add_argument(
                "fecnac",
                type = str,
                required=True,
                help="Falta ingresar la Fecha de Nacimiento"
            )    
            parser.add_argument(
                "sexo",
                type=str,
                required=False,
                help='Falta ingresar el sexo de la Persona'
            )
            parser.add_argument(
                "correo",
                type=str,
                required=False,
                help='Falta ingrsar el Correo Electrónico'
            )
            parser.add_argument(
                "celular",
                type=str,
                required=False,
                help='Falta ingrsar el Celular'
            )
            parser.add_argument(
                "observacion",
                type=str,
                required=False,
                help='Falta ingresar la Observacion'
            )
            parser.add_argument(
                "estado",
                type=bool,
                required=False,
                help='Falta ingresar el estado de la Persona'
            )
            data = parser.parse_args()
            persona.dni = data['dni']
            persona.nombres = data['nombres']
            persona.apellidos = data['apellidos']
            persona.fecnac = data['fecnac']
            persona.sexo = data['sexo']
            persona.correo = data['correo']
            persona.celular = data['celular']            
            persona.observacion = data['observacion']
            persona.estado = data['estado']            
            persona.guardar_bd()
            return {
                'ok':True,
                'content':persona.mostrar_json(),
                'message': None
            }
        else:
            return {
                'ok': False,
                'content': None,
                'message': 'No existe el registro personal con id: '+str(per_id)
            }, 404
    def delete(self, per_id):
        # desahiblitar ese estante segun su ID
        persona = PersonaModel.query.filter_by(id=per_id).first()
        if persona:
            if persona.estado == True:
                persona.estado = False
                persona.guardar_bd()
                return {
                    'ok': True,
                    'content': None,
                    'message': 'Se inhabilito exitosamente el registro personal'
                }
            else:
                # si el registro personal ya esta deshabilitado que indique que ya lo esta
                return {
                    'ok': False,
                    'content': None,
                    'message': 'El registro personal ya se encuentra deshabilitado'
                }, 400
        else:
            return {
                'ok': False,
                'content':None,
                'message': 'No existe el registro personal'
            }, 400