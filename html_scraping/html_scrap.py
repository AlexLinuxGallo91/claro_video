from bs4 import BeautifulSoup
from utils import constantes_claro_video as const
from utils.request_utils import RequestUtils
from result_serie.result_serie import ResultSerie
from result_serie.result_capitulo import ResultCapitulo

class HtmlScraping:

    @staticmethod
    def obtencion_capitulos_temporadas_por_id_serie_ag(lista_series_result: list[ResultSerie]):

        index_columna_id_temp = index_columna_orden_temporada = index_columna_episodes = index_columna_orden_capitulo = 0
        columna_id_temp = 'ID Temp.'
        columna_orden_temporada = 'Orden Temporada'
        columna_episodes = 'EPISODES'
        columna_orden_capitulo = 'Orden Capitulo'

        for serie_result in lista_series_result:
            url_por_consultar = const.URL_CONSULTA_CAPITULOS_SERIE_HTML.format(serie_result.id_serie_ag)
            serie_result.url_obtencion_data_capitulos = url_por_consultar
            page = RequestUtils.obtener_data_request_get(url_por_consultar)
            soup = BeautifulSoup(page.content, "html5lib")

            tabla_episodios = soup.find('table')
            lista_columnas_header = tabla_episodios.findAll('th')
            lista_filas_tr_localizadas = tabla_episodios.findAll('tr')
            lista_filas_td_localizadas = [tr.findAll('td') for tr in lista_filas_tr_localizadas if
                                          len(tr.findAll('td')) > 1]

            # se obtienen los indices de los headers de los capitulos y temporadas
            for index, columna_header in enumerate(lista_columnas_header):
                if columna_id_temp == columna_header.get_text(): index_columna_id_temp = index
                if columna_episodes == columna_header.get_text(): index_columna_episodes = index
                if columna_orden_temporada == columna_header.get_text(): index_columna_orden_temporada = index
                if columna_orden_capitulo == columna_header.get_text(): index_columna_orden_capitulo = index

            # de la lista de filas td, se obtienen los datos de cada capitulo de la serie y la almacena
            # en el objeto ResultSerie

            for episodio_td in lista_filas_td_localizadas:

                result_episodio = ResultCapitulo(
                    episodio_td[index_columna_id_temp].get_text(),
                    episodio_td[index_columna_orden_temporada].get_text(),
                    episodio_td[index_columna_episodes].get_text(),
                    episodio_td[index_columna_orden_capitulo].get_text()
                )

                serie_result.lista_de_episodios.append(result_episodio)

        return lista_series_result





