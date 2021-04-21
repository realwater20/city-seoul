# -*- coding: utf-8 -*- 
# 서울시 대기오염별 관계 그래프 (연속으로 노출하기)
import numpy as np
import math  as mt
from matplotlib import pyplot as plt, font_manager, rc

from operator import eq
import csv
import sys

def mean(x):
    return sum(x) / len(x)

def dot(v,w):
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def covariance(x,y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)

def analyzePollutionCompare():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    # 연도별 대기오염 평균 csv 파일 읽어오기
    # 연도, 이산화질소농도(ppm), 오존농도(ppm), 일산화탄소농도(ppm), 아황산가스(ppm), 미세먼지(㎍/㎥)
    bf_date = ''
    yearIdx = 0
    monthIdx = 0
    pollutionData = [[[0 for col in range(0)] for row in range(10)] for row in range(5)]
    
    polltutionDatafile = 'csv/Airpollution_tot.csv'
    with open(polltutionDatafile, 'rt') as f :
        rowData = csv.reader(f, delimiter = ',')
        for colIdx2, data in enumerate(rowData):
            for colIdx1, value in enumerate(data):
                if colIdx1 == 0 :
                    if eq(bf_date, '') == True :
                        bf_date = value[:4]
                    elif eq(bf_date, value[:4]) == False : # 연도별로 데이터 담기
                        bf_date = value[:4]
                        yearIdx += 1
                        monthIdx = 0
                    continue
                
                # [연도별][오염종류별][오염수치]
                pollutionData[colIdx1-1][yearIdx].insert(monthIdx, float(value))
                
            monthIdx += 1
                
    # 정규화 처리
    # 공식 : (X - min(X') / (max(X') - min(X'))
    for idx1, yearData in enumerate(pollutionData) :
        for idx2, polData in enumerate(yearData):
                minVal = min(polData)
                maxVal = max(polData)
                for idx3, val in enumerate(polData):
                   rangeVal = (maxVal - minVal)
                   pollutionData[idx1][idx2][idx3] = (pollutionData[idx1][idx2][idx3] - minVal) / rangeVal
    
    for pol1, pol2 in zip(pollutionData[2],pollutionData[3]):
        print pol2
    
       
    x = [ covariance(pol1, pol2) for pol1, pol2 in zip(pollutionData[0],pollutionData[3])]
    y = [ covariance(pol1, pol2) for pol1, pol2 in zip(pollutionData[3],pollutionData[0])]
    

    plt.scatter(x, y,alpha=0.5)

    # 그래프 노출
    plt.show()

if __name__== '__main__':
    analyzePollutionCompare()
