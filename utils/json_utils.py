import utils.constantes_claro_video as const
from result_serie.result_serie import ResultSerie
from typing import List

class JsonUtils:

    @staticmethod
    def generar_json_result(lista_result_serie : List[ResultSerie]):

        json = {'superhighlight':{'superhighlight': const.PARAM_NODO, 'region':const.PARAM_REGION}}
        json['superhighlight']['response'] = []

        for result_serie in lista_result_serie:
            json_serie = {}
            json_serie['group_id'] = result_serie.group_id
            json_serie['title'] = result_serie.titulo_de_la_serie

            if 'images' not in json_serie:
                json_serie['images'] = {}

            for result_image in result_serie.lista_validaciones_url_imagenes_por_revisar:
                json_serie['images'][result_image.nombre_imagen_por_probar] = {}
                json_serie['images'][result_image.nombre_imagen_por_probar]['request'] = 'SUCCESS' if \
                    result_image.validacion_correcta else 'FAIL'
                json_serie['images'][result_image.nombre_imagen_por_probar]['image'] = result_image.url_por_probar

            json['superhighlight']['response'].append(json_serie)

        return json




