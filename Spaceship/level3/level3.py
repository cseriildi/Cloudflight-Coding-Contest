###########
# LEVEL 3 #
###########

import os


class Kata:
  def __init__(self, filename: str):
    self.path = os.path.dirname(os.path.abspath(__file__))
    self.filename = filename
    self.input = self.readInput()
    self.space_stations = []
    self.time_limits = []
    self.result = ""

    self.parse()
    self.solve()
    self.generate_outfile()

#########
# PARSE #
#########

  def parse(self):
    for line in self.input.splitlines()[1:]:
      station, time = line.split(" ")
      self.space_stations.append(int(station))
      self.time_limits.append(int(time))

############
# SOLUTION #
############

  def getTime(self, pacelist: list[int]) -> int:
    return sum(abs(pace) + (pace == 0) for pace in pacelist)

  def getSpace(self, pacelist: list[int]) -> int:
    return sum(pace // abs(pace) if pace else 0 for pace in pacelist)

  def speedUp(self, current_speed: int, direction: int) -> int:
    match abs(current_speed):
      case 0:
        return 5 * direction
      case 1:
        return current_speed
      case _:
        return current_speed - direction

  def slowDown(self, current_speed: int, direction: int) -> int:
    return 0 if abs(current_speed) in (0, 5) else current_speed + direction

  def getOptimalPaces(self, start: int, goal: int) -> list[int]:
    direction = 1 if goal >= start else -1
    distance = abs(goal - start)
    speed = 0
    paces = [speed]

    for remaining_distance in range(distance, 0, -1):
      if speed == 0 or remaining_distance > (6 - abs(speed)):
        speed = self.speedUp(speed, direction)
      elif remaining_distance < (6 - abs(speed)):
        speed = self.slowDown(speed, direction)
      paces.append(speed)

    paces.append(0)  # Ensure we end with speed 0

    return paces

  def checkResult(self, pacelist: list[int], goal: int, time_limit: int):
    if self.getTime(pacelist) > time_limit:
      print(f"Impossible to reach space station at {goal} in time {time_limit}")
      raise ValueError("IMPOSSIBLE")
    if self.getSpace(pacelist) != goal:
      print(f"Didn't reach the space station at {goal}!")
      raise ValueError("ERROR")
    if pacelist[0] != 0 or pacelist[-1] != 0:
      print("Pace list must start and end with 0!")
      raise ValueError("ERROR")

  def solve(self):
    for space_station, time_limit in zip(self.space_stations, self.time_limits):
      optimal_paces = self.getOptimalPaces(0, space_station)
      self.checkResult(optimal_paces, space_station, time_limit)
      self.result += f"{' '.join([str(pace) for pace in optimal_paces])}\n"

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

