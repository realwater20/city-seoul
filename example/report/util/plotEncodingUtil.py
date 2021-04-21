# -*- coding: utf-8 -*- 
# matPlot 기본 인코딩 관련 Util 모듈
from matplotlib import pyplot as plt, font_manager, rc
import sys

# matplot 전용 한글 인식 인코딩 기본 SET 함수
def plotKrRecognition():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
