from result_serie.result_serie import ResultSerie
from utils.format_utils import FormatUtils
from typing import List

class ValidacionEpisodiosUtils:

    @staticmethod
    def establecer_numero_de_capitulos_a_int(result_serie:ResultSerie):
        for capitulo in result_serie.lista_de_episodios:

            capitulo.id_temp = int(capitulo.id_temp) if FormatUtils.is_int(
                capitulo.id_temp) else capitulo.id_temp

            capitulo.orden_capitulo = int(capitulo.orden_capitulo) if FormatUtils.is_int(
                capitulo.orden_capitulo) else capitulo.orden_capitulo

            capitulo.episodes = int(capitulo.episodes) if FormatUtils.is_int(
                capitulo.episodes) else capitulo.episodes

            capitulo.orden_de_temporada = int(capitulo.orden_de_temporada) if FormatUtils.is_int(
                capitulo.orden_de_temporada) else capitulo.orden_de_temporada

        return result_serie

    @staticmethod
    def obtencion_orden_total_de_temporadas_y_episodios(result_serie:ResultSerie):

        lista_temporadas = []

        [lista_temporadas.append(cap.orden_de_temporada) for cap in result_serie.lista_de_episodios]
        lista_temporadas = list(dict.fromkeys(lista_temporadas))

        for temp in lista_temporadas:
            result_serie.orden_total_temporadas_episodios[temp] = []
            for episodio in result_serie.lista_de_episodios:
                if episodio.orden_de_temporada == temp:
                    result_serie.orden_total_temporadas_episodios[temp].append(episodio.orden_capitulo)
            sorted(result_serie.orden_total_temporadas_episodios[temp])

        return result_serie

    @staticmethod
    def validar_capitulos_faltantes_en_lista(lista_capitulos:List[int]):
        if len(lista_capitulos) > 0:
            return [x for x in range(lista_capitulos[0], lista_capitulos[-1] + 1)if x not in lista_capitulos]
        else:
            return []

    @staticmethod
    def validar_capitulos_faltantes_por_temporada(result_serie:ResultSerie):

        for temporada in result_serie.orden_total_temporadas_episodios:
            lista_capitulos_faltantes = []
            lista_capitulos_faltantes = ValidacionEpisodiosUtils.validar_capitulos_faltantes_en_lista(
                result_serie.orden_total_temporadas_episodios[temporada])

            if len(lista_capitulos_faltantes) > 0:
                result_serie.orden_total_temporadas_episodios_faltantes[temporada] = lista_capitulos_faltantes

        return result_serie


