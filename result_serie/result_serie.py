from result_serie.result_validacion import ResultValidacionEpisodios
from result_serie.result_serie_encabezado import ResultSerieEncabezado

class ResultSerie:

    def __init__(self, group_id, result_serie_encabezado:ResultSerieEncabezado=None):

        if isinstance(result_serie_encabezado, ResultSerieEncabezado):
            self.result_serie_encabezado = result_serie_encabezado
        else:
            self.result_serie_encabezado = ResultSerieEncabezado({})

        self.group_id = group_id
        self.titulo_de_la_serie = ''
        self.lista_de_episodios = []
        self.orden_total_temporadas_episodios = {}
        self.orden_total_temporadas_episodios_faltantes = {}
        self.numero_total_de_capitulos = 0
        self.id_serie_ag = None
        self.nodo = ''
        self.region = ''
        self.url_obtencion_data_encabezado = ''
        self.url_obtencion_data_id_serie_ag = ''
        self.url_obtencion_data_capitulos = ''
        self.lista_validaciones_url_imagenes_por_revisar = []
        self.validacion_continuidad_capitulos = ResultValidacionEpisodios()

    def __str__(self):
        text = ''
        text += 'titulo de la serie: {}\n'.format(self.titulo_de_la_serie)
        text += 'group id: {}\n'.format(self.group_id)
        text += 'lista de episodios: {}\n'.format(self.lista_de_episodios)
        text += 'id serie ag: {}\n'.format(self.id_serie_ag)

        return text
