# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:10:38 2019

@author: tanmay.sidhu
"""
import pandas as pd
import os
import pylogger

class generic_sanity_checks:
    def __init__(self,path=None,file_name,sheet_name=None):
        
        self.path=path
        self.file_name=file_name
        self.extn=self.file_name[self.file_name.find(".")+1:]
        self.sheet_name=sheet_name if self.extn !="csv" else self.sheet_name=None
            
        
        
    def data_loader(self):
        if self.extn in ["csv"]:
            df_csv=pd.read_csv(os.path.join(self.path,self.file_name))
        elif self.extn in ["xlsx"]:
            df_xlsx=pd.ExcelFile(os.path.join(self.path,self.file_name))

