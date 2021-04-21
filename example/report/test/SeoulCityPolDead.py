# -*- coding: utf-8 -*- 
# 서울시 대기오염과 사망자 현황 관계 그래프
import numpy as np
import matplotlib.pyplot as plt
from operator import eq
import csv

def analyzePollutionDie():
    
    # 연도 및 월별 서울시 사망자 현황 csv 파일 읽어오기
    dieData = []
    dieDatafile = 'csv/SeoulDeadReport.csv'
    with open(dieDatafile, 'rt') as f :
        data = csv.reader(f, delimiter = ',')
        for d in data:
            dieData.append(d)
    
    # 2016년 서울시 사망자 현황 csv 파일 데이터 배열로 만들기
    dieIndex = 0
    dieArray = []
    for date, dieCnt in dieData:
        if eq('2016', date[:4]): # 2016년도 자료만 발췌        
            # 행은 연도 열은 월기준으로 데이터를 만든다.
            dieArray.insert(dieIndex, dieCnt)
            dieIndex += 1 

    # 2016년 대기오염 평균 csv 파일 읽어오기
    pollutionData = []
    polltutionDatafile = 'csv/SeoulAirpollution.csv'
    with open(polltutionDatafile, 'rt') as f :
        data = csv.reader(f, delimiter = ',')
        for d in data:
            pollutionData.append(d) 

    # 2016년 대기오염 성분별 csv 정보 읽어오기
    # 연도, 이산화질소농도(ppm), 오존농도(ppm), 일산화탄소농도(ppm), 아황산가스(ppm), 미세먼지(㎍/㎥), 초미세먼지(㎍/㎥)
    polArray = [pol3 for year, pol1, pol2, pol3, pol4, pol5, pol6 in pollutionData]

    # X축 월별 배열 정보 선언
    month = ['1','2','3','4','5','6','7','8','9','10','11','12']
    
    # 그래프 메인 타이틀 설정
    
    plt.title('Death of Seoul City and Air Pollution')
    
    # 2016년 사망자 정보 plot 설정
    plt.plot(month, dieArray, 'b-o', label="Dead")
    plt.xlabel('Month')
    plt.ylabel('Dead Count')
    plt.legend()
    
    # 2016년 대기오염 정보 plot 설정
    ax2 = plt.twinx()
    plt.plot(month, polArray, 'r-s', label="Air pollution")
    plt.ylabel('AirPollution Count')
    plt.legend()
    ax2.yaxis.tick_right()

    # 그래프 노출
    plt.show()

if __name__== '__main__':
    analyzePollutionDie()
