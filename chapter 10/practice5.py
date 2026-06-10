# Write a class Train which has methods to book a ticket, get status
# (no of seats) and get fare information of train running under Indian Railways.
from random import randint
class train:
   def __init__(self,trainNo):
      self.trainNo=trainNo
      
   

   def book(self):
      print(f"Ticket is booked in train number: {self.trainNo}")


   def getStatus(self):
      print(f"the train of train number: {self.trainNo} is running on time ")


   def getFair(self,fro,to):
      print(f"the ticket fair for train no:{self.trainNo} from:{fro} to:{to} is {randint(200,300)}")


w=train(124)
w.book()
w.getStatus()
w.getFair("kottayam","palai")
   