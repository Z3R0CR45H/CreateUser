import os
import win32security
import win32net
import win32netcon
import ntsecuritycon as con
from pyad import aduser,adcontainer

tGHou = "OU=Teachers,OU=Goose Hill,OU=Instruct OU,DC=CSH,DC=K12"
tLHou = "OU=Teachers,OU=Lloyd Harbor,OU=Instruct OU,DC=CSH,DC=K12"
tWSou = "OU=Teachers,OU=West Side,OU=Instruct OU,DC=CSH,DC=K12"
tHSou = "OU=Teachers,OU=High School,OU=Instruct OU,DC=CSH,DC=K12"
print("Cold Spring Harbor Create a User")



print("Please Input User Type: ")
print("A = Admin \n"
      "T = Teacher \n"
      "S = Student")
text = input("Enter User Type: ")  # Python 3

if  text == "S" or text =="s" :
     sFirstName = input("Enter Student First Name: ")
     sLastName = input("Enter Student Last Name: ")
     sUsername = input("Enter Student Username: ") # Stores Student Username
     sPassword = password = input("Enter Student Password: ")  # Store Student Password
     sEmail = input("Enter Student Email Address: ") # Retrieves user input and stores
     sOu = adcontainer.ADContainer.from_dn(input("Enter Student OU: "))  # Stores Student OU
     sPath = input("Enter HomeFolder Path: ") # Stores User Path
     sGradYear = input("Enter Student Graduation Year: ")
     sDrive = "H:"
     sDisplayName = sLastName + ', ' + sFirstName;
     if not os.path.exists(sPath):  # Creates User Folder
         os.makedirs(sPath)

     sUser= aduser.ADUser.create(sUsername,sOu,password = sPassword,upn_suffix="none",enable ="true",optional_attributes= {"mail": sEmail,"givenName":sFirstName,"sn":sLastName,"homeDirectory":sPath,"homeDrive":sDrive, "displayName": sDisplayName})

elif text =="T" or text =="t":
     tFirstName = input("Enter Teacher First Name: ")
     tLastName = input("Enter Teacher Last Name: ")
     tUsername = input("Enter Teacher Username: ")  # Stores Teacher Username
     tPassword = password = input("Enter Teacher Password: ")  # Store Teacher Password
     tEmail = input("Enter Teacher Email Address: ")  # Retrieves user input and stores
     tBuilding = input("Enter Building Location: ")

     if tBuilding == "High School":
          print("Departments:  ")
          tDepartment = input("Enter Department Number:") # Enter Department

     if tBuilding == "Goose Hill" :
          print("Departments: \n")
          tDepartment = input("Enter Department Number:")  # Enter Department

     if tBuilding == "West Side" :
          print("Departments: \n")
          tDepartment = input("Enter Department Number:")  # Enter Department

     if tBuilding == "Lloyd Harbor":
          print("Departments: \n")
          tDepartment = input("Enter Department Number:")  # Enter Department

     tOu = adcontainer.ADContainer.from_dn()  # Stores Teacher OU

     if tBuilding == "High School":
          print("Groups:  \n")
          tDepartment = input("Enter Group Number:") # Enter Department

     if tBuilding == "Goose Hill" :
          print("Groups:  \n")
          tDepartment = input("Enter Groups Number:")  # Enter Department

     if tBuilding == "West Side" :
          print("Groups: \n")
          tDepartment = input("Enter Groups Number:")  # Enter Department

     if tBuilding == "Lloyd Harbor":
          print("Groups: \n")
          tDepartment = input("Enter Groups Number:")  # Enter Department


     tPath = input("Enter HomeFolder Path: ")  # Stores User Path
     tDrive = "H:"
     tDisplayName =  tLastName + ', ' + tFirstName;
     tUser = aduser.ADUser.create(tUsername,tOu, password=tPassword, upn_suffix="none", enable="true",optional_attributes={"mail": tEmail, "givenName": tFirstName, "sn": tLastName,"homeDirectory": tPath, "homeDrive": tDrive, "displayName": tDisplayName })
     if not os.path.exists(tPath):  # Creates User Folder
        os.makedirs(tPath)

elif text == "A" or text =="a":
    aName = input("Enter Admin Name: ")
else:
     print("Invaild Selection")


