############
# SOLUTION #
############

def	room_planner(width, length):

	room = [['.' for _ in range(width)] for _ in range(length)]

	if width % 3 == 2 and width % 2 == 1:
		if length % 3 == 2:
			horizontal = False
		elif length % 2 == 1:
			horizontal = True
	if width % 3 == 2 or length % 2 == 1:
		horizontal = True
	elif width % 2 == 1 or length % 3 == 2:
		horizontal = False
	else:
		horizontal = False

	if horizontal:
		max_x = width - (4 - (width % 3) * 2)
		max_y = length - (3 - (length % 2) * 3)
	else:
		max_x = width - (3 - (width % 2) * 3)
		max_y = length - (4 - (length % 3) * 2)

	if horizontal:
		part_x = [i for i in range(max_x) if i % 3 != 2]
		part_y = range(0, max_y, 2)
	else:
		part_x = range(0, max_x, 2)
		part_y = [i for i in range(max_y) if i % 3 != 2]
	
	for row in part_y:
		for column in part_x:
			room[row][column] = "X"


	if horizontal:
		adj_max_x = max_x - (width % 2 == 0)
		adj_max_y = max_y - (length % 3 == 1) * 2
	else:
		adj_max_x = max_x - (width % 3 == 1) * 2
		adj_max_y = max_y - (length % 2 == 0)
		
	if max_x != width:

		if horizontal:
			part_x = range(max_x + 1, width, 2)
			part_y = [i for i in range(adj_max_y) if i % 3 != 2]
		else:	
			part_x = range(max_x + 1, width)
			part_y = range(0, adj_max_y, 2)

		for row in part_y:
			for column in part_x:
				room[row][column] = "X"


	if max_y != length:
		if horizontal:
			part_x = range(0, adj_max_x, 2)
			part_y = range(max_y + 1, length)
		else:	
			part_x = [i for i in range(adj_max_x) if i % 3 != 2]
			part_y = range(max_y + 1, length, 2)

		for row in part_y:
			for column in part_x:
				room[row][column] = "X"

	""" 
	# this part is incorrect and the maps are incomplete

	if  horizontal:
		if width - adj_max_x >= 3 and length - adj_max_y >= 2:
			room[-1][-1] = "X"
			room[-2][-1] = "X"
			room[-1][-4] = "X"
			room[-1][-3] = "X"
	
	else:
		if width - adj_max_x >= 2 and length - adj_max_y >= 3:
			room[-1][-1] = "X"
			room[-1][-2] = "X"
			room[-4][-1] = "X"
			room[-3][-1] = "X"
 """
	return '\n'.join([''.join(line) for line in room]) + "\n"

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