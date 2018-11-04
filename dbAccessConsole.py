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



def main():
  uID, pasw = userAuthentication()
  establishconnection(uID, pasw)
  quitFlag = False
  while (not quitFlag):
    option = menuPrompt()
    if   (option == 'a'):
      print("Option a")
    elif (option == 'b'):
      print("Option b")
    elif (option == 'c'):
      print("Option c")
    elif (option == 'q'):
      quitFlag = True
    else:
      print("Invalid Option: ", option, "Please choose agian ")

#Run main()
main() 
