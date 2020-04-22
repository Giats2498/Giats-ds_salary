# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:34:19 2020

@author: Giats
"""

import glassdoor_scraper as gs
import pandas as pd
path = "chromedriver"

df = gs.get_jobs('data scientist',1000,False,path,10)

df.to_csv("glassdoor_jobs.csv",  index=False)