import matplotlib.pyplot as plt
import func.py

def poligon(v):
	v = sorted(v)
	vint = []
	vi = [15.5, 18, 34, 45, 52, 69, 74, 87, 89]
	vint = [15, 16, 20, 26, 42, 48, 56, 62, 82, 89]
	ni = find_ni_int(v, vint)
	plt.plot(vi, ni)
	# plt.label("poligon")
	plt.ylabel('ni')
	plt.xlabel('xi')
	plt.show()

def gistogramm(v):
	v.append(15)
	v = sorted(v)
	vint = [15, 16, 20, 27, 42, 49, 56, 62, 82, 89]
	ni = find_ni_int(v, vint)
	ni.append(0)
	plt.bar(vint, ni, width = 22, align = 'edge')
	plt.xticks(vint)
	plt.show() 
