from flask_restful import Resource, reqparse
from models.habilidad import HabilidadModel

class HabilidadesController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "descripcion",
        type=str,
        required=True,
        help="Falta ingresar la descripcion"
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
        habilidades = HabilidadModel.query.all()
        resultado = []
        for habilidad in habilidades:
            # print(laboral)
            temporal = habilidad.mostrar_json()
            temporal['persona'] = habilidades.persona.mostrar_json()
            resultado.append(temporal)
            print(habilidad.persona.mostrar_json())            
            # print(laboral.lab_id)
        return {
            'ok':True,
            'content':resultado            
        }
    def post(self):
        data = self.parser.parse_args()
        habilidad = HabilidadModel(data['descripcion'],data['observacion'],data['estado'],data['per_id'])
        try:
            habilidad.guardar_bd()
            print(habilidad)
            return {
                'ok':True,
                'message':'Se guardo exitosamente el registro Habilidad',
                'content': habilidad.mostrar_json()
            }
        except:
            return {
                'ok':False,
                'message':'No se pudo guardar el registro Habilidad en la bd'
            },500

class HabilidadController(Resource):
    def get(self, hab_id):
        habilidad = HabilidadModel.query.filter_by(id=hab_id).first()
        informacion = habilidad.mostrar_json()
        personaf = habilidad.persona.mostrar_json()
        informacion['persona'] = personaf
        if hobbie:
            return {
                'ok':True,
                'content':informacion,
                'message':None
            }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro habilidad con id: '+str(hab_id)
            }, 404

    def put(self, hab_id):
        habilidad = HabilidadModel.query.filter_by(id=hab_id).first()
        if habilidad:
            parser = reqparse.RequestParser()                   
            parser.add_argument(
                "descripcion",
                type=str,
                required=True,
                help="Falta ingresar la descripcion"
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
            habilidad.descripcion = data['descripcion']            
            habilidad.observacion = data['observacion']
            habilidad.estado = data['estado']            
            habilidad.guardar_bd()
            return {
                'ok':True,
                'content':habilidad.mostrar_json(),
                'message':None
            }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro habilidad con el id: '+str(hab_id)
            }

    def delete(self, hab_id):
        habilidad = HabilidadModel.query.filter_by(id=hab_id).first()
        if habilidad:
            if habilidad.estado == True:
                habilidad.estado = False
                habilidad.guardar_bd()
                return {
                    'ok':True,
                    'content':None,
                    'message':'El registro habilidad fue deshabilitado correctamente'
                }
            else:
                return {
                    'ok':False,
                    'content':None,
                    'message':'El registro habilidad ya se encuentra deshabilitado'
                }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro habilidades'
            }, 400

class EncontrarHabilidadController(Resource):
    def get(self, palabra):
        resultado = HabilidadModel.query.filter(HabilidadModel.descripcion.like('%'+palabra+'%')).all()
        if resultado:
            respuesta = []
            for habilidad in resultado:
                respuesta.append(habilidad.mostrar_json())
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