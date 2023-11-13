# This is a mock database with some assumptions
# 1: Queue must run independently (not controlled by anything else)
# 2: Queue must have an interface to interact with that enables:
#   Interface to add to queue (M3: load (mockDB(seperatefile) + mockNoise(hardcoded))) (possible shuffle), key is name (M3: assumption no two patients have the same name),
#   (COMPLETE) print list of users (debug purposes super simple m3) 
#   (COMPLETE) TO BE TREATED LIST (TBTL) -> implements kick 
#   (M4: Kick cond. 1: Timeout 2: Confirm treated)
#   (COMPLETE) TBTL.kick(patient) -> remove patient from TBTL, then dequeue item on queue and put into TBTL
#   (COMPLETE) for now M3; have kick place patient at end of queue (infinite loop)

import socket
import threading
import json
import time
import sys

file_path = "mockDB.json"

with open(file_path, 'r') as openfile:
  data = json.load(openfile)


class ED_list:
  #verified
  def __init__(self):
    self.list = []

  #verified
  def is_empty(self):
    return len(self.list) == 0
  
  #verified to work when given a list, and single item
  def add(self, item):
    if isinstance(item, list):
      for thing in item:
        self.list.append(thing)
    else:
      self.list.append(item)
  
  #verified to work when given key that matches
  #verified to work when given key that doesn't match
  #verified to not remove dict items when given key that doesn't match
  #verified to work with single items
  #verified to return none without a match
  def remove(self, key, key_name = 'name'):
    try:
      self.list.remove(key)
      return key
    except ValueError:
      for item in self.list:
        if isinstance(item, dict):
          try:
            if item[key_name] == key:
              value = item
              self.list.remove(item)
              return value
          except KeyError:
            continue
          
    return None
      
  #verified
  def size(self):
    return len(self.list)
  
  #verified
  def print_list(self):
    print(f"This is ", self, "'s list")
    for item in self.list:
      print(item)

  
  def clear(self):
    self.list = []
   

class Queue(ED_list):
  def __init__(self):
    super().__init__()
  
  #verified
  def dequeue(self):
    if not self.is_empty():
      return self.list.pop(0)
    else:
      return None

class TBTL(ED_list):

  #verified
  def __init__(self, capacity = 3):
    super().__init__()
    self.capacity = capacity
    self.queue = Queue()
  
  
  def clear(self):
    self.list = []
    self.queue.list = []
  
  #verified
  def add(self, item):
    if len(self.list) >= self.capacity:
      print("TBTL is full")
    elif isinstance(item, list):
      if len(item) > (self.capacity - len(self.list)):
        print(f"TBTL can't fit: ", item)
      else:
        super().add(item)
    else:
      super().add(item)
  
  #verified
  def kick(self, key):
    # if infinite loop of patients isn't required, remove the patient variable
    patient = self.remove(key)
    if patient == None:
      print(f"No match in TBTL for: ", key)
      return
    # temporary infinite loop of rotating patients for development/demonstration purposes
    self.queue.add(patient)
    
    patient = self.queue.dequeue()
    if patient != None:
      self.add(patient)
  
  def print_queue(self):
    self.queue.print_list()

# List of dictionaries
# Dictionaries are defined by my_dict = {"trait0": "trait0 content", "trait1": "trait1 content"}
mockNoiseDB = [
{"name": "Johnathan", "email": "<INSERT YOUR EMAIL>", "nearestED": "Victoria General Hopsital", "EDqueue": 5}, 
{"name": "Emiree", "email": "<INSERT YOUR EMAIL>", "nearestED": "Royal Jubilee Hospital", "EDqueue": 2}, 
{"name": "Samuel", "email": "<INSERT YOUR EMAIL>", "nearestED": "Oak Bay Urgent Care Clinic", "EDqueue": 0}]


def cycleEDqueue(a):
  interval = 30
  while True:
    print(f"----------------------------------------\nKicking :", a.list[0])
    print("----------------------------------------\nPost-Kick:")
    print("----------------------------------------")
    a.kick(a.list[0])
    a.print_list()
    print("----------------------------------------")
    a.print_queue()
    print("----------------------------------------")
    print(f"Sleeping for ", interval, " seconds")
    time.sleep(interval)

# Thread function that recives poll requests and returns whether or not the polled target is in the TBTL
def listenForPoll(s, a):
  while True:
    # Wait for a data package to be sent to us
    recieved_data = s.recv(1024)
    recieved_data = json.loads(recieved_data.decode())

    print("+++")
    print("Responding to poll request...")
    print("+++")

    in_tbtl = "False" #M4 todo: check if bools can be json'd & socketed
    for person in a.list:
      if person['name'] == recieved_data.get("name"):
        in_tbtl = "True"

    package = json.dumps({"should_send_notif": in_tbtl})
    s.send(package.encode())

def main():
  # Setup & config socket for ED communication as client
  server = socket.socket()
  host = socket.gethostname()
  port = 9981
  server.bind((host, port))

  # Wait for MISTER ED to ask to connect to socket
  print("Awaiting socket connection request...")
  server.listen(1)
  s, addr = server.accept()
  print("Request accepted")
  print("")

  # Setup & config the ED object
  print("Starting ED usage... ")
  time.sleep(1)
  print("TBTL initialization")
  a = TBTL()
  a.add(data)
  a.queue.add(mockNoiseDB)
  print("")

  print("----------------------------------------")
  a.print_list()
  print("----------------------------------------")
  a.print_queue()

  # Attempt a connection to the ED server
  try:
    # Create and start the thread that manages the queue
    queuethread = threading.Thread(target=cycleEDqueue, args=(a,))
    queuethread.start()

    # Create and start the thread that sends data across the socket
    listenthread = threading.Thread(target=sendPollRequest, args=(s, a))
    listenthread.start()
  except Exception:
    sys.exit(1)



def tests():
  print("Sanity testing via prints")
  # list = ED_list()

  """
  print(list.is_empty())
  """
  # list.is_empty() correctly identifies an empty list
  """
  list.print_list()
  """
  # correctly prints empty list

  # list.add(mockNoiseDB)
  # list.add correctly adds lists to itself element by element when given a list
  # lists are defined by [thing0, thing1, thing2]

  """
  list.printlist()
  """
  # list.print_list correctly prints current list
  
  """
  list.add(mockNoiseDB[2])
  list.print_list()
  """
  # list.add() correctly adds single items to itself
  

  """
  print(list.is_empty())
  """
  # list.is_empty() correctly identifies not empty list

  
  """
  list.remove("Johnathan")
  list.remove("Samuel")
  """
  # list.remove correctly removes element in dict if it finds a match

  """
  list.print_list()
  list.add(2)
  list.print_list()
  list.remove(2, "")
  list.print_list()
  """
  # list.add and remove work with single items

  """
  something = list.remove("This isn't in the list")
  print(something)
  """
  # list.remove returns None with no match

  """
  list.remove("Samuel", "name")
  list.print_list()
  """
  # list.remove works when given valid key_name

  """
  list.remove("Samuel", "")
  list.print_list()
  """
  # list.remove works when not given a valid key_name

  """
  list.print_list()
  print(f"size: ", list.size())
  list.add(2)
  print(f"size: ", list.size())
  """
  # list.size() correctly returns size of list

  """
  thing = list.remove("Johnathan")
  print(f"This is the removed item: ", thing)
    """
    # list.remove() returns the removed item

    # list0 = Queue()

  """ 
  print(list0.dequeue())
  """
  # Queue.dequeue() returns none when empty

  """
  list0.print_list()
  list0.add(1)
  list0.add(2)
  list0.add(3)
  list0.print_list()
  print(f"Dequeued: ", list0.dequeue())
  """
  # Queue.dequeue() returns first item added to list

  # c = TBTL()

  """
  print(c.capacity)
  """
  # TBTL correctly has default capacity of 3

  """
  d = TBTL(9)
  print(d.capacity)
  """
  # TBTL correctly can redefine capacity

  """
  c.queue.add(mockNoiseDB)
  c.queue.print_list()
  c.queue.dequeue()
  c.queue.print_list()
  """
  # TBTL has a queue and can add/remove stuff to it

  """
  d = TBTL(1)
  d.add(mockNoiseDB)
  """
  # TBTL.add correctly doesn't fit when list is too long

  """
  d = TBTL(3)
  d.add(1)
  d.add(2)
  d.add(3)
  d.print_list()
  d.add(4)
  d.print_list()
  d.remove(1)
  d.remove(2)
  d.remove(3)
  d.print_list()
  print(d.is_empty())
  d.add(mockNoiseDB)
  d.print_list()
  d.clear()
  d.capacity = 2
  print(d.capacity)
  d.add([1,2,3,4])
  """
  # TBTL.add verification mess, just wanted to do it faster

  """
  d = TBTL()
  d.add([1,2,3])
  d.queue.add([4,5,6])
  print(f"Prekick\nTBTL: ", d.list, "\nQueue: ", d.queue.list)
  d.kick(1)
  print(f"Postkick\nTBTL: ", d.list, "\nQueue: ", d.queue.list)
  d.kick(7)
  e = TBTL()
  e.add(mockNoiseDB)
  e.queue.add(2)
  print(f"Prekick\nTBTL: ", e.list, "\nQueue: ", e.queue.list)
  e.kick("Emiree")
  print(f"Postkick\nTBTL: ", e.list, "\nQueue: ", e.queue.list)
  e.kick(2)
  print(f"Postkick\nTBTL: ", e.list, "\nQueue: ", e.queue.list)
  """
  # TBTL.kick() verifying, verified it refills queue, kicks by element
  # doesn't kick anything if nothing matches key, properly rotates items


if __name__ == "__main__":
    main()