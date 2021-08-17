# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 22:48:31 2021

@author: mat_c
"""

import glassdoorselenium as gs
import pandas as pd
path = "C:/Users/mat_c/OneDrive/Desktop/datascience/chromedriver"
df = gs.get_jobs('data scientist',15, False, path, 15)