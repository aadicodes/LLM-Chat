# Setup your development environment in few steps
Note: My Laptop is a Apple Macbook with Apple Silicon (M2) with 8 GB RAM and Sequoia 15.6
## Install Software
1. Python V3.12.7
2. Install Python packages and SQLite db
   ```
   pip install transformers langchain sqlalchemy accelerate
   ```
3. Check SQLite install using below command
   ```
   sqlite3 --version
   ```

## Setup Test data
1. Open SQLite DB from commandline. Open a Terminal window and execute below command.
```
   sqlite3 enterprise_data.db
```
2. Create Table and Insert test data using commands from TestData.txt
3. Exit Database 
```
   .exit
```
