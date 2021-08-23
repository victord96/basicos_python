import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False 

def positivo_en_covid(persona):
    if persona:
        covid = persona
        return covid
    else:
        return persona

class PruebaDeCristalTest(unittest.TestCase):
    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 17
        
        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)

    def test_sin_covid(self):
        persona = []    
        covid = positivo_en_covid(persona)

        self.assertEqual(persona, covid)

        persona = ['Juan']    
        covid = positivo_en_covid(persona)

        self.assertEqual(persona, covid)
        
        persona = ['Juan','David']    
        covid = positivo_en_covid(persona)

        self.assertEqual(persona, covid)

if __name__ == '__main__':
    unittest.main()