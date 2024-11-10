############
# SOLUTION #
############

def	room_planner(width, length):
	room = []
	room_index = 0

	column = width % 3 * -1
	max_row = length - length % 3

	for _ in range(length):
		line = []
		for x in range(width):
			if x < width + column:
				if x % 3 == 0:
					room_index += 1
				line.append(str(room_index))
			else:
				line.append("0")

		room.append(line[:])

	if width % 3 != 0:
		for row in range(0, max_row, 3):
			room_index += 1
			room[row][column] = str(room_index)
			room[row + 1][column] = str(room_index)
			room[row + 2][column] = str(room_index)

			if column == -2:
				room_index += 1
				room[row][column + 1] = str(room_index)
				room[row + 1][column + 1] = str(room_index)
				room[row + 2][column + 1] = str(room_index)

	return '\n'.join([' '.join(line) for line in room]) + "\n"

#########
# UTILS #
#########

import os

def parser(file_path):
	with open("input/" + file_path, 'r') as infile:
		lines = int(infile.readline())
		return [infile.readline().split() for _ in range(lines)]

def generate_outfile(file_path):
	input = parser(file_path)

	folder_path = "output/"
	os.makedirs(folder_path, exist_ok=True)

	outfile_path = folder_path  + file_path.split(".")[0] + ".out"

	with open(outfile_path, 'w') as outfile:
		for line in input:
			outfile.write(room_planner(int(line[0]), int(line[1])))
			outfile.write("\n")

level = os.path.basename(__file__).split(".")[0]

generate_outfile(level + "_example.in")
generate_outfile(level + "_1.in")
generate_outfile(level + "_2.in")
generate_outfile(level + "_3.in")
generate_outfile(level + "_4.in")
generate_outfile(level + "_5.in")