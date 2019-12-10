4-pavan-rahul

NHSEE Judging Scoring

By Team 4

Description:

The purpose of the New Hampshire Science and Engineering Exposition Association (NHSEEA) is the advancement of science education in the State of New Hampshire.

Created a NHSEE web application to display scores and ranks for the students of each projects.

The application shows the students, judges, projects, judge_assignment information.

Source is Excel files, which are located in spreadsheets folder in project.

Installation Guide:

1.Install python virtual environment with Django: pipenv install django==2.2.4 --python=3.7

2.Start virtual environment:pipenv shell

3.Install xlrd to read excel files:pip install xlrd

4.Migrate the database:python manage.py migrate nhsee

5.python manage.py migrate nhsee :python manage.py runserver

6. pipenv install -r requirements.txt

7. installing gunicorn for heroku configuration

   pipenv install gunicorn==20.0.0

8. installing whitenoise for allowing static files

   pipenv install whitenoise

Usage:

Delete logic: initially we have to delete the data in child tables are student and judge assignment tables after that we can delete data from project and judges tables.

Import logic: first we load data into project and judge tables, after loading we can import data into student and judge assignment tables.

Click on student button, we can see the student information like student name,
school name, project id

click on judges, we can see the judges information like judge id and judge name
 and also for each judge we have Details button. If we click on Details button,
 it display the projects information under that judge.

 Click on Judge assignment, we can see the project, judge id  along with raw_scores

 Click on projects, we can see the project id , project description, avg score,
 rank by avg score, scaled z score, z score, sclaed rank, isef score, isef rank.

 the calcultion docuement located in documents folder.

 documents/calculations of NHSEE project.docx

Acknowledgements:

 to know more about python,

https://www.w3schools.com/python/python_lists.asp

to know more about Django,

https://djangobook.com/beginning-django-tutorial-contents/

https://www.guru99.com/django-tutorial.html

Reading the excel file,

xlrd is a library for reading data and formatting information from Excel files, whether they are .xlsm or .xlsx file

https://www.geeksforgeeks.org/reading-excel-file-using-python/

https://xlrd.readthedocs.io/en/latest/

For CSS and html for styling purpose,

https://www.w3schools.com/tags/att_script_src.asp

https://www.w3schools.com/css/

https://www.w3schools.com/html/

To know more about git branching and merging,

https://www.atlassian.com/git/tutorials/using-branches

For Heroku deployment and also deployment document placed in documents folder in project.

https://devcenter.heroku.com/articles/django-assets

https://www.codementor.io/jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4


Project Status,

Overall completion of project status is 95 %

Tasks which are Completed:

    Django installation
    Nhsee project and app creation
    Data models creations with code refactoring
    Making migrations
    Creation of urls.py file for all objects includes home as well
    Creation of views for project, judges, student and judge assignment
    creation of HTMl files for project, judges, student and judge assignment
    Creation of calculation document in document folder
    Creation of calculations for project in project_views.py file
    Creation of snapshots folder and added snapshots of each page
    updated README.md and resources.md file
    added source files in Spreadsheets folder
    Updated project artifacts
    Individual Project document
    Heroku deployment
    Heroku deployment document preparation

Tasks are in progress,

    Test cases for application

Tasks which are not started,

None




Authors

Pavan Kumar Dondapati -- Team Lead (https://www.linkedin.com/in/pavan-kumar-dondapati-6a3591193/)

Phani Rahul Battula (LinkedIn Profile Link)
