from typing import List
from result_serie.result_validacion import ResultValidacionImagen
import sys
import requests

class RequestUtils:

    @staticmethod
    def obtener_data_request_get(url_por_consultar):
        hubo_problema = False

        try:
            return requests.get(url_por_consultar)
        except requests.exceptions.ConnectionError:
            print('Se presenta error de conexion al servidor sin obtener respuesta hacia {}'.format(url_por_consultar))
            hubo_problema = True

        except TimeoutError:
            print('Se presenta error Timeout hacia el servidor sin obtener respuesta hacia {}'.format(
                url_por_consultar))
            hubo_problema = True

        except Exception as e:
            print('Se presenta error de conexion al servidor sin obtener respuesta hacia {}. Error detallado: {}'.
                  format(url_por_consultar, e))
            hubo_problema = True

        if hubo_problema:
            sys.exit(1)

    @staticmethod
    def la_url_es_valida(url_por_verificar:str):
        try:
            response = requests.get(url_por_verificar)
        except requests.exceptions.ConnectionError:
            return False
        except TimeoutError:
            return False
        except Exception:
            return False

        if response.status_code != 200:
            return False

        return True

    @staticmethod
    def la_url_contiene_imagen(url_por_verificar:str):

        image_formats = ("image/png", "image/jpeg", "image/jpg")
        response = requests.head(url_por_verificar)

        if response.headers["content-type"] in image_formats:
            return True
        else:
            return False

    @staticmethod
    def validar_url_imagen(url_por_verificar:str):
        return RequestUtils.la_url_es_valida(url_por_verificar) and \
               RequestUtils.la_url_contiene_imagen(url_por_verificar)

    @staticmethod
    def validar_lista_url_imagenes(lista_url_imagenes:List[ResultValidacionImagen]):

        for result in lista_url_imagenes:
            result.validacion_correcta = RequestUtils.validar_url_imagen(result.url_por_probar)

        return lista_url_imagenes