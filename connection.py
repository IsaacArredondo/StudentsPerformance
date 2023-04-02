import pandas as pd
import sqlalchemy

#Appending data to table created in MySQL Workbench

def append_myqsl_data():
    df.to_sql("students", engine, if_exists='append', index =  False)
    
df = pd.read_csv('StudentsPerformance.csv')

engine = sqlalchemy.create_engine('mysql+mysqldb://root:xPAFx#JATV4@localhost/performance')

columns_names = {
    'gender': 'GENDER',
    'race/ethnicity': 'ETHNICITY',
    'parental level of education': 'PARENTAL EDUCATION LEVEL',
    'lunch': 'LUNCH',
    'test preparation course': 'TEST PREPARATION COURSE',
    'math score': 'MATH SCORE',
    'reading score': 'READING SCORE',
    'writing score': 'WRITING SCORE'
}
    
df.rename(columns = columns_names, inplace = True)