import unittest
import complejos

class Prueba_complejos(unittest.TestCase):
    def test_suma(self):
        pc=(3,-1)
        sc=(1,4)
        res=(4, 3)
        rescod=complejos.suma(pc,sc)
        self.assertEqual(res,rescod)

    def test_resta(self):
        pc=(5,7)
        sc=(7,-4)
        res=(-2, 11)
        rescod=complejos.resta(pc,sc)
        self.assertEqual(res,rescod)

    def test_multi(self):
        pc=(3,-1)
        sc=(1,4)
        res=(7, 11)
        rescod=complejos.multiplicacion(pc,sc)
        self.assertEqual(res,rescod)

    def test_division(self):
        pc=(1,2)
        sc=(1,3)
        res=(0.7, -0.1)
        rescod=complejos.division(pc,sc)
        self.assertEqual(res,rescod)

    def test_modulo(self):
        pc=(4,-2)
        res=4.47213595499958
        rescod=complejos.modulo(pc)
        self.assertEqual(res,rescod)

    def test_conjugado(self):
        pc=(9,-3)
        res=(9, 3)
        rescod=complejos.conjugado(pc)
        self.assertEqual(res,rescod)

    def test_polar(self):
        pc=(5,-3)
        res=(5.830951894845301, -0.5404195002705842)
        rescod=complejos.polar(pc)
        self.assertEqual(res,rescod)

    def test_cartesiano(self):
        pc=(3,29)
        res=(-2.244172589067001, -1.9909016526389025)
        rescod=complejos.cartesiano(pc)
        self.assertEqual(res,rescod)

    def test_fase(self):
        pc=(6,-8)
        res=-0.9272952180016122
        rescod=complejos.fase(pc)
        self.assertEqual(res,rescod)

    def test_sum_vec(self):
        pv=[(6,-4),(7,3),(4.2,-8.1),(0,-3)]
        sv=[(16,2.3),(0,-7),(6,0),(0,-4)]
        res=[(22, -1.7000000000000002), (7, -4), (10.2, -8.1), (0, -7)]
        rescod=complejos.suma_vector_comp(pv,sv)
        self.assertEqual(res,rescod)

    def test_inv_vec(self):
        pv=[(6,-4),(7,3),(4.2,-8.1),(0,-3)]
        res=[(-6, 4), (-7, -3), (-4.2, 8.1), (0, 3)]
        rescod=complejos.inversa_vector_comp(pv)
        self.assertEqual(res,rescod)

    def test_mult_esc_vec(self):
        esc=(3,2)
        pm=[(6,3),(0,0),(5,1),(4,0)]
        res=[(12, 21), (0, 0), (13, 13), (12, 8)]
        rescod=complejos.multi_esca_vecto(esc,pm)
        self.assertEqual(res,rescod)

    def test_sum_mat(self):
        pm=[[(2,6),(-1,3)],[(3,9),(2,-2)]]
        sm=[[(1,4),(4,7)],[(1,1),(0,5)]]
        res=[[(3, 10), (3, 10)], [(4, 10), (2, 3)]]
        rescod=complejos.suma_matrices(pm,sm)
        self.assertEqual(res,rescod)

    def test_inv_mat(self):
        pm=[[(2,6),(-1,3)],[(3,9),(2,-2)]]
        res=[[(-2, -6), (1, -3)], [(-3, -9), (-2, 2)]]
        rescod=complejos.inv_mat_comp(pm)
        self.assertEqual(res,rescod)

    def test_mult_esc_mat(self):
        esc=(2,-5)
        pm=[[(1,4),(4,7)],[(1,1),(0,5)]]
        res=[[(22, 3), (43, -6)], [(7, -3), (25, 10)]]
        rescod=complejos.multi_esca_mat(esc,pm)
        self.assertEqual(res,rescod)

    def test_matr_trans(self):
        pm=[[(1,1),(-2,3)],[(8,0),(-7,-4)]]
        res=[[(1, 1), (8, 0)], [(-2, 3), (-7, -4)]]
        rescod=complejos.mat_trans(pm)
        self.assertEqual(res,rescod)

    def test_matr_conjug(self):
        pm=[[(7,2),(-1,9)],[(0,4),(5,-6)]]
        res=[[(7, -2), (-1, -9)], [(0, -4), (5, 6)]]
        rescod=complejos.mat_conju(pm)
        self.assertEqual(res,rescod)

    def test_matr_adju(self):
        pm=[[(1,-2),(-3,4)],[(5,-6),(-7,8)]]
        res=[[(1, 2), (5, 6)], [(-3, -4), (-7, -8)]]
        rescod=complejos.mat_adjun(pm)
        self.assertEqual(res,rescod)

    def test_accion(self):
        vec=[[(1,2),(3,4)]]
        pm=[[(4,5),(6,7)],[(8,9),(0,-1)]]
        res=[[(-18, 72), (-4, 16)]]
        rescod=complejos.accion_mat(vec,pm)
        self.assertEqual(res,rescod)

    def test_norma(self):
        pm=[[(4,5),(6,7)],[(8,9),(0,-1)]]
        res=16.492
        rescod=complejos.norma_mat(pm)
        self.assertEqual(res,rescod)

    def test_distancia(self):
        pm=[[(2,6),(-1,3)],[(3,9),(2,-2)]]
        sm=[[(1,4),(4,7)],[(1,1),(0,5)]]
        res=12.923
        rescod=complejos.distancia_mat(pm,sm)
        self.assertEqual(res,rescod)

    def test_unit(self):
        pm=[[(1,0),(0,0)],[(0,0),(1,0)]]
        res=True
        rescod=complejos.unitaria(pm)
        self.assertEqual(res,rescod)

    def test_hermi(self):
        pm=[[(1,0),(0,0)],[(0,0),(1,0)]]
        res=True
        rescod=complejos.hermitian(pm)
        self.assertEqual(res,rescod)

    def test_prod_tens_vec(self):
        pv=[(3,0),(4,0),(7,0)]
        sv=[(-1,0),(2,0)]
        res=[(-3, 0), (6, 0), (-4, 0), (8, 0), (-7, 0), (14, 0)]
        rescod=complejos.produc_tensor_vec(pv,sv)
        self.assertEqual(res,rescod)

    def test_prod_tens_mat(self):
        pm=[[(1,3),(1,8)],[(1,2),(3,1)]]
        sm=[[(2,5),(3,5)],[(4,6),(2,9)]]
        res=[[[(-13, 11), (-12, 14)], [(-14, 18), (-25, 15)]], [[(-38, 21), (-37, 29)], [(-44, 38), (-70, 25)]], [[(-8, 9), (-7, 11)], [(-8, 14), (-16, 13)]], [[(1, 17), (4, 18)], [(6, 22), (-3, 29)]]]
        rescod=complejos.produc_tensor_mat(pm,sm)
        self.assertEqual(res,rescod)

if __name__ == '__main__':
    unittest.main()
