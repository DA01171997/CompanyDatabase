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
#Return false if can't connect
#return connection if connected
def establishconnection(uID, pasw):
  try:
    cnx = connection.MySQLConnection(user = uID, password = pasw, host='127.0.0.1', database='company')
    return cnx
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
      return False
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
      return False
    else:
      print(err)
      return False
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
  cursor = cnx.cursor()
  supervisorLname = input("Please enter supervisor last name: ")
  semiRecursiveSupervisorHierarchy(cursor, supervisorLname, None)
  cursor.close()

#Recursively print supervisor's supervisees and 
#any supervisees under his hierarchy 
def semiRecursiveSupervisorHierarchy(cursor, supervisorLname, Ssn = None):
 
  #***Base case query if provided with Ssn***
  if Ssn is not None:
    query1 = ("SELECT E.Fname, E.Lname, E.Ssn " \
              "FROM EMPLOYEE AS E " \
              "WHERE E.Ssn = '%s'" % Ssn)
  #***Recursive case query if provided with Lname***
  else:
    query1 = ("SELECT E.Fname, E.Lname, E.Ssn " \
              "FROM EMPLOYEE AS E " \
              "WHERE E.Lname = '%s'" % supervisorLname)
  cursor.execute(query1)
  row1s = cursor.fetchall()
  row1sCount = len(row1s)
  
  #Supervisor doesn't exist
  if (row1sCount == 0):
    print("EMPLOYEE %s DOES NOT EXISTS" % supervisorLname)
  
  #Multiple supervisors with same last name
  elif (row1sCount > 1):
    print("Multiple supervisor with last name", supervisorLname)
    for (Fname, Lname, Ssn) in row1s:
      print( "{}\t{}\t{}\t".format(Fname, Lname, Ssn,))
    selectedSsn = input("Select Ssn from list: ")
    semiRecursiveSupervisorHierarchy(cursor, Lname, selectedSsn)  
  
  #Fetch supervisee if no 
  #supervisor with same last name
  elif (row1sCount == 1):
    row2s = queryForAllSupervisees(cursor, supervisorLname, Ssn)
    rows2Count = len(row2s) 
    if rows2Count is 0:
      print(supervisorLname," has no supervisees")
    else:
      #print all supervisees
      printAllSupervisees(row2s, supervisorLname)
      #print all supervisees's supervisees
      print("")
      print("\t '%s' SUPERVISEES'S SUPERVISEES HIERARCHY" % supervisorLname)
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
  print("\t\t%s'S SUPERVISEES  " % supervisorLname)
  print("{:10s}\t{}\t\t{} ".format("Fname", "Lname", "Ssn"))
  print("--------------------------------------------------------")
  for (Fname, Lname, Ssn) in rows:
    print("{:10s}\t{}\t\t{} ".format(Fname, Lname, Ssn))
  print("--------------------------------------------------------")

#Print top five highest paid workers
def optionB(cnx):
  cursor = cnx.cursor()
  query = ("SELECT E.Fname, E.Lname, E.Ssn, E.Salary " \
            "FROM EMPLOYEE AS E " \
            "ORDER BY E.Salary DESC")
  cursor.execute(query)
  rows = cursor.fetchall()
  counter = 0
  print("\t\t FIVE HIGHEST PAID WORKERS")
  print ("{:10s}{:10s}{:10s}\t{}".format("Fname", "Lname", "Ssn", "Salary"))
  print("--------------------------------------------------------")
  for (Fname, Lname, Ssn, Salary) in rows:
    if(counter>=5):
      break
    print ("{:10s}{:10s}{:10s}\t{}".format(Fname, Lname, Ssn, Salary))
    counter+=1
  print("--------------------------------------------------------")
  cursor.close()

#Print top five most worked workers
def optionC(cnx):
  cursor = cnx.cursor()
  query = ("SELECT E.Fname, E.Lname, E.SSn, W.hours, P.Pname " \
           "FROM EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P " \
           "WHERE E.Ssn = W.Essn AND P.Pnumber = W.Pno "
           "ORDER BY W.Hours DESC")
  counter = 0
  cursor.execute(query)
  rows = cursor.fetchall()
  print("\t\t FIVE MOST WORKED WORKERS")
  print("{:10s}{:10s}{:10s}\t{}\t{}".format("Fname","Lname", "Ssn", "Hours", "Pname"))
  print("--------------------------------------------------------")
  for (Fname, Lname, Ssn, Hours, Pname) in rows:
    if(counter>=5):
      break
    print("{:10s}{:10s}{:10s}\t{}\t{}".format(Fname, Lname, Ssn, Hours, Pname))
    counter+=1
  print("--------------------------------------------------------")
  cursor.close()

def main():
  #Authentication
  uID, pasw = userAuthentication()
  cnx = establishconnection(uID, pasw)
  if cnx is not False:
    quitFlag = False
    #Menu
    while (not quitFlag):
      option = menuPrompt()
      if (option == 'a'):
        optionA(cnx)
      elif (option == 'b'):
        optionB(cnx)
      elif (option == 'c'):
        optionC(cnx)
      elif (option == 'q'):
        quitFlag = True
      else:
        print("Invalid Option: ", option, "Please choose again ")
    cnx.close()

#Run main()
main() 
