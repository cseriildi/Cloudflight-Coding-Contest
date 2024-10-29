import pprint as pp

def parser(file_path):

	with open(file_path, 'r') as file:
		lines = int(file.readline())
		result = [file.readline().split() for _ in range(lines)]
		return result

def get_outfile_name(file_path):
	result = file_path.split(".")[0] + ".out"
	return result

def	create_room(x, y):
	room = [['.' for _ in range(x)] for _ in range(y)]

	max_column = x
	if x % 4 < 3:
		max_column -= x % 4
	for row in range(0, y, 2):
		for column in [i for i in range(max_column) if i % 4 != 3]:
			room[row][column] = "X"

	max_row = y
	if y % 4 < 3:
		max_row -= y % 4
	if x % 4 in (range(1, 3)):
		for row in [i for i in range(max_row) if i % 4 != 3]:
			room[row][-1] = 'X'

	result = '\n'.join([''.join(line) for line in room])
	return result

def level4(file_path):
	input = parser(file_path)

	with open(get_outfile_name(file_path), 'w') as file:
		for room in input:
			file.write(create_room(int(room[0]), int(room[1])))
			file.write("\n\n")


# level4("input/level4_example.in")

level4("input/level4_1.in")
level4("input/level4_2.in")
level4("input/level4_3.in")
level4("input/level4_4.in")
level4("input/level4_5.in")