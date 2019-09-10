from sys import stdin as a
import math
def suma(t1,t2):
    res_r=t1[0]+t2[0]
    res_i=t1[1]+t2[1]
    fin=(res_r,res_i)
    return fin
            

def resta(t1,t2):
    res_r=t1[0]-t2[0]
    res_i=t1[1]-t2[1]
    fin=(res_r,res_i)
    return fin


def multiplicacion(t1,t2):
    res_r=t1[0]*t2[0]+((t1[1]*t2[1])*-1)
    res_i=t1[0]*t2[1]+t1[1]*t2[0]
    fin=(res_r,res_i)
    return fin


def division(t1,t2):
    res_r=(t1[0]*t2[0] + t1[1]*t2[1])/((t2[0]**2)+(t2[1]**2))
    res_i=(t1[1]*t2[0] - t1[0]*t2[1])/((t2[0]**2)+(t2[1]**2))
    fin=(res_r,res_i)
    return fin


def modulo(t1):
    fin=(t1[0]**2 + t1[1]**2)**0.5
    return fin


def conjugado(t1):
    fin=(t1[0],t1[1]* -1)
    return fin


def polar(t1):
    res_mag=modulo(t1)
    res_ang=math.atan(t1[1]/t1[0])
    fin=(res_mag,res_ang)
    return fin


def cartesiano(t1):
    res_r=t1[0]*math.cos(t1[1])
    res_i=t1[0]*math.sin(t1[1])
    fin=(res_r,res_i)
    return fin


def fase(t1):
    fin=math.atan(t1[1]/t1[0])
    return fin


def suma_vector_comp(a1,a2):
    ar_fin=[]
    for i in range(len(a1)):
        ar_fin.append(suma(a1[i],a2[i]))
    return ar_fin

print(suma_vector_comp([(6,-4),(7,3),(4.2,-8.1),(0,-3)],[(16,2.3),(0,-7),(6,0),(0,-4)]))
#respuesta:[(22, -1.7000000000000002), (7, -4), (10.2, -8.1), (0, -7)]

def inversa_vector_comp(a1):
    ar_fin=[]
    for i in a1:
        tupla=(i[0]*-1,i[1]*-1)
        ar_fin.append(tupla)
    return ar_fin

print(inversa_vector_comp([(6,-4),(7,3),(4.2,-8.1),(0,-3)]))
#respuesta:[(-6, 4), (-7, -3), (-4.2, 8.1), (0, 3)]

def multi_esca_vecto(esc,a1):
    ar_fin=[]
    for i in range(len(a1)):
        ar_fin.append(multiplicacion(esc,a1[i]))
    return ar_fin

print(multi_esca_vecto((3,2),[(6,3),(0,0),(5,1),(4,0)]))
#respuesta:[(12, 21), (0, 0), (13, 13), (12, 8)]

def suma_matrices(mat1,mat2):
    mat_fin=[[None]*len(mat1) for i in range(len(mat1))]
    for i in range(len(mat_fin)):
        for j in range(len(mat_fin[i])):
            mat_fin[i][j]=suma(mat1[i][j],mat2[i][j])
    return mat_fin

print(suma_matrices([[(2,6),(-1,3)],[(3,9),(2,-2)]],[[(1,4),(4,7)],[(1,1),(0,5)]]))
#respuesta:[[(3, 10), (3, 10)], [(4, 10), (2, 3)]]
    
def inv_mat_comp(mat):
    mat_fin=[[0]*len(mat) for x in range(len(mat))]
    inv=(-1,0)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat_fin[i][j]=multiplicacion(inv,mat[i][j])
    return mat_fin
print(inv_mat_comp([[(2,6),(-1,3)],[(3,9),(2,-2)]]))
#respuesta:[[(-2, -6), (1, -3)], [(-3, -9), (-2, 2)]]

def multi_esca_mat(escalar,mat):
    mat_fin=[[0]*len(mat) for x in range(len(mat))]
    if type(escalar) is tuple:
        pass
    else:
        escalar=(escalar,0)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat_fin[i][j]=multiplicacion(escalar,mat[i][j])
    return mat_fin

print(multi_esca_mat((2,-5),[[(1,4),(4,7)],[(1,1),(0,5)]]))
#respuesta:[[(22, 3), (43, -6)], [(7, -3), (25, 10)]]

def mat_trans(mat):
    mat_fin=[[0]*len(mat) for x in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat_fin[i][j]=mat[j][i]
    return mat_fin

print(mat_trans([[(1,1),(-2,3)],[(8,0),(-7,-4)]]))
#respuesta:[[(1, 1), (8, 0)], [(-2, 3), (-7, -4)]]

def mat_conju(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j]=conjugado(mat[i][j])
    return mat

print(mat_conju([[(7,2),(-1,9)],[(0,4),(5,-6)]]))
#respuesta:[[(7, -2), (-1, -9)], [(0, -4), (5, 6)]]

def mat_adjun(mat):
    res=mat_trans(mat_conju(mat))
    return res

print(mat_adjun([[(1,-2),(-3,4)],[(5,-6),(-7,8)]]))
#respuesta:[[(1, 2), (5, 6)], [(-3, -4), (-7, -8)]]

def multi_mat(vec,mat):
    mat_fin=[[(0,0)]*len(mat[0]) for x in range(len(vec))]
    aux=0
    if len(mat_fin)==1:
        aux=1
    for i in range(len(vec)):
        for j in range(len(mat[0])):
            for k in range(len(mat_fin)+aux):

                mat_fin[i][j]=suma(mat_fin[i][j],multiplicacion(vec[i][k],mat[k][j]))
    return mat_fin

def accion_mat(vec,mat):
    return multi_mat(vec,mat)

print(accion_mat([[(1,2),(3,4)]],[[(4,5),(6,7)],[(8,9),(0,-1)]]))
#respuesta:[[(-18, 72), (-4, 16)]]

def norma_mat(mat):
    num1=0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            x=mat[i][j]
            num1+=(x[0]**2+x[1]**2)
    res=round(num1**0.5,3)
    return res

print(norma_mat([[(4,5),(6,7)],[(8,9),(0,-1)]]))
#respuesta:16.492

def distancia_mat(mat1,mat2):
    mat_fin=[[(0,0)]*len(mat1[0]) for x in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat_fin[i][j]=resta(mat1[i][j],mat2[i][j])
    res=norma_mat(mat_fin)
    return res

print(distancia_mat([[(2,6),(-1,3)],[(3,9),(2,-2)]],[[(1,4),(4,7)],[(1,1),(0,5)]]))
#respuesta:12.923

def unitaria(mat):
    mat_fin=multi_mat(mat,mat_adjun(mat))
    mat_uni=[[(0,0)]*len(mat[0])for x in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i==j:
                mat_uni[i][j]=(1,0)
    print(mat_uni)
    if mat_fin==mat_uni:
        return True
    else:
        return False

print(unitaria([[(1,0),(0,0)],[(0,0),(1,0)]]))
#respuesta:True

def hermitian(mat):
    if mat==mat_adjun(mat):
        return True
    else:
        return False

print(hermitian([[(1,0),(0,0)],[(0,0),(1,0)]]))
#respuesta:True

def produc_tensor_vec(vec1,vec2):
    fin=[]
    for i in range(len(vec1)):
        for j in range(len(vec2)):
            fin.append(multiplicacion(vec1[i],vec2[j]))
    return fin
print(produc_tensor_vec([(3,0),(4,0),(7,0)],[(-1,0),(2,0)]))
#respuesta:[(-3, 0), (6, 0), (-4, 0), (8, 0), (-7, 0), (14, 0)]

def produc_tensor_mat(mat1,mat2):
    fin=[]
    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            fin.append(multi_esca_mat(mat1[i][j],mat2))
    return fin

print(produc_tensor_mat([[(1,3),(1,8)],[(1,2),(3,1)]],[[(2,5),(3,5)],[(4,6),(2,9)]]))
#respuesta:[[[(-13, 11), (-12, 14)], [(-14, 18), (-25, 15)]], [[(-38, 21), (-37, 29)], [(-44, 38), (-70, 25)]], [[(-8, 9), (-7, 11)], [(-8, 14), (-16, 13)]], [[(1, 17), (4, 18)], [(6, 22), (-3, 29)]]]
