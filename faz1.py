def left(mat):
    for j in range(n) :
        if mat[j][0]!=0 :
            for i in range(n-1) :
                if (mat[j][i]>2) and (mat[j][i]==mat[j][i+1]) :
                    mat[j][i]=mat[j][i]+mat[j][i+1]
                    mat[j][i+1]=0
                    break
                elif (mat[j][i]==1 and mat[j][i+1]==2) or (mat[j][i]==2 and mat[j][i+1]==1):
                    mat[j][i]=mat[j][i]+mat[j][i+1]
                    mat[j][i+1]=0
                    break
        for i in range(n-1) :
            if(mat[j][i]==0):
                (mat[j][i],mat[j][i+1])=(mat[j][i+1],mat[j][i])
    return mat 
#________________________________________________________________________________________________
def right(mat):
    for j in range(n):
        a=mat[j]
        a=a[::-1]
        for i in range(n-1):
            if a[0]!=0 :
                if (a[i]>2) and (a[i]==a[i+1]) : 
                    a[i]=a[i]+a[i+1]
                    a[i+1]=0
                    break
                elif (a[i]==1 and a[i+1]==2)or (a[i]==2 and a[i+1]==1):
                    a[i]=a[i]+a[i+1]
                    a[i+1]=0
                    break
        for i in range(n-1):
                if(a[i]==0) :
                    (a[i],a[i+1])=(a[i+1],a[i])
        mat[j]=a[::-1]
    return(mat)
#___________________________________________________________________________________________________         
def down(a) :
    for j in range(n) : 
        mat=[]
        for i in range(n):
            mat+=[a[i][j]]
        mat = mat[::-1]
        for i in range(n-1):
            if mat[0]!=0  : #plus
                if (mat[i]>2) and (mat[i]==mat[i+1]) :
                    mat[i]=mat[i]+mat[i+1]
                    mat[i+1]=0
                    break
                elif (mat[i]==1 and mat[i+1]==2)or (mat[i]==2 and mat[i+1]==1):
                    mat[i]=mat[i]+mat[i+1]
                    mat[i+1]=0
                    break
        for i in range(n-1):
                if(mat[i]==0):
                    (mat[i],mat[i+1])=(mat[i+1],mat[i])
        for i in range(n):
            a[i][j]=mat[::-1][i]
    return(a)
#_______________________________________________________________________________________________________
def up(a):
    for j in range(n):
        mat=[]
        for i in range(n):
            mat+=[a[i][j]]    
        for i in range(n-1) :
            if mat[0]!=0 : #plus
                if (mat[i]>2) and (mat[i]==mat[i+1]) :
                    mat[i]=mat[i]+mat[i+1]
                    mat[i+1]=0
                    break
                elif (mat[i]==1 and mat[i+1]==2) or (mat[i]==2 and mat[i+1]==1):
                    mat[i]=mat[i]+mat[i+1]
                    mat[i+1]=0
                    break
        for i in range(n-1):
            if (mat[i]==0) :
                (mat[i],mat[i+1])=(mat[i+1],mat[i])
        for i in range(n):
            a[i][j]=mat[i]
    return(a)
#____________________________________________________________________________________________________         
def L_random(mat) :
    list1 = []
    dic = {}
    m=0
    for i in range(n) :  #random num be soton akhar ezafe khahad shod
        if mat[i][n-1]==0:
            m += 1
            list1 += [i]
    if m!=0 :
        for j in range(m) :
            dic[j] = list1[j]
        if k%m<=m-1: #plus 
            mat[dic[k%m]][n-1] = d #plus
            return(mat)
    return mat #plus
#__________________________________________________________________________________________________
def R_random(mat): #random num be soton aval ezafe khahad shod
    list1 = []
    dic = {}
    m=0
    for i in range(n) :
        if mat[i][0]==0:
            m += 1
            list1 += [i]
    if m!=0 :
        for j in range(m) :
            dic[j] = list1[j]
        if k%m<=m-1 : #plus
            mat[dic[k%m]][0] = d #plus
            return(mat)
    return mat #plus
#____________________________________________________________________________________________________
def U_random(mat) :
    list1 = []
    dic = {}
    m=0
    for i in range(n) :
        if mat[n-1][i]==0:
            m += 1
            list1 += [i]
    if m!=0:
        for j in range(m) :
            dic[j] = list1[j]
        if k%m<=m-1:  #plus 
            mat[n-1][dic[k%m]] = d #plus
            return(mat)
    return (mat) #plus
#____________________________________________________________________________________________________
def D_random(mat) :
    list1 = []
    dic = {}
    m=0
    for i in range(n) :
        if mat[0][i]==0:
            m += 1
            list1 += [i]
    if m!=0 :
        for j in range(m) :
            dic[j] = list1[j]
        if k%m<=m-1 :  #plus
            mat[0][dic[k%m]] = d #plus
            return mat  
    return mat         #plus
#____________________________________________________________________________________________________
import copy
def final(mat) :
    if (mat==up(copy.deepcopy(mat))) and mat==down(copy.deepcopy(mat)) and mat==right(copy.deepcopy(mat)) and mat==left(copy.deepcopy(mat)) :
        return True
    return False
#_____________________________________________________________________________________________________
n=int(input()) #input1
mat1=[]        #safhe avalie bazii
for i in range(n) :
    inp1=input().split()
    for j in range(n) :
        inp1[j]=int(inp1[j])
    mat1+=[inp1]
s=input()
list2=list(s)
import copy
for i in range(len(list2)) :
    if mat1 !=down([i[:] for i in mat1]) and list2[i] =='D':
        A=input().split()
        k=int(A[0]) 
        d=int(A[1])
        mat1=down(mat1)
        mat1=D_random(mat1)               
    elif mat1 !=up([i[:] for i in mat1])and list2[i] =='U' :
        A=input().split()
        k=int(A[0]) 
        d=int(A[1])
        mat1=up(mat1)
        mat1=U_random(mat1)
    elif mat1 !=right([i[:] for i in mat1]) and list2[i] =='R' :
        A=input().split()
        k=int(A[0]) 
        d=int(A[1])
        mat1=right(mat1)
        mat1=R_random(mat1)
    elif mat1 != left([i[:] for i in mat1]) and list2[i] =='L' : 
        A=input().split()
        k=int(A[0]) 
        d=int(A[1])
        mat1=left(mat1)
        mat1=L_random(mat1)
for i in range(n) :
    for j in range(n) :
        print(mat1[i][j],end="\t")
    print()
list3=[]
for i in range(n):
    for j in range(n):
        if (mat1[i][j]!=0) and (mat1[i][j]!=1) and (mat1[i][j]!=2) :
            list3+=[mat1[i][j]]
point=0
for i in range(len(list3)):
    x=list3[i]//3
    K=0
    while x!=1 :
        K+=1
        x=x//2
    point+=3**(K+1)
    
if final(mat1) :
    print("The final score is "+str(point)+'.')
else:
    print("The partial score is "+str(point)+'.')
    