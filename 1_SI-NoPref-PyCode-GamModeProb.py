mode_num = 0

import sympy as sp 
import itertools
a1,a2,b1,b2,a3,a4,b3,b2,b4,c1,c2,c3,c4 = sp.symbols('a1,a2,b1,b2,a3,a4,b3,b2,b4,c1,c2,c3,c4')    
r= sp.symbols('r')
q=sp.symbols('q')
v=sp.symbols('v')
vp=sp.symbols('vp')
rp=sp.symbols('rp')
qp=sp.symbols('qp')
t=sp.symbols('t')
(ppc)=sp.symbols('(ppc)')
(pdm)=sp.symbols('(pdm)')
(pmp)=sp.symbols('(pmp)')

import copy
from sympy import *
from itertools import permutations 
from itertools import chain
from itertools import product

#SWAPS OUTTER SET -C
def swap_r1(z, i, j, x, y=2):
    tmp=copy.deepcopy(z)
    tmp[i][x][y], tmp[j][x][y] =  tmp[j][x][y], tmp[i][x][y]
    return tmp

#SWAPS MIDDLE SET-B
def swap_r2(z, i,j,x,y=1):
    tmp=copy.deepcopy(z)
    tmp[i][x][y:], tmp[j][x][y:] =  tmp[j][x][y:], tmp[i][x][y:]
    return tmp

#SWAPS INNER SET-A
def swap_r3(z, i,j,x):
    tmp=copy.deepcopy(z)
    tmp[i][x], tmp[j][x] =  tmp[j][x], tmp[i][x]
    return tmp
    
def biv_D(arrng):
    events_D_list=[[]]
    dg_D=[arrng]
    
    r_events = [[],[r,0,2,0],[r,0,2,1],[q,0,2,0],[q,0,2,1],[v,0,2,0],[v,0,2,1], \
         [r,1,3,0],[r,1,3,1],[q,1,3,0],[q,1,3,1],[v,1,3,0],[v,1,3,1]]
    
    for event in [1,2,3,4,5,6,7,8,9,10,11,12]:
        tmp_events_D_list0=copy.deepcopy(events_D_list)
        tmp_events_D_list1=copy.deepcopy(events_D_list)
        
        for recomb in [0,1]:
            if (recomb == 0):
                p = (1 - r_events[event][0])
                
                dg_0=dg_D 
                for i in tmp_events_D_list0:
                    i.append(p)
                    
            else:
                p = r_events[event][0]
                
                for i in range(len(dg_D)):
                    tmp = dg_D[i]
                    
                    if r_events[event][0] == r:
                        dg = swap_r1(tmp, r_events[event][1], r_events[event][2],r_events[event][3])
                        dg_D.append(dg)
                    elif r_events[event][0] == q:
                        dg = swap_r2(tmp, r_events[event][1], r_events[event][2],r_events[event][3])
                        dg_D.append(dg)
                    elif r_events[event][0] == v:
                        dg = swap_r3(tmp, r_events[event][1], r_events[event][2],r_events[event][3])
                        dg_D.append(dg)    
                for i in tmp_events_D_list1:
                    i.append(p)
                    
        events_D_list=[]
        for i in tmp_events_D_list0:
            events_D_list.append(i)
        for i in tmp_events_D_list1:
            events_D_list.append(i)

    product_D_list=[]
    for i in events_D_list:
        SUM = 1
        for j in i:
            SUM *= j
        product_D_list.append([SUM])
    product_D_list=[[item * ((1-t) + t*(1-pmp-ppc-pdm))/3 for item in subl][0] for subl in product_D_list]
    
    return dg_D, product_D_list
    
def quad_A_D(arrng):
    
    events_A_list = [[]]
    dg_A =[arrng]
    
    r_events = [[],[r,0,2,0],[r,0,2,1],[q,0,2,0],[q,0,2,1],[vp,0,2,0],\
        [vp,0,2,1],[r,1,3,0],[r,1,3,1],[q,1,3,0],[q,1,3,1],\
        [vp,1,3,0],[vp,1,3,1],[vp,0,1,0],[vp,0,1,1],[vp,2,3,0],\
        [vp,2,3,1]]
    
    for event in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
        tmp_events_A_list0=copy.deepcopy(events_A_list)
        tmp_events_A_list1=copy.deepcopy(events_A_list)
        
        for recomb in [0,1]:
            if (recomb == 0):
                p = (1 - r_events[event][0])

                dg_0 = dg_A
                for i in tmp_events_A_list0:
                    i.append(p)
            else:
                p = r_events[event][0]
                    
                for i in range(len(dg_A)):
                    tmp=dg_A[i]
                    
                    if r_events[event][0] == r:
                        dg = swap_r1(tmp, r_events[event][1], r_events[event][2],r_events[event][3])
                        dg_A.append(dg)
                    elif r_events[event][0] == q:
                        dg = swap_r2(tmp, r_events[event][1], r_events[event][2],r_events[event][3])
                        dg_A.append(dg)
                    elif r_events[event][0] == v or r_events[event][0] == vp:
                        dg = swap_r3(tmp, r_events[event][1], r_events[event][2],r_events[event][3])
                        dg_A.append(dg)
                        
                for i in tmp_events_A_list1:
                    i.append(p)
                    
        events_A_list=[]
        for i in tmp_events_A_list0:
            events_A_list.append(i)
        for i in tmp_events_A_list1:
            events_A_list.append(i)

    product_A_list=[]
    for i in events_A_list:
        SUM = 1
        for j in i:
            SUM *= j
        product_A_list.append([SUM])
    product_A_list1=[[item *(t)*(ppc)/24 for item in subl][0] for subl in product_A_list]

    return dg_A,  product_A_list1
    
def quad_B_D(arrng):
    events_b_list = [[]]
    dg_B = [arrng]
    
    r_events = [[],[rp,0,2,0],[rp,0,2,1],[rp,1,3,0],[rp,1,3,1],\
        [rp,0,1,0],[rp,0,1,1],[q,0,1,0],[q,0,1,1],\
        [v,0,1,0],[v,0,1,1],[rp,2,3,0],[rp,2,3,1],\
        [q,2,3,0],[q,2,3,1],[v,2,3,0],[v,2,3,1]]
    
    for event in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
        tmp_events_b_list_0=copy.deepcopy(events_b_list)
        tmp_events_b_list_1=copy.deepcopy(events_b_list)
        
        for recomb in [0,1]:
            if (recomb == 0):
                p = (1 - r_events[event][0])
                    
                dg_0 = dg_B
                for i in tmp_events_b_list_0:
                    i.append(p)
            else:
                p = r_events[event][0]
                    
                for i in range(len(dg_B)):
                    tmp=dg_B[i]
                    
                    if r_events[event][0] == r or r_events[event][0] == rp:
                        dg = swap_r1(tmp, r_events[event][1], r_events[event][2],r_events[event][3])
                        dg_B.append(dg)
                    elif r_events[event][0] == q:
                        dg = swap_r2(tmp, r_events[event][1], r_events[event][2],r_events[event][3])
                        dg_B.append(dg)
                    elif r_events[event][0] == v:
                        dg = swap_r3(tmp, r_events[event][1], r_events[event][2],r_events[event][3])
                        dg_B.append(dg)
                    
                for i in tmp_events_b_list_1:
                    i.append(p)
                    
        events_b_list=[]
        for i in tmp_events_b_list_0:
            events_b_list.append(i)
        for i in tmp_events_b_list_1:
            events_b_list.append(i)
    
    product_b_list=[]
    for i in events_b_list:
        SUM = 1
        for j in i:
            SUM *= j
        product_b_list.append([SUM])
    product_b_list1=[[item *(t)*(pdm)/24 for item in subl][0] for subl in product_b_list]
    
    return dg_B, product_b_list1
    
def quad_C_D(arrng):
    events_c_list = [[]]
    dg_C =[arrng]
    
    r_events = [[],[r,0,2,0],[r,0,2,1],[qp,0,2,0],[qp,0,2,1],\
        [r,1,3,0],[r,1,3,1],[qp,1,3,0],[qp,1,3,1],\
        [qp,0,1,0],[qp,0,1,1],[v,0,1,0],[v,0,1,1],\
        [qp,2,3,0],[qp,2,3,1],[v,2,3,0],[v,2,3,1]]
    
    for event in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
        tmp_events_c_list_0=copy.deepcopy(events_c_list)
        tmp_events_c_list_1=copy.deepcopy(events_c_list)
        for recomb in [0,1]:
            if (recomb == 0):
                p = (1 - r_events[event][0])
                
                dg_0 = dg_C
                for i in tmp_events_c_list_0:
                    i.append(p)
            else:
                p = r_events[event][0]
                    
                for i in range(len(dg_C)):
                    tmp=dg_C[i]
                    
                    if r_events[event][0] == r:
                        dg = swap_r1(tmp, r_events[event][1], r_events[event][2],r_events[event][3])
                        dg_C.append(dg)
                    elif r_events[event][0] == q or r_events[event][0] == qp:
                        dg = swap_r2(tmp, r_events[event][1], r_events[event][2],r_events[event][3])
                        dg_C.append(dg)
                    elif r_events[event][0] == v:
                        dg = swap_r3(tmp, r_events[event][1], r_events[event][2],r_events[event][3])
                        dg_C.append(dg)  
                    
                for i in tmp_events_c_list_1:
                    i.append(p)
                    
        events_c_list=[]
        for i in tmp_events_c_list_0:
            events_c_list.append(i)
        for i in tmp_events_c_list_1:
            events_c_list.append(i)
    
    product_c_list=[]
    for i in events_c_list:
        SUM = 1
        for j in i:
            SUM *= j
        product_c_list.append([SUM])
    product_c_list1=[[item *(t)*(pmp)/24 for item in subl][0] for subl in product_c_list]
    
    return dg_C, product_c_list1
    
def ana(r_list,is_biv):
    
    if is_biv == 0:
        ana_events = [[0,0,2,0],[0,1,2,1],[0,0,2,1],[0,1,2,0],[1,0,3,0],\
            [1,1,3,1],[1,0,3,1],[1,1,3,0],[0,0,3,0],[0,1,3,1],\
            [0,0,3,1],[0,1,3,0],[1,0,2,0],[1,1,2,1],[1,0,2,1],\
            [1,1,2,0]]
    else:
        ana_events = [[0,0,1,0],[0,1,1,1],[0,0,1,1],[0,1,1,0],[2,0,3,0],\
            [2,1,3,1],[2,0,3,1],[2,1,3,0],[0,0,3,0],[0,1,3,1],\
            [0,0,3,1],[0,1,3,0],[2,0,1,0],[2,1,1,1],[2,0,1,1],\
            [2,1,1,0]]
    
    pair = [[] for event in range(len(ana_events))]
    
    for event in range(len(ana_events)):
        for i in range(len(r_list)):
            pair[event].append([copy.deepcopy(r_list[i][ana_events[event][0]][ana_events[event][1]]),\
                                                copy.deepcopy(r_list[i][ana_events[event][2]][ana_events[event][3]])])
    
    total_gamete_list = [copy.deepcopy(pair[event][gamete]) for event in range(len(ana_events)) for gamete in range(len(pair[event]))]
    
    return total_gamete_list

def total_list(lists):
    prob=[[item / 16 for item in [subl]] for subl in lists]
    prod=list(map(sum, prob))
    total_prob=prod+prod+prod+prod+prod+prod+prod+prod+prod+prod+prod+prod+prod+prod+prod+prod
    return total_prob
    
a, b, c = sp.symbols('a, b, c', cls=Function)

def subQ(x):
    
    if x == a(1):
        return a1
    if x == b(1):
        return b1
    if x == c(1):
        return c1
    if x == c(2):
        return c2
    if x == c(3):
        return c3
    if x == c(4):
        return c4
    if x == a(2):
        return a2
    if x == b(2):
        return b2
    if x == a(3):
        return a3
    if x == b(3):
        return b3
    if x == a(4):
        return a4
    if x == b(4):
        return b4
        
def get_mode_gametes(mode):
    
    mode_set = list({modes[mode][hap][locus] for hap in [0,1] for locus in [0,1,2]})
    mode_set.sort()

    M = []
    
    if len(mode_set) == 1:
        for i in range(1,5):
            M.append([[subQ(a(i)), subQ(b(i)), subQ(c(i))], [subQ(a(i)), subQ(b(i)), subQ(c(i))]])
    elif len(mode_set) == 2:
        for i in range(1,5):
            for j in range(1,5):
                exec("%s = %d" % (mode_set[0],i))
                exec("%s = %d" % (mode_set[1],j))
                if i!=j:
                     M.append([[subQ(a(eval(modes[mode][0][0]))), 
                            subQ(b(eval(modes[mode][0][1]))), 
                            subQ(c(eval(modes[mode][0][2])))], 
                           [subQ(a(eval(modes[mode][1][0]))), 
                            subQ(b(eval(modes[mode][1][1]))), 
                            subQ(c(eval(modes[mode][1][2])))]])
        
        for i in range(len(M)):
            rd=[M[i][1], M[i][0]]
            M.append(rd) 
        
        tmp_u = []
        for item in M: 
            if item not in tmp_u: 
                tmp_u.append(item)
                
        M = tmp_u
        
    elif len(mode_set) == 3:
        for i in range(1,5):
            for j in range(1,5):
                for k in range(1,5):
                    exec("%s = %d" % (mode_set[0],i))
                    exec("%s = %d" % (mode_set[1],j))
                    exec("%s = %d" % (mode_set[2],k))
                    if i!=j:
                        if j!=k:
                            if i!=k:
                                M.append([[subQ(a(eval(modes[mode][0][0]))), 
                                    subQ(b(eval(modes[mode][0][1]))), 
                                    subQ(c(eval(modes[mode][0][2])))], 
                                   [subQ(a(eval(modes[mode][1][0]))), 
                                    subQ(b(eval(modes[mode][1][1]))), 
                                    subQ(c(eval(modes[mode][1][2])))]])
                                
        for i in range(len(M)):
            rd=[M[i][1], M[i][0]]
            M.append(rd) 
        
        tmp_u = []
        for item in M: 
            if item not in tmp_u: 
                tmp_u.append(item)
                
        M = tmp_u
        
    elif len(mode_set) == 4:
        for i in range(1, 5):
            for j in range (1,5):
                for k in range(1, 5):
                    for l in range(1,5):
                        exec("%s = %d" % (mode_set[0],i))
                        exec("%s = %d" % (mode_set[1],j))
                        exec("%s = %d" % (mode_set[2],k))
                        exec("%s = %d" % (mode_set[3],l))
                        if i!=j:
                            if j!=k:
                                if i!=k:
                                    if i!=l:
                                        if j!=l:
                                            if k!=l:
                                                M.append([[subQ(a(eval(modes[mode][0][0]))), 
                                                    subQ(b(eval(modes[mode][0][1]))), 
                                                    subQ(c(eval(modes[mode][0][2])))], 
                                                   [subQ(a(eval(modes[mode][1][0]))), 
                                                    subQ(b(eval(modes[mode][1][1]))), 
                                                    subQ(c(eval(modes[mode][1][2])))]])
                                                
        for i in range(len(M)):
            rd=[M[i][1], M[i][0]]
            M.append(rd) 
        
        tmp_u = []
        for item in M: 
            if item not in tmp_u: 
                tmp_u.append(item)
                
        M = tmp_u
        
    return M
    
def gam_mode(gametes, gamete_probabilities, mode_list):
    gametes_in_mode = []
    prob_modes = []
    for i in range(len(gametes)):
        if gametes[i] in mode_list:
            gametes_in_mode.append(gametes[i])
            prob_modes.append(gamete_probabilities[i])
    return sum(prob_modes), len(gametes_in_mode)
    
def mode_prob(x, y, z, perm, mode_number):
    
    M = get_mode_gametes(mode_number)
    
    if x==0:
        
        D=biv_D(perm[z])
        A=ana(D[0],1)
        T=total_list(D[1])
        G=gam_mode(A, T, M)
        return G
                           
    else:
        if y==0:
            
            A=quad_A_D(perm[z])
            AA=ana(A[0],0)
            T=total_list(A[1])
            G=gam_mode(AA, T, M)
            return G
        
        if y==1:
            
            B=quad_B_D(perm[z])
            A=ana(B[0],0)
            T=total_list(B[1])
            G=gam_mode(A, T, M)
            return G
        
        if y==2:
            
            C=quad_C_D(perm[z])
            A=ana(C[0],0)
            T=total_list(C[1])
            G=gam_mode(A, T, M)
            return G
            
modes = [[['i_m','i_m','i_m'],['i_m','i_m','i_m']],[['i_m','j_m','i_m'],['i_m','j_m','i_m']],\
[['i_m','i_m','i_m'],['i_m','j_m','i_m']],[['i_m','j_m','i_m'],['i_m','k_m','i_m']],\
[['i_m','i_m','j_m'],['i_m','i_m','j_m']],[['i_m','j_m','j_m'],['i_m','j_m','j_m']],\
[['i_m','k_m','j_m'],['i_m','k_m','j_m']],[['i_m','i_m','j_m'],['i_m','j_m','j_m']],\
[['i_m','i_m','j_m'],['i_m','k_m','j_m']],[['i_m','j_m','j_m'],['i_m','k_m','j_m']],\
[['i_m','k_m','j_m'],['i_m','l_m','j_m']],[['i_m','i_m','i_m'],['i_m','i_m','j_m']],\
[['i_m','j_m','i_m'],['i_m','j_m','j_m']],[['i_m','k_m','i_m'],['i_m','k_m','j_m']],\
[['i_m','i_m','i_m'],['i_m','j_m','j_m']],[['i_m','j_m','i_m'],['i_m','i_m','j_m']],\
[['i_m','i_m','i_m'],['i_m','k_m','j_m']],[['i_m','k_m','i_m'],['i_m','i_m','j_m']],\
[['i_m','j_m','i_m'],['i_m','k_m','j_m']],[['i_m','k_m','i_m'],['i_m','j_m','j_m']],\
[['i_m','k_m','i_m'],['i_m','l_m','j_m']],[['i_m','i_m','j_m'],['i_m','i_m','k_m']],\
[['i_m','j_m','j_m'],['i_m','j_m','k_m']],[['i_m','l_m','j_m'],['i_m','l_m','k_m']],\
[['i_m','i_m','j_m'],['i_m','j_m','k_m']],[['i_m','j_m','j_m'],['i_m','i_m','k_m']],\
[['i_m','i_m','j_m'],['i_m','l_m','k_m']],[['i_m','j_m','j_m'],['i_m','k_m','k_m']],\
[['i_m','k_m','j_m'],['i_m','j_m','k_m']],[['i_m','k_m','j_m'],['i_m','l_m','k_m']],\
[['i_m','l_m','j_m'],['i_m','k_m','k_m']],[['i_m','i_m','i_m'],['j_m','i_m','i_m']],\
[['i_m','j_m','i_m'],['j_m','j_m','i_m']],[['i_m','k_m','i_m'],['j_m','k_m','i_m']],\
[['i_m','i_m','i_m'],['j_m','j_m','i_m']],[['i_m','j_m','i_m'],['j_m','i_m','i_m']],\
[['i_m','i_m','i_m'],['j_m','k_m','i_m']],[['i_m','k_m','i_m'],['j_m','i_m','i_m']],\
[['i_m','j_m','i_m'],['j_m','k_m','i_m']],[['i_m','k_m','i_m'],['j_m','j_m','i_m']],\
[['i_m','k_m','i_m'],['j_m','l_m','i_m']],[['j_m','i_m','i_m'],['k_m','i_m','i_m']],\
[['j_m','j_m','i_m'],['k_m','j_m','i_m']],[['j_m','l_m','i_m'],['k_m','l_m','i_m']],\
[['j_m','i_m','i_m'],['k_m','j_m','i_m']],[['j_m','j_m','i_m'],['k_m','i_m','i_m']],\
[['j_m','i_m','i_m'],['k_m','l_m','i_m']],[['j_m','j_m','i_m'],['k_m','k_m','i_m']],\
[['j_m','k_m','i_m'],['k_m','j_m','i_m']],[['j_m','j_m','i_m'],['k_m','l_m','i_m']],\
[['j_m','l_m','i_m'],['k_m','j_m','i_m']],[['i_m','i_m','i_m'],['j_m','i_m','j_m']],\
[['i_m','i_m','j_m'],['j_m','i_m','i_m']],[['i_m','k_m','i_m'],['j_m','k_m','j_m']],\
[['i_m','k_m','j_m'],['j_m','k_m','i_m']],[['i_m','i_m','i_m'],['j_m','j_m','j_m']],\
[['i_m','j_m','i_m'],['j_m','i_m','j_m']],[['i_m','i_m','j_m'],['j_m','j_m','i_m']],\
[['i_m','j_m','j_m'],['j_m','i_m','i_m']],[['i_m','i_m','i_m'],['j_m','k_m','j_m']],\
[['i_m','k_m','i_m'],['j_m','i_m','j_m']],[['i_m','i_m','j_m'],['j_m','k_m','i_m']],\
[['i_m','k_m','j_m'],['j_m','i_m','i_m']],[['i_m','k_m','i_m'],['j_m','l_m','j_m']],\
[['i_m','l_m','j_m'],['j_m','k_m','i_m']],[['i_m','i_m','i_m'],['j_m','i_m','k_m']],\
[['i_m','i_m','k_m'],['j_m','i_m','i_m']],[['i_m','j_m','i_m'],['j_m','j_m','k_m']],\
[['i_m','j_m','k_m'],['j_m','j_m','i_m']],[['i_m','k_m','i_m'],['j_m','k_m','k_m']],\
[['i_m','k_m','k_m'],['j_m','k_m','i_m']],[['i_m','l_m','i_m'],['j_m','l_m','k_m']],\
[['i_m','l_m','k_m'],['j_m','l_m','i_m']],[['i_m','i_m','i_m'],['j_m','j_m','k_m']],\
[['i_m','j_m','i_m'],['j_m','i_m','k_m']],[['i_m','i_m','k_m'],['j_m','j_m','i_m']],\
[['i_m','j_m','k_m'],['j_m','i_m','i_m']],[['i_m','i_m','i_m'],['j_m','k_m','k_m']],\
[['i_m','k_m','i_m'],['j_m','i_m','k_m']],[['i_m','i_m','k_m'],['j_m','k_m','i_m']],\
[['i_m','k_m','k_m'],['j_m','i_m','i_m']],[['i_m','i_m','i_m'],['j_m','l_m','k_m']],\
[['i_m','l_m','i_m'],['j_m','i_m','k_m']],[['i_m','i_m','k_m'],['j_m','l_m','i_m']],\
[['i_m','l_m','k_m'],['j_m','i_m','i_m']],[['i_m','j_m','i_m'],['j_m','k_m','k_m']],\
[['i_m','k_m','i_m'],['j_m','j_m','k_m']],[['i_m','j_m','k_m'],['j_m','k_m','i_m']],\
[['i_m','k_m','k_m'],['j_m','j_m','i_m']],[['i_m','j_m','i_m'],['j_m','l_m','k_m']],\
[['i_m','l_m','i_m'],['j_m','j_m','k_m']],[['i_m','j_m','k_m'],['j_m','l_m','i_m']],\
[['i_m','l_m','k_m'],['j_m','j_m','i_m']],[['i_m','k_m','i_m'],['j_m','l_m','k_m']],\
[['i_m','l_m','i_m'],['j_m','k_m','k_m']],[['i_m','k_m','k_m'],['j_m','l_m','i_m']],\
[['i_m','l_m','k_m'],['j_m','k_m','i_m']],[['i_m','i_m','k_m'],['j_m','i_m','l_m']],\
[['i_m','k_m','k_m'],['j_m','k_m','l_m']],[['i_m','i_m','k_m'],['j_m','j_m','l_m']],\
[['i_m','j_m','k_m'],['j_m','i_m','l_m']],[['i_m','i_m','k_m'],['j_m','k_m','l_m']],\
[['i_m','k_m','k_m'],['j_m','i_m','l_m']],[['i_m','i_m','l_m'],['j_m','k_m','k_m']],\
[['i_m','k_m','l_m'],['j_m','i_m','k_m']],[['i_m','k_m','k_m'],['j_m','l_m','l_m']],\
[['i_m','l_m','k_m'],['j_m','k_m','l_m']]]

B_base=[[[a1,b1,c1], [a1,b1,c1]],[[a2,b2,c2], [a2,b2,c2]], [[a3,b3,c3], [a3,b3,c3]],[[a4,b4,c4], [a4,b4,c4]]]

perm_D = [list(p) for p in itertools.permutations(B_base)]

from joblib import Parallel, delayed, parallel_backend
import multiprocessing

num_cores = 16

with parallel_backend('multiprocessing'):
    res_0 = Parallel(n_jobs=num_cores)(delayed(mode_prob)(0, 0, i, perm_D, mode_num) \
                                                               for i in range(3))
                                                               
with parallel_backend('multiprocessing'):
    res_1_0 = Parallel(n_jobs=num_cores)(delayed(mode_prob)(1, 0, i, perm_D, mode_num) \
                                                                     for i in range(24))
                                                                     
with parallel_backend('multiprocessing'):
    res_1_1 = Parallel(n_jobs=num_cores)(delayed(mode_prob)(1, 1, i, perm_D, mode_num) \
                                                                 for i in range(24))
                                                                 
with parallel_backend('multiprocessing'):
    res_1_2 = Parallel(n_jobs=num_cores)(delayed(mode_prob)(1, 2, i, perm_D, mode_num) \
                                                                 for i in range(24))
                                                                 
import pickle

with open("res_0.out", 'wb') as outf:
    pickle.dump(res_0, outf)

with open("res_1_0.out", 'wb') as outf:
    pickle.dump(res_1_0, outf)
    
with open("res_1_1.out", 'wb') as outf:
    pickle.dump(res_1_1, outf)
    
with open("res_1_2.out", 'wb') as outf:
    pickle.dump(res_1_2, outf)
    
