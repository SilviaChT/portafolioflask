from flask_restful import Resource, reqparse
from models.laboral import LaboralModel

class LaboralesController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "descripcion",
        type=str,
        required=True,
        help="Falta ingresar la descripcion laboral"
    )
    parser.add_argument(
        "fecini",
        type=str,
        required=True,
        help="Falta ingresar la fecha de inicio laboral"
    )
    parser.add_argument(
        "fecfin",
        type=str,
        required=True,
        help="Falta ingresar el fecha de finalización laboral"
    )
    parser.add_argument(
        "contacnombre",
        type=str,
        required=True,
        help="Falta ingresar el nombre del contacto laboral"
    )
    parser.add_argument(
        "contaccelular",
        type=str,
        required=True,
        help="Falta ingresar el celular del contacto laboral"
    )
    parser.add_argument(
        "observacion",
        type=str,
        required=True,
        help="Falta ingresar la observacion del contacto laboral"
    )
    parser.add_argument(
        "estado",
        type=bool,
        required=True,
        help='Falta ingresar el estado laboral'
    )
    parser.add_argument(
        "per_id",
        type=str,
        required=True,
        help='Falta ingresar el id de la persona'
    )
    def get(self):
        laborales = LaboralModel.query.all()
        resultado = []
        for laboral in laborales:
            # print(laboral)
            temporal = laboral.mostrar_json()
            temporal['persona'] = laboral.persona.mostrar_json()
            resultado.append(temporal)
            print(laboral.persona.mostrar_json())
            # print(laboral.lab_id)
        return {
            'ok':True,
            'content':resultado            
        }
    def post(self):
        data = self.parser.parse_args()
        laboral = LaboralModel(data['descripcion'],data['fecini'],data['fecfin'], data['contacnombre'], data['contaccelular'], data['observacion'],data['estado'],data['per_id'])
        try:
            laboral.guardar_bd()
            print(laboral)
            return {
                'ok':True,
                'message':'Se guardo exitosamente el registro Laboral',
                'content': laboral.mostrar_json()
            }
        except:
            return {
                'ok':False,
                'message':'No se pudo guardar el registro Laboral en la bd'
            },500

class LaboralController(Resource):
    def get(self, lab_id):
        laboral = LaboralModel.query.filter_by(id=lab_id).first()
        informacion = laboral.mostrar_json()
        personaf = laboral.persona.mostrar_json()
        informacion['persona'] = personaf
        if laboral:
            return {
                'ok':True,
                'content':informacion,
                'message':None
            }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro laboral con id: '+str(lab_id)
            }, 404

    def put(self, lab_id):
        laboral = LaboralModel.query.filter_by(id=lab_id).first()
        if laboral:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "descripcion",
                type=str,
                required=True,
                help="Falta ingresar la descripcion laboral"
            )
            parser.add_argument(
                "fecini",
                type=str,
                required=True,
                help="Falta ingresar la fecha de inicio laboral"
            )
            parser.add_argument(
                "fecfin",
                type=str,
                required=True,
                help="Falta ingresar el fecha de finalización laboral"
            )
            parser.add_argument(
                "contacnombre",
                type=str,
                required=True,
                help="Falta ingresar el nombre del contacto laboral"
            )
            parser.add_argument(
                "contaccelular",
                type=str,
                required=True,
                help="Falta ingresar el celular del contacto laboral"
            )
            parser.add_argument(
                "observacion",
                type=str,
                required=True,
                help="Falta ingresar la observacion del contacto laboral"
            )
            parser.add_argument(
                "estado",
                type=bool,
                required=True,
                help='Falta ingresar el estado laboral'
            )
            parser.add_argument(
                "per_id",
                type=str,
                required=True,
                help='Falta ingresar el id de la persona'
            )
            data = parser.parse_args()
            laboral.descripcion = data['descripcion']
            laboral.fecini = data['fecini']
            laboral.fecfin = data['fecfin']
            laboral.contacnombre = data['contacnombre']
            laboral.contaccelular= data['contaccelular']
            laboral.observacion = data['observacion']
            laboral.estado = data['estado']            
            laboral.guardar_bd()
            return {
                'ok':True,
                'content':laboral.mostrar_json(),
                'message':None
            }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro laboral con el id: '+str(lab_id)
            }

    def delete(self, lab_id):
        laboral = LaboralModel.query.filter_by(id=lab_id).first()
        if laboral:
            if laboral.estado == True:
                laboral.estado = False
                laboral.guardar_bd()
                return {
                    'ok':True,
                    'content':None,
                    'message':'El registro laboral fue deshabilitado correctamente'
                }
            else:
                return {
                    'ok':False,
                    'content':None,
                    'message':'El registro laboral ya se encuentra deshabilitado'
                }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro laboral'
            }, 400

class EncontrarLaboralController(Resource):
    def get(self, palabra):
        resultado = LaboralModel.query.filter(LaboralModel.descripcion.like('%'+palabra+'%')).all()
        if resultado:
            respuesta = []
            for laboral in resultado:
                respuesta.append(laboral.mostrar_json())
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