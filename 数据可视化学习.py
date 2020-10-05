################################################################################################折线图
# from matplotlib import pyplot as plt
# import random
# import matplotlib
# from matplotlib import font_manager
# 
# my_font = font_manager.FontProperties(fname = "C:/WINDOWS/FONTS/MSYH.TTC")
# 
# x =range( 0, 120 )
# y = [random.randint(20,35) for i in range(120)]
#
#设置图像大小
# plt.figure( figsize = (20,8), dpi = 80)
# plt.plot(x,y)
# 
# 
# _xtick_labels = [ "10点{}分".format(i) for i in range(60) ]
# _xtick_labels += [ "11点{}分".format(i) for i in range(60) ]
# plt.xticks(list(x)[::3],_xtick_labels[::3],rotation = 45,FontProperties = my_font)

#横纵坐标描述
# plt.xlabel("时间", FontProperties = my_font)
# plt.ylabel("温度 单位(℃)", FontProperties = my_font)
#标题
# plt.title("10点到12点每分钟的气温情况" , FontProperties = my_font)

# plt.show()
##################################################################################################

##################################################################################################散点图
# from matplotlib import pyplot as plt
# from matplotlib import font_manager
# 
# # 定义中文
# my_font = font_manager.FontProperties(fname = "C:/WINDOWS/FONTS/MSYH.TTC")
# 
# y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
# y2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
# # y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
# x = range(11,31)
# 
# # 设置图形大小
# plt.figure(figsize = (20,8),dpi=80)
# 
# plt.plot(x,y1,label = "自己", color = "cyan",linestyle=":",linewidth = 5)
# plt.plot(x,y2,label = "同桌", color = "orange",linestyle="--",linewidth = 5)
# 
# #设置x轴刻度
# _xtick_labels = ["{}岁".format(i) for i in x]
# plt.xticks(x,_xtick_labels,FontProperties = my_font)#设置中文  FontProperties = my_font
# 
# #设置网格
# plt.grid(range(0,9),alpha = 0.4,linestyle=":")

#添加图例
# plt.legend(prop = my_font,loc="upper left")#只在这里添加prop显示中文，其他地方都是FontProperties

# plt.show()
##################################################################################################

##################################################################################################散点图
# from matplotlib import pyplot as plt
# from matplotlib import font_manager
# my_font = font_manager.FontProperties(fname = "C:/WINDOWS/FONTS/MSYH.TTC")
# 
# y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,12,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
# y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
# 
# x_3 = range(1,32)
# x_10 = range(51,82)
# 
# # # 设置图形大小
# plt.figure(figsize = (20,8),dpi=80)
# plt.scatter(x_3,y_3,label = "3月份")
# plt.scatter(x_10,y_10,label = "10月份")
# 
# #调整x轴刻度
# _x = list(x_3) + list(x_10)
# _xtick_labels = ["3月{}日".format(i) for i in x_3]
# _xtick_labels += ["3月{}日".format(i-50) for i in x_10]
# plt.xticks(_x[::3],_xtick_labels[::3],rotation = 45,FontProperties = my_font)
# 
# #添加图例
# plt.legend(loc = "upper left",prop = my_font)
# 
# #添加描述信息
# plt.xlabel("时间", FontProperties = my_font)
# plt.ylabel("温度", FontProperties = my_font)
# plt.title("标题", FontProperties = my_font)
#  
# plt.show()
#####################################################################################################

#####################################################################################################绘制条形图
# from matplotlib import pyplot as plt
# from matplotlib import font_manager
# 
# my_font = font_manager.FontProperties(fname = "C:/WINDOWS/FONTS/MSYH.TTC")
# 
# a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚3:\n最后的骑士","摔跤吧！爸爸","加勒比海盗5:\n死无对证"]
# b = [56.01,26.94,17.53,16.49,15.25,12.96,11.8]
# 
# plt.figure(figsize = (20,8),dpi=80)
# 
# plt.bar(range(len(a)),b,width = 0.3)
# 
# plt.xticks(range(len(a)),a,FontProperties = my_font)
# 
# plt.show()
############################################横着的
# from matplotlib import pyplot as plt
# from matplotlib import font_manager
# 
# my_font = font_manager.FontProperties(fname = "C:/WINDOWS/FONTS/MSYH.TTC")
# 
# a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚3:\n最后的骑士","摔跤吧！爸爸","加勒比海盗5:\n死无对证"]
# b = [56.01,26.94,17.53,16.49,15.25,12.96,11.8]
# 
# plt.figure(figsize = (20,8),dpi=80)
# 
# #barh表示绘制竖着的条形图
# plt.barh(range(len(a)),b,height = 0.7)
# 
# plt.grid()
# 
# plt.yticks(range(len(a)),a,FontProperties = my_font)
# 
# plt.show()
#####################################################################################################

#####################################################################################################绘制多次条形图
# from matplotlib import pyplot as plt
# from matplotlib import font_manager
# 
# my_font = font_manager.FontProperties(fname = "C:/WINDOWS/FONTS/MSYH.TTC")
# 
# a = ["猩球崛起:终极之战","敦刻尔克","蜘蛛侠:英雄归来","战狼2"]
# b_16 = [15746,312,4997,319]
# b_15 = [12357,156,2045,168]
# b_14 = [2358,399,2358,263]
# 
# bar_width = 0.2
# x_14 = list(range(len(a)))
# x_15 = [i+bar_width for i in x_14]
# x_16 = [i+bar_width*2 for i in x_14]
# 
# plt.figure(figsize = (20,8),dpi=80)
# 
# #barh表示绘制竖着的条形图
# plt.bar(range(len(a)),b_14,width = bar_width,label = "9月14日")
# plt.bar(x_15,b_15,width = bar_width,label = "9月15日")
# plt.bar(x_16,b_16,width = bar_width,label = "9月16日")
# 
# plt.grid()
# 
# #设置x轴刻度
# plt.xticks(x_15,a,FontProperties = my_font)
# 
# plt.legend(prop = my_font)
# plt.show()
#####################################################################################################

#####################################################################################################绘制直方图
# from matplotlib import pyplot as plt
# from matplotlib import font_manager
# 
# my_font = font_manager.FontProperties(fname = "C:/WINDOWS/FONTS/MSYH.TTC")
# 
# a=[131,  98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 119, 128, 121, 142, 127, 130, 124, 101, 110, 116, 117, 110, 128, 128, 115,  99, 136, 126, 134,  95, 138, 117, 111,78, 132, 124, 113, 150, 110, 117,  86,  95, 144, 105, 126, 130,126, 130, 126, 116, 123, 106, 112, 138, 123,  86, 101,  99, 136,123, 117, 119, 105, 137, 123, 128, 125, 104, 109, 134, 125, 127,105, 120, 107, 129, 116, 108, 132, 103, 136, 118, 102, 120, 114,105, 115, 132, 145, 119, 121, 112, 139, 125, 138, 109, 132, 134,156, 106, 117, 127, 144, 139, 139, 119, 140,  83, 110, 102,123,107, 143, 115, 136, 118, 139, 123, 112, 118, 125, 109, 119, 133,112, 114, 122, 109, 106, 123, 116, 131, 127, 115, 118, 112, 135,115, 146, 137, 116, 103, 144,  83, 123, 111, 110, 111, 100, 154,136, 100, 118, 119, 133, 134, 106, 129, 126, 110, 111, 109, 141,120, 117, 106, 149, 122, 122, 110, 118, 127, 121, 114, 125, 126,114, 140, 103, 130, 141, 117, 106, 114, 121, 114, 133, 137,  92,121, 112, 146,  97, 137, 105,  98, 117, 112,  81,  97, 139, 113,134, 106, 144, 110, 137, 137, 111, 104, 117, 100, 111, 101, 110,105, 129, 137, 112, 120, 113, 133, 112,  83,  94, 146, 133, 101,131, 116, 111,  84, 137, 115, 122, 106, 144, 109, 123, 116, 111,111, 133, 150]
# 
# # 设置组距
# d = 3
# # 计算组数
# num_bins = (max(a)-min(a))//d
# 
# # 设置图形的大小
# plt.figure(figsize = (20,8),dpi=80)
# #绘制直方图
# plt.hist(a,num_bins, density = 1)#density表示显示频率
# 
# # 设置x轴刻度
# plt.xticks(range(min(a), max(a)+d,d))
# 
# plt.grid()
# 
# plt.show()
#####################################################################################################

#####################################################################################################以绘制条形图方法绘制直方图
# from matplotlib import pyplot as plt
# from matplotlib import font_manager
# 
# my_font = font_manager.FontProperties(fname = "C:/WINDOWS/FONTS/MSYH.TTC")
# 
# interval = [0,5,10,15,20,25,30,35,40,45,60,90]#时间段，绘制于x轴
# width = [5,5,5,5,5,5,5,5,5,15,30,60]#组距
# quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]#数据
# 
# 
# # 设置组距
# # d = [5,5,5,5,5,5,5,5,5,15,30,60]
# # # 计算组数
# # num_bins = (max(a)-min(a))//d
# 
# # 设置图形的大小
# plt.figure(figsize = (20,8),dpi=80)
# #绘制直方图
# plt.bar(range(len(quantity)), quantity,width = 1)
# 
# # 设置x轴刻度
# _x = [i - 0.5 for i in range(13)]
# _xtick_labels = interval + [150]
# plt.xticks( _x, _xtick_labels )
# 
# #添加网格
# plt.grid(alpha = 0.4)
# 
# plt.show()
#####################################################################################################

#######################################################################################################################################numpy
###########################################################################################功能测试
import numpy as np
import random

# t1 = np.array([1,2,3])#array可以添加元素
# print(t1)
# print(type(t1))
# 
# t2 = np.array(range(10))
# print(t2.dtype)#dtype可以输出数组内元素的类型
# 
# t3 = np.arange(4,10,3)
# print(t3)

# t4 = np.array([1,1,0,1,0,0],dtype = bool)#在定义时后面加dtype可以定义元素的类型
# print(t4)
# print(t4.dtype)
# 
# t6 = t4.astype("int8")#astype可以改变元素的类型
# print(t6)
# print(t6.dtype)
# 
# a1 = random.random()#生成小数
# print(a1)
# 
# #numpy中的小数
# t7 = np.array([random.random() for i in range(10)])#随机生成0到1之间10个小数
# print(t7)
# print(t7.dtype)
# 
# t8 = np.round(t7,2)#保留两位小数
# print(t8)
# 
# t9 = round(random.random(),3)#保留三位小数
# print(t9)
###########################################################################################
# import numpy as np
# 
# t1 = np.arange(12)#arange作用类似于range
# print(t1)
# print(t1.shape)
# 
# t2 = np.array([[1,2,3],[4,5,6]])
# print(t2)
# print(t2.shape)#shape可以输出数组的形状
# 
# t3 = t2.reshape((6,1))#reshape可以改变数组的形状,此处表示6行1列,不过需要用一个变量去接它
# print(t3)
# t4 = np.arange(24).reshape(2,3,4)#此处表示两块，三行，四列
# print(t4)
# t5 = t4.flatten()
# print(t4.flatten())#flatten可以将数组展开为一维数组
# print(t4)
# print(t5)
# 
# ###########数组运算
# print(t5+2)
# print(t5*2)
# print(t5/2)
#######################################################################################################################################