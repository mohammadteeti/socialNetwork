# socialNetwork
Simple Social Web App Build in Django

a simple implementation of few features found in a social netwok web application.


  # Features: 
 
  * __User Registraion (Adding New Users to the System)__
    * a registration form is provided ,the user can fill registration data [username,email,password ... etc]
    
   * __Password Management__
     * user can Reset or change his password through corrosponding forms designed for that purpose.
     * Reset Link is sent on console as fake email using django fake backend email 
  
  * __Follow/Follow Back__
    * Allows user to view other profiles and choose which to follow ,user can also unfollow other profiles
  
  * __Update User Status__
     * User can post a __Dweet__ to express his thoughts , User can see other friends dweets on dashboard
    
  * __Sqlite3 and MySQL database__
    * __Sqlite3__  is the Default DataBase manager , You can switch to __MYSQL__ as follows:
      
      ### On Linux:
         Before Running server use `export DJANGO_DATABASE="mysqlDB"`,then run server `python manage.py runserver`
      
      ### On Windows:
         Before Running server use  ` set DJANGO_DATABASE="mysqlDB" `  to add mysqlDB to  classpath 
         
         you will need to create a new Mysql database and name it __dwitter__ for this example ,with the user name and password shown below 
         ``` pyhton
                DATABASES = {
                            'default': {
                            'ENGINE': 'django.db.backends.sqlite3',
                            'NAME': BASE_DIR / 'db.sqlite3',
                            }
                            ,
                            'mysqlDB':{
                            'ENGINE': 'django.db.backends.mysql',
                            'NAME': 'dwitter',
                            'HOST':'127.0.0.1',
                            'PORT':'3306',
                            'USER':'root',
                            'PASSWORD':'Mohammad@#$123',
                                }
                            }
                            default_database=environ.get('DJANGO_DATABASE','default')
                            DATABASES['default'] = DATABASES[default_database]

         ```
         Note that the database should be created and __migrations__ must be made to create all tables before exporting the environment variable 
   # Video:


https://user-images.githubusercontent.com/37085987/209462894-ea5c534a-e230-48a4-a3f8-b9508ec2c01c.mp4




       


