# -*- coding: utf-8 -*-
"""Week 3 ModSim.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EHTf6TnKMMAC2nssFfBe8dPsmjyrUnAH
"""

class Server:
  def __init__(self, name, w_hrs, busy ): 

    self.name = name 
    self.workHours = work_hours
    self.busy = busy
    self.customer = None 
    self.entCust = True

def setName(self, thename):
    self.name = thename

def setWorkHours(self, theworkHours):
    self.workHours = theworkHours

def setBusy(self, busy):
    self.busy = busy

def assignCustomer(self, customers):
    self.customer = customers

def ent_cust(self, entcust):
    self.entCust = entcust

class Customer:
  def __init__(self, serviceTime, served):
    self.serviceTime = serviceTime
    self.served = True

def beingServed(self, beingS ):
    self.served = beingServed

import random
Q = []
c = Customer()
simPeriod = 60
currentService=60

s1 = Server('Hermione', 8, 'free')
s2 = Server('Harry', 8, 'free')

for i in range(2):
  server.setName = "Server ", i

for t in range(simPeriod):
  print('At time: ', t)
  arrival = random.randit(0,1)
  if arrival == 1:
    cus_time = random.randit(3,5)
    c.beingServed(cus_time)
    Q.append(c.serviceTime)

    print('New arrival.. Current Queue: ' + str(Q) + '\n')

  else:

    print('No new customers')
    

    if s1.busy != 'busy' and len(Q)>=0: # len returns the length of string or data
      Q.pop() 
      s1.set_busy('busy')
      currentService=currentService-1
      print('Server', s1.name , 'currently busy. Time left: ', currentService, ' minutes')
    if s2.busy == 'free' and len(Q)>=0: # len returns the length of string or data
      Q.pop() 
      s2.set_busy('busy')
      currentService=currentService-1
      print('Server', s2.name , 'currently busy. Time left: ', currentService, ' minutes')
    if s1.busy == 'busy' and currentService>0: # len returns the length of string or data
      currentService=currentService-1
    if s2.busy == 'busy' and currentService>0: # len returns the length of string or data
      currentService=currentService-1