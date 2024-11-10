############
# SOLUTION #
############

def	room_planner(width, length):
	return str(width // 3 * length)

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