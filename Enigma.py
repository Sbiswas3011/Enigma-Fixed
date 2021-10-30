# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:55:08 2020

@author: Snehangsu
"""
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from collections import Counter
from matplotlib import style
import numpy as np
import random
import copy

switch=0
style.use("ggplot")

colr1='white'
colr2='white'

#hardcoded 

'''rty1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

maindict={}
for i in range(len(rty1)):
    maindict[rty1[i]]=0

ref1=['h','q','u','t','v','m','r','a','l','s','z','i','f','y','x','w','b','g','j','d','c','e','p','o','n','k']
ref2=['f','q','i','k','y','a','s','n','c','r','d','w','u','h','x','z','b','j','g','v','m','t','l','o','e','p']
ref3=['c','r','a','h','q','n','i','d','g','m','l','k','j','f','p','o','e','b','w','v','z','t','s','y','x','u']

R1=['z', 'x', 'v', 'u', 'k', 'o', 'f', 'h', 'd', 'q', 'i', 't', 'm', 'l', 'w', 'e', 'n', 'p', 'y', 'b', 'g', 'r', 's', 'c', 'j', 'a']
R2=['d', 'i', 't', 'l', 's', 'e', 'r', 'y', 'x', 'w', 'h', 'g', 'z', 'q', 'v', 'c', 'n', 'j', 'u', 'a', 'm', 'p', 'o', 'f', 'b', 'k']
R3=['p', 'y', 'g', 'c', 'k', 'z', 'w', 'e', 'l', 'd', 'j', 'a', 'u', 'q', 'n', 'm', 'i', 't', 'b', 'h', 's', 'r', 'o', 'f', 'v', 'x']
R4=['i', 'c', 'g', 'z', 'e', 'm', 'j', 'n', 'v', 'b', 'd', 'o', 'a', 'w', 'p', 'h', 'y', 's', 'f', 'r', 'q', 'l', 'k', 'x', 'u', 't']
R5=['v', 't', 'g', 'q', 'i', 'u', 'r', 'b', 's', 'h', 'm', 'n', 'd', 'z', 'a', 'c', 'l', 'x', 'j', 'y', 'o', 'e', 'p', 'f', 'k', 'w']

R1O=['z', 'x', 'v', 'u', 'k', 'o', 'f', 'h', 'd', 'q', 'i', 't', 'm', 'l', 'w', 'e', 'n', 'p', 'y', 'b', 'g', 'r', 's', 'c', 'j', 'a']
R2O=['d', 'i', 't', 'l', 's', 'e', 'r', 'y', 'x', 'w', 'h', 'g', 'z', 'q', 'v', 'c', 'n', 'j', 'u', 'a', 'm', 'p', 'o', 'f', 'b', 'k']
R3O=['p', 'y', 'g', 'c', 'k', 'z', 'w', 'e', 'l', 'd', 'j', 'a', 'u', 'q', 'n', 'm', 'i', 't', 'b', 'h', 's', 'r', 'o', 'f', 'v', 'x']
R4O=['i', 'c', 'g', 'z', 'e', 'm', 'j', 'n', 'v', 'b', 'd', 'o', 'a', 'w', 'p', 'h', 'y', 's', 'f', 'r', 'q', 'l', 'k', 'x', 'u', 't']
R5O=['v', 't', 'g', 'q', 'i', 'u', 'r', 'b', 's', 'h', 'm', 'n', 'd', 'z', 'a', 'c', 'l', 'x', 'j', 'y', 'o', 'e', 'p', 'f', 'k', 'w']

R1_internal=[25,22,19,17,6,9,-1,0,-5,7,-2,8,0,-2,8,-11,-3,-2,6,-18,-14,-4,-4,-21,-15,-25]
R2_internal=[3,7,17,8,14,-1,11,17,15,13,-3,-5,13,3,7,-13,-3,-8,2,-19,-8,-6,-8,-18,-23,-15]
R3_internal=[15,23,4,-1,6,20,16,-3,3,-6,-1,-11,8,3,-1,-3,-8,2,-17,-12,-2,-4,-8,-18,-3,-2]
R4_internal=[8,1,4,22,0,7,3,6,13,-8,-7,3,-12,9,1,-8,8,1,-13,-2,-4,-10,-12,0,-4,-6]
R5_internal=[21,18,4,13,4,15,11,-6,10,-2,2,2,-9,12,-14,-13,-5,6,-9,5,-6,-17,-7,-18,-14,-3]

R1_internalO=[25,22,19,17,6,9,-1,0,-5,7,-2,8,0,-2,8,-11,-3,-2,6,-18,-14,-4,-4,-21,-15,-25]
R2_internalO=[3,7,17,8,14,-1,11,17,15,13,-3,-5,13,3,7,-13,-3,-8,2,-19,-8,-6,-8,-18,-23,-15]
R3_internalO=[15,23,4,-1,6,20,16,-3,3,-6,-1,-11,8,3,-1,-3,-8,2,-17,-12,-2,-4,-8,-18,-3,-2]
R4_internalO=[8,1,4,22,0,7,3,6,13,-8,-7,3,-12,9,1,-8,8,1,-13,-2,-4,-10,-12,0,-4,-6]
R5_internalO=[21,18,4,13,4,15,11,-6,10,-2,2,2,-9,12,-14,-13,-5,6,-9,5,-6,-17,-7,-18,-14,-3]


reflector=[ref1,ref2,ref3]
rotorI=[R1_internal,R2_internal,R3_internal,R4_internal,R5_internal]
rotorIO=[R1_internalO,R2_internalO,R3_internalO,R4_internalO,R5_internalO]
rotorE=[R1,R2,R3,R4,R5]
rotorEO=[R1O,R2O,R3O,R4O,R5O]'''


rty1=[]

maindict={}

ref1=[]
ref2=[]
ref3=[]

R1=[]
R2=[]
R3=[]
R4=[]
R5=[]

R1O=[]
R2O=[]
R3O=[]
R4O=[]
R5O=[]

R1_internal=[]
R2_internal=[]
R3_internal=[]
R4_internal=[]
R5_internal=[]

R1_internalO=[]
R2_internalO=[]
R3_internalO=[]
R4_internalO=[]
R5_internalO=[]


reflector=[]
rotorI=[]
rotorIO=[]
rotorE=[]
rotorEO=[]


def randomizer(button,num,turn):
    global switch
    switch=num
    
    global maindict
    
    global rty1
    global ref1
    global ref2
    global ref3
    global R1
    global R2
    global R3
    global R4
    global R5
    global R1O
    global R2O
    global R3O
    global R4O
    global R5O
    global R1_internal
    global R2_internal
    global R3_internal
    global R4_internal
    global R5_internal
    global R1_internalO
    global R2_internalO
    global R3_internalO
    global R4_internalO
    global R5_internalO
    
    global reflector
    global rotorI
    global rotorIO
    global rotorE
    global rotorEO
    
    global colr1
    global colr2
    
    if button['bg'] == 'green':
        button['bg'] = 'red'
    else:
        button['bg'] = 'green'
        button['activebackground'] = button['bg']
        print('Button pressed')
    
    if turn==0:
         
        rotordict=[]
        rty1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
              '1','2','3','4','5','6','7','8','9','0','/',' ','.','!','?','&','<','>',':',';']
        
        
        for i in range(len(rty1)):
            maindict[rty1[i]]=0
            
        #print(maindict)
        for j in range(8):
            dic={}
            keys=[]
            rty2=copy.deepcopy(rty1)
            for i in range(int(len(rty1)/2)):
                ele=rty2[0]
                rty2.pop(0)
                ele2=random.choice(rty2)
                dic[ele2]=ele
                rty2.remove(ele2)
            rty2=copy.deepcopy(rty1)   
            for key, value in dic.items():
                i1=rty2.index(key)
                i2=rty2.index(value)
                rty2[i1],rty2[i2]=rty2[i2],rty2[i1]
            rotordict.append(rty2)
        print(len(rotordict))
        
        index=[]
        for i in range(5):
            indexing=[]
            for j in range(len(rty1)):
                i1=rty1.index(rotordict[i+3][j])-j
                indexing.append(i1)
            index.append(indexing)
            
        ref1=copy.deepcopy(rotordict[0])
        ref2=copy.deepcopy(rotordict[1])
        ref3=copy.deepcopy(rotordict[2])
        
        R1=copy.deepcopy(rotordict[3])
        R1O=copy.deepcopy(rotordict[3])
        R2=copy.deepcopy(rotordict[4])
        R2O=copy.deepcopy(rotordict[4])
        R3=copy.deepcopy(rotordict[5])
        R3O=copy.deepcopy(rotordict[5])
        R4=copy.deepcopy(rotordict[6])
        R4O=copy.deepcopy(rotordict[6])
        R5=copy.deepcopy(rotordict[7])
        R5O=copy.deepcopy(rotordict[7])
        
        R1_internal=copy.deepcopy(index[0])
        R2_internal=copy.deepcopy(index[1])
        R3_internal=copy.deepcopy(index[2])
        R4_internal=copy.deepcopy(index[3])
        R5_internal=copy.deepcopy(index[4])
        
        R1_internalO=copy.deepcopy(index[0])
        R2_internalO=copy.deepcopy(index[1])
        R3_internalO=copy.deepcopy(index[2])
        R4_internalO=copy.deepcopy(index[3])
        R5_internalO=copy.deepcopy(index[4])
        
        reflector=[ref1,ref2,ref3]
        rotorI=[R1_internal,R2_internal,R3_internal,R4_internal,R5_internal]
        rotorIO=[R1_internalO,R2_internalO,R3_internalO,R4_internalO,R5_internalO]
        rotorE=[R1,R2,R3,R4,R5]
        rotorEO=[R1O,R2O,R3O,R4O,R5O]
        
        colr1='white'
        colr2='green'
    else:
        
        rty1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        
        for i in range(len(rty1)):
            maindict[rty1[i]]=0
        
        ref1=['h','q','u','t','v','m','r','a','l','s','z','i','f','y','x','w','b','g','j','d','c','e','p','o','n','k']
        ref2=['f','q','i','k','y','a','s','n','c','r','d','w','u','h','x','z','b','j','g','v','m','t','l','o','e','p']
        ref3=['c','r','a','h','q','n','i','d','g','m','l','k','j','f','p','o','e','b','w','v','z','t','s','y','x','u']
        
        R1=['z', 'x', 'v', 'u', 'k', 'o', 'f', 'h', 'd', 'q', 'i', 't', 'm', 'l', 'w', 'e', 'n', 'p', 'y', 'b', 'g', 'r', 's', 'c', 'j', 'a']
        R2=['d', 'i', 't', 'l', 's', 'e', 'r', 'y', 'x', 'w', 'h', 'g', 'z', 'q', 'v', 'c', 'n', 'j', 'u', 'a', 'm', 'p', 'o', 'f', 'b', 'k']
        R3=['p', 'y', 'g', 'c', 'k', 'z', 'w', 'e', 'l', 'd', 'j', 'a', 'u', 'q', 'n', 'm', 'i', 't', 'b', 'h', 's', 'r', 'o', 'f', 'v', 'x']
        R4=['i', 'c', 'g', 'z', 'e', 'm', 'j', 'n', 'v', 'b', 'd', 'o', 'a', 'w', 'p', 'h', 'y', 's', 'f', 'r', 'q', 'l', 'k', 'x', 'u', 't']
        R5=['v', 't', 'g', 'q', 'i', 'u', 'r', 'b', 's', 'h', 'm', 'n', 'd', 'z', 'a', 'c', 'l', 'x', 'j', 'y', 'o', 'e', 'p', 'f', 'k', 'w']
        
        R1O=['z', 'x', 'v', 'u', 'k', 'o', 'f', 'h', 'd', 'q', 'i', 't', 'm', 'l', 'w', 'e', 'n', 'p', 'y', 'b', 'g', 'r', 's', 'c', 'j', 'a']
        R2O=['d', 'i', 't', 'l', 's', 'e', 'r', 'y', 'x', 'w', 'h', 'g', 'z', 'q', 'v', 'c', 'n', 'j', 'u', 'a', 'm', 'p', 'o', 'f', 'b', 'k']
        R3O=['p', 'y', 'g', 'c', 'k', 'z', 'w', 'e', 'l', 'd', 'j', 'a', 'u', 'q', 'n', 'm', 'i', 't', 'b', 'h', 's', 'r', 'o', 'f', 'v', 'x']
        R4O=['i', 'c', 'g', 'z', 'e', 'm', 'j', 'n', 'v', 'b', 'd', 'o', 'a', 'w', 'p', 'h', 'y', 's', 'f', 'r', 'q', 'l', 'k', 'x', 'u', 't']
        R5O=['v', 't', 'g', 'q', 'i', 'u', 'r', 'b', 's', 'h', 'm', 'n', 'd', 'z', 'a', 'c', 'l', 'x', 'j', 'y', 'o', 'e', 'p', 'f', 'k', 'w']
        
        R1_internal=[25,22,19,17,6,9,-1,0,-5,7,-2,8,0,-2,8,-11,-3,-2,6,-18,-14,-4,-4,-21,-15,-25]
        R2_internal=[3,7,17,8,14,-1,11,17,15,13,-3,-5,13,3,7,-13,-3,-8,2,-19,-8,-6,-8,-18,-23,-15]
        R3_internal=[15,23,4,-1,6,20,16,-3,3,-6,-1,-11,8,3,-1,-3,-8,2,-17,-12,-2,-4,-8,-18,-3,-2]
        R4_internal=[8,1,4,22,0,7,3,6,13,-8,-7,3,-12,9,1,-8,8,1,-13,-2,-4,-10,-12,0,-4,-6]
        R5_internal=[21,18,4,13,4,15,11,-6,10,-2,2,2,-9,12,-14,-13,-5,6,-9,5,-6,-17,-7,-18,-14,-3]
        
        R1_internalO=[25,22,19,17,6,9,-1,0,-5,7,-2,8,0,-2,8,-11,-3,-2,6,-18,-14,-4,-4,-21,-15,-25]
        R2_internalO=[3,7,17,8,14,-1,11,17,15,13,-3,-5,13,3,7,-13,-3,-8,2,-19,-8,-6,-8,-18,-23,-15]
        R3_internalO=[15,23,4,-1,6,20,16,-3,3,-6,-1,-11,8,3,-1,-3,-8,2,-17,-12,-2,-4,-8,-18,-3,-2]
        R4_internalO=[8,1,4,22,0,7,3,6,13,-8,-7,3,-12,9,1,-8,8,1,-13,-2,-4,-10,-12,0,-4,-6]
        R5_internalO=[21,18,4,13,4,15,11,-6,10,-2,2,2,-9,12,-14,-13,-5,6,-9,5,-6,-17,-7,-18,-14,-3]
        
        
        reflector=[ref1,ref2,ref3]
        rotorI=[R1_internal,R2_internal,R3_internal,R4_internal,R5_internal]
        rotorIO=[R1_internalO,R2_internalO,R3_internalO,R4_internalO,R5_internalO]
        rotorE=[R1,R2,R3,R4,R5]
        rotorEO=[R1O,R2O,R3O,R4O,R5O]
        
        colr1='green'
        colr2='white'
        
 
    print(colr1,colr2)   
'''reflector=[rotordict[0],rotordict[1],rotordict[2]]
rotorI=[index[0],index[1],index[2],index[3],index[4]]
rotorE=[rotordict[3],rotordict[4],rotordict[5],rotordict[6],rotordict[7]]'''
    
#in progress above



def shift(n,ar):
    temp=[]
    
    n=int(n)
    for i in range(0,n-1):
        temp.append(ar[i])
    del ar[0:n-1]
    ar=ar+temp
    return ar
    
def RR(m,lists): 
    output_list = [] 
      
    n=len(lists)
    for j in range(0,m):
        output_list.append(lists[n-1])
    
        for i in range(0,n-1):
            output_list.append(lists[i])
          
    return output_list 


root = Tk()
root.title("Enigma Simulator")
#root.geometry("900x350")
root.resizable(width=False, height=False)

win=Toplevel(root)
win.geometry("1000x500")
win.title("Encrypted letter Frequency")

fig = Figure(figsize=(10, 10), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=win)  # A tk.DrawingArea.
canvas.get_tk_widget().pack()
toolbar = NavigationToolbar2Tk(canvas, win)

def plot(num=0):
    fig.clear()
    plot1=fig.add_subplot(111)
    st=e2.get()
    res = Counter(st)
    ndic = dict(list(maindict.items()) + list(res.items()))
    
    if num==1:
        ndic.pop(' ')

    plot1.bar(color='red',*zip(*ndic.items()))
    canvas.draw_idle()
    

def reset(O1n=0,O2n=0,O3n=0,refn=0,IR1=0,IR2=0,IR3=0,ER1=0,ER2=0,ER3=0,ed=False): 
    
    global FL_list
    global ref
    global O1
    global O2
    global O3
    global rotorI
    global rotorE
    rotorI[O1-1]=copy.deepcopy(rotorIO[O1-1])
    rotorI[O2-1]=copy.deepcopy(rotorIO[O2-1])
    rotorI[O3-1]=copy.deepcopy(rotorIO[O3-1])
    
    rotorE[O1-1]=copy.deepcopy(rotorEO[O1-1])
    rotorE[O2-1]=copy.deepcopy(rotorEO[O2-1])
    rotorE[O3-1]=copy.deepcopy(rotorEO[O3-1])
    
    
    if (ed==False):
        e2.delete(0,'end')
        e4.delete(0,'end')
        e4.insert(0,0)
        e.delete(0,'end')
        FL_list.clear()
        
    ref=refn
    O1=O1n
    O2=O2n
    O3=O3n

    var1=IntVar(root)
    var1.set(IR1)
    var2=IntVar(root)
    var2.set(IR2)
    var3=IntVar(root)
    var3.set(IR3)
    var4=IntVar(root)
    var4.set(ER1)
    var5=IntVar(root)
    var5.set(ER2)
    var6=IntVar(root)
    var6.set(ER3)
    InternalR1.config(textvariable=var1)
    InternalR2.config(textvariable=var2)
    InternalR3.config(textvariable=var3)
    ExternalR1.config(textvariable=var4)
    ExternalR2.config(textvariable=var5)
    ExternalR3.config(textvariable=var6)
    
    print(O1,O2,O3,ref,FL_list)

#start of setup parameters

var1=IntVar(root)
var1.set(0)
var2=IntVar(root)
var2.set(0)
var3=IntVar(root)
var3.set(0)
var4=IntVar(root)
var4.set(0)
var5=IntVar(root)
var5.set(0)
var6=IntVar(root)
var6.set(0)
 
rotor_cnt=0 
O1=0
O2=0
O3=0  
ref=0
FL_list=[]
cnt_flip=0
def rotor_input(i,switch): 
    
    global rotor_cnt,O1,O2,O3,ref
    if rotor_cnt==3:
        rotor_cnt=0
    print(rotor_cnt)
    if(switch==0):
        if rotor_cnt==0:
            O1=int(i)
        elif rotor_cnt==1:
            O2=int(i)
        elif rotor_cnt==2:
            O3=int(i)  
        rotor_cnt+=1
    elif(switch==1):
        ref=int(i)
    elif(switch==2):
        cnt_flip=0
        FL=e3.get()
        if FL[0] and FL[1] in rty1:
            if e4.get()==str(int(len(rty1)/2)):
                s=str(int(len(rty1)/2)) + " is MAX"
                e3.delete(0,END)
                e4.delete(0,END)
                e4.insert(0,s)
            else:
                FL=e3.get()
                if not any(FL[0] in x for x in FL_list) and not any(FL[1] in x for x in FL_list):
                    FL_list.append([FL[0],FL[1]])
                    cnt_flip+=1
                else:
                    e3.delete(0,END)
                    #e4.delete(0,END)
                    #e4.insert(0,"Pair cable in use")
                    
            if(cnt_flip>0):
                i=int(e4.get())+1
                e4.delete(0,END)
                e3.delete(0,END)
                e4.insert(0,i)
        else:
            e3.delete(0,END)
            
           
    print(O1,O2,O3,ref,FL_list)
        
print(O1,O2,O3,ref,FL_list)

#end of setup parameters and start of button initialization

l1=Label(root,text="Encrypt/Decrypt").grid(row=0,column=0,columnspan=1,padx=5,pady=5)
l2=Label(root,text="Output").grid(row=1,column=0,columnspan=1,padx=5,pady=5)

e = Entry(root,width=100,borderwidth=4)
e.grid(row=0,column=1,columnspan=5,padx=5,pady=5)
e2 = Entry(root,width=100,borderwidth=4)
e2.grid(row=1,column=1,columnspan=5,padx=5,pady=5)

I_button=Button(root,text="I",padx=50,pady=20,command=lambda: rotor_input(1,0)).grid(row=2,column=1)
II_button=Button(root,text="II",padx=50,pady=20,command=lambda: rotor_input(2,0)).grid(row=2,column=2)
III_button=Button(root,text="III",padx=50,pady=20,command=lambda: rotor_input(3,0)).grid(row=2,column=3)
IV_button=Button(root,text="IV",padx=50,pady=20,command=lambda: rotor_input(4,0)).grid(row=2,column=4)
V_button=Button(root,text="V",padx=50,pady=20,command=lambda: rotor_input(5,0)).grid(row=2,column=5)

InternalR1=IntVar()
InternalR2=IntVar()
InternalR3=IntVar()
ExternalR1=IntVar()
ExternalR2=IntVar()
ExternalR3=IntVar()

InternalR1 = Spinbox(root, from_=0, to=int(len(rty1)),font=("helvetica",10),textvariable=var1)
InternalR1.grid(row=3,column=1)
InternalR2 = Spinbox(root, from_=0, to=int(len(rty1)),font=("helvetica",10),textvariable=var2)
InternalR2.grid(row=3,column=3)
InternalR3 = Spinbox(root, from_=0, to=int(len(rty1)),font=("helvetica",10),textvariable=var3)
InternalR3.grid(row=3,column=5)

ExternalR1 = Spinbox(root, from_=0, to=int(len(rty1)),font=("helvetica",10),textvariable=var4)
ExternalR1.grid(row=4,column=1)
ExternalR2 = Spinbox(root, from_=0, to=int(len(rty1)),font=("helvetica",10),textvariable=var5)
ExternalR2.grid(row=4,column=3)
ExternalR3 = Spinbox(root, from_=0, to=int(len(rty1)),font=("helvetica",10),textvariable=var6)
ExternalR3.grid(row=4,column=5)

I2_button=Button(root,text="I",padx=50,pady=20,command=lambda: rotor_input(1,1)).grid(row=5,column=1)
II2_button=Button(root,text="II",padx=50,pady=20,command=lambda: rotor_input(2,1)).grid(row=5,column=3)
III2_button=Button(root,text="III",padx=50,pady=20,command=lambda: rotor_input(3,1)).grid(row=5,column=5)

e3 = Entry(root,width=60,borderwidth=4)
e3.grid(row=6,column=1,columnspan=3,padx=5,pady=5)

e4 = Entry(root,width=20,borderwidth=4)
e4.grid(row=6,column=5,columnspan=1,padx=5,pady=5)
e4.insert(0,0)
        
enter_button=Button(root,text="ENTER",padx=50,pady=10,command=lambda: rotor_input(0,2)).grid(row=6,column=4)

#end of button initialization

win2=Toplevel(root)
win2.geometry("1000x500")
win2.title("UnEncrypted letter Frequency")

fig2 = Figure(figsize=(10, 10), dpi=100)
canvas2 = FigureCanvasTkAgg(fig2, master=win2)  # A tk.DrawingArea.
canvas2.get_tk_widget().pack()
toolbar = NavigationToolbar2Tk(canvas2, win2)


def plot2(num=0):
    fig2.clear()
    plot1=fig2.add_subplot(111)
    st=e.get()
    res = Counter(st)
    ndic = dict(list(maindict.items()) + list(res.items()))
    if num==1:
        ndic.pop(" ")
    
    plot1.bar(color='blue',*zip(*ndic.items()))
    canvas2.draw_idle()
    
    
def crypt(O1,O2,O3,rotorI,rotorE,ref,reflector,FL_list,encrypt):
        
    e2.delete(0,END)
    
    print(rty1)
    
    
    IR1=int(InternalR1.get())+1
    IR2=int(InternalR2.get())+1
    IR3=int(InternalR3.get())+1
    ER1=int(ExternalR1.get())+1
    ER2=int(ExternalR2.get())+1
    ER3=int(ExternalR3.get())+1
    
    rotorI[O1-1]=shift(IR1,rotorI[O1-1]) 
    rotorI[O2-1]=shift(IR2,rotorI[O2-1])
    rotorI[O3-1]=shift(IR3,rotorI[O3-1]) 
    

            
    for i in range((len(rty1))):
        if(i+rotorI[O1-1][i]>(len(rty1)-1)):       
            rotorE[O1-1][i]=rty1[(i+rotorI[O1-1][i])-(len(rty1))]
        elif(i+rotorI[O1-1][i]<0):
            rotorE[O1-1][i]=rty1[(len(rty1))+(i+rotorI[O1-1][i])]
        else:
            rotorE[O1-1][i]=rty1[i+rotorI[O1-1][i]]
            
            
    for i in range((len(rty1))):
        if(i+rotorI[O2-1][i]>(len(rty1)-1)):       
            rotorE[O2-1][i]=rty1[(i+rotorI[O2-1][i])-(len(rty1))]
        elif(i+rotorI[O2-1][i]<0):
            rotorE[O2-1][i]=rty1[(len(rty1))+(i+rotorI[O2-1][i])]
        else:
            rotorE[O2-1][i]=rty1[i+rotorI[O2-1][i]]
            
    for i in range((len(rty1))):
        if(i+rotorI[O3-1][i]>(len(rty1)-1)):       
            rotorE[O3-1][i]=rty1[(i+rotorI[O3-1][i])-(len(rty1))]
        elif(i+rotorI[O3-1][i]<0):
            rotorE[O3-1][i]=rty1[(len(rty1))+(i+rotorI[O3-1][i])]
        else:
            rotorE[O3-1][i]=rty1[i+rotorI[O3-1][i]]
        

    rotorE[O1-1]=shift(ER1,rotorE[O1-1]) 
    rotorE[O2-1]=shift(ER2,rotorE[O2-1])
    rotorE[O3-1]=shift(ER3,rotorE[O3-1]) 
    

    st=str(e.get())
    
    storage=[]
    
    if encrypt:
        r1_cnt=0
        r2_cnt=0
        r3_cnt=0
        #st
        for i in range(0,len(st)):
            if(st[i]==" "):
                e2.insert(i," ")
                storage.append(" ")
                continue
            else:
                cnt=0
                s1=rotorE[O1-1][rty1.index(st[i])]#step 1
                s2=rotorE[O2-1][rty1.index(s1)]#step 2
                s3=rotorE[O3-1][rty1.index(s2)]#step 3
                s4=reflector[ref-1][rty1.index(s3)]#step 4
                s5=rty1[rotorE[O3-1].index(s4)]#step 5
                s6=rty1[rotorE[O2-1].index(s5)]#step 6
                s7=rty1[rotorE[O1-1].index(s6)]#step 7
                for left, right in FL_list:
                    if(s7==left):
                        s7=right
                        cnt+=1
                        #print(s7,end='')
                        e2.insert(i,s7)
                        storage.append(s7)
                    elif(s7==right):
                        s7=left
                        cnt+=1
                        #print(s7,end='')
                        e2.insert(i,s7)
                        storage.append(s7)
                if(cnt==0):
                    #print(s7,end='')
                    e2.insert(i,s7)
                    storage.append(s7)
                rotorE[O1-1]=RR(1,(rotorE[O1-1]))
                r1_cnt+=1
                if(r1_cnt>len(rty1)-1):
                    rotorE[O2-1]=RR(1,(rotorE[O2-1]))
                    r2_cnt+=1
                    r1_cnt=0
                if(r2_cnt>len(rty1)-1):
                    rotorE[O3-1]=RR(1,(rotorE[O3-1]))
                    r3_cnt+=1
                    r2_cnt=0
                    
    else:
        st=list(st)
        r1_cnt=0
        r2_cnt=0
        r3_cnt=0
        for i in range(0,len(st)):
            if(st[i]==" "):
                #print(" ",end='')
                e2.insert(i," ")
                storage.append(" ")
                continue
            else:
                cnt=0
                for left, right in FL_list:
                    if(st[i]==left):
                        st[i]=right
                        cnt+=1                   
                    elif(st[i]==right):
                        st[i]=left
                        cnt+=1                              
                s1=rotorE[O1-1][rty1.index(st[i])]#step 1
                s2=rotorE[O2-1][rty1.index(s1)]#step 2
                s3=rotorE[O3-1][rty1.index(s2)]#step 3
                s4=reflector[ref-1][rty1.index(s3)]#step 4
                s5=rty1[rotorE[O3-1].index(s4)]#step 5
                s6=rty1[rotorE[O2-1].index(s5)]#step 6
                s7=rty1[rotorE[O1-1].index(s6)]#step 7
                #print(s7,end='')
                e2.insert(i,s7)
                storage.append(s7)
                rotorE[O1-1]=RR(1,(rotorE[O1-1]))
                r1_cnt+=1
                if(r1_cnt>len(rty1)-1):
                    rotorE[O2-1]=RR(1,(rotorE[O2-1]))
                    r2_cnt+=1
                    r1_cnt=0
                if(r2_cnt>len(rty1)-1):
                    rotorE[O3-1]=RR(1,(rotorE[O3-1]))
                    r3_cnt+=1
                    r2_cnt=0
        
                
    storage=' '.join(map(str, storage))
    print(storage)
    
   
    reset(O1,O2,O3,ref,IR1-1,IR2-1,IR3-1,ER1-1,ER2-1,ER3-1,ed=True)
    plot(1)
    plot2(1)
    
def random_crypt(O1,O2,O3,rotorI,rotorE,ref,reflector,FL_list,encrypt):
        
    e2.delete(0,END)
    
    print(rty1)
    
    
    IR1=int(InternalR1.get())+1
    IR2=int(InternalR2.get())+1
    IR3=int(InternalR3.get())+1
    ER1=int(ExternalR1.get())+1
    ER2=int(ExternalR2.get())+1
    ER3=int(ExternalR3.get())+1
    
    rotorI[O1-1]=shift(IR1,rotorI[O1-1]) 
    rotorI[O2-1]=shift(IR2,rotorI[O2-1])
    rotorI[O3-1]=shift(IR3,rotorI[O3-1]) 
    

            
    for i in range((len(rty1))):
        if(i+rotorI[O1-1][i]>(len(rty1)-1)):       
            rotorE[O1-1][i]=rty1[(i+rotorI[O1-1][i])-(len(rty1))]
        elif(i+rotorI[O1-1][i]<0):
            rotorE[O1-1][i]=rty1[(len(rty1))+(i+rotorI[O1-1][i])]
        else:
            rotorE[O1-1][i]=rty1[i+rotorI[O1-1][i]]
            
            
    for i in range((len(rty1))):
        if(i+rotorI[O2-1][i]>(len(rty1)-1)):       
            rotorE[O2-1][i]=rty1[(i+rotorI[O2-1][i])-(len(rty1))]
        elif(i+rotorI[O2-1][i]<0):
            rotorE[O2-1][i]=rty1[(len(rty1))+(i+rotorI[O2-1][i])]
        else:
            rotorE[O2-1][i]=rty1[i+rotorI[O2-1][i]]
            
    for i in range((len(rty1))):
        if(i+rotorI[O3-1][i]>(len(rty1)-1)):       
            rotorE[O3-1][i]=rty1[(i+rotorI[O3-1][i])-(len(rty1))]
        elif(i+rotorI[O3-1][i]<0):
            rotorE[O3-1][i]=rty1[(len(rty1))+(i+rotorI[O3-1][i])]
        else:
            rotorE[O3-1][i]=rty1[i+rotorI[O3-1][i]]
        

    rotorE[O1-1]=shift(ER1,rotorE[O1-1]) 
    rotorE[O2-1]=shift(ER2,rotorE[O2-1])
    rotorE[O3-1]=shift(ER3,rotorE[O3-1]) 
    

    st=str(e.get())
    
    storage=[]
    
    if encrypt:
        r1_cnt=0
        r2_cnt=0
        r3_cnt=0
        #st
        for i in range(0,len(st)):
            cnt=0
            s1=rotorE[O1-1][rty1.index(st[i])]#step 1
            s2=rotorE[O2-1][rty1.index(s1)]#step 2
            s3=rotorE[O3-1][rty1.index(s2)]#step 3
            s4=reflector[ref-1][rty1.index(s3)]#step 4
            s5=rty1[rotorE[O3-1].index(s4)]#step 5
            s6=rty1[rotorE[O2-1].index(s5)]#step 6
            s7=rty1[rotorE[O1-1].index(s6)]#step 7
            for left, right in FL_list:
                if(s7==left):
                    s7=right
                    cnt+=1
                    #print(s7,end='')
                    e2.insert(i,s7)
                    storage.append(s7)
                elif(s7==right):
                    s7=left
                    cnt+=1
                    #print(s7,end='')
                    e2.insert(i,s7)
                    storage.append(s7)
            if(cnt==0):
                #print(s7,end='')
                e2.insert(i,s7)
                storage.append(s7)
            rotorE[O1-1]=RR(1,(rotorE[O1-1]))
            r1_cnt+=1
            if(r1_cnt>len(rty1)-1):
                rotorE[O2-1]=RR(1,(rotorE[O2-1]))
                r2_cnt+=1
                r1_cnt=0
            if(r2_cnt>len(rty1)-1):
                rotorE[O3-1]=RR(1,(rotorE[O3-1]))
                r3_cnt+=1
                r2_cnt=0
            
                
                    
    else:
        st=list(st)
        r1_cnt=0
        r2_cnt=0
        r3_cnt=0
        for i in range(0,len(st)):
            
            cnt=0
            for left, right in FL_list:
                if(st[i]==left):
                    st[i]=right
                    cnt+=1                   
                elif(st[i]==right):
                    st[i]=left
                    cnt+=1                              
            s1=rotorE[O1-1][rty1.index(st[i])]#step 1
            s2=rotorE[O2-1][rty1.index(s1)]#step 2
            s3=rotorE[O3-1][rty1.index(s2)]#step 3
            s4=reflector[ref-1][rty1.index(s3)]#step 4
            s5=rty1[rotorE[O3-1].index(s4)]#step 5
            s6=rty1[rotorE[O2-1].index(s5)]#step 6
            s7=rty1[rotorE[O1-1].index(s6)]#step 7
            #print(s7,end='')
            e2.insert(i,s7)
            storage.append(s7)
            rotorE[O1-1]=RR(1,(rotorE[O1-1]))
            r1_cnt+=1
            if(r1_cnt>len(rty1)-1):
                rotorE[O2-1]=RR(1,(rotorE[O2-1]))
                r2_cnt+=1
                r1_cnt=0
            if(r2_cnt>len(rty1)-1):
                rotorE[O3-1]=RR(1,(rotorE[O3-1]))
                r3_cnt+=1
                r2_cnt=0
        
                
    storage=' '.join(map(str, storage))
    print(storage)
    
   
    reset(O1,O2,O3,ref,IR1-1,IR2-1,IR3-1,ER1-1,ER2-1,ER3-1,ed=True)
    plot()
    plot2()
    
    
def cryptswitch(O1,O2,O3,rotorI,rotorE,ref,reflector,FL_list,encrypt,switch):
    if switch==0:
        crypt(O1,O2,O3,rotorI,rotorE,ref,reflector,FL_list,encrypt)
    else:
        random_crypt(O1,O2,O3,rotorI,rotorE,ref,reflector,FL_list,encrypt)
        
    
   

reset_button=Button(root,text="RESET",padx=40,pady=20,command=reset).grid(row=7,column=1)

encrypt_button=Button(root,text="ENCRYPT",padx=40,pady=20,command=lambda: cryptswitch(O1,O2,O3,rotorI,rotorE,ref,reflector,FL_list,True,switch)).grid(row=7,column=3)
decrypt_button=Button(root,text="DECRYPT",padx=40,pady=20,command=lambda: cryptswitch(O1,O2,O3,rotorI,rotorE,ref,reflector,FL_list,False,switch)).grid(row=7,column=5)
Preset_button=Button(root,text="PRESET",padx=40,pady=20,command=lambda: randomizer(Preset_button,0,1)).grid(row=8,column=2)
Randomizer_button=Button(root,text="RANDOM",padx=40,pady=20,command=lambda: randomizer(Randomizer_button,1,0)).grid(row=8,column=4)

#encrypt_button=Button(root,text="ENCRYPT",padx=40,pady=20,command=lambda: crypt(O1,O2,O3,rotorI,rotorE,ref,reflector,FL_list,True)).grid(row=7,column=3)
#decrypt_button=Button(root,text="DECRYPT",padx=40,pady=20,command=lambda: crypt(O1,O2,O3,rotorI,rotorE,ref,reflector,FL_list,False)).grid(row=7,column=5)

root.mainloop()


