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
	subplot_s_1.plot(arr_alpha, arr_season_1, "g-.",label=u'第1季度')
	#<<<< subplot_s_4 = plt.subplot(2, 2, 4) 提前后，不能用 plt设置xylabel
	#plt.xlabel(u'仰角$\\alpha$($^{\circ}$)')
	#plt.ylabel(u'修正量$(m)$')
	subplot_s_1.set_xlabel(u'仰角$\\alpha$($^{\circ}$)')
	subplot_s_1.set_ylabel(u'修正量$(m)$')
	#subplot_s_2 = plt.subplot(2, 2, 2)
	#<<<< Error.  label=u'$第2季度$' 会有乱码
	subplot_s_2.plot(arr_alpha, arr_season_2, "r-*", label=u'第2季度')
	subplot_s_2.set_xlabel(u'仰角$\\alpha$($^{\circ}$)')
	subplot_s_2.set_ylabel(u'修正量$(m)$')
	#subplot_s_3 = plt.subplot(2, 2, 3)
	subplot_s_3.plot(arr_alpha, arr_season_3, "b-<", label=u'第3季度')
	subplot_s_3.set_xlabel(u'仰角$\\alpha$($^{\circ}$)')
	subplot_s_3.set_ylabel(u'修正量$(m)$')
	#subplot_s_4 = plt.subplot(2, 2, 4)
	subplot_s_4.plot(arr_alpha, arr_season_4, "y->", label=u'第4季度')
	subplot_s_4.set_xlabel(u'仰角$\\alpha$($^{\circ}$)')
	subplot_s_4.set_ylabel(u'修正量$(m)$')
	#subplot_s_1.set_title(u'第1季度修正量')
	#subplot_s_2.set_title(u'第2季度修正量')
	#subplot_s_3.set_title(u'第3季度修正量')
	#subplot_s_4.set_title(u'第4季度修正量')
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
	createPlt('XL', u'光斑半径与仰角关系')
	createPlt('NS', u'光斑半径与仰角关系')
	createPlt('LDH', u'光斑半径与仰角关系')
	createPlt('LJ', u'光斑半径与仰角关系')