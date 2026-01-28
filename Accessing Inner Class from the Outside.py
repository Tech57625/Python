
class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"

    def display(self):
      print("Hello from inner class")

outer = Outer()
inner = outer.Inner()
inner.display() 