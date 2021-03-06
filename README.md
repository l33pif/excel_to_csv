# excel to csv


You'll need to create a virtual enviroment :
   Create a carpet 
   In Termial go to the carpet and create the venv:
    python3 -m venv env-name
    source env-name/bin/activate
   Then you'll need to install the next libraries:
    pip install pandas
    pip install xlrd
    pip install openpyxl
   run the .py file with the excel file as an argunt
   ex: 
    python convert_ex_to_csv.py 'name_of_xl_file'
   now you should have the csv file in the carpet
    'deactivate' to go out of the venv
