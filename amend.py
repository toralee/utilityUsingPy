import matplotlib.pyplot as plt
import numpy as np
from pylab import * 

def createPlt(area, station):
	arr_alpha = []
	arr_season_1 = []
	arr_season_2 = []
	arr_season_3 = []
	arr_season_4 = []
	file = open("D:\\workspace\\30.proj\\hu\\recv\\amend" + area + ".txt", "r")
	file.readline()
	lineList=file.readlines()
	file.close()
	matrix_data = [line.strip().split('\t') for line in lineList]
	arr_alpha = [float(i[0]) for i in matrix_data]
	arr_season_1 = [float(i[1]) for i in matrix_data]
	arr_season_2 = [float(i[2]) for i in matrix_data]
	arr_season_3 = [float(i[3]) for i in matrix_data]
	arr_season_4 = [float(i[4]) for i in matrix_data]
	subplot_s_1 = plt.subplot(2, 2, 1)
	subplot_s_2 = plt.subplot(2, 2, 2)
	subplot_s_3 = plt.subplot(2, 2, 3)
	subplot_s_4 = plt.subplot(2, 2, 4)
	subplot_s_1.plot(arr_alpha, arr_season_1, "g-.",label=u'��1����')
	#<<<< subplot_s_4 = plt.subplot(2, 2, 4) ��ǰ�󣬲����� plt����xylabel
	#plt.xlabel(u'����$\\alpha$($^{\circ}$)')
	#plt.ylabel(u'������$(m)$')
	subplot_s_1.set_xlabel(u'����$\\alpha$($^{\circ}$)')
	subplot_s_1.set_ylabel(u'������$(m)$')
	#subplot_s_2 = plt.subplot(2, 2, 2)
	#<<<< Error.  label=u'$��2����$' ��������
	subplot_s_2.plot(arr_alpha, arr_season_2, "r-*", label=u'��2����')
	subplot_s_2.set_xlabel(u'����$\\alpha$($^{\circ}$)')
	subplot_s_2.set_ylabel(u'������$(m)$')
	#subplot_s_3 = plt.subplot(2, 2, 3)
	subplot_s_3.plot(arr_alpha, arr_season_3, "b-<", label=u'��3����')
	subplot_s_3.set_xlabel(u'����$\\alpha$($^{\circ}$)')
	subplot_s_3.set_ylabel(u'������$(m)$')
	#subplot_s_4 = plt.subplot(2, 2, 4)
	subplot_s_4.plot(arr_alpha, arr_season_4, "y->", label=u'��4����')
	subplot_s_4.set_xlabel(u'����$\\alpha$($^{\circ}$)')
	subplot_s_4.set_ylabel(u'������$(m)$')
	#subplot_s_1.set_title(u'��1����������')
	#subplot_s_2.set_title(u'��2����������')
	#subplot_s_3.set_title(u'��3����������')
	#subplot_s_4.set_title(u'��4����������')
	#plt.legend()	#<<<<Error.
	subplot_s_1.legend()
	subplot_s_2.legend()
	subplot_s_3.legend()
	subplot_s_4.legend()
	plt.savefig("D:\\workspace\\30.proj\\hu\\recv\\radius"+area+".png")
	plt.show()

if __name__ == "__main__":
	mpl.rcParams['font.sans-serif'] = ['SimHei']
	mpl.rcParams['axes.unicode_minus'] = False
	createPlt('XL', u'��߰뾶�����ǹ�ϵ')
	createPlt('NS', u'��߰뾶�����ǹ�ϵ')
	createPlt('LDH', u'��߰뾶�����ǹ�ϵ')
	createPlt('LJ', u'��߰뾶�����ǹ�ϵ')