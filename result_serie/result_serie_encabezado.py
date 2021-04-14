import utils.constantes_claro_video as const
from typing import Dict

class ResultSerieEncabezado:

    def __init__(self, json_encabezado:Dict={}):

        self.title = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_TITLE] if 'title' in json_encabezado.keys() else const.CADENA_VACIA

        self.title_uri = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_TITLE_URI] if 'title_uri' in json_encabezado.keys() else const.CADENA_VACIA

        self.volant = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_VOLANT] if 'volant' in json_encabezado.keys() else const.CADENA_VACIA

        self.crest = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_CREST] if 'crest' in json_encabezado.keys() else const.CADENA_VACIA

        self.url = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_URL] if 'url' in json_encabezado.keys() else const.CADENA_VACIA

        self.image_highlight = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_IMAGE_HIGHLIGHT] if 'image_highlight' in json_encabezado.keys() else \
            const.CADENA_VACIA

        self.image_large = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_IMAGE_LARGE] if 'image_large' in json_encabezado.keys() else const.CADENA_VACIA

        self.image_medium = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_IMAGE_MEDIUM] if 'image_medium' in json_encabezado.keys() else const.CADENA_VACIA

        self.image_small = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_IMAGE_SMALL] if 'image_small' in json_encabezado.keys() else const.CADENA_VACIA

        self.image_background = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_IMAGE_BACKGROUND] if 'image_background' in json_encabezado.keys() else \
            const.CADENA_VACIA

        self.group_id = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_GROUP_ID] if 'group_id' in json_encabezado.keys() else const.CADENA_VACIA

        self.special = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_SPECIAL] if 'special' in json_encabezado.keys() else const.CADENA_VACIA

        self.section = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_SECTION] if 'section' in json_encabezado.keys() else const.CADENA_VACIA

        self.format_types = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_FORMAT_TYPES] if 'format_types' in json_encabezado.keys() else const.CADENA_VACIA

        self.live_enabled = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_LIVE_ENABLED] if 'live_enabled' in json_encabezado.keys() else const.CADENA_VACIA

        self.live_type = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_LIVE_TYPE] if 'live_type' in json_encabezado.keys() else const.CADENA_VACIA

        self.live_ref = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_LIVE_REF] if 'live_ref' in json_encabezado.keys() else const.CADENA_VACIA

        self.rating_code = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_RATING_CODE] if 'rating_code' in json_encabezado.keys() else const.CADENA_VACIA

        self.proveedor_name = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_PROVEEDOR_NAME] if 'proveedor_name' in json_encabezado.keys() else \
            const.CADENA_VACIA

        self.proveedor_code = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_PROVEEDOR_CODE] if 'proveedor_code' in json_encabezado.keys() else \
            const.CADENA_VACIA

        self.is_series = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_IS_SERIES] if 'is_series' in json_encabezado.keys() else const.CADENA_VACIA

        self.user_status = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_USER_STATUS] if 'user_status' in json_encabezado.keys() else const.CADENA_VACIA

        self.type = json_encabezado[
            const.KEY_SERIE_ENCABEZADO_TYPE] if 'type' in json_encabezado.keys() else const.CADENA_VACIA
