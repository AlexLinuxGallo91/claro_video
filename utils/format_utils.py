
class FormatUtils:

    @staticmethod
    def is_int(cadena: str):
        try:
            int(cadena)
            return True
        except ValueError:
            return False
