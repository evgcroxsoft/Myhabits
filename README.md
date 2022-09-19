# **MyHabits**

## **About project**

### **An app that helps kids build habits and complete time-limited tasks**

## **Tech:** 
### Flask, PosgreSQL, SQLAlchemy, Jinja2, HTML, Bootstrap, TelegramBot, Email, Flask login manager, Hesh werkzeug.

## **Description**:
All registered users (Register table) can create their own
Habit (Habit table) or choose from existing Habits. Delete,
a habit can be edited by the user, only the one who created it.
After successfully creating or selecting an existing habit, you can create already your Task (table Task) in which to specify the start date, the period from 14-30 days and days of the week, the number of lives is also possible, the default is 3.
Editing and deleting tasks can also be done by the user.
In the profile, the system makes a selection and analysis of which tasks should be shown based on the day, period, day of the week, number of lives. After sampling, the application remembers the values ​​and creates entries in the (Statistics table)
You can make different selections by different criteria, including selections by statuses in progress or end life(game over).

## **Experience:**
I got acquainted with Flask, how I forwarded and collected requests through the address bar,
connecting to table via SQLAlchemy, Jinja2 how to display information via
render_template and for authorized users. My first introduction to HTML
structure and bootstrap. Connected TelegramBot and Email. session counter and
tracking the number of user visits to the site. During registration
connected email and password templates, event output in case of errors. Ruthy methods
GET, SEND. Receipt and recording of a dynamic application.form. There was a high level of plugging,
but thank god I figured it out.

## **Views**

![Habits](/media/habits.png)
***
![Profile](/media/profile.png)

![Task](/media/create_%20task.png)