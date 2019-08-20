import unittest
import complejos

class Pruebas_complejos(unittest.TestCase):
    def prueba_suma(self):
        pc=(3,-1)
        sc=(1,4)
        res=(4, 3)
        rescod=complejos.suma(pc,sc)
        self.assertEqual(res,rescod)

    def prueba_resta(self):
        pc=(5,7)
        sc=(7,-4)
        res=(-2, 11)
        rescod=complejos.resta(pc,sc)
        self.assertEqual(res,rescod)

    def prueba_multi(self):
        pc=(3,-1)
        sc=(1,4)
        res=(7, 11)
        rescod=complejos.multiplicacion(pc,sc)
        self.assertEqual(res,rescod)

    def prueba_division(self):
        pc=(3,2)
        sc=(8,5)
        res=(0.4657534246575342, 0.0136986301369863)
        rescod=complejos.division(pc,sc)
        self.assertEqual(res,rescod)

    def prueba_division(self):
        pc=(1,2)
        sc=(1,3)
        res=(0.7, -0.1)
        rescod=complejos.division(pc,sc)
        self.assertEqual(res,rescod)

    def prueba_modulo(self):
        pc=(4,-2)
        res=4.47213595499958
        rescod=complejos.modulo(pc)
        self.assertEqual(res,rescod)

    def prueba_conjugado(self):
        pc=(9,-3)
        res=(9, 3)
        rescod=complejos.conjugado(pc)
        self.assertEqual(res,rescod)

    def prueba_polar(self):
        pc=(5,-3)
        res=(5.830951894845301, -0.5404195002705842)
        rescod=complejos.polar(pc)
        self.assertEqual(res,rescod)

    def prueba_cartesiano(self):
        pc=(3,29)
        res=(-2.244172589067001, -1.9909016526389025)
        rescod=complejos.cartesiano(pc)
        self.assertEqual(res,rescod)

    def prueba_fase(self):
        pc=(6,-8)
        res=-0.9272952180016122
        rescod=complejos.fase(pc)
        self.assertEqual(res,rescod)

if __name__ == '__main__':
    unittest.main()
