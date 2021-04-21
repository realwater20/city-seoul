# -*- coding: utf-8 -*- 
# 파일 읽기 처리 모듈
import csv

class ExcelFileReader:
    path = ""
    delimiter = ""
    
    def __init__(self, path, delimiter):
        self.path = path
        self.delimiter = delimiter
    
    def csvRead(self):
        f = open(self.path, 'rt')
        fileData = csv.reader(f, delimiter = self.delimiter)
        
        return fileData
    
    