createCompanyDb mysql - script that creates company database
insertDataCompanyDb mysql - script that  populates company tables

dbAccessConsole - python program that presents user with a menu of 3 choices:

(a) Find supervisees at all levels: In this option, the user is prompted for the last
name of an employee. If there are several employees with the same last name,
the user is presented with a list of social security numbers of employees with the
same last name and asked to choose one. The program then proceeds to list all
the supervisees of the employee and all levels below him or her in the employee
hierarchy.
(b) Find the top 5 highest paid employees: In this option, the program finds five
employees who rank in the top 5 in salary and lists them.
(c) Find the top 5 highest worked employees: In this option, the program finds five
employees who rank in the top 5 in number of hours worked and lists them.

Example:

Enter userid: user1
Enter password: user1
QUERY OPTIONS
(a) Find Supervisees at all levels.
(b) Find Highest paid workers.
(c) Find the most worked workers.
(q) Quit.
Type in your option: a
Enter last name of employee : King
King, Kate 666666602 
King, Billie 666666604
King, Ray 666666606
Select ssn from list : 666666602
SUPERVISEES

FNAME LNAME SSN

----------------------------------------

Gerald Small 666666607
Arnold Head 666666608
Helga Pataki 666666609
Naveen Drew 666666610
Carl Reedy 666666611
Sammy Hall 666666612
Red Bacher 666666613
QUERY OPTIONS
(a) Find Supervisees at all levels.
(b) Find Highest paid workers.
(c) Find the most worked workers.
(q) Quit.
Type in your option:
