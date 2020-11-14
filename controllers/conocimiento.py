from flask_restful import Resource, reqparse
from models.conocimiento import ConocimientoModel

class ConocimientosController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "descripcion",
        type=str,
        required=True,
        help="Falta ingresar la descripcion"
    )
    parser.add_argument(
        "fecini",
        type=str,
        required=True,
        help="Falta ingresar la fecha de inicio"
    )
    parser.add_argument(
        "fecfin",
        type=str,
        required=True,
        help="Falta ingresar el fecha de finalización"
    )
    parser.add_argument(
        "cestudios",
        type=str,
        required=True,
        help="Falta ingresar el centro de estudios"
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
        conocimientos = ConocimientoModel.query.all()
        resultado = []
        for conocimiento in conocimientos:
            # print(laboral)
            temporal = conocimiento.mostrar_json()
            temporal['persona'] = conocimiento.persona.mostrar_json()
            resultado.append(temporal)
            print(conocimiento.persona.mostrar_json())            
            # print(laboral.lab_id)
        return {
            'ok':True,
            'content':resultado            
        }
    def post(self):
        data = self.parser.parse_args()
        conocimiento = ConocimientoModel(data['descripcion'],data['fecini'],data['fecfin'], data['cestudios'], data['observacion'],data['estado'],data['per_id'])
        try:
            conocimiento.guardar_bd()
            print(conocimiento)
            return {
                'ok':True,
                'message':'Se guardo exitosamente el registro Conocimiento',
                'content': conocimiento.mostrar_json()
            }
        except:
            return {
                'ok':False,
                'message':'No se pudo guardar el registro Conocimiento en la bd'
            },500

class ConocimientoController(Resource):
    def get(self, conoci_id):
        conocimiento = ConocimientoModel.query.filter_by(id=conoci_id).first()
        informacion = conocimiento.mostrar_json()
        personaf = conocimiento.persona.mostrar_json()
        informacion['persona'] = personaf
        if conocimiento:
            return {
                'ok':True,
                'content':informacion,
                'message':None
            }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro conocimiento con id: '+str(conoci_id)
            }, 404

    def put(self, conoci_id):
        conocimiento = ConocimientoModel.query.filter_by(id=conoci_id).first()
        if conocimiento:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "descripcion",
                type=str,
                required=True,
                help="Falta ingresar la descripcion"
            )
            parser.add_argument(
                "fecini",
                type=str,
                required=True,
                help="Falta ingresar la fecha de inicio"
            )
            parser.add_argument(
                "fecfin",
                type=str,
                required=True,
                help="Falta ingresar el fecha de finalización"
            )
            parser.add_argument(
                "cestudios",
                type=str,
                required=True,
                help="Falta ingresar el centro de estudios"
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
            conocimiento.descripcion = data['descripcion']
            conocimiento.fecini = data['fecini']
            conocimiento.fecfin = data['fecfin']
            conocimiento.cestudios = data['cestudios']            
            conocimiento.observacion = data['observacion']
            conocimiento.estado = data['estado']            
            conocimiento.guardar_bd()
            return {
                'ok':True,
                'content':conocimiento.mostrar_json(),
                'message':None
            }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro conocimiento con el id: '+str(conoci_id)
            }

    def delete(self, conoci_id):
        conocimiento = ConocimientoModel.query.filter_by(id=conoci_id).first()
        if conocimiento:
            if conocimiento.estado == True:
                conocimiento.estado = False
                conocimiento.guardar_bd()
                return {
                    'ok':True,
                    'content':None,
                    'message':'El registro conocimiento fue deshabilitado correctamente'
                }
            else:
                return {
                    'ok':False,
                    'content':None,
                    'message':'El registro conocimiento ya se encuentra deshabilitado'
                }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro conocimiento'
            }, 400

class EncontrarConocimientoController(Resource):
    def get(self, palabra):
        resultado = ConocimientoModel.query.filter(ConocimientoModel.descripcion.like('%'+palabra+'%')).all()
        if resultado:
            respuesta = []
            for conocimiento in resultado:
                respuesta.append(conocimiento.mostrar_json())
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