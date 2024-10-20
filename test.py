# file called node and import class Node in the file
from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit

  def push(self, value):
    item = Node(value)
    # set the next node into top item
    item.set_next_node(self.top_item)
    # set item into top item
    self.top_item = item
    # Increment stack size by 1 here:
    self.size += 1

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      # updaate the next node up top item 
      self.top_item = item_to_remove.get_next_node()
      # decrement by 1
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    else:
      print("Nothing to see here!")
      
  # Define has_space() and is_empty() below:
  def has_space(self):
    if self.limit > self.size:
      return True

