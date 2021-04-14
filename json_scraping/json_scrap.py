from utils import constantes_claro_video as const
from utils.request_utils import RequestUtils
from result_serie.result_serie import ResultSerie
from result_serie.result_serie_encabezado import ResultSerieEncabezado
from typing import List, Dict

class JsonScraping:

    @staticmethod
    def obtencion_lista_result_series_encabezado(json:Dict={}):
        lista_series_localizados_en_encabezado = []

        if 'msg' in json and 'OK' == json['msg'] and 'response' in json and 'highlight' in json['response']:
            for data_serie_json in json['response']['highlight']:
                result_serie_encabezado = ResultSerieEncabezado(data_serie_json)
                lista_series_localizados_en_encabezado.append(result_serie_encabezado)

        return lista_series_localizados_en_encabezado

    @staticmethod
    def obtencion_lista_result_series_con_group_id(lista_series_encabezado:List[ResultSerieEncabezado]=[]):

        cadena_validacion_serie = '/SERIES/'
        lista_series_con_group_id = []

        for serie_encabezado in lista_series_encabezado:

            if cadena_validacion_serie in serie_encabezado.image_highlight or cadena_validacion_serie in\
            serie_encabezado.image_large or cadena_validacion_serie in serie_encabezado.image_medium or\
            cadena_validacion_serie in serie_encabezado.image_small:

                result_serie_con_group_id = ResultSerie(serie_encabezado.group_id, serie_encabezado)
                result_serie_con_group_id.titulo_de_la_serie = result_serie_con_group_id.result_serie_encabezado.title
                result_serie_con_group_id.url_obtencion_data_encabezado = const.URL_FORMADA
                result_serie_con_group_id.nodo = const.PARAM_NODO
                result_serie_con_group_id.region = const.PARAM_REGION

                lista_series_con_group_id.append(result_serie_con_group_id)

        return lista_series_con_group_id

    @staticmethod
    def obtencion_id_serie_ag_mediante_group_id(lista_result_serie:list[ResultSerie]=[]):

        for result_serie in lista_result_serie:

            result_serie.url_obtencion_data_id_serie_ag = const.URL_API_CONSULTA_GROUP_ID.format(result_serie.group_id)
            page = RequestUtils.obtener_data_request_get(result_serie.url_obtencion_data_id_serie_ag).json()
            result_serie.id_serie_ag = page['_source']['INFO_SERIE'][0]['ID_SERIE_AG']

        return lista_result_serie












