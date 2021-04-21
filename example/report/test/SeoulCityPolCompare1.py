# -*- coding: utf-8 -*- 
# 서울시 대기오염별 관계 그래프
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

    nInputPol1 = 3;
    nInputPol2 = 4;
    
    if (nInputPol1 < 1 or nInputPol1 > 6) or (nInputPol2 < 1 or nInputPol2 > 6) :
        print "비교할 입력 변수는 1~6까지 입니다."
        return 0

    # 2016년 대기오염 평균 csv 파일 읽어오기
    # 연도, 이산화질소농도(ppm), 오존농도(ppm), 일산화탄소농도(ppm), 아황산가스(ppm), 미세먼지(㎍/㎥), 초미세먼지(㎍/㎥)
    pollutionData = [[0 for col in range(0)] for row in range(7)]
    polltutionDatafile = 'csv/SeoulAirpollution.csv'
    with open(polltutionDatafile, 'rt') as f :
        rowData = csv.reader(f, delimiter = ',')
        for colIdx2, data in enumerate(rowData):
            for colIdx1, d in enumerate(data):
               pollutionData[colIdx1].insert(colIdx2, float(d))
    
    # 정규화 처리
    for idx, pol in enumerate(pollutionData):
        minVal = min(pollutionData[idx])
        maxVal = max(pollutionData[idx])
        for valIdx, val in enumerate(pol):
           rangeVal = (maxVal - minVal)
           pollutionData[idx][valIdx] = (pollutionData[idx][valIdx] - minVal) / rangeVal 
    
    # 오염 제목 리스트
    polName = ["이산화질소농도", "오존농도", "일산화탄소농도", "아황산가스", "미세먼지", "초미세먼지"]
     
    # X축 월별 배열 정보 선언
    month = ['1','2','3','4','5','6','7','8','9','10','11','12']
    
    # 그래프 메인 타이틀 설정
    plt.title('서울시 오염 비교')
    
    # 2016년 대기오염 정보 plot 설정
    plt.plot(month, pollutionData[nInputPol1], 'b-o', label=polName[nInputPol1])
    plt.plot(month, pollutionData[nInputPol2], 'r-s', label=polName[nInputPol2])
    plt.xlabel('월')
    plt.ylabel('오염도')
    plt.legend()
   
    # 그래프 노출
    plt.show()

if __name__== '__main__':
    analyzePollutionCompare()
