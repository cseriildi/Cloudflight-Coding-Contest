###########
# LEVEL 2 #
###########

import os


class Kata:
  def __init__(self, filename: str):
    self.path = os.path.dirname(os.path.abspath(__file__))
    self.filename = filename
    self.input = self.readInput()
    self.data = self.parse()
    self.result = self.solve()
    self.generate_outfile()

#########
# PARSE #
#########

  def parse(self):
    return self.input.splitlines()

############
# SOLUTION #
############

  def solve(self):
    result = []
    for line in self.data:
      result.append(line)

    return "\n".join(result)

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

  Kata(level + "_example")
  Kata(level + "_1")
  Kata(level + "_2")
  Kata(level + "_3")
  Kata(level + "_4")
  Kata(level + "_5")
