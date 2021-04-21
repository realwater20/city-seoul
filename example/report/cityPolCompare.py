# -*- coding: utf-8 -*- 
# 2007~2016 연도별 대기오염 vs 대기오염 비교 그래프
import numpy as np
import math  as mt

from matplotlib import pyplot as plt
from operator import eq

import common.cityPolConst as cityConst
import util.plotEncodingUtil as pltEncoding
from util.fileReaderUtil import ExcelFileReader
import util.dataCalUtil as dataNormalUtil

def analyzeProc(): 
    # matplot 그래프 한글 인식 인코딩
    pltEncoding.plotKrRecognition()

    # 연도별 대기오염 평균 csv 파일 읽어오기
    # 연도, 이산화질소농도(ppm), 오존농도(ppm), 일산화탄소농도(ppm), 아황산가스(ppm), 미세먼지(㎍/㎥)
    pollutionFileReader = ExcelFileReader('csv/PollutionData.csv', ',')
    pollutionFileData = pollutionFileReader.csvRead()
    
    bf_date = ''
    yearIdx = 0
    monthIdx = 0
    pollutionData = [[[0 for col in range(0)] for row in range(5)] for row in range(10)]
    for data in pollutionFileData:
        for idx1, value in enumerate(data):
            if idx1 == 0 :
                if eq(bf_date, '') == True :
                    bf_date = value[:4]
                elif eq(bf_date, value[:4]) == False : # 연도별로 데이터 담기
                    bf_date = value[:4]
                    yearIdx += 1
                    monthIdx = 0
                continue
            
            # [연도별][오염종류별][오염수치]
            pollutionData[yearIdx][idx1-1].insert(monthIdx, float(value))
            
        monthIdx += 1
                
    # 오염 데이터 정규화 처리
    pollutionData = dataNormalUtil.threeNormalization(pollutionData)
    
    # 오염 제목 리스트
    polName = cityConst.POL_NAME_LIST

    # 그래프 수치 년도 (2007 ~ 2016)
    year = cityConst.POL_YEAR_2007_2016_LIST
    
    # X축 월별 배열 정보 선언 (1월 ~ 12월)
    month = cityConst.POL_MONTH_LIST
    
    # 대기오염 정보 plot 설정
    f, axarr = plt.subplots(4, 3)

    # 오염 종류 및 연도별 노출
    xIdx = 2
    yIdx = 4
    plotX = 0
    plotY = 0
    for yearIdx in range(0, 10):
        axarr[plotX, plotY].set_title(year[yearIdx])
        axarr[plotX, plotY].plot(month, pollutionData[yearIdx][xIdx], '-o', label=polName[xIdx], color='b')
        axarr[plotX, plotY].plot(month, pollutionData[yearIdx][yIdx], 'r-s', label=polName[yIdx], color='r')
        axarr[plotX, plotY].set_ylabel("오염도 ")
        axarr[plotX, plotY].legend()

        plotY += 1 

        if (plotY > 2) :
            plotX += 1
            plotY = 0
                 
    # 그래프 노출
    plt.show()

if __name__== '__main__':
    analyzeProc()
