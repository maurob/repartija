# -- coding=utf-8 --

import unittest
from repartija import Repartija

class Test(unittest.TestCase):

    def test_precio_de_hora_igual(self):
        """ Si cobramos igual la hora, deberíamos repartirnos en función de las horas trabajadas """
        uut = Repartija()
        uut.set_precios_por_hora({'martin': 10, 'mauro': 10})
        
        # Igual horas trabajadas
        uut.set_trabajo({'martin': 1, 'mauro': 1})
        r = uut.ganancia_individual()
        self.assertEqual(r['martin'], r['mauro'])

        # Sólo uno trabaja
        uut.set_trabajo({'martin': 0, 'mauro': 1})
        r = uut.ganancia_individual()
        self.assertEqual(r['martin'], 0)
        self.assertEqual(r['mauro'], 10)
        
    def test_precio_de_hora_diferentes(self):
        """ Si cobramos diferente la hora pero trabajamos la misma cantidad de horas,
        las ganancias debería ser directamente el precio por hora individual por la
        cantidad de horas. """
        uut = Repartija()
        uut.set_precios_por_hora({'martin': 230, 'mauro': 170})

        uut.set_trabajo({'martin': 1, 'mauro': 1})
        r = uut.ganancia_individual()
        self.assertEqual(r['martin'], 230)
        self.assertEqual(r['mauro'], 170)

        uut.set_trabajo({'martin': 2, 'mauro': 2})
        r = uut.ganancia_individual()
        self.assertEqual(r['martin'], 230*2)
        self.assertEqual(r['mauro'], 170*2)
        
    def test_uno_no_trabaja(self):
        """ Si uno no trabaja el otro tiene que cobrar el precio_medio_por_hora,
        es decir el precio expuesto para el cliente """
        uut = Repartija()
        uut.set_precios_por_hora({'martin': 230, 'mauro': 170})
        self.assertEqual(uut.precio_medio_por_hora(), 200)

        uut.set_trabajo({'martin': 1, 'mauro': 0})
        r = uut.ganancia_individual()
        self.assertEqual(r['martin'], 200)
        self.assertEqual(r['mauro'], 0)
        
    def test_uno_trabaja_gratis(self):
        """ Si uno trabaja gratis el otro se ve afectado por cuanto trabaje el gratuito """
        uut = Repartija()
        uut.set_precios_por_hora({'martin': 100, 'mauro': 0})
        self.assertEqual(uut.precio_medio_por_hora(), 50)
        
        # El gratuito no trabaja
        uut.set_trabajo({'martin': 1, 'mauro': 0})
        r = uut.ganancia_individual()
        self.assertEqual(r['martin'], 50)
        self.assertEqual(r['mauro'], 0)

        # El gratuito trabaja lo mismo
        uut.set_trabajo({'martin': 1, 'mauro': 1})
        r = uut.ganancia_individual()
        self.assertEqual(r['martin'], 100)
        self.assertEqual(r['mauro'], 0)

        # El gratuito trabaja más
        uut.set_trabajo({'martin': 1, 'mauro': 2})
        r = uut.ganancia_individual()
        self.assertEqual(r['martin'], 150)
        self.assertEqual(r['mauro'], 0)

        # Sólo el gratuito trabaja y sobra plata
        uut.set_trabajo({'martin': 0, 'mauro': 1})
        r = uut.ganancia_individual()
        self.assertEqual(r[None], 50)
        self.assertEqual(r['mauro'], 0)
        self.assertEqual(r['martin'], 0)

if __name__=='__main__':
    unittest.main()
