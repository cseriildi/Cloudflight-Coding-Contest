###########
# LEVEL 2 #
###########

import os


class Kata:
  def __init__(self, filename: str):
    self.path = os.path.dirname(os.path.abspath(__file__))
    self.filename = filename
    self.input = self.readInput()
    self.spaceships = []
    self.result = ""

    self.parse()
    self.solve()
    self.generate_outfile()

#########
# PARSE #
#########

  def parse(self):
    self.spaceships = [[int(i) for i in line.split(" ")] for line in self.input.splitlines()[1:]]

############
# SOLUTION #
############

  def getTime(self, pacelist: list[int]) -> int:
    return sum(abs(pace) + (pace == 0) for pace in pacelist)

  def getSpace(self, pacelist: list[int]) -> int:
    return sum(pace // abs(pace) if pace else 0 for pace in pacelist)

  def solve(self):
    for ship in self.spaceships:
      self.result += f"{self.getSpace(ship)} {self.getTime(ship)}\n"

#########
# UTILS #
#########

  def readInput(self):
    input_file = os.path.join(self.path, "input", self.filename + ".in")
    try:
      with open(input_file, 'r') as infile:
        return infile.read()
    except FileNotFoundError:
      print(f"Error: {input_file} not found")
      raise

  def generate_outfile(self):
    folder_path = os.path.join(self.path, "output")
    os.makedirs(folder_path, exist_ok=True)

    outfile_path = os.path.join(folder_path, self.filename + ".out")

    with open(outfile_path, 'w') as outfile:
      outfile.write(self.result)

if __name__ == "__main__":
  level = os.path.basename(__file__).split(".")[0]

  Kata(level + "_0_example")
  Kata(level + "_1_small")
  Kata(level + "_2_large")

