# -*- coding: utf-8 -*- 
# 2007~2016 대기오염 vs 대기오염 합산 비교 그래프 (개발중..)
import numpy as np
import math  as mt
from matplotlib import pyplot as plt, font_manager, rc

from operator import eq
import csv
import sys

def analyzeProc():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    # 연도별 대기오염 평균 csv 파일 읽어오기
    # 연도, 이산화질소농도(ppm), 오존농도(ppm), 일산화탄소농도(ppm), 아황산가스(ppm), 미세먼지(㎍/㎥)
    yearArray = []
    polDataArray = [[0 for col in range(0)] for row in range(5)]
    polltutionDatafile = 'csv/Airpollution_tot.csv'
    with open(polltutionDatafile, 'rt') as f :
        rowData = csv.reader(f, delimiter = ',')
        for colIdx2, data in enumerate(rowData):
            for colIdx1, d in enumerate(data):
               if colIdx1 == 0 : 
                   yearArray.insert(colIdx2, d)
               else :
                   polDataArray[colIdx1-1].insert(colIdx2, float(d))
               
    # 정규화 처리
    # 공식 : (X - min(X') / (max(X') - min(X'))
    for idx, pol in enumerate(polDataArray):
        minVal = min(polDataArray[idx])
        maxVal = max(polDataArray[idx])
        for valIdx, val in enumerate(pol):
           rangeVal = (maxVal - minVal)
           polDataArray[idx][valIdx] = (polDataArray[idx][valIdx] - minVal) / rangeVal 

    # 오염 제목 리스트
    polName = ["이산화질소", "오존", "일산화탄소", "아황산가스", "미세먼지"]
       
    # 비교대상 오염정보 Index
    nPolIndex1 = 2
    nPolIndex2 = 4

    plt.plot(polDataArray[nPolIndex1], polDataArray[nPolIndex2], label=polName[nPolIndex1])
    #plt.scatter(yearArray, polDataArray[nPolIndex2], c='red', label=polName[nPolIndex2])
    #plt.xlabel('년월')
    #plt.ylabel('오염도')
    plt.legend()       
    
    # 그래프 노출
    plt.show()

if __name__== '__main__':
    analyzeProc()
