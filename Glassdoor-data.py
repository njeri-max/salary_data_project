# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:15:19 2024

@author: NjeriWanjiru
"""
import pandas as pd

df=pd.read_csv('C:\\Users\\NjeriWanjiru\\Documents\\salary_data_project\\glassdoor_data.csv')
print(df)


#Salaryparsing
#company name test only
#state field
#company age
#parsing of job description 

#SALARY PARSING
#remove -1 from the salary estimate column
df = df[df['Salary Estimate'] != '-1']

#create a new column for per hour and Employer provided salary from salary estimate column
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

#lamda functions
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
salary_dk_signs=salary.apply(lambda x: x.replace('K', '').replace('$', ''))


min_hr = salary_dk_signs.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

df['min_salary'] = min_hr.apply(lambda x: int(float(x.split('-')[0])))
df['max_salary'] = min_hr.apply(lambda x: int(float(x.split('-')[-1])))
df['avg_sal'] = (df.min_salary+df.max_salary)/2


#COMPANY NAME TESXT
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#STATE FIELD
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[-1])
df.job_state.value_counts()

#df['same_state']= df.apply(lambda x: 1 if x.Location == x)
#COMPANY AGE
df['company_age'] = df['Founded'].apply(lambda x: x if x < 1 else 2024 - x)

#PARSE THE JOB DESCRIPTION
#python
df['python-ys']=df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['python-ys'].value_counts()
#r
df['R_ys']=df['Job Description'].apply(lambda x: 1 if 'r studio'  or  'r-studio' in x.lower() else 0)
df.R_ys.value_counts()
#spark
df['spark_ys']=df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark_ys.value_counts()
#aws
df['aws_ys']=df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws_ys.value_counts()

df.to_csv('cleaned_data_results.csv', index=False)