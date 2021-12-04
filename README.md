# reddit
Steps to follow 
1.  Clone repository

2.  Create Virtualenv 
        Commond - virtualenv YOUR_VIRTUAL_ENV_NAME
        
3.  Activate virtual environment
        Commond Prompt- YOUR_VIRTUAL_ENV_NAME\Scripts\activate.bat
        Power Shell- YOUR_VIRTUAL_ENV_NAME\Scripts\activate.ps1
        UNIX/Linux/Mac Terminal- source YOUR_VIRTUAL_ENV_NAME\bin\activate
        
4.  Install dependencies (Supporting Packages)
        Either install individual packages
            Commond (In virtual environment): pip install PACKAGE_NANE
        or install all packages at once from requirements.txt
            Commond (In virtual environment): pip install -r requirements.txt
            NOTE: This commond will install all the supporting packages listed in requirements.txt files
            
5.  Create Super User to access admin panel.
        Commond Prompt (In virtual environment)- python manage.py createsuperuser
        complete the registration of super user by adding username and password.
        
6.  Run Migrations
        1. makemigrations: This commond will detect all the changes throughout the project model files
            Commond Prompt (In virtual environment): python manage.py makemigrations 
        2. migrate : This commond will add new changes to database.
            Commond Prompt (In virtual environment): python manage.py migrate
            
7.  Run Server
        Commond Prompt (In virtual environment): python manage.py runserver 
        
        
        
    
    