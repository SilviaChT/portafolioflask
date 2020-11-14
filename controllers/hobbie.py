from flask_restful import Resource, reqparse
from models.hobbie import HobbieModel

class HobbiesController(Resource):
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
        hobbies = HobbieModel.query.all()
        resultado = []
        for hobbie in hobbies:
            # print(laboral)
            temporal = hobbie.mostrar_json()
            temporal['persona'] = hobbies.persona.mostrar_json()
            resultado.append(temporal)
            print(hobbie.persona.mostrar_json())            
            # print(laboral.lab_id)
        return {
            'ok':True,
            'content':resultado            
        }
    def post(self):
        data = self.parser.parse_args()
        hobbie = HobbieModel(data['descripcion'],data['observacion'],data['estado'],data['per_id'])
        try:
            hobbie.guardar_bd()
            print(hobbie)
            return {
                'ok':True,
                'message':'Se guardo exitosamente el registro Hobbie',
                'content': hobbie.mostrar_json()
            }
        except:
            return {
                'ok':False,
                'message':'No se pudo guardar el registro Hobbie en la bd'
            },500

class HobbieController(Resource):
    def get(self, conoci_id):
        hobbie = HobbieModel.query.filter_by(id=hob_id).first()
        informacion = hobbie.mostrar_json()
        personaf = hobbie.persona.mostrar_json()
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
                'message':'No existe el registro hobbie con id: '+str(hob_id)
            }, 404

    def put(self, hob_id):
        hobbie = HobbieModel.query.filter_by(id=hob_id).first()
        if hobbie:
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
            hobbie.descripcion = data['descripcion']            
            hobbie.observacion = data['observacion']
            hobbie.estado = data['estado']            
            hobbie.guardar_bd()
            return {
                'ok':True,
                'content':hobbie.mostrar_json(),
                'message':None
            }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro hobbie con el id: '+str(hob_id)
            }

    def delete(self, hob_id):
        hobbie = HobbieModel.query.filter_by(id=hob_id).first()
        if hobbie:
            if hobbie.estado == True:
                hobbie.estado = False
                hobbie.guardar_bd()
                return {
                    'ok':True,
                    'content':None,
                    'message':'El registro hobbie fue deshabilitado correctamente'
                }
            else:
                return {
                    'ok':False,
                    'content':None,
                    'message':'El registro hobbie ya se encuentra deshabilitado'
                }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el registro hobbie'
            }, 400

class EncontrarHobbieController(Resource):
    def get(self, palabra):
        resultado = HobbieModel.query.filter(HobbieModel.descripcion.like('%'+palabra+'%')).all()
        if resultado:
            respuesta = []
            for hobbie in resultado:
                respuesta.append(hobbie.mostrar_json())
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