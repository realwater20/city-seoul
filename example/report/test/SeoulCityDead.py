# -*- coding: utf-8 -*- 
# 서울시 월별 연간 사망자 수 집계 
import numpy as np
import matplotlib.pyplot as plt
from operator import eq
import csv

def analyzeDie():
    
    # csv 파일 읽어오기
    pieces = []
    datafile = '.\\csv\\SeoulDeadReport.csv'
    with open(datafile, 'rt') as f :
        data = csv.reader(f, delimiter = ',')
        for d in data:
            pieces.append(d)
    
    # csv 파일 데이터 배열로 만들기
    bf_date = ''
    dieCol = 0
    dieRow = 0
    dieArray = [[0 for col in range(0)] for row in range(7)]
    for date, dieCnt in pieces:
        if eq(bf_date, '') == True :
            bf_date = date[:4]
            
        elif eq(bf_date, date[:4]) == False : # 연도별로 데이터 담기
            bf_date = date[:4]
            dieCol += 1
            dieRow = 0
        
        # 행은 연도 열은 월기준으로 데이터를 만든다.
        dieArray[dieCol].insert(dieRow, dieCnt)   

    month = ['1','2','3','4','5','6','7','8','9','10','11','12']
    year  = ['2010', '2011', '2012', '2013', '2014', '2015', '2016']
    color = ['b','g','r','c','m','y','k']
    
    n_groups = 12 # 노출되는 그래프 x축 개수

    index = np.arange(n_groups)
    bar_width = 0.1 # 막대그래프 넓이
     
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    
    width_g = 0 
    cnt = 0
    for yearDieArray in dieArray:
        plt.bar(index+width_g-0.2, yearDieArray, bar_width,
                alpha=opacity,
                color=color[cnt],
                error_kw=error_config,
                label=year[cnt],
                align='edge')
        
        width_g = width_g + bar_width
        cnt = cnt + 1

    plt.xlabel('Year') # X축 제목
    plt.ylabel('Count') # Y축 제목
    plt.title('Analyze Die Graph') # 메인 제목 설정
    plt.xticks(index + bar_width, month)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__== '__main__':
    analyzeDie()