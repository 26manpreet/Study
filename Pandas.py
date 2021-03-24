PANDAS
- analysis/calculation on large set of data can be easliy done
- dataframes, makes easier for sql people to play.
- Data piplines or ETL - connect to diff types of datasources (CSV,JSON,EXCEL,RDBMS) and put data into diff source after cleansing (can serve ETL purpose)
- Data visulisation
- can easily handle Null/None values as well
- load data from huge file



#check pandas version
pip show pandas

pandas.__version__


#----------------------------------
#PANDAS DATA STRUCTURES:
#----------------------------------
    --Series    1-D
    --Dataframe 2-D 
    --Panel     3-D


    #----------------------------------
    #------------1) Series-------------
    #----------------------------------
    
    #---pd.series(data (constant/list/dict/numpyarray), index, dtype)
        import pandas as pd
        s = pd.Series([1,2,3,4])# by default index will be start from 0......n , and doesnt have any name since array only has index and its value
        
        s = pd.Series([1,2,3,4],index=[101,102,103,104])
        
        s = pd.Series([1,2,3,4],index=['A','B','C','D']) #index can also be string
        
       
    
    #access Series (Normally , as we do access List)
    
        >>> s
        0    1
        1    2
        2    3
        3    4
        dtype: int64
        >>> list(s)
        [1, 2, 3, 4]
        
        s[1]    #2
        s['B']  #2  
    
    #--------------------------------------
    #-----------------2) Dataframe---------
    #--------------------------------------
    
    - Each DataFrame will have data, index and columns. (Column name and index values are case-sensitive)
    
    
    # 1) Create Dataframe from list of list/tuple
        df1 = pd.DataFrame([[10, 2], [40, 5], [70, 8]])#---index will be integer 0.... and column will be 0,1
        
        df1 = pd.DataFrame( data = [[10, 2], [40, 5], [70, 8]],
                            index=['cobra', 'viper', 'sidewinder'],
                            columns=['max_speed', 'shield'])
        
        
        # O/P -- df1
                    max_speed 	shield
            cobra 	10 	2
            viper 	40 	5
            sidewinder 	70 	8
    
        
    # 2) Dataframe from Series
        s1=pd.Series([1,2])
        s2 = pd.Series(['Python', 'Programming',])
        s3 = pd.Series(['Pythobvkjdsjkn', 'Progrsnmdsamming','test'])
        df = pd.DataFrame([s1,s2,s3])
    
    
    # 3) Datframe from dict of list/nupmy/series
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}  # all values must be of same length, otherwise ValueError 
        df = pd.DataFrame(data) 
    
    
    # 4) from source csv/excel/sql/json
    
    
    
    # 5) from another DataFrame
    
        
        
    df.set_index('any_column') -- specify column that need to be consider as index
    
    
#------------------------------------------
# ------IMPORT DATA------------------------
#------------------------------------------
    # Dataframe from CSV   -- better than object/csv_reader due to its various options as below
    df=pd.read_csv('ign.csv',delimiter=',')  #just sep also works
    """
    header     - row no. to use as column , if we use header=5 , then 5th line will be considered as header and before lines will be auto skipped.
    index_col  - column to be used as index , index_col='id'
    usecols    - only these column will be fetched ,e.g, usecols=['id','Currency']
    nrows      - no of rows will be fetched.
    skiprows   - no of lines to skip at starting, if header is used then from its index.
    skipfooter - no of lines to skip at end
    dtype={'Name':str,'Age':int}
    names=['memo','ind','cur']  # when files doesnt has any header, to svoid conisdering first row as header use names
    na_values=['??','###']   # treat these values as Nan
    """

    # Dataframe from EXCEL , can read from local or url
    df=pd.read_excel('test.xlsx',sheet_name='sheet1')  # OTHER PARAMETERS WORK SAME AS ABOVE FOR CSV


    # Dataframe from JSON
    df=pd.read_json(jsonstr/jsonurl/jsonfile) # if json format is not as per dataframe , first read nd then change.


    # Dataframe from database
    df=pd.read_sql(sqlquery,conn) # params is extra parameter for bind values
    sql_query="""select * from t where c1={}""".format(column_value)

    #Pandas give NaN nd None value while reading data from csv and database
    NaN - Null for numerical columns
    None - null for other columns 
    


    
#------------------------------------------    
# --------EXPORT DATA----------
#------------------------------------------

    # Dataframe to CSV   (usually used to write cleaned data back into file)
    df.to_csv(file_name,sep=',',index=False,encoding='utf-8')#index-->False means dont write its values


    # Dataframe to EXCEL
    df.to_excel('Name.xlsx', index = False ,sheet_name='Sample_sheet')


    # Dataframe to JSON
    to_json
    
    
    # Datfarme to database
    to_sql
    
    for index, row in df.iterrows(): # return index and series (of row)
        cur.execute ('insert into t1 values (:1 ,:2 ,:3 )',row['c1'],row['c2'],row['c3'])
        ins=ins+1
    print('Rows inserted are :' + str(ins))
    
    # better performance (Bulk insert) and single line of code with to_sql
    from sqlalchemy import create_engine
    conn = create_engine('oracle+cx_oracle://hr:hr@Localhost:1521/xe')
    df.to_sql('emp',con=conn,index=True,index_label='id',chunksize=1000)   # insert index as well and name it as id
    
    """
    schema : string, optional
        Specify the schema (if database flavor supports this). If None, use
        default schema.
    if_exists : {'fail', 'replace', 'append'}, default 'fail'
        How to behave if the table already exists.

        * fail: Raise a ValueError.
        * replace: Drop the table before inserting new values.
        * append: Insert new values to the existing table.
     """
     

#------------------------------------------
#---------VIEW / INSPECTING DATA-----------
#------------------------------------------
    df.head(n)  -- First n rows of the DataFrame, if n is not passed--5 rows
    df.tail(n)  -- Last n rows of the DataFrame, if n is not passed--5 rows
    
    
    df.shape    --Number of rows and columns -->tuple(rows,columns)          --count
    df.info()   -- Index, columns(count,datatype) and Memory usuage                          --desc table


# better to check individual details
    #------- INDEX ---------
    df.index   --row labels (index names/values)
    
    
    #-------- COLUMNS ----------
    df.columns --column labels (column names)
    df.column[0] --first column label
    
    #------ DATA TYPES -------
    int64,float64,object (for string) ,datetime64
    
    
    df.dtypes         # data type of each column
  
    s.astype(float)     -- Convert the datatype of the series to float
    df['salaray'] = df['salaray'].astype('int64')
    
    
    #-----MEMORY USAGE-----------
    df.memory_usage() # memory size of each column

    

#------------------------------------------
#------STATISTICAL FUNCTIONS------------
#------------------------------------------
    #return in dataframe
    df.describe() -- Summary statistics for all numerical columns(count,min,max,std)
    
    
    #below return in series
    #df.count()['Age'] -- OF PARTICULAR COLUMN
    df.count() -- Returns the number of non-null values for each column (both numerical and non numerical)
    df.mean() -- Returns the mean of all numerial columns
    df.max()   -- Returns the highest value in each column
    df.min()   -- Returns the lowest value in each column
    df.median() -- Returns the median of each column
    
    df.std() -- Returns the standard deviation of each column
    df.corr() -- Returns the correlation between columns in a DataFrame
    
    
    
    
    df['Salaray'].mean() #average salaray
    
    
    
     
#------------------------------------------
# ----------SELECTION AND INDICING---------
#------------------------------------------

# select all rows and columns , select * from t;
    df

# select first or last 10 rows
        df.head(10) or df.tail(10)
        df.iloc[0:9]

#Selection by Column
    
    #single column
    df['column_name'] -- return column in Series (By column name)
    or. df[df.columns[0]]  -- By column position   # df.columns -- contain all columns
    df.Name # check if it works
    
    #Multiple column
    df[['col1','col2']] -- return as Dataframe


#Selection by row
    df.loc['index']  -- by index name
    df.iloc[0]       --by index position
    #diff can be obsereved by sorting dataframe then position will be still 0,1,2... and index will be changed

    df.iloc[1:]--all rows starting from index position =1


#Selection on row +column
    df.iloc[1:,1]--all rows from index position=1 and only 2nd column


# distinct values
    df['Name'].unique() # works on series or for one column
    #or df.Name.unique()
    
    df['Name'].drop_duplicates()
    
    
# count    
    - for whole dataframe use shape
    - count()
        df.count()           # count of each column (non null values)
        df['memo'].count()   # count of memo column
    
    - value_counts() - count True values, use for dataframe with True/False values
        #count whose salary>50000
        df['SALARY']>50000.value_counts()  #works on series
        df['memo'].value_counts()  # count of each value in memo column , return series



#---------------------------------------------
# Add columns
#---------------------------------------------
    #df['new']=None
    df['SALARY_NEW']=df['SALARY']+10000
    
    df.insert(2,'new','')# insert new column at poition 2 with blank values

#---------------------------------------------
# drop columns
#---------------------------------------------

    df.drop(columns='Total Cost',inplace=True)
    
    #df=df.drop(columns='Total Cost')

#---------------------------------------------
# Rename columns
#---------------------------------------------
    df.rename(columns = {'empid':'e_id'}, inplace = True) # inplace=True , for permament changes in existong dataframe
    
    #df.columns = ['a','b','c'] -- Rename columns
    
    

#---------------------------------------------
# Add/ Drop Row
#---------------------------------------------
# Drop Row first row
    df_new.drop(df.index[0])


# ADD ROW
    #1. using df.loc
    df = pd.DataFrame(columns=['id','name']
    df.loc[len(df.index)] = [1 ,'ABC']
    
    #2. using df.append()
    new_row = {id:1 , 'name':'ABC'}
    df = df.append(new_row,ignore_index=True) # index_lable=True is used to add series into pandas otherwise genrate erro




#------------------------------------------
#----------DATA CLEANING--------------Check for DML's
#------------------------------------------

# ----- Identify null values--------
    df['Salary'].isnull()                -- Checks for null Values, Returns dataframe with True False if dataframes is being used  # check if isNULL is wprking????
    df['Salary'].notnull()              -- check for not null values
        
    df[df['Salary'].isnull()]  # complete dataframe , where salary is null
        
    
    df.isnull().any()  # return columns with True/False oif they have null values
    
    df.isnull().sum()  # no. of null values in each columns
    
    df['Salary'].isnull().sum()         --count of null values



# ----- Handling missing or Null values ----
    - drop
        df.dropna()                -- Drop null values from dataframe , USE INPLACE=True  , USE SERIES FOR PARTICULAR COLUMN
        df.dropna(axis=1)          -- Drop all COLUMNS that contain null values    
        df.dropna(axis=0)          -- Drop all ROWS that have null values.
        
        #drop rows or column on the basis of one column values
        df.dropna(subset=['empid'],axis=0,inplace=True) # inplace allows to make changes in dataframe
    
    
    - Replace
        
        - Null values
        df['salary'].replace(np.nan, df['salary'].mean())  # use replace mostly for non null values
        
        or,
        df.fillna(x,inplace=True)               -- Replace all null values with x  , x can also be something mean etc
        df['Salary'].fillna(x)     -- fill NaN in column
        
        
        - Non Null values
        df.replace(1,'one')               --Replace all values equal to 1 with 'one'
        df.replace([1,3],['one','three']) -- Replace all 1 with 'one' and 3 with 'three'
  



#----------------------------------------
# ------- Arithmetic ---------------------
#----------------------------------------
- All the common mathematical operators that work in Python, like +, -, *, /, and ^ will work in series/Dataframe
    
    df['score'] / 2   # divide all score by 2
    
    df['score']='XXXX'          # replace all values of column 'score' with XXXX


#----------------------------
#--------FILTERS------------
#----------------------------

    # df['SALARY']    -->return SALARY column only as Series.
    # df['SALARY']>10000  --> return all rows of salary column with True False
    
    df[df['SALARY']==10000] --select dataframe with rows which satisfy this condition
    
    # When filtering with multiple conditions, it's important to put each condition in parentheses, 
    # and separate them with a single ampersand (&).
    df[(df['SALARY']>=10000) & (df['SALARY']<=510000)]
    
    
    
    # LIKE Operator in Pandas
    df[ df['Name'].str.startswith('Man')]
    df[ df['Name'].str.endswith('Singh')]
    df[ df['Name'].str.contains('preet')]
    
    #select Name,city from t where name like '%preet%';
    df[ df['Name'].str.contains('preet')] [['Name','City']]
    
    # In and NOT   , isin()
    df[df['cur'].isin(['AUD','INR'])] # where cur in ('AUD','INR')
    df[~df['cur'].isin(['AUD'])]      # where cur not in ('AUD')




#------------------------
#------SORTING----------
#------------------------
    df.sort_values(col2,ascending=False) -- Sort values by col2 in descending order  
    df.sort_values([col1,col2],ascending=[True,False])
    #na_position : {‘first’, ‘last’}, default ‘last’
    
    
    
    # Top 10 selary records
        df.sort_values('SALARY',ascending=False).head(10)




#--------------------------------
# ------ Pivot-----------------
#--------------------------------





#------------------------------------------
#------GROUP BY-----------
#------------------------------------------

    #df.groupby(by=['score_phrase']).score.max()
    df.groupby(by=['JOB_ID'])['SALARY'].max()  #select max(salary) from <table> group by job_id;
    df.groupby(by=['JOB_ID'])['SALARY','FIRST_NAME'].max()
    
    df.groupby(by=['JOB_ID','CITY'])[['SALARY']].max()
    
    
    
    #----filter + group by 
    df_filter=df[(df['SALARY']>10000 )&(df['SALARY']<=50000 )]
    df[df_filter].groupby(by=['JOB_ID'])[['SALARY']].max()
    
    or,
    df[(df['SALARY']>10000 )&(df['SALARY']<=50000 )].groupby(by=['JOB_ID'])['SALARY'].max()
    
    
    #------APPLY---------
    df['score'].apply(lambda score: score+100 if score%2==0  else score)   #applying valuees of df['score'] to function






#-------------------------------------------------------
#--------------------JOIN/COMBINE-----------------------
#-------------------------------------------------------
#df1
	C1	C2
0	1	A
1	2	B

#df2
	C1	C2
0	1	A
1	2	B
----------------------------------------------------------------------------------------------------------
df1.append(df2)                    -- Add rows of df2 to end of df1 (column should be identical)#--UNION
----------------------------------------------------------------------------------------------------------

    C1	C2	C3	C4
0	1.0	A	NaN	NaN
1	2.0	B	NaN	NaN
0	NaN	NaN	3.0	C
1	NaN	NaN	4.0	D
2	NaN	NaN	5.0	E

#if both dataframes has same column names :
    C1	C2	
0	1.0	A
1	2.0	B
0	3.0	C
1	4.0	D
2	5.0	E

#above index values are according to each dataframe , to have sequential index values use --> df.append(df2,ignore_index=True)

# add row without second dataframe
df1.append({c1: 1, c2: 10},ignore_index='True')

----------------------------------------------------------------------------------------------------------
pd.concat([df1,df2],ignore_index=True)  --Add rows of df2 to end of df1 (rows should be identical)#ignore_index=True-->proper index after conact
pd.concat([df1,df2],axis=1)             --behave as join and join on index
----------------------------------------------------------------------------------------------------------

# Diff bw append and concat
    - concat : can add rows in axis=0 (default, add to end of df1) and axis=1 ( add  beside to df1, if index same then in same row else in diff)
    - append : can add only to end of df (i.e, axis=0 behaviour)
    

# Join     
- Join based on the indexes ( or set by set_index) and  how variable =['left','right','inner','outer'] 
- both dataframe must have diff column names otherwise error wil be generated.

    
    df1.join(df2,how='left')  #left--->all rows from left dataframe and matching rows from right and nonmatching will have NaN (as NULL in sql)  


    df.join(df2.set_index('col1'),on=col1,how='left') # can join on column as well, but column name should be same in both dataframes.



#Merge
-Join based on column names of each dataframe defined under left_on/right_on and how variable 

    df1.merge(df2,on='col')             #By default inner join and joins on index
    df1.merge(df2,on='col1',how='left')

    #--join on multiple columns---
    df1.merge(df2,on=['col1','col2','col3'],how='left')

    #---fillna--
    df1.merge(df2,on=['col1','col2','col3'],how='left').fillna('Insert')
    
    #--fillna particular column only in dataframe
    df1['c1_y']=df1['c1_y'].fillna('Insert')


    #---use left_on and right_on, when joining column name is not same on both dataframes
    #---by default has suffix _x and _y
    df1.merge(df2,  how ='left', left_on='county_ID', right_on='countyid',suffixes=('_left', '_right'))



# Diff bw Join and Merge 
    - Join : based on the indexes ( or set by set_index) and  how variable =['left','right','inner','outer'] 
    - Merge: based on column names of each dataframe defined under left_on/right_on , how variable and suffixes option


#-----Set operations-----
- Minus/Union/unionall/intersect




#---------------------------------------------
#-------- Interview questions ----------------
#---------------------------------------------
# 1. ---------- Huge data file --------------

    import pandas as pd
    import datetime as dt
    
    print(dt.datetime.now())
    df = pd.read_csv('sales_1M.csv')
    print(dt.datetime.now())


    # --- use chunksize ----little faster and avoids memory issue
    import pandas as pd
    import datetime as dt
    print(dt.datetime.now())
    
    for df in pd.read_csv('sales_1M.csv',chunksize=500000): # chunksize can also be used in read_Sql
        print(df.shape)
        
    print(dt.datetime.now())


# 2. ----------- How to use transformation function