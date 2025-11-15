###########
# LEVEL 5 #
###########

import os


class Kata:
  def __init__(self, filename: str):
    self.path = os.path.dirname(os.path.abspath(__file__))
    self.filename = filename
    self.input = self.readInput()
    self.spaceships = []
    self.time_limits = []
    self.asteroids = []
    self.count = 0
    self.result = ""
    self.parse()
    self.solve()
    self.generate_outfile()

#########
# PARSE #
#########

  def parse(self):
    lines = self.input.splitlines()[1:]
    self.count = len(lines) // 2
    for line in range(0, len(lines), 2):
      position, time = lines[line].split(" ")
      posx, posy = position.split(",")
      aposx, aposy = lines[line + 1].split(",")
      self.spaceships.append((int(posx), int(posy)))
      self.time_limits.append(int(time))
      self.asteroids.append((int(aposx), int(aposy)))

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
    paces.append(0)
    return paces

  def checkResult(self, pacelist: list[int], goal: int, time_limit: int):
    if self.getTime(pacelist) > time_limit:
      print(f"Impossible to reach space station at {goal} in time {time_limit}")
      raise ValueError("IMPOSSIBLE")
    if self.getSpace(pacelist) != goal:
      print(f"Didn't reach the space station at {goal}!")
      raise ValueError("ERROR")
    if pacelist[0] != 0 or pacelist[-1] != 0:
      print("Pace list must start and end with 0 speed!")
      raise ValueError("ERROR")

  def getOptimalPaces2D(self, start: tuple[int, int], goal: tuple[int, int]) -> tuple[list[int], list[int]]:
    paces_x = self.getOptimalPaces(start[0], goal[0])
    paces_y = self.getOptimalPaces(start[1], goal[1])
    return paces_x, paces_y

  def getOptimalPaces2DWithTimeAdjustment(self, start: tuple[int, int], goal: tuple[int, int]) -> tuple[list[int], list[int]]:
    paces_x = self.getOptimalPaces(start[0], goal[0])
    paces_y = self.getOptimalPaces(start[1], goal[1])

    time_x = self.getTime(paces_x)
    time_y = self.getTime(paces_y)
    max_time = max(time_x, time_y)
    paces_x += [0] * (max_time - time_x)
    paces_y += [0] * (max_time - time_y)
    return paces_x, paces_y

  def getDirection(self, pace):
    return (pace != 0) * (1 if pace >= 0 else -1)

  def getPath(self, paces, time):
    result = []
    pos = 0

    result.append(pos)
    for pace in paces[1:-1]:
      for _ in range(abs(pace)):
        result.append(pos)
        time -= 1
      pos += self.getDirection(pace)
    for _ in range(time):
      result.append(pos)

    return result

  def findCollision(self, path, asteroid):
    danger = [(asteroid[0] + dx, asteroid[1] + dy) for dx in range(-2, 3) for dy in range(-2, 3)]

    for step in path:
      if step in danger:
        return step
    return None

  def solve(self):
    for i in range(self.count):
      posx, posy = self.spaceships[i]
      asteroid = self.asteroids[i]
      time = self.time_limits[i]

      paces_x = self.getOptimalPaces(0, posx)
      paces_y = self.getOptimalPaces(0, posy)

      max_time = max(self.getTime(paces_x), self.getTime(paces_y))

      path_x = self.getPath(paces_x, max_time)
      path_y = self.getPath(paces_y, max_time)

      path = list(zip(self.getPath(paces_x, max_time),  self.getPath(paces_y, max_time)))

      collision = self.findCollision(path, asteroid)
      if collision:
        last_valid_pos = path[path.index(collision) - 1] if collision else path[-1]

        dx = asteroid[0] - last_valid_pos[0]
        dy = asteroid[1] - last_valid_pos[1]

        break_point_1 = list(last_valid_pos)
        if abs(dx) >= abs(dy):
          break_point_1[1] += (3 + abs(dy)) * (1 if dy >= 0 else -1)
        else:
          break_point_1[0] += (3 + abs(dx)) * (1 if dx >= 0 else -1)

        new_dx = asteroid[0] - break_point_1[0]
        new_dy = asteroid[1] - break_point_1[1]

        break_point_2 = break_point_1[:]

        if break_point_2[0] == last_valid_pos[0]:
          break_point_2[0] += (3 + abs(new_dx)) * (1 if new_dx >= 0 else -1)
        else:
          break_point_2[1] += (3 + abs(new_dy)) * (1 if new_dy >= 0 else -1)

        paces_x1, paces_y1 = self.getOptimalPaces2DWithTimeAdjustment((0, 0), (break_point_1))
        adj_paces_x, adj_paces_y = self.getOptimalPaces2DWithTimeAdjustment((break_point_1), (break_point_2))
        paces_x2, paces_y2 = self.getOptimalPaces2D((break_point_2), (posx, posy))

        paces_x = paces_x1[:-1] + adj_paces_x[1:-1] + paces_x2[1:]
        paces_y = paces_y1[:-1] + adj_paces_y[1:-1] + paces_y2[1:]

      self.result += f"{' '.join([str(pace) for pace in paces_x])}\n"
      self.result += f"{' '.join([str(pace) for pace in paces_y])}\n\n"

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

