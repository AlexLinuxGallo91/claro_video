from json_scraping.json_scrap import JsonScraping
from html_scraping.html_scrap import HtmlScraping
from utils.arg_utils import ArgUtils
from utils import constantes_claro_video as const
from utils.request_utils import RequestUtils
from utils.validacion_episodios_utils import ValidacionEpisodiosUtils
import sys

def main(json_param):
    const.PARAM_NODO = json_param['nodo']
    const.PARAM_REGION = json_param['region']
    const.URL_FORMADA = const.URL_NODO_BASE.format(const.PARAM_NODO, const.PARAM_REGION)

    json_encabezado = RequestUtils.obtener_data_request_get(const.URL_FORMADA).json()

    # obtiene toda la informacion de todos los encabezados como peliculas, series y documentales
    lista_series_en_encabezado = JsonScraping.obtencion_lista_result_series_encabezado(json_encabezado)

    # se obtienen los group id de las series
    lista_result_serie = JsonScraping.obtencion_lista_result_series_con_group_id(lista_series_en_encabezado)

    # buscamos y establecemos el "id serie ag" de cada serie
    lista_result_serie = JsonScraping.obtencion_id_serie_ag_mediante_group_id(lista_result_serie)

    # buscamos los capitulos de cada serie por medio de web scrapping en la tabla html
    lista_result_serie = HtmlScraping.obtencion_capitulos_temporadas_por_id_serie_ag(lista_result_serie)

    # validacion de lista de capitulos
    for result_serie in lista_result_serie:
        result_serie.numero_total_de_capitulos = len(result_serie.lista_de_episodios)
        result_serie = ValidacionEpisodiosUtils.establecer_numero_de_capitulos_a_int(result_serie)
        result_serie = ValidacionEpisodiosUtils.obtencion_orden_total_de_temporadas_y_episodios(result_serie)
        result_serie = ValidacionEpisodiosUtils.validar_capitulos_faltantes_por_temporada(result_serie)

    [print(result) for result in lista_result_serie]

args = ArgUtils.validar_args(sys.argv)
main(args)