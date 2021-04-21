# -*- coding: utf-8 -*- 
# 데이터 계산 모듈

# 1차원 배열 정규화 처리
def oneNormalization(arrayData):
    minVal = min(arrayData)
    maxVal = max(arrayData)
    for idx2, oneDepthData in enumerate(arrayData):
       rangeVal = (maxVal - minVal)
       arrayData[idx1][idx2] = (arrayData[idx1][idx2] - minVal) / rangeVal
    
    return arrayData

# 2차원 배열 정규화 처리
def twoNormalization(arrayData):
    for idx1, oneDepthData in enumerate(arrayData):
        minVal = min(oneDepthData)
        maxVal = max(oneDepthData)
        for idx2, twoDepthData in enumerate(oneDepthData):
           rangeVal = (maxVal - minVal)
           arrayData[idx1][idx2] = (arrayData[idx1][idx2] - minVal) / rangeVal
    
    return arrayData

# 3차원 배열 정규화 처리    
def threeNormalization(arrayData):
    for idx1, oneDepthData in enumerate(arrayData) :
        for idx2, twoDepthData in enumerate(oneDepthData):
            minVal = min(twoDepthData)
            maxVal = max(twoDepthData)
            for idx3, treeDepthData in enumerate(twoDepthData):
                rangeVal = (maxVal - minVal)
                arrayData[idx1][idx2][idx3] = (arrayData[idx1][idx2][idx3] - minVal) / rangeVal
                
    return arrayData    

