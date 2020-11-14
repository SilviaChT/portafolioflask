from flask_restful import Resource, reqparse
from models.academico import AcademicoModel

class AcademicosController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "nivel",
        type=str,
        required=True,
        help="Falta ingresar el nivel"
    )
    parser.add_argument(
        "cestudios",
        type=str,
        required=True,
        help="Falta ingresar el centro de estudios"
    )
    parser.add_argument(
        "carrera",
        type=str,
        required=True,
        help="Falta ingresar la carrera"
    )
    parser.add_argument(
        "observacion",
        type=str,
        required=True,
        help="Falta ingresar la observacion"
    )
    parser.add_argument(
        "estado",
        type=bool,
        required=True,
        help='Falta ingresar el estado'
    )
    parser.add_argument(
        "per_id",
        type=str,
        required=True,
        help='Falta ingresar el id de la persona'
    )
    def get(self):
        academicos = AcademicoModel.query.all()
        resultado = []
        for academico in academicos:
            # print(academico)
            temporal = academico.mostrar_json()
            temporal['persona'] = academico.persona.mostrar_json()
            resultado.append(temporal)
            print(academico.persona.mostrar_json())            
            # print(academico.acad_id)
        return {
            'ok':True,
            'content':resultado            
        }
    def post(self):
        data = self.parser.parse_args()
        academico = AcademicoModel(data['nivel'],data['cestudios'],data['carrera'],data['observacion'],data['estado'],data['per_id'])
        try:
            academico.guardar_bd()
            print(academico)
            return {
                'ok':True,
                'message':'Se guardo exitosamente el registro Academico',
                'content': academico.mostrar_json()
            }
        except:
            return {
                'ok':False,
                'message':'No se pudo guardar el registro Academico en la bd'
            },500

class AcademicoController(Resource):
    def get(self, acad_id):
        academico = AcademicoModel.query.filter_by(id=acad_id).first()
        informacion = academico.mostrar_json()
        personaf = academico.persona.mostrar_json()
        informacion['persona'] = personaf
        if academico:
            return {
                'ok':True,
                'content':informacion,
                'message':None
            }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro academico con id: '+str(acad_id)
            }, 404

    def put(self, acad_id):
        academico = AcademicoModel.query.filter_by(id=acad_id).first()
        if academico:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "nivel",
                type=str,
                required=True,
                help="Falta ingresar el nivel"
            )
            parser.add_argument(
                "cestudios",
                type=str,
                required=True,
                help="Falta ingresar el centro de estudios"
            )
            parser.add_argument(
                "carrera",
                type=str,
                required=True,
                help="Falta ingresar la carrera"
            )
            parser.add_argument(
                "observacion",
                type=str,
                required=True,
                help="Falta ingresar la observacion"
            )
            parser.add_argument(
                "estado",
                type=bool,
                required=True,
                help='Falta ingresar el estado'
            )
            parser.add_argument(
                "per_id",
                type=str,
                required=True,
                help='Falta ingresar el id de la persona'
            )
            data = parser.parse_args()
            academico.nivel = data['nivel']
            academico.cestudios = data['cestudios']
            academico.carrera = data['carrera']
            academico.observacion = data['observacion']
            academico.estado = data['estado']            
            academico.guardar_bd()
            return {
                'ok':True,
                'content':academico.mostrar_json(),
                'message':None
            }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro academico con el id: '+str(acad_id)
            }

    def delete(self, acad_id):
        academico = AcademicoModel.query.filter_by(id=acad_id).first()
        if academico:
            if academico.estado == True:
                academico.estado = False
                academico.guardar_bd()
                return {
                    'ok':True,
                    'content':None,
                    'message':'El registro academico fue deshabilitado correctamente'
                }
            else:
                return {
                    'ok':False,
                    'content':None,
                    'message':'El registro academico ya se encuentra deshabilitado'
                }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro academico'
            }, 400

class EncontrarAcademicoController(Resource):
    def get(self, palabra):
        resultado = AcademicoModel.query.filter(AcademicoModel.carrera.like('%'+palabra+'%')).all()
        if resultado:
            respuesta = []
            for academico in resultado:
                respuesta.append(academico.mostrar_json())
            return{
                'Ok':True,
                'content':respuesta,
                'message':''
            }
        else:
            return{
                'Ok':False,
                'content':None,
                'message':'No se encontro ninguna coincidencia'
            }, 404