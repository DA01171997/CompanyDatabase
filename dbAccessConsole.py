#progress:
#menu is done
#part a is done
#part b c are not done

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


#Option A 
def optionA(cnx):
  print("Option a")
  cursor = cnx.cursor()
  supervisorLname = input("Please enter supervisor last name: ")
  RecursiveSupervisorHierarchy(cursor, supervisorLname, None)
  cursor.close()

def RecursiveSupervisorHierarchy(cursor, supervisorLname, Ssn = None):
  #Get supervisor last name
  sLnameUpper = supervisorLname
  sLnameUpper.upper()
  #***Base case if provided with Ssn***
  if Ssn is not None:
    query1 = ("SELECT E.Fname, E.Lname, E.Ssn " \
              "FROM EMPLOYEE AS E " \
              "WHERE E.Ssn = '%s'" % Ssn)
  #***Recursive case if provided with Lname***
  else:
    query1 = ("SELECT E.Fname, E.Lname, E.Ssn " \
              "FROM EMPLOYEE AS E " \
              "WHERE E.Lname = '%s'" % supervisorLname)
  cursor.execute(query1)
  row1s = cursor.fetchall()
  row1sCount = len(row1s)

  #Supervisor doesn't exist
  if (row1sCount == 0):
    print("EMPLOYEE %s DOES NOT EXISTS", sLnameUpper)
  #Multiple supervisor with same Last name
  elif (row1sCount > 1):
    print("Multiple supervisor with last name", supervisorLname)
    for (Fname, Lname, Ssn) in row1s:
      print( "{}\t{}\t{}\t".format(Fname, Lname, Ssn,))
    selectedSsn = input("Select Ssn from list: ")
    RecursiveSupervisorHierarchy(cursor, Lname, selectedSsn)  
  #Fetch supervisee if no 
  #supervisor with same last name
  elif (row1sCount == 1):
    #print all supervisees
    row2s = queryForAllSupervisees(cursor, supervisorLname, Ssn)
    rows2Count = len(row2s) 
    if rows2Count is 0:
      print(supervisorLname," has no supervisees")
    else:
      printAllSupervisees(row2s, supervisorLname)
      #print all supervisees's supervisees
      print("")
      print("\tPRINT %s SUPERVISEES'S SUPERVISEES" % sLnameUpper)
      print("")
      for (_, Lname,Ssn) in row2s:
        rows3 = queryForAllSupervisees(cursor, Lname, Ssn)
        rows3Count=len(rows3)
        if rows3Count is 0:
          print(Lname," has no supervisees")
        else:
          printAllSupervisees(rows3, Lname)
  
#Query then return superviseefor supervisor
def queryForAllSupervisees(cursor, supervisorLname, Ssn):
  if Ssn is None:
    query2 = ("SELECT E.Fname, E.Lname, E.Ssn "  \
                "FROM EMPLOYEE AS E, EMPLOYEE AS S "  \
                "WHERE E.Super_ssn = S.Ssn AND S.Lname = '%s'" % supervisorLname)
  else:
    query2 = ("SELECT E.Fname, E.Lname, E.Ssn "  \
                "FROM EMPLOYEE AS E, EMPLOYEE AS S "  \
                "WHERE E.Super_ssn = S.Ssn AND S.Lname = '%s' AND S.Ssn = '%s'" % (supervisorLname, Ssn))
  cursor.execute(query2)
  rows = cursor.fetchall()
  return rows

#Print all supervisees Fname Lname Ssn 
def printAllSupervisees(rows, supervisorLname):
  sLnameUpper = supervisorLname
  sLnameUpper.upper()
  print("\t\t%s'S SUPERVISEES  " % sLnameUpper)
  print("FNAME\t\tLNAME\t\tSSN")
  print("--------------------------------------------------------")
  for (Fname, Lname, Ssn) in rows:
    print("{}\t\t{}\t\t{} ".format( Fname, Lname, Ssn))
  print("--------------------------------------------------------")





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
