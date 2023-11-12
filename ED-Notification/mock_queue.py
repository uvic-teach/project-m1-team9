# This is a mock database with some assumptions
# 1: Queue must run independently (not controlled by anything else)
# 2: Queue must have an interface to interact with that enables:
#   Interface to add to queue (M3: load (mockDB(seperatefile) + mockNoise(hardcoded))) (possible shuffle), key is name (M3: assumption no two patients have the same name),
#   (COMPLETE) print list of users (debug purposes super simple m3) 
#   (COMPLETE) TO BE TREATED LIST (TBTL) -> implements kick 
#   (M4: Kick cond. 1: Timeout 2: Confirm treated)
#   (COMPLETE) TBTL.kick(patient) -> remove patient from TBTL, then dequeue item on queue and put into TBTL
#   (COMPLETE) for now M3; have kick place patient at end of queue (infinite loop)

import json

file_path = "mockDB.json"

with open(file_path, 'r') as openfile:
  data = json.load(openfile)


class ED_list:
  def __init__(self):
    self.list = []

  def is_empty(self):
    return len(self.list) == 0
  
  def add(self, item):
    for thing in item:
      self.list.append(thing)
  
  def remove(self, key):
    for item in self.list:
      if item['name'] == key:
        return self.list.remove(item)
      

  def size(self):
    return len(self.list)
  
  def print_list(self):
    for item in self.list:
      print(item)
   

class Queue(ED_list):
  def __init__(self):
    super().__init__()
    
  # enqueue function is not meant to be a duplicate of the add() function of ED_lists
  # future implementation would implement a smarter insertion of elements into the queue
  # future implementation goal is to use smarter insertion to implement a priority queue
  def enqueue(self, patient):
    for thing in patient:
      self.list.append(thing)
  
  def dequeue(self):
    if not self.is_empty():
      return self.list.pop(0)
    else:
      return None

class TBTL(ED_list):

  def __init__(self, capacity = 3):
    super().__init__()
    self.capacity = capacity
    self.queue = Queue()
  
  
  def add(self, item):
    if len(self.list) >= self.capacity:
      print("TBTL is full")
    else:
      self.list.append(item)
  
  def kick(self, key):
    # if infinite loop of patients isn't required, remove the patient variable
    patient = self.remove(key)
    # temporary infinite loop of rotating patients for development/demonstration purposes
    self.queue.enqueue(patient)
    
    patient = self.queue.dequeue()
    if patient != None:
      self.add(patient)
  
  def print_queue(self):
    self.queue.print_list()

mockNoiseDB = [
{"name": "Johnathan", "email": "<INSERT YOUR EMAIL>", "nearestED": "Victoria General Hopsital", "EDqueue": 5}, 
{"name": "Emiree", "email": "<INSERT YOUR EMAIL>", "nearestED": "Royal Jubilee Hospital", "EDqueue": 2}, 
{"name": "Samuel", "email": "<INSERT YOUR EMAIL>", "nearestED": "Oak Bay Urgent Care Clinic", "EDqueue": 0}]

def main():
  # Sanity testing via prints and object creation
  list = ED_list()
  list.add(mockNoiseDB)
  #list.print_list()
  list.remove("Johnathan")
  #print(list.is_empty())
  #list.print_list()
  print(list.size())
  list.add([mockNoiseDB[0]])
  list.print_list()

  

  




if __name__ == "__main__":
    main()
