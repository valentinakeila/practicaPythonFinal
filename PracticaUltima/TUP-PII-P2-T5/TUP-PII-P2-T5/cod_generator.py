import random
import string

class CodGenerator():

    @staticmethod
    def generar_codigo() -> str:
        '''
            Genera un codigo de todos caracteres numericos de longitud 10
        '''
        numbers = string.digits
        result_str = ''.join(random.choice(numbers) for i in range(10))
        return result_str