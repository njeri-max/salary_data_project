# -*- coding: utf-8 -*-
"""
Created on Sat May 18 04:14:08 2024

@author: NjeriWanjiru
"""

import glassdoor_scraper as gs
import pandas as pd
path = r'C:\Users\NjeriWanjiru\Documents\salary_data_project'

df = gs.get_jobs('data scientist', 15, False, path, 15)