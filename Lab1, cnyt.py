from sys import stdin as a
import math
def suma(t1,t2):
    res_r=t1[0]+t2[0]
    res_i=t1[1]+t2[1]
    fin=(res_r,res_i)
    return fin
            
suma((3,-1),(1,4))

def resta(t1,t2):
    res_r=t1[0]-t2[0]
    res_i=t1[1]-t2[1]
    fin=(res_r,res_i)
    return fin
    
resta((5,7),(7,-4))

def multiplicacion(t1,t2):
    res_r=t1[0]*t2[0]+((t1[1]*t2[1])*-1)
    res_i=t1[0]*t2[1]+t1[1]*t2[0]
    fin=(res_r,res_i)
    return fin

multiplicacion((3,-1),(1,4))

def division(t1,t2):
    res_r=(t1[0]*t2[0] + t1[1]*t2[1])/((t1[0]**2)+(t2[0]**2))
    res_i=(t1[1]*t2[0] - t1[0]*t2[1])/((t1[0]**2)+(t2[0]**2))
    fin=(res_r,res_i)
    return fin

division((3,2),(8,5))

def modulo(t1):
    fin=(t1[0]**2 + t1[1]**2)**0.5
    return fin

modulo((4,-2))

def conjugado(t1):
    fin=(t1[0],t1[1]* -1)
    return fin

conjugado((9,-3))

def polar(t1):
    res_mag=modulo(t1)
    res_ang=math.atan(t1[1]/t1[0])
    fin=(res_mag,res_ang)
    return fin

polar((5,-3))

def cartesiano(t1):
    res_r=t1[0]*math.cos(t1[1])
    res_i=t1[0]*math.sin(t1[1])
    fin=(res_r,res_i)
    return fin

cartesiano((3,29))

def fase(t1):
    fin=math.atan(t1[1]/t1[0])
    return fin

fase((6,-8))
