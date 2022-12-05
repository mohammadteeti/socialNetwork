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
         
       


