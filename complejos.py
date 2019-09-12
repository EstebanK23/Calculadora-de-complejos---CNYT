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


def inversa_vector_comp(a1):
    ar_fin=[]
    for i in a1:
        tupla=(i[0]*-1,i[1]*-1)
        ar_fin.append(tupla)
    return ar_fin


def multi_esca_vecto(esc,a1):
    ar_fin=[]
    for i in range(len(a1)):
        ar_fin.append(multiplicacion(esc,a1[i]))
    return ar_fin


def suma_matrices(mat1,mat2):
    mat_fin=[[None]*len(mat1) for i in range(len(mat1))]
    for i in range(len(mat_fin)):
        for j in range(len(mat_fin[i])):
            mat_fin[i][j]=suma(mat1[i][j],mat2[i][j])
    return mat_fin

   
def inv_mat_comp(mat):
    mat_fin=[[0]*len(mat) for x in range(len(mat))]
    inv=(-1,0)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat_fin[i][j]=multiplicacion(inv,mat[i][j])
    return mat_fin

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


def mat_trans(mat):
    mat_fin=[[0]*len(mat) for x in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat_fin[i][j]=mat[j][i]
    return mat_fin

def mat_conju(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j]=conjugado(mat[i][j])
    return mat


def mat_adjun(mat):
    res=mat_trans(mat_conju(mat))
    return res


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


def norma_mat(mat):
    num1=0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            x=mat[i][j]
            num1+=(x[0]**2+x[1]**2)
    res=round(num1**0.5,3)
    return res


def distancia_mat(mat1,mat2):
    mat_fin=[[(0,0)]*len(mat1[0]) for x in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat_fin[i][j]=resta(mat1[i][j],mat2[i][j])
    res=norma_mat(mat_fin)
    return res


def unitaria(mat):
    mat_fin=multi_mat(mat,mat_adjun(mat))
    mat_uni=[[(0,0)]*len(mat[0])for x in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i==j:
                mat_uni[i][j]=(1,0)
    if mat_fin==mat_uni:
        return True
    else:
        return False


def hermitian(mat):
    if mat==mat_adjun(mat):
        return True
    else:
        return False


def produc_tensor_vec(vec1,vec2):
    fin=[]
    for i in range(len(vec1)):
        for j in range(len(vec2)):
            fin.append(multiplicacion(vec1[i],vec2[j]))
    return fin

def produc_tensor_mat(mat1,mat2):
    fin=[]
    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            fin.append(multi_esca_mat(mat1[i][j],mat2))
    return fin
