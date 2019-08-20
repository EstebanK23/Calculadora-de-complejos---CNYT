from sys import stdin as a
import math
def suma(t1,t2):
    res_r=t1[0]+t2[0]
    res_i=t1[1]+t2[1]
    fin=(res_r,res_i)
    return fin
            
print(suma((3,-1),(1,4)))
#respuesta:(4, 3)

def resta(t1,t2):
    res_r=t1[0]-t2[0]
    res_i=t1[1]-t2[1]
    fin=(res_r,res_i)
    return fin
    
print(resta((5,7),(7,-4)))
#respuesta:(-2, 11)

def multiplicacion(t1,t2):
    res_r=t1[0]*t2[0]+((t1[1]*t2[1])*-1)
    res_i=t1[0]*t2[1]+t1[1]*t2[0]
    fin=(res_r,res_i)
    return fin

print(multiplicacion((3,-1),(1,4)))
#respuesta:(7, 11)

def division(t1,t2):
    res_r=(t1[0]*t2[0] + t1[1]*t2[1])/((t2[0]**2)+(t2[1]**2))
    res_i=(t1[1]*t2[0] - t1[0]*t2[1])/((t2[0]**2)+(t2[1]**2))
    fin=(res_r,res_i)
    return fin

print(division((1,2),(1,3)))
#respuesta:(0.4657534246575342, 0.0136986301369863)

def modulo(t1):
    fin=(t1[0]**2 + t1[1]**2)**0.5
    return fin

print(modulo((4,-2)))
#respuesta:4.47213595499958

def conjugado(t1):
    fin=(t1[0],t1[1]* -1)
    return fin

print(conjugado((9,-3)))
#respuesta:(9, 3)

def polar(t1):
    res_mag=modulo(t1)
    res_ang=math.atan(t1[1]/t1[0])
    fin=(res_mag,res_ang)
    return fin

print(polar((5,-3)))
#respuesta:(5.830951894845301, -0.5404195002705842)

def cartesiano(t1):
    res_r=t1[0]*math.cos(t1[1])
    res_i=t1[0]*math.sin(t1[1])
    fin=(res_r,res_i)
    return fin

print(cartesiano((3,29)))
#respuesta:(-2.244172589067001, -1.9909016526389025)

def fase(t1):
    fin=math.atan(t1[1]/t1[0])
    return fin

print(fase((6,-8)))
#respuesta:-0.9272952180016122
