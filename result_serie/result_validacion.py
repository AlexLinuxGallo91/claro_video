class ResultValidacionImagen:

    def __init__(self, nombre_imagen_por_probar='', url_por_probar = ''):
        self.nombre_imagen_por_probar = nombre_imagen_por_probar
        self.url_por_probar = url_por_probar
        self.validacion_correcta = True

class ResultValidacionEpisodios:

    def __init__(self):
        self.msg_error = ''
        self.validacion_correcta = True