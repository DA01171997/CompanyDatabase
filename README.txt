createCompanyDb mysql - script that creates company database
insertDataCompanyDb mysql - script that  populates company tables

dbAccessConsole - python program that presents user with a menu of 3 choices:

(a) Find supervisees at all levels: In this option, the user is prompted for the last
name of an employee. If there are several employees with the same last name,
the user is presented with a list of social security numbers of employees with the
same last name and asked to choose one. The program then proceeds to list all
the supervisees of the employee and all levels below him or her in the employee
hierarchy.
.
(b) Find the top 5 highest paid employees: In this option, the program finds five
employees who rank in the top 5 in salary and lists them.
.
(c) Find the top 5 highest worked employees: In this option, the program finds five
employees who rank in the top 5 in number of hours worked and lists them.

A sample interaction with the user is shown below (console application):

Enter UserID: 
Enter Password: 
(a) Find Supervisees at all levels.
(b) Find highest paid workers.
(c) Find the most worked workers.
(q) Quit.
Type in your option: a
Please enter supervisor last name: Borg
                Borg'S SUPERVISEES
Fname           Lname           Ssn
--------------------------------------------------------
Franklin        Wong            333445555
Jennifer        Wallace         987654321
--------------------------------------------------------

         'Borg' SUPERVISEES'S SUPERVISEES HIERARCHY

                Wong'S SUPERVISEES
Fname           Lname           Ssn
--------------------------------------------------------
John            Smith           123456789
Ramesh          Narayan         666884444
Joyce           English         453453453
Fake            Smith           123463524
--------------------------------------------------------
                Wallace'S SUPERVISEES
Fname           Lname           Ssn
--------------------------------------------------------
Alicia          Zelaya          999887777
Ahmad           Jabbar          987987987
--------------------------------------------------------
(a) Find Supervisees at all levels.
(b) Find highest paid workers.
(c) Find the most worked workers.
(q) Quit.
Type in your option: a
Please enter supervisor last name: Smith
Multiple supervisor with last name Smith
John    Smith   123456789
Fake    Smith   123463524
Select Ssn from list: 123456789
Smith  has no supervisees
(a) Find Supervisees at all levels.
(b) Find highest paid workers.
(c) Find the most worked workers.
(q) Quit.
Type in your option: b
                 FIVE HIGHEST PAID WORKERS
Fname     Lname     Ssn         Salary
--------------------------------------------------------
James     Borg      888665555   55000.00
Jennifer  Wallace   987654321   43000.00
Franklin  Wong      333445555   40000.00
Ramesh    Narayan   666884444   38000.00
John      Smith     123456789   30000.00
--------------------------------------------------------
(a) Find Supervisees at all levels.
(b) Find highest paid workers.
(c) Find the most worked workers.
(q) Quit.
Type in your option: c
                 FIVE MOST WORKED WORKERS
Fname     Lname     Ssn         Hours   Pname
--------------------------------------------------------
Ramesh    Narayan   666884444   40.0    ProductZ
Ahmad     Jabbar    987987987   35.0    Computerization
John      Smith     123456789   32.5    ProductX
Alicia    Zelaya    999887777   30.0    Newbenefits
Joyce     English   453453453   20.0    ProductX
--------------------------------------------------------
(a) Find Supervisees at all levels.
(b) Find highest paid workers.
(c) Find the most worked workers.
(q) Quit.
Type in your option: