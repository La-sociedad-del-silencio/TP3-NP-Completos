import unittest
from certificador_eficiente import *

class CertificadorEficiente(unittest.TestCase):

    def test_1_suma_igual_a_B(self):
        self.assert_solucion_valida(self.setUp)
    
    def test_2_suma_menor_a_B(self):
        self.assert_solucion_valida(self.setUp_con_B_mayor_a_suma)
        
    def test_3_suma_mayor_a_B(self):
        self.assert_solucion_invalida(self.setUp_con_B_menor_a_suma)
        
    def test_4_hay_maestros_sin_grupo(self):
        self.assert_solucion_invalida(self.setUp_maestro_sin_grupo)
        
    def test_5_hay_maestros_con_mas_de_un_grupo(self):
        self.assert_solucion_invalida(self.setUp_maestro_con_mas_de_un_grupo)
        
    def test_6_hay_menos_de_k_grupo(self):
        self.assert_solucion_invalida(self.setUp_menos_de_k_grupos)
        
    def test_7_hay_mas_de_k_grupo(self):
        self.assert_solucion_invalida(self.setUp_mas_de_k_grupos)
  
    def assert_solucion_valida(self, funcion_set_up):
        habilidades, k, B, S = funcion_set_up()
        es_valida = validador_problema_tribu_del_agua(habilidades, k, B, S)
        self.assertTrue(es_valida)
        
    def assert_solucion_invalida(self, funcion_set_up):
        habilidades, k, B, S = funcion_set_up()
        es_valida = validador_problema_tribu_del_agua(habilidades, k, B, S)
        self.assertFalse(es_valida)
    
    def setUp(self):
        k = 3
        habilidades = [("Hasook", 120), ("Hama", 445), ("Senna", 546), ("Hama I", 222), ("Wei", 551), ("Wei I", 330)] 
        S = [{"Wei", "Hasook"}, {"Senna", "Hama I"}, {"Hama", "Wei I"}]
        B = 1640690
        return habilidades, k, B, S
    
    def setUp_con_B_mayor_a_suma(self):
        habilidades, k, B, S = self.setUp()
        return habilidades, k, B+1, S
    
    def setUp_con_B_menor_a_suma(self):
        habilidades, k, B, S = self.setUp()
        return habilidades, k, B-1, S
    
    def setUp_maestro_sin_grupo(self):
        habilidades, k, B, S = self.setUp()
        S[2].remove("Hama")
        return habilidades, k, B, S
    
    def setUp_maestro_con_mas_de_un_grupo(self):
        habilidades, k, B, S = self.setUp()
        S[2].add("Wei")
        return habilidades, k, B, S
    
    def setUp_menos_de_k_grupos(self):
        habilidades, k, B, S = self.setUp()
        S.pop()
        return habilidades, k, B, S
    
    def setUp_mas_de_k_grupos(self):
        habilidades, k, B, S = self.setUp()
        S.append({"Infiltrado"})
        return habilidades, k, B, S
        
        
if __name__ == '__main__':
    unittest.main()