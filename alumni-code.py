import mysql.connector
import random
from gtts import gTTS
import os
print("                                                          COMPUTER SCIENCE PROJECT                                                                                     ")
print("                                                          ALUMNI MANAGEMENT SYSTEM                                                                                     ")
print("         Alumni management system enables organizations, typically universities and colleges, to stay in touch with their alumni, engage \n                   them through communications and events, and solicit donations. An alumni management system helps an institution \n                             to ensure that they never lose contact with their alumni's and continue to be engaged \n                                               with them long after they have graduated.\n")
r="Alumni management system enables organizations, typically universities and colleges, to stay in touch with their alumni, engage them through communications and events, and solicit donations. An alumni management system helps an institution to ensure that they never lose contact with their alumni's and continue to be engaged with them long after they have graduated."
x= gTTS(text=r)
x.save("a.mp3")
os.system("a.mp3")
constr=mysql.connector.connect(host="localhost", user="root", password="root", database="aldb")
print("")
mycursor=constr.cursor()
#mycursor.execute("create database aldb")
#mycursor.execute("create table alureg(alu_id varchar(10) primary key, first_name varchar(30), last_name varchar(30), dob date, gender varchar(10), email_id varchar(50), add_corr varchar(40), add_offc varchar(40), mob_no varchar(10), curr_city varchar(30), curr_company varchar(30), desg varchar(30), session_from year(4), session_to year(4), branch varchar(30));")
#mycursor.execute("create table event(id varchar(10) primary key, event_name varchar(50), event_date date, venue varchar(40), status varchar(40));")
constr.commit()

#The function RegisterAlumni is used for registration of a new alumnus.
def RegisterAlumni():
     ch="y"
     while ch=="Y" or ch=="y":
          L=[]
          fname=input("Enter Your First Name: ")
          L.append(fname)
          lname=input("Enter Your Last Name:")
          L.append(lname)
          dob=input("Enter Dob in YYYY-MM-DD Format: ")
          L.append(dob)
          gender=input("Enter Your Gender: ")
          L.append(gender)
          email=input("Enter your email address Eg: aa@gmail.com: ")
          L.append(email)
          add_c=input("Enter your correspondence address: ")
          L.append(add_c)
          add_of=input("Enter your official address: ")
          L.append(add_of)
          mob=input("Enter Your Mobile No: ")
          L.append(mob)
          cur_c=input("Enter City Name You Stay: ")
          L.append(cur_c)
          com=input("Enter Company/Organization You are Working: ")
          L.append(com)
          desg=input("Enter Your Desgination in Company/Organization: ")
          L.append(desg)
          start_y=input("Enter Your Session Start Year in College: ")
          L.append(start_y)
          start_e=input("Enter Your Session End Year in College: ")
          L.append(start_e)
          branch=input("Enter Your Branch in College: ")
          L.append(branch)
          alid="AL"+ str(random.randint(564783,25611850))
          L.insert(0,alid)
          alumni=(L)
          sql="insert into alureg(alu_id,first_name,last_name,dob,gender,email_id,add_corr,add_offc,mob_no,curr_city,curr_company,desg,session_from,session_to,branch) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
          mycursor.execute(sql,alumni)
          constr.commit()
          print("========================================================You Have Been Successfully Registered=======================================================\nYour AlumniID: ", alid)
          print("Use it for futher correspondence")
          ch=input("Do you want to register more records (y/n)... ")
    
#The function ViewAlumniDetails is used to view details of a specific alumnus or to view details of all registered alumni.      
def ViewAlumniDetails():
     ch="y"
     while ch=="Y" or ch=="y":
          print("Select the criteria to View Details: ")
          print("1. First Name")
          print("2. Last Name")
          print("3. Company")
          print("4. Stream")
          print("5. City")
          print("6. Session Start")
          print("7. To View All Records")
          ch=int(input("Enter the choice: "))
          if ch==1 :
              s=input("Enter First Name of the Alumni to Be Searched For: ")
              rl=(s,)
              sql="select * from alureg where first_name like %s"
              mycursor.execute(sql,rl)
              d=mycursor.fetchone()
              print(d)
          elif ch==2:
              s=input("Enter Last Name of the Alumni to Be Searched For: ")
              rl=(s,)
              sql="select * from alureg where last_name like %s"
              mycursor.execute(sql,rl)
              d=mycursor.fetchone()
              print(d)
          elif ch==3:
              s=input("Enter Company Name of the Alumni to Be Searched For: ")
              rl=(s,)
              sql="select * from alureg where curr_company=%s"
              mycursor.execute(sql,rl)
              d=mycursor.fetchone()
              print(d)
          elif ch==4:
              s=input("Enter Stream of the Alumni to be Searched For: ")
              rl=(s,)
              sql="select * from alureg where branch=%s"
              mycursor.execute(sql,rl)
              d=mycursor.fetchone()
              print(d)
          elif ch==5:
              s=input("Enter City of the residence of the Alumni: ")
              rl=(s,)
              sql="select * from alureg where curr_city=%s"
              mycursor.execute(sql,rl)
              d=mycursor.fetchone()
              print(d)
          elif ch==6:
              s=input("Enter Session Start Year of the Alumni: ")
              rl=(s,)
              sql="select * from alureg where session_from=%s"
              mycursor.execute(sql,rl)
              d=mycursor.fetchone()
              print(d)
          elif ch==7:
              sql="select * from alureg"
              mycursor.execute(sql)
              L=mycursor.fetchall()
              print("=========================================================The Alumni Details are as Follows :============================================================")
              print("\nAlumni Id's")
              for i in range (0,len(L)):
                   print(L[i][0])
              print("\nFirst Names")
              for i in range (0,len(L)):
                   print(L[i][1])
              print("\nLast Names")
              for i in range (0,len(L)):
                   print(L[i][2])
              print("\nDate of Birth")
              for i in range (0,len(L)):
                   print(L[i][3])
              print("\nGender")
              for i in range (0,len(L)):
                   print(L[i][4])
              print("\nEmail Address")
              for i in range (0,len(L)):
                   print(L[i][5])
              print("\nCorrespondence Address")
              for i in range (0,len(L)):
                   print(L[i][6])
              print("\nOfficial Address")
              for i in range (0,len(L)):
                   print(L[i][7])
              print("\nMobile Numbers")
              for i in range (0,len(L)):
                   print(L[i][8])
              print("\nCity Name of Residence")
              for i in range (0,len(L)):
                   print(L[i][9])
              print("\nCurrent Company/Organization")
              for i in range (0,len(L)):
                   print(L[i][10])
              print("\nDesgination in Company/Organization")
              for i in range (0,len(L)):
                   print(L[i][11])
              print("\nSession Start Year in College")
              for i in range (0,len(L)):
                   print(L[i][12])
              print("\n Session End Year in college")
              for i in range (0,len(L)):
                   print(L[i][13])
              print("\nBranch in College")
              for i in range (0,len(L)):
                   print(L[i][14])
          else:
               print("Wrong Input")
          ch=input("\nDo you want to view more records (y/n)... ")

#The function EditAlumni is used to edit the pre-existing records of the alumni.         
def EditAlumni():
     ch="y"
     while ch=="Y" or ch=="y":
          alid=input("Enter Alumni ID to be edited: ")
          sql="select * from alureg where alu_id=%s"
          ed=(alid,)
          mycursor.execute(sql,ed)
          res=mycursor.fetchall()
          if res==None:
               print("!!!No such ID exists!!!")
          else:
               for x in res:
                   print("")
                   print("first_name")
                   print("last_name")
                   print("dob")
                   print("gender")
                   print("email_id")
                   print("add_corr")
                   print("add_offc")
                   print("mob_no")
                   print("curr_city")
                   print("curr_company")
                   print("desg")
                   print("session_from year")
                   print("session_to year")
                   print("branch")
                   fld=input("\nEnter the field which you want to edit : ")
                   val=input("\nEnter the value you want to set : ")
                   sql="Update alureg set " + fld +"='" + val + "' where alu_id='" + alid + "'"
                   sq=sql
                   mycursor.execute(sql)
                   print("\n============================================================Alumnus Edited Successfully================================================================ ")
                   s=input("\nDo you want to view the updated record (y/n)... ")
                   if s=="y":
                        print("\n==============================================================After updation the record is:==============================================================")
                        sql="select * from alureg where alu_id=%s"
                        ed=(alid,)
                        mycursor.execute(sql,ed)
                        res=mycursor.fetchall()
                        for x in res:
                            print(x)
                            constr.commit()
          ch=input("\nDo you want to edit more records (y/n)... ")

#The function SearchAlumni is used to search for a specified alumnus and if found it prints "Record Found".                   
def SearchAlumni():
     ch="y"
     while ch=="Y" or ch=="y":
          aluid=input("Enter the Alumni ID of the alumni to be searched for: ")
          sql="select * from alureg where alu_id=%s"
          rl=(aluid,)
          mycursor.execute(sql,rl)
          res=mycursor.fetchone()
          if res==None:
               print("\n!!!Record not Found!!!\n ")
               f=input("Do you want register this alumni (y/n)... ")
               if f=="y":
                    RegisterAlumni()
          else:
               print("Record Found")
               f=input("\nDo you want view the details of the alumni (y/n)... ")
               if f=="y":
                    ViewAlumniDetails()
          ch=input("\nDo you want to search more records (y/n)... ")
         
#The function DeleteAlumni is used delete the record(s) of a specified alumnus.
def DeleteAlumni():
     ch="y"
     while ch=="Y" or ch=="y":
          aluid=input("Enter the Alumni ID for the alumni to be deleted : ")
          sql="Delete from alureg where alu_id=%s"
          rl=(aluid,)
          mycursor.execute(sql,rl)
          constr.commit()
          print("\n==========================================================Record Deleted Successfully==============================================================")
          ch=input("\nDo you want to delete more records  (y/n)... ")
          
#The function ScheduleEvent is used to schedule an alumni meet or any other event(s) for the alumni.
def ScheduleEvent():
     ch="y"
     while ch=="Y" or ch=="y":
          E=[]
          ename=input("Enter Event Name to be Scheduled: ")
          E.append(ename)
          edate=input("Enter Event Date in YYYY-MM-DD: ")
          E.append(edate)
          evenue=input("Enter Venue of Event: ")
          E.append(evenue)
          estat=input("Enter Event Status as Completed Or Not Completed: ")
          E.append(estat)
          g="E"+ str(random.randint(4516,9112))
          E.insert(0,g)
          event=(E)
          sql="insert into event (id,event_name,event_date,venue,status) values (%s,%s,%s,%s,%s)"
          mycursor.execute(sql,event)
          constr.commit()
          print("========================================================You have succesfully added the Event============================================================\n")
          print("Event ID is: ",g)
          ch=input("\nDo you want to enter more records (y/n)... ")

#The function ViewEventDetails is used to view the details of a specified event(s).            
def ViewEventDetails():
     ch="y"
     while ch=="Y" or ch=="y":
          print("Select the criteria to View Event Details : ")
          print("\n1. Event Name")
          print("2. Venue")
          print("3. Status")
          print("4. Date")
          print("5. To View All Records")
          ch=int(input("\nEnter the choice : "))
          if ch==1 :
              s=input("\nEnter Event Name to Be Searched For: ")
              rl=(s,)
              sql="select * from event where event_name like %s"
              mycursor.execute(sql,rl)
              d=mycursor.fetchone()
              print(d)
          elif ch==2:
              s=input("\nEnter Venue Name to Be Searched For: ")
              rl=(s,)
              sql="select * from event where venue like %s"
              mycursor.execute(sql,rl)
              d=mycursor.fetchone()
              print(d)
          elif ch==3:
              s=input("\nEnter Status to Be Searched For: ")
              rl=(s,)
              sql="select * from event where status=%s"
              mycursor.execute(sql,rl)
              d=mycursor.fetchone()
              print(d)
          elif ch==4:
              s=input("\nEnter Event Date to Be Searched For (YYYY-MM-DD: )")
              rl=(s,)
              sql="select * from event where event_date like %s"
              mycursor.execute(sql,rl)
              d=mycursor.fetchone()
              print(d)
          elif ch==5:
               sql="select * from event"
               mycursor.execute(sql)
               res=mycursor.fetchall()
               print("\n==========================================================The Event Details are as Follows:==============================================================")
               print("\n(Event_Name,Event_Date,Venue,Status)")
               for x in res:
                    print(x)
          ch=input("\nDo you want to view more records (y/n)... ")
          
#The function SearchEvent is used search for the specified event, if found it shows "Event Found".
def SearchEvent():
     ch="y"
     while ch=="Y" or ch=="y":
          Eid=input("Enter the Event ID of the event to be viewed : ")
          sql="select * from event where id=%s"
          rl=(Eid,)
          mycursor.execute(sql,rl)
          res=mycursor.fetchone()
          if res==None:
               print("\n!!!No such Event was Found!!! ")
               f=input("\nDo you want schedule this event (y/n)... ")
               if f=="y":
                    ScheduleEvent()
          else:
               print("\nEvent Found")
               k=input("\nDo you want view this event (y/n)... ")
               if k=="y":
                    ViewEventDetails()
          ch=input("\nDo you want to search more records (y/n)... ")

#The function EditEvent is used to edit the details of a scheduled event.       
def EditEvent():
     ch="y"
     while ch=="Y" or ch=="y":
          EEid=input("Enter Event ID to be edited: ")
          sql="select * from event where id=%s"
          ed=(EEid,)
          mycursor.execute(sql,ed)
          n=mycursor.fetchall()
          for x in n:
              print("")
              print("event_name")
              print("event_date")
              print("venue")
              print("status")
              fld=input("\nEnter the field which you want to edit: ")
              val=input("Enter the value you want to set : ")
              sql="Update event set " + fld +"='" + val + "' where id='" +      EEid + "'"
              sq=sql
              mycursor.execute(sql)
              print("\n==============================================================Event Edited Successfully=================================================================")
              s=input("\nDo you want to view the updated record (y/n)... ")
              if s=="y":
                   print("\n==========================================================After correction the record is:==============================================================\n ")
                   sql="select * from event where id=%s"
                   ed=(EEid,)
                   mycursor.execute(sql,ed)
                   res=mycursor.fetchall()
                   for x in res:
                       print(x)
                       constr.commit()
          ch=input("\nDo you want to edit more records (y/n)... ")


          
#The function DeleteEvent is used to delete a specified event.          
def DeleteEvent():
     ch="y"
     while ch=="Y" or ch=="y":
          ename=input("Enter the Event ID to be deleted : ")
          sql="Delete from event where id=%s"
          rl=(ename,)
          mycursor.execute(sql,rl)
          constr.commit()
          print("\n====================================================The specified event was deleted successfully========================================================")
          ch=input("\nDo you want to delete more records (y/n)... ")

#The function MainMenu is the main function and it asks the user for the operation that is to be performed.     
def MainMenu():
     ch="y"
     while ch=="Y" or ch=="y":
          print("\nEnter 1 : To Register an Alumni ")
          print("Enter 2 : To Search Alumni ")
          print("Enter 3 : To View Alumni Details ")
          print("Enter 4 : To Edit Alumni Details ")
          print("Enter 5 : To Delete Alumni ")
          print("Enter 6 : To Schedule an Event ")
          print("Enter 7 : To Search for an Event ")
          print("Enter 8 : To View Details of an Event ")
          print("Enter 9 : To Edit Event Details ")
          print("Enter 10 : To Delete an Event ")
          try:
              userInput = int(input("\nPlease Select An Option: "))
          except ValueError:
              exit("!!!You Had Entered Wrong Choice!!!")
          else:
              print("\n")
          if(userInput == 1):
              RegisterAlumni()
          elif (userInput==2):
              SearchAlumni()
          elif (userInput==3):
              ViewAlumniDetails()
          elif (userInput==4):
              EditAlumni()
          elif (userInput==5):
              DeleteAlumni()
          elif (userInput==6):
              ScheduleEvent()
          elif (userInput==7):
              SearchEvent()
          elif (userInput==8):
              ViewEventDetails()
          elif (userInput==9):
              EditEvent()
          elif (userInput==10):
              DeleteEvent()
          else:
              print("!!!Enter correct choice!!!")
          ch=input("\nDo you want to run the program again (y/n)... ")
         
MainMenu()





