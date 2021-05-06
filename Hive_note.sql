-----------------------------
-- HIVE  (query interface)
-----------------------------
	- DWH framework(OLAP) on top hadoop , use to read,write,manage 
	  large amount of data in distributed storage using SQL like HQL (- Syntax similar to MySQL).
	- adhoc querying data with SQL
	- Its not RDBMS , but make a interface like it	
	- developed by FB, developed abstraction interface on top of MapReduce to enable SQL developer to analyse data simply on Hadoop.
	  Supports, almost all sql queries.
	  

-- How it works
	- Hive execution engine converts HQL into JAR files(MapReduce) to get executed on clusters.	
	- see in details ...metastore an all.
	

-- advantage	
		- it was really difficult to analyse large file with MapReduce( required more lines of code in MapReduce).
		

-- disadvantage
		- Not suitable for OLTP , since doesnt supports insert/update at row level.
		- No ACID support.
		- Not for unstructured data.



--------------------------------------------
-- how data is organised in hive 
--------------------------------------------
	1. DATABASE

	2. TABLES
				---------------------------------------------			----------------------------------------
							Managed	 (or Internal)												External
				---------------------------------------------			----------------------------------------
				- Hive owns defination + data								- Hive own data defination only
				- Each table maps to a directory, which is under 			- Points to file in HDFS (location is specified while table creation)
				  /user/hive/warehouse by default in HDFS.
				  --e.g., /user/hive/warehouse/emp -- for emp table
				- When table is dropped , data is deleted altogether		- Dropping table doesnt effect actual data in HDFS
				- Use case : intermediate table for data processing			- Use case : Analyse processed data present in HDFS
																		

	3. PARTITIONS -- ( when cardinality of column is low)
		- Similar to RDBMS, can increase performance by hitting particular partition - I/O and time of the query is greatly reduced
		- Each Partition will has seperate file of data.
		- Partition column maps to subdirectory in tables directory.

	4. BUCKETS (OR CLUSTERS) -- ( when cardinality of column is high)
		- Similar to Partitions that divides table into segments.
		- bucketting column maps to file in table directory
		- bucketing can be use alone or with Partitions to imrove better performance


		emp:
		|-Id  -- Bucketing
		|-Dept Id -- Partitions
		|-Salary -- Bucketing
		|-Year_of_joining -- Partitions
		|-country -- Partitions

	5. VIEWS






------------------------------------------------------------
-- Hive architecture
------------------------------------------------------------
- Hive clients : interface through which query is passed - Hive CLI, Ambari UI
		--3 ways to connect to Hive server:
			1. Thrift Client: This is used to run all the hive commands using a different programming language 
							  such as Java, C++, PHP, Python or Ruby.
			2. ODBC Driver: This will support the ODBC protocol
			3. JDBC Driver: This will support the JDBC protocol

- Metastore  : stores metadata such as table, columns, partitions, location , Usually, as RDBMS and its details can be found at : hive-site.xml

- Driver : 
	- syntax and semantic checks
	- parse query
	- generated execution plan with the help of metastore
	- Execution plan created by compiler is DAG of stages
	- finally, Jar files are created out of hive query and these are run by MapReduce

- Hadoop core componenets 
	- HDFS : actual data stores here at hive warehouse directory
	- Mapreduce : When we fire any query -> converted into JAR files ->execute this JAR file as Map Reduce



					-----------------------------------------
					|			Hive Clients
					-----------------------------------------
									|
					-----------------------------------------				------------------------
					|			Driver							<--------> 		Metastore
					-----------------------------------------				------------------------
									|
					----------------------------------------
					|			Map Reduce
					----------------------------------------
									|
					----------------------------------------
					|			HDFS
					----------------------------------------




---------------------------
-- Data Types
---------------------------
	--1.Primitive Types
		--Integers
			TINYINT—1 byte integer (2^0
			SMALLINT—2 byte integer (2^1)
			INT—4 byte integer (2^2)
			BIGINT—8 byte integer (2^3)
			
		--Floating point numbers
			FLOAT—single precision
			DOUBLE—Double precision
			DECIMAL—a fixed point value of user defined scale and precision
			
		--Boolean type
			BOOLEAN—TRUE/FALSE
	
		--String types
			STRING—sequence of characters in a specified character set
			VARCHAR—sequence of characters in a specified character set with a maximum length
			CHAR—sequence of characters in a specified character set with a defined length
			
		--Date and time types
			TIMESTAMP — A date and time without a timezone ("LocalDateTime" semantics)
			TIMESTAMP WITH LOCAL TIME ZONE — A point in time measured down to nanoseconds ("Instant" semantics)
			DATE—a date
			
		--Binary types
			BINARY—a sequence of bytes
	
	
	--2. Complex or collection types
		array - collection of same type of data
			e.g, array(12,3,4) -- select col[0] from table
			
		map	- key value pairs
			map('k1',1,'k2',2) -- select col.a from table
			
		struct - collection of diff types of data
			  ('a',1,1.22)
		
		union - 



	--3. Data type conversion
		CAST('100' as INT)
	
--------------------------------
-- Hive Basic commands
--------------------------------		

	--To check what is present in the HDFS, 
	hadoop fs – ls
	--To create a directory in the current path (let’s say the name is ‘foo’),
	hadoop fs - mkdir foo


	-- hive version
	hive --version

	--To get started with the hive shell, 
	hive
	--To come out of the hive shell, 
	quit;
	
	
	hive> -- all commands will be run into hive shell

	-- available functions in hive
	show functions;
------------------------------
-- Database 	
------------------------------
	-- create database in hive shell
		create database emp_db;  -- by default db file stores at : hadoop fs -ls /user/hive/warehouse/emp_db.db

	-- create database at desired location
		create database emp_db location '/user/cloudera/myhivedata';
	
	-- available databases
		show databases;

		SHOW DATABASES LIKE 'my.*';
	
	-- use database
		use emp_db;
	
	-- drop database along with table	
		drop database emp cascade; -- cascade drops tables as well

	--change location of database
		ALTER DATABASE myhivebook SET LOCATION '/tmp/data/myhivebook';
	
	
------------------------------
-- Tables
------------------------------	
	-- check tables in database
		show tables;  -- show all tables in database
		SHOW TABLES '*sam*'; -- Show tables name contains "sam"
		SHOW TABLES '*sam|lily*'; -- Show tables name contains "sam" or
	

	-- create Internal table in database
		create table [if not exists] emp
		(id int,name string,city string,continent string)
		row format delimited
		fields terminated by ','
		stored as textfile ; -- stored as ORC
	
	-- drop table 
		drop table emp ;
	
	-- see structure of table
		describe emp;
		describe formatted emp; --formatted can be used to see metadata like managed or external table etc

	-- create DDL statement of tables
		SHOW CREATE TABLE emp;

	--Show table properties for the specified table:
		SHOW TBLPROPERTIES emp;
		
	--load data from local file system into the hive table,
		--LOAD DATA [LOCAL] INPATH 'filepath' [OVERWRITE] INTO TABLE tablename [PARTITION (partcol1=val1, partcol2=val2 ...)];
		load data local inpath 'employee.txt' into table emp;

		LOAD DATA INPATH '/tmp/hivedemo/data/employee.txt' OVERWRITE INTO TABLE employee;
		
	-- Query table
		select * from emp  ;		
		
	-- By default, data gets stored at below locations
		hadoop fs -ls /user/hive/warehouse/emp_db.db  -- database file
		hadoop fs -ls /user/hive/warehouse/emp_db.db/ -- will have all the tables
		hadoop fs -cat /user/hive/warehouse/emp_db.db/emp/employee.txt -- data loaded from local file system is stored here.
		


-------------------------------------
-- Simple DDL operations
-------------------------------------
	-- truncate table

	-- drop table

	-- rename table
	alter table temp_old rename to temp_new ;
	
	-- rename column
	alter table auto_details change fuel fuel_type string ;
	
	-- add column
	alter table auto_details add columns (milage double) ;
	
	-- drop columns (mention columns which need to remain inside the brackets after “replace” keyword) 
	alter table auto_details replace (company string, model string, fuel_type string) ;

-----------------------------
--External tables in hive
-----------------------------

	--copy a file from local file system to hdfs location (hdfs file system)
	hadoop fs  – put empglobal.csv empdata
	
	--see the contents of the file
	hadoop df – cat empdata/empglobal.csv
	
	
	Create external table table_name (id int,myfields string)
	location ‘/user/cloudera/myhivedata’;

---------------------------------	
-- Loading different file formats
---------------------------------

-- know the type of table internal or external
	describe extended emp;

-- To load the data into orc table,
	insert into table emp_global_orc select * from emp_global ;

--Create a table whose schema is exactly like an existing table,
	create table emp_global_seq LIKE emp_global_orc stored as sequencefile ;




-----------------------------------
-- Advanced features
-----------------------------------
1. Explode() -- converts array type into separate rows

		e.g, 
		--Table:
		col1    col2 
		A		[1,2,3]
		B		[4,5,6]


		select explode(col2) from t;
		--o/p:
			1
			2
			3
			4
			5
			6



2.	Lateral View - if we use other column with explode , then it will throw error. In that case we use Lateral view.

		-- Table:
			col1    col2 
			A		[1,2,3]
			B		[4,5,6]

		-- Lateral view create one virtaul table ( explode o/p)
				1
				2
				3
				4
				5
				6

		-- final o/p
			A	1
			A	2
			A	3
			B	4
			B	5
			B	6

		select col1,sep_col2 from t
		LATERAL VIEW explode(col2) vir_table AS sep_col2



		-- for multiple array columns
			SELECT myCol1, myCol2 FROM baseTable
			LATERAL VIEW explode(col1) myTable1 AS myCol1
			LATERAL VIEW explode(col2) myTable2 AS myCol2;


3. Variables in Hive
	- set variable and use its value in query

		e.g.,
		hive > set year=2020
		hive > set year ---> year = 2020
		-- how to use variable in query
		hive > select * from t where dt = ${hiveconf:year} -- in a same way we can use table name as well


-----------------------------------
-- Query Operations on Hive tables
-----------------------------------
	
	-- all columns
	select * from empdata where department = “HR”  ;
	select * from empdata where department = “HR”  limit 10;
	select distinct city from empdata where department = “HR”  ;
	
	-- particular columns
	select empname, age from empdata where department =”HR” and salary > 25000 ;
	
	-- distinct , case ,inline view/query, with clause

	-- sort data
	select * from empdata order by salary ;
	select * from empdata order by salary desc ;
	
	-- no. of rows in table
	select count(*) from empdata ;
	
	-- null values
	select * from empdata where salary is null ;
	
	-- aggragation
	select department, count(*) from empdata group by department ;
	select department, avg(salary) from empdata group by department;
	
	-- pattern matching
	select * from empdata where designation like “%Manager%”
	select * from empdata where designation rlike “Manager” or rlike “manager” or “Lead” ;  --rlike regular expressionlike
	
	-- joins
	--enable join operations in the hive shell
	SET hive.auto.convert.join = False;
	
	--To perform a INNER join operation
	select emp.empname, emp.salary 
	from emp_epf pf join empdata emp 
	on (pf.empid = emp.empid) ;
	
	--To perform a LEFT outer join operation
	select emp.empname, emp.salary from emp_epf pf left outer join empdata emp on (pf.empid = emp.empid) ;
	
	--To perform a RIGHT outer join operation
	select emp.empname, emp.salary from emp_epf pf right outer join empdata emp on (pf.empid = emp.empid) ;
	
	--To perform a FULL outer join operation
	select emp.empname, emp.salary from emp_epf pf full outer join empdata emp on (pf.empid = emp.empid) ;
	--*** SPECIAL JOINS

	-- windowing functions
		-- syntax same as SQL, rank,dense_Rank, row_number, lead/lag, first_value,last_value
	
	-- set opearations,
		union,unionall,intersect,minus (works similar to SQL)
		
	-- supports subquery as well

------------------------------
-- Views
------------------------------
	--create view
	create view if not exists high_sal 
	as
	select * from empdata where salary > 50000 ;
	
	--query view
	select * from high_sal ;
	
	-- see views
	show tables ;
	
	--see the table type, (virtual or Managed),
	describe formatted high_sal ;


-----------------------------------
-- Partitions
-----------------------------------
- Partition divides table into small segments, to improve performance.
- Each partition will have separate directory/file
- Only Suitable for low cardinality columns like - year,department. If we create partition on ID, timestamp column that will results in million partitions
  and will impact again performance. In that case (high cardinality) buckets are preferred, e.g bucket1 - ID [1-100], bucket 2 - ID[101-200] etc.

	create table emp_part (id int, name string, city string)
	partitined by (country string) -- this column doesnt need to be specified above, it will be included implicitly
	row format delimited
	fields terminated by ','
	stored as textfile ;



-- Multiple partitions
	CREATE TABLE partitioned_user(
        firstname VARCHAR(64),
        lastname  VARCHAR(64),
        address   STRING,
        city 	  VARCHAR(64),
        post      STRING,
        )
    PARTITIONED BY (country VARCHAR(64), state VARCHAR(64))
    STORED AS SEQUENCEFILE;


-- check partitions
	SHOW PARTITIONS partitioned_user;

-- INSERT DATA INTO PARTITIONS CAN BE DONE IN 2 WAYS :
	1. STATIC PARTITIONING   :
		- when we have LIMITED  set of partition values (like departments or state names etc), use static partitioning. 
		- Static partitioning is FASTER for loading data as partition values are mentioned in query and only limited partitions get created acc to values.
	
		LOAD DATA LOCAL INPATH '${env:HOME}/staticinput.txt'
      	INTO TABLE partitioned_user
      	PARTITION (country = 'US', state = 'CA'); --This will create separate directory under the default warehouse directory in HDFS.
		  										  --/user/hive/warehouse/partitioned_user/country=US/state=CA/

		
		ALTER TABLE partitioned_user ADD PARTITION (country = 'US', state = 'CA')
    	LOCATION '/hive/external/tables/user/country=us/state=ca'


	2. DYNAMIC PARTITIONING	:
		- No need to mention parttion keys value .Suitable for multiple values in which multiple partitions expected.
		- Slower than Static partitions as partitions are automatically decided.
		- to use dynamic partitioning , below parameter needs to be set as by default HIVE doesnt allows  dynamic partioning
			set hive.exec.dynamic.partition=true;
			set hive.exec.dynamic.partition.mode=nonstrict;
			set hive.exec.max.dynamic.partitions=1000;
			set hive.exec.max.dynamic.partitions.pernode=1000;

		LOAD DATA LOCAL INPATH '${env:HOME}/staticinput.txt'
      	INTO TABLE partitioned_user;


-- check add/remove partitions


-----------------------------------
-- Bucketting
-----------------------------------
- Divides tables into smaller segments similar to partitions
- Suitable for high cardinality columns.


	set hive.enforce.bucketing = true;

	CREATE TABLE user_info_bucketed(user_id BIGINT, firstname STRING, lastname STRING)
	COMMENT 'A bucketed copy of user_info'
	PARTITIONED BY(ds STRING)
	CLUSTERED BY(user_id) INTO 256 BUCKETS;

	set hive.enforce.bucketing = true;  -- (Note: Not needed in Hive 2.x onwards)
	FROM user_id
	INSERT OVERWRITE TABLE user_info_bucketed
	PARTITION (ds='2009-02-25')
	SELECT userid, firstname, lastname WHERE ds='2009-02-25';


------------------------------------------
-- Create HIVE tables
------------------------------------------
-- Load file and skip first 3 lines ( top 3 lines contains file information)
	create table emp ( id int, name varchar)  -- check varchar is allowed or not
	row format delimited
	fields terminated by ','
	stored as textfile
	tblproperties("skip.header.line.count"="3");


--Create table only if another table of the same name doesn’t exist and an input multiple values in a single column using an array,
	create table if not exists sibling_data (
	name string, age int, country string, siblings array<string> )
	row format delimited
	fields terminated by ‘ , ‘
	collection items terminated by ‘#’
	lines terminated by ‘\n’
	stored as textfile ;

--create table with multiple inputs of different data type in a single column, 
	create table auto_details(company string, model string, fuel string,
	basic_specs struct<vehicle_type : string, doors : int, gears : int>,
	engine_specs struct<cc : int, bhp : double>)
	row format delimited
	fields terminated by ','
	collection items terminated by '#' ;


-- create table with location and parquet format
	create table emp ( id int, name varchar)  
	row format delimited
	fields terminated by ','
	stored as parquet
 	location '/data/in/employee_parquet' ;

-- create a table with structure similar to existing table
   create table emp_replica like emp;

------------------------------------------
-- Load Data into Hive Tables
------------------------------------------

--1) using INSERT
		-- using values
		insert into table emp values (123,'ABC','XXX');

		-- using Select statement
		INSERT INTO TABLE employee SELECT * FROM ctas_employee;


--2) using LOAD
	--a) From Local File System to HIVE
		
		--Load local data into table, internal or external. 
		LOAD DATA LOCAL INPATH '/home/dayongd/Downloads/employee_hr.txt' OVERWRITE INTO TABLE employee_hr;

		--Load the local data to a partition:
		LOAD DATA LOCAL INPATH '/home/dayongd/Downloads/employee_hr.txt' OVERWRITE INTO TABLE employee_partitioned PARTITION (year=2018, month=12);


-- b) From Hadoop File System to HIVE

		--Load data from HDFS to a table using the URI:
		LOAD DATA INPATH '/tmp/hivedemo/data/employee.txt' INTO TABLE employee; -- Without OVERWRITE, it appends data

		-- Use full URI
		LOAD DATA INPATH 'hdfs://localhost:9000/tmp/hivedemo/data/employee.txt' OVERWRITE INTO TABLE employee;

--3) using HDFS
		hdfs dfs - put /localpath/emp.csv /user/hive/warehouse/emp


-- Export import data???


-- TRANSACTIONS **
	Limitations of HIVE Transactions :
		- all transactions in HQL are auto-committed without supporting BEGIN, COMMIT, and ROLLBACK, like as with relational databases. 
		- Tables needs to be bucketted and must has ORC file format
		- configuration parameters must be set appropriately in hive-site.xml
				SET hive.support.concurrency = true;
				SET hive.enforce.bucketing = true;
				SET hive.exec.dynamic.partition.mode = nonstrict;
				SET hive.txn.manager = org.apache.hadoop.hive.ql.lockmgr.DbTxnManager;
				SET hive.compactor.initiator.on = true;
				SET hive.compactor.worker.threads = 1;



	--INSERT 
	CREATE TABLE employee_trans (
								emp_id int,
								name string,
								start_date date,
								quit_date date,
								quit_flag string
								)
				CLUSTERED BY (emp_id) INTO 2 BUCKETS STORED as ORC
				TBLPROPERTIES ('transactional'='true'); -- Also need to set this

 	INSERT INTO TABLE employee_trans VALUES
										(100, 'Michael', '2017-02-01', null, 'N'),
										(101, 'Will', '2017-03-01', null, 'N'),
										(102, 'Steven', '2018-01-01', null, 'N'),
										(104, 'Lucy', '2017-10-01', null, 'N');


	-- UPDATE ,DELETE ,MERGE WORKS AS NORMAL


-- LOCKS 
	-- like RDMS , hive also accures lock for ACID properties
	
	SHOW LOCKS;






--*** Have a look at complex type tables, create, insert and select data


--employee.txt:
$ vi /home/hadoop/employee.txt
Michael|Montreal,Toronto|Male,30|DB:80|Product:Developer^DLead
Will|Montreal|Male,35|Perl:85|Product:Lead,Test:Lead
Shelley|New York|Female,27|Python:80|Test:Lead,COE:Architect
Lucy|Vancouver|Female,57|Sales:89,HR:94|Sales:Lead


-- Create an internal table and load the data:
> CREATE TABLE IF NOT EXISTS employee_internal (
> name STRING COMMENT 'this is optinal column comments',
> work_place ARRAY<STRING>,-- table column names are NOT case
sensitive
> gender_age STRUCT<gender:STRING,age:INT>,
> skills_score MAP<STRING,INT>, -- columns names are lower case
> depart_title MAP<STRING,ARRAY<STRING>>-- No "," for the last
column
> )





------------------------------------------------------------
-- Hive Performance
------------------------------------------------------------
1. Performance Utilities
	-- Explain plan
		Explain [FORMATTED | EXTENDED | DEPENDENCY]  <HQL_QUERY>;

		EXPLAIN 
		SELECT gender_age.gender, count(*)
		FROM employee_partitioned WHERE year=2018
		GROUP BY gender_age.gender LIMIT 2;

		-- Explain plan can also be checked in Ambari UI

	-- Analyze stats
		ANALYZE TABLE employee COMPUTE STATISTICS;


2. Design optimisation
	-- correct partition and Bucket
	-- correct index usuage  (same as SQL)
		-- speed up retrieval operations
		-- 2 types of indexes in HIVE:
			1. Bitmap - for low cardinality
			2. Compact

			hive.optimize.index.filter = True -- will enable to use index in queries

			create emp_idx on emp(id) as 'compact' -- or 'bitmap'
			with deferred rebuild; -- clause used in rebuilding index

			alter index emp_id on emp rebuild;

			show formatted index on emp;

3. Data optimisation
	-- in terms of format, compression and storage		
	1. File Formats
		- Hive supports TEXTFILE, SEQUENCEFILE, AVRO, RCFILE, ORC, and PARQUET file formats
		- format is defined while creating table


		a. TEXTFILE (default file format for table creation)  -- plain file or CSV
			- simple file and can easily split into multiple for parallel processing
			
		b. SEQUENCEFILE
			- binary storage format for key/value pairs. The benefit of a sequence file is that it is more compact than a text file 
			and fits well with the MapReduce output format.

		c. AVRO
			- Row based file format
			- schema of data can be defined in JSON format
			- More than that, it is also a serialization and deserialization framework.
		
		d. PARQUET
			- column based file format --( more efficient in reading)

		e. RCFILE --(Record Columnar File)

		f. ORC --(Optimized Row Columnar)




