# FitBitLit
This is a  project named FitBitLit.  I teach dance exercise classes and  I would like to have better organization for my music collection, student dance preferences,  and contact information.  Although those are my ultimate goals,  I had to limit my class project due to time constraints and specific class requirenments.  I plan on expanding it later after the course ends.  
I used Window and SQL Express.   To run my project your must do the following: Go to github.com/deartc/DanceMusic.  Clone the repository.  Open in a Sql compatabile program (  I only tested with SQL Express).  


I satsified the requirements by doing the following:

   The following are included in  the git hub section  called DDL tables to clarify I completed the table requirements.  I  created a relational database schema with a minimum of 3 tables and created DDL (Data Definition Language) for tables and views. At least 2 of the tables  contain 4 or more columns. Two of the tables  have a many-to-many relationship.  Two of the tables  have a one-to-many relationship.The following data types are present somewhere in the table definitions: DATETIME, INT, VARCHAR
Each table is related to one or more of the other tables via a primary key/foreign key relationship.

The following are included in the git hub section called Insertion to clarify I completed the requirementsL
 I created DML (Data Manipulation Language) to load the tables with sample data.
I populated these tables with data by manually inserting data, or using some sort of import tool.  I have included input script. 

The following are included inthe git hub section called Stored Produres to clafiy I completed the requriements. 
I Created and called at least 4 stored procedures to expose CRUD (Create, Read, Update, and Delete) functionality.

I included a separate section of my git hub to clarify I completed features from all 3 group
Chose at least 1 item from each group on the Features List below and implemented them in my stored procedures or DDL script:


Group 1 Used: Reading Data from a Database
Write a  SELECT query that utilizes a JOIN.



Group 1  not used:
Write a  SELECT query that utilizes a JOIN with 3 or more tables.
Write a  SELECT query that utilizes a LEFT JOIN.
Write a  SELECT query that utilizes a variable in the WHERE clause.
Write a  SELECT query that utilizes an ORDER BY clause.
Write a  SELECT query that utilizes a GROUP BY clause along with an aggregate function.
Write a SELECT query that utilizes a CALCULATED FIELD.
Write a SELECT query that utilizes a SUBQUERY.
Write a SELECT query that utilizes a JOIN, at least 2 OPERATORS (AND, OR, =, IN, BETWEEN, ETC) AND A GROUP BY clause with an aggregate function.
Write a SELECT query that utilizes a JOIN with 3 or more tables, at 2 OPERATORS (AND, OR, =, IN, BETWEEN, ETC), a GROUP BY clause with an aggregate function, and a HAVING clause.
Write a SELECT query that uses a WHERE clause.
Write a  SELECT query that uses an OR and an AND operator.
Write a  SELECT query that filters NULL rows using IS NOT NULL.







Group 2: Updating / Deleting Data from a Database  I used the following one to satisfy requiremnts:

  I used the write a DML statement that UPDATEs a set of rows with a WHERE clause. The values used in the WHERE clause should be a variable.


UPDATE album
SET country = 'USA'
WHERE country= 'Great Britain';


I did not use these group 2 features:
Write a a DML statement that DELETEs a set of rows with a WHERE clause. The values used in the WHERE clause should be a variable.
Write a DML statement that DELETEs rows from a table that another table references. This script will have to also DELETE any records that reference these rows. Both of the DELETE statements need to be wrapped in a single TRANSACTION.


Group 3: Optimizing a Database

I included the following third feature:   Design a NONCLUSTERED INDEX with ONE KEY COLUMN that improves the performance of one of the above queries.

UPDATE music AS m
SET albumID = (SELECT albumID FROM albumList AS a WHERE m.songalbum = a.album) 
WHERE albumID IS NULL
  AND EXISTS (SELECT 1 FROM albumList AS a WHERE m.songalbum = a.album) ; 



I did not include the folowing third features:
Design a NONCLUSTERED INDEX with TWO KEY COLUMNS that improves the performance of one of the above queries.
Design a NONCLUSTERED INDEX with AT LEAST ONE KEY COLUMN and AT LEAST ONE INCLUDED COLUMN that improves the performance of one of the above queries.


Correct use of Git/Github and commits: I followed the correct steps in the project guidelines to create and name the github repository that would reflect a distinct repository. I then used the proper guidelines to initialize the project and add files using git bash and the command line. I then far exceeded the minimum number of commits needed to pass.

I also named my file a distinct name describing my project of DanceMusic




