# Job Scraper

## Description: 
The program searches for vacancies for the desired query on the sites djinni.co and stackoverflow.com/jobs and displays on the vacancies page as "Job Title | Company | Location | Link". It is also possible to download the list of vacancies in .csv format.
To run locally, do the usual:

#. Create a Python 3.8 virtualenv

#. Install dependencies::

    sudo pip install flask
    pip install request
    pip install BeautifulSoup4
    
#. Run::

    python ./main.py
     
