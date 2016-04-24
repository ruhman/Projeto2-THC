import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def funcdif(taxaAbs, bioDisp, dose, vd, kel, t):
	dcdt = ((taxaAbs*bioDisp*dose*math.e**(-taxaAbs*t))/vd) - (kel * concentracao)
	return dcdt

#parametros
peso = 70
vdtaxa= 3.4
vd = vdtaxa * peso
volumeSangue = 0.04*peso
bioDisp = 0.2
dose = 20
kp = 0.5
clearence = 14.9
kel = clearence/vd
taxaAbs = 0.18
concentracao = dose/volumeSangue
#estoques
estoquePulmao = []
estoqueCentral=[]
#série temporal
tempo = np.arange(0, 8760, 0.001) 
qtde = 0
t=0
#entrada=0
central=0
while t<= 8760:
	if t%24==0:
		entrada = 0.7*dose
		central = central +(entrada * kp)

	f = int(odeint(funcdif, central, t, args=(taxaAbs,bioDisp,dose,vd,kel)))
	central = central - f
	print (central)
	t+=1


