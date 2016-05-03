'''
Created on 2016年5月2日

@author: huangshuai
'''
import math
n,m,a = input().split(" ")
width = math.ceil(float(n)/float(a))
height = math.ceil(float(m)/float(a))
print(width * height)