#Hack4Missions - Project BeagleBone

## Dependencies:
The following python modules are required. They can be installed with the command `pip install`
```
mysql-connector
tornado
APScheduler
numpy 
```
The following programs are required:
* Python 2.7+
* MySQL

## Install Flow

* Install python, mysql, and required modules
* Setup mysql database with tables in SQL_Files
* Edit paramaters.py with mysql database settings
* Run main.py to start the scheduler
* Run GUI.py to start the interface. 

## Using the Interface

Navigate to [http://localhost:8888](http://localhost:8888). 
Enter desired parameters and click submit. 
The scheduled entry should now be in the `schedule` table. 