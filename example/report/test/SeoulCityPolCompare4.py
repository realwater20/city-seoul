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

    # 연도별 대기오염 평균 csv 파일 읽어오기
    # 연도, 이산화질소농도(ppm), 오존농도(ppm), 일산화탄소농도(ppm), 아황산가스(ppm), 미세먼지(㎍/㎥)
    bf_date = ''
    yearIdx = 0
    monthIdx = 0
    pollutionData = [[[0 for col in range(0)] for row in range(5)] for row in range(10)]
    
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
                pollutionData[yearIdx][colIdx1-1].insert(monthIdx, float(value))
                
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
    
    # 오염 제목 리스트
    polName = ["이산화질소", "오존", "일산화탄소", "아황산가스", "미세먼지"]
       
    # X축 월별 배열 정보 선언
    month = ['1','2','3','4','5','6','7','8','9','10','11','12']
    
    # 그래프 수치 년도
    year = ['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
    
    # 그래프 수치 표시 색상
    color = ['#99FF00','#6600FF','#333333','#FF9966','#FF6666','#CC3399','#CC0033','#339900','#0000FF','#663333']
    
    # 비교대상 오염정보 Index
    nPolIndex = 0
    
    # 대기오염 정보 plot 설정
    f, axarr = plt.subplots(2, 3)

    # 오염 종류 및 연도별 노출
    xIdx = 0
    yIdx = 0
    for val1 in range(0, 5):
        for val2 in range(0, 10):
            axarr[xIdx, yIdx].set_title(polName[val1])
            axarr[xIdx, yIdx].plot(month, pollutionData[val2][val1], '-o', label=year[val2], color=color[val2])
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
