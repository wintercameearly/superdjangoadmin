# Django-Admin Extension
This app adds extra features to the out-of-the-box Django Admin.

Enables admin staff to check user metrics such as registration rate per day, week, shows daily user creation in a cool graph and has features to send broadcast emails to all users

LIVE DEMO : https://nifemiinternshiptest.herokuapp.com
#### Below is an Image of the Change List page with the functionality 
![Entire Page](https://github.com/wintercameearly/superdjangoadmin/blob/master/images/Screenshot%202020-08-25%20at%2023.55.13.png)

DEFAULT credentials username: root , password: password

## Features 

##### 1. Shows user metrics such as new users per week and month.

![User Metrics](https://github.com/wintercameearly/superdjangoadmin/blob/master/images/Screenshot%202020-08-25%20at%2023.55.04.png)

##### 2. Custom Action button to set users to active/inactive.

![Custom Action](https://github.com/wintercameearly/superdjangoadmin/blob/master/images/Screenshot%202020-08-25%20at%2023.54.48.png)

##### 3. Functionality Page to send emails to all users.

![Email Action](https://github.com/wintercameearly/superdjangoadmin/blob/master/images/Screenshot%202020-08-25%20at%2023.55.49.png)

##### 4. Users per day(in a nifty bar chart)

![Bar Chart](https://github.com/wintercameearly/superdjangoadmin/blob/master/images/Screenshot%202020-08-25%20at%2023.54.26.png)



## Installation Instructions
1. Clone the repo
2. run pip install requirements.txt
3. make migrations and migrate using django manage.py makemigrations
4. run the dummy server
5. Navigate to the admin route and login with the default credentials
