import matplotlib.pyplot as plt
import scipy
import numpy

def find_Xsr(v):
	Xsr = 0
	n = len(v)
	for i in range(n):
		Xsr += v[i]/n
	return Xsr

def find_Dispers(v, Xsr):
	S2 = 0
	n = len(v)
	for i in range(n):
		S2 += ((v[i] - Xsr)**2)/n
	return S2

def find_Median(v):
	n = len(v)
	sortedV = sorted(v)
	if n%2 == 0:
		return (sortedV[int(n/2)] + sortedV[int(n/2 + 1)])/2
	else:
		return sortedV[int(n/2 + 1)]

def find_ni(v):
	ni = []
	for i in range(len(v)):
		ni.append(1.0)
		for j in range(i):
			if v[j] == v[i]:
				ni[j] += 1.0
				ni[i] += 1.0
	# for i in range(len(ni)):
	# 	ni[i] = ni[i]/(len(v))
	return ni

def find_ni_int(v, vint):
	ni = []
	for i in range(1, len(vint)):
		ni.append(0)
		for j in range(len(v)):
			if vint[i-1] < v[j] <= vint[i]:
				ni[i-1] += 1
	return ni

def find_Moda(v, ni):
	Moi = 0
	for i in range(len(v)):
		if ni[i] > ni[Moi]:
			Moi = i
	return v[Moi]

def find_Ex(v, ni, Xsr, S):
	m4 = 0
	n = len(v)
	for i in range(n):
		m4 += ((v[i] - Xsr)**4.0)*ni[i]/n
	Ex = (m4/S**4.0) - 3.0

	# if Ex  0:
		# print("Ne norm. raspr.")
	# else:
		# print("Norm. raspr.")
	return Ex

def find_As(v, ni, Xsr, S):
	m3 = 0
	n = len(v)
	for i in range(n):
		m3 += ((v[i] - Xsr)**3.0)*ni[i]/n
	return m3/S**3

def Fn(x, v, ni):
	Sum = 0.0
	n = len(v)
	for i in range(n):
		if v[i] < x:
			Sum += float(ni[i])/float(n)
	return Sum

def empir(v):
	v = sorted(v)
	ni = find_ni(v)
	F = []
	for i in range(len(v)):
		F.append(Fn(v[i], v, ni))
	ax = plt.gca()
	ax.bar(v, F, align='edge')
	ax.set_xticks(v)
	plt.plot(v, F)
	plt.ylabel('ni')
	plt.xlabel('xi')
	plt.show()


