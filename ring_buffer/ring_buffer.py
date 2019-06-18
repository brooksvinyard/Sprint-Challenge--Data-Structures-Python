class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item

    # Set current +1 but if it reaches the capacity, loop to zero
    if self.current == len(self.storage)-1:
      self.current = 0
    else:
      self.current += 1

  def get(self):
    return [val for val in self.storage if val is not None]