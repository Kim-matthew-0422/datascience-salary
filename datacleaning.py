# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 00:25:16 2021

@author: mat_c
"""

import pandas as pd


df = pd.read_csv('glassdoor_jobs.csv')

#salary cleaning 
#company name text
#state field
#age of company
#parsing of job description
df = df[df['Salary Estimate'] != '-1']

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)


df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)


df['age'] = df.Founded.apply(lambda x: x if x<1 else 2021 - x)

df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

df['r_studio'] = df['Job Description'].apply(lambda x: 1 if 'r-studio' in x.lower() or 'r studio' in x.lower() else 0)
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df_out = df.drop(['Unnamed: 0'], axis = 1)

df_out.to_csv('salary_data_cleaned.csv',index = False)

