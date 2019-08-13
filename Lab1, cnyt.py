from sys import stdin as a
def suma(t1,t2):
    res1=t1[0]+t2[0]
    res2=t1[1]+t2[1]
    if res2>0:
        print(str(res1)+"+"+str(res2)+"i")
    elif res2<0:
        print(str(res1)+str(res2)+"i")
    else:
        print(res1)

        
suma((3,-1),(1,4))

def resta(t1,t2):
    res1=t1[0]-t2[0]
    res2=t1[1]-t2[1]
    if res2>0:
        print(str(res1)+"+"+str(res2)+"i")
    elif res2<0:
        print(str(res1)+str(res2)+"i")
    else:
        print(res1)
    
resta((5,7),(7,-4))

def mult(t1,t2):
    res1=t1[0]*t2[0]+((t1[1]*t2[1])*-1)
    res2=t1[0]*t2[1]+t1[1]*t2[0]
    if res2>0:
        print(str(res1)+"+"+str(res2)+"i")
    elif res2<0:
        print(str(res1)+str(res2)+"i")
    else:
        print(res1)

mult((3,-1),(1,4))

##def div(t1,t2):
