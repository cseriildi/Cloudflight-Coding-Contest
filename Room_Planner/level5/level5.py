import pprint as pp

def parser(file_path):

	with open(file_path, 'r') as file:
		lines = int(file.readline())
		result = [file.readline().split() for _ in range(lines)]
		return result

def get_outfile_name(file_path):
	result = file_path.split(".")[0] + ".out"
	return result

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def	create_room(x, y):

	room = [['.' for _ in range(x)] for _ in range(y)]

	if x % 3 == 2 and x % 2 == 1:
		if y % 3 == 2:
			horizontal = False
		elif y % 2 == 1:
			horizontal = True
	if x % 3 == 2 or y % 2 == 1:
		horizontal = True
	elif x % 2 == 1 or y % 3 == 2:
		horizontal = False
	else:
		horizontal = False

	if horizontal:
		max_x = x - (4 - (x % 3) * 2)
		max_y = y - (3 - (y % 2) * 3)
	else:
		max_x = x - (3 - (x % 2) * 3)
		max_y = y - (4 - (y % 3) * 2)

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
		adj_max_x = max_x - (x % 2 == 0)
		adj_max_y = max_y - (y % 3 == 1) * 2
	else:
		adj_max_x = max_x - (x % 3 == 1) * 2
		adj_max_y = max_y - (y % 2 == 0)
		

	print(horizontal, max_x, max_y, adj_max_x, adj_max_y, x, y)

	if max_x != x:

		if horizontal:
			part_x = range(max_x + 1, x, 2)
			part_y = [i for i in range(adj_max_y) if i % 3 != 2]
		else:	
			part_x = range(max_x + 1, x)
			part_y = range(0, adj_max_y, 2)

		for row in part_y:
			for column in part_x:
				room[row][column] = "X"


	if max_y != y:
		if horizontal:
			part_x = range(0, adj_max_x, 2)
			part_y = range(max_y + 1, y)
		else:	
			part_x = [i for i in range(adj_max_x) if i % 3 != 2]
			part_y = range(max_y + 1, y, 2)

		for row in part_y:
			for column in part_x:
				room[row][column] = "X"

	if  horizontal:
		if x - adj_max_x >= 3 and y - adj_max_y >= 2:
			room[-1][-1] = "X"
			room[-2][-1] = "X"
			room[-1][-4] = "X"
			room[-1][-3] = "X"
	
	else:
		if x - adj_max_x >= 2 and y - adj_max_y >= 3:
			room[-1][-1] = "X"
			room[-1][-2] = "X"
			room[-4][-1] = "X"
			room[-3][-1] = "X"


	result = '\n'.join([''.join(line) for line in room])
	return result

def level5(file_path):
	input = parser(file_path)

	with open(get_outfile_name(file_path), 'w') as file:
		for room in input:
			file.write(create_room(int(room[0]), int(room[1])))
			file.write("\n\n")


# level5("input/level5_example.in")

level5("input/level5_1.in")
level5("input/level5_2.in")
level5("input/level5_3.in")
level5("input/level5_4.in")
level5("input/level5_5.in")
