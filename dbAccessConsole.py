#progress:
#menu is done
#query is not done

import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode

#Authenticate user access to database
def userAuthentication():
  userID = input("Enter UserID: ")
  pasw = input("Enter Password: ")
  return userID, pasw

#Connect to database
def establishconnection(uID, pasw):
  try:
    cnx = connection.MySQLConnection(user = uID, password = pasw, host='127.0.0.1', database='company')
    return cnx
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cnx.close()

#Display option menu
def menuPrompt():
  print("(a) Find Supervisees at all levels. ")
  print("(b) Find highest paid workers.")
  print("(c) Find the most worked workers.")
  print("(q) Quit. ")
  option = input("Type in your option: ")
  return option

#Query then return superviseefor supervisor
def queryForAllSupervisees(cursor, supervisorLname):
  query2 = ("SELECT E.Fname, E.Lname, E.Ssn "  \
              "FROM EMPLOYEE AS E, EMPLOYEE AS S "  \
              "WHERE E.Super_ssn = S.Ssn AND S.Lname = '%s'" % supervisorLname)
  cursor.execute(query2)
  rows = cursor.fetchall()
  return rows

#Print all supervisees Fname Lname Ssn 
def printAllSupervisees(rows,supervisorLname):
  sLname = supervisorLname.upper()
  print("FNAME\t\tLNAME\tSSN OF ALL %s'S SUPERVISEE  " % sLname)
  print("--------------------------------------------------------")
  for (Fname, Lname, Ssn) in rows:
    print("{}\t{}\t{} ".format( Fname, Lname, Ssn))
  print("--------------------------------------------------------")

#Option A 
def optionA(cnx):
  print("Option a")
  cursor = cnx.cursor()

  #Get supervisor last name
  supervisorLname = input("Please enter supervisor last name: ")
  query1 = ("SELECT COUNT(E.Fname) " \
            "FROM EMPLOYEE AS E " \
            "WHERE E.Lname = '%s'" % supervisorLname)
  cursor.execute(query1)
  row = cursor.fetchone()

  #Fetch supervisee if no 
  #supervisor with same last name
  if row[0] is 1:
    
    #print all supervisees
    rows = queryForAllSupervisees(cursor, supervisorLname)
    sLname = supervisorLname.upper()
    printAllSupervisees(rows,supervisorLname)
    print()
    print("\tPRINT SUPERVISEES OF %s'S SUPERVISEES" % sLname)
    print()
    
    #print all supervisees's supervisees
    for (_, Lname,_) in rows:
      rows2 = queryForAllSupervisees(cursor, Lname)
      printAllSupervisees(rows2, Lname)
  #else:
    
  cursor.close()



def main():
  uID, pasw = userAuthentication()
  cnx = establishconnection(uID, pasw)
  quitFlag = False
  while (not quitFlag):
    option = menuPrompt()
    if   (option == 'a'):
      optionA(cnx)
    elif (option == 'b'):
      print("Option b")
    elif (option == 'c'):
      print("Option c")
    elif (option == 'q'):
      quitFlag = True
    else:
      print("Invalid Option: ", option, "Please choose again ")
  cnx.close()

#Run main()
main() 
