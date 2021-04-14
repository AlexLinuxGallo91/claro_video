from typing import List
import json
import sys

class ArgUtils:

    @staticmethod
    def validar_args(args:List):
        param = {}

        if len(args) < 2:
            print('Parametro no establecido, favor de establecer el parametro en formato JSON.')
            sys.exit(1)

        try:
            param = json.loads(args[1])
        except ValueError as e:
            print('El parametro establecido no tiene formato JSON, favor de establecerlo correctamente.')
            sys.exit(1)

        if 'nodo' not in param.keys():
            print('El parametro "nodo" no se encuentra establecido dentro del JSON, favor de establecerlo '
                  'correctamente.')
            sys.exit(1)

        if 'region' not in param.keys():
            print('El parametro "region" no se encuentra establecido dentro del JSON, favor de establecerlo '
                  'correctamente.')
            sys.exit(1)

        return param