# -*- coding: utf-8 -*- 
# 서울시 대기오염별 관계 그래프 (연속으로 노출하기)
import numpy as np
import math  as mt
from matplotlib import pyplot as plt, font_manager, rc

from operator import eq
import csv
import sys

def analyzePollutionCompare():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    # 2016년 대기오염 평균 csv 파일 읽어오기
    # 연도, 이산화질소농도(ppm), 오존농도(ppm), 일산화탄소농도(ppm), 아황산가스(ppm), 미세먼지(㎍/㎥), 초미세먼지(㎍/㎥)
    pollutionData = [[0 for col in range(0)] for row in range(6)]
    polltutionDatafile = 'csv/SeoulAirpollution.csv'
    with open(polltutionDatafile, 'rt') as f :
        rowData = csv.reader(f, delimiter = ',')
        for colIdx2, data in enumerate(rowData):
            for colIdx1, d in enumerate(data):
               if colIdx1 == 0 : continue
               
               pollutionData[colIdx1-1].insert(colIdx2, float(d))
               
    # 정규화 처리
    # 공식 : (X - min(X') / (max(X') - min(X'))
    for idx, pol in enumerate(pollutionData):
        minVal = min(pollutionData[idx])
        maxVal = max(pollutionData[idx])
        for valIdx, val in enumerate(pol):
           rangeVal = (maxVal - minVal)
           pollutionData[idx][valIdx] = (pollutionData[idx][valIdx] - minVal) / rangeVal 

    # 오염 제목 리스트
    polName = ["이산화질소", "오존", "일산화탄소", "아황산가스", "미세먼지", "초미세먼지"]
       
    # X축 월별 배열 정보 선언
    month = ['1','2','3','4','5','6','7','8','9','10','11','12']

    # 비교대상 오염정보 Index
    nPolIndex = 0
    
    # 2016년 대기오염 정보 plot 설정
    f, axarr = plt.subplots(2, 3)

    # 비교대상 오염정보와 타 오염정보를 비교함
    xIdx = 0
    yIdx = 0
    for idx, data in enumerate(pollutionData):
        if idx == nPolIndex: continue

        axarr[xIdx, yIdx].plot(month, pollutionData[nPolIndex], 'b-o', label=polName[nPolIndex])
        axarr[xIdx, yIdx].plot(month, data, 'r-s', label=polName[idx])
        axarr[xIdx, yIdx].set_title(polName[nPolIndex]+" / "+polName[idx])
        #axarr[xIdx, yIdx].set_xlabel("월")
        axarr[xIdx, yIdx].set_ylabel("오염도 ")
        axarr[xIdx, yIdx].legend()
        
        yIdx += 1
        
        if (yIdx > 2) :
            xIdx += 1
            yIdx = 0
            
    # 그래프 노출
    plt.show()

if __name__== '__main__':
    analyzePollutionCompare()
