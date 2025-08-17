# SQL Commands 
## Create Table
```
CREATE TABLE branch_revenue (
    branch_name TEXT,
    quarter TEXT,
    year INTEGER,
    revenue FLOAT
);
```
## Insert Data
```
INSERT INTO branch_revenue VALUES ('Phoenix', 'Q2', 2025, 4200000.00);
INSERT INTO branch_revenue VALUES ('Austin', 'Q2', 2025, 3800000.00);
INSERT INTO branch_revenue VALUES ('Denver', 'Q2', 2025, 3500000.00);
```
## Check if above data is present in database
``` 
SELECT * FROM branch_revenue;
```