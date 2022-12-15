class Vector:

  def __init__(self, a, b=None):
    if b == None:
      self.x, self.y = a
    else:
      self.x = a
      self.y = b
  
  def __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x, y)

  def __sub__(self, other):
    x = self.x - other.x
    y = self.y - other.y
    return Vector(x, y)

  def dumb_normalize(self):
      if self.x > 1:
          self.x = 1
      elif self.x < -1:
          self.x = -1    
      if self.y > 1:
          self.y = 1
      elif self.y < -1:
          self.y = -1

  def to_tuple(self):
    return (self.x, self.y)

  def manhattan_distance(self, other):
    return abs(self.x - other.x) + abs(self.y - other.y)

  def __repr__(self):
    return f"({self.x},{self.y})"

  def __hash__(self):
    return hash((self.x, self.y))

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __iter__(self):
    return (self.x, self.y).__iter__()
