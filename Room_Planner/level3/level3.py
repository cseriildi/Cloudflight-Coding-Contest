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
	room = []
	line = []
	i = 0


	column = x % 3 * -1
	max_row = y - y % 3

	for _ in range(y):
		for n in range(x):
			if n < x + column:
				if n % 3 == 0:
					i += 1
				line.append(str(i))
			else:
				line.append("0")

		room.append(line[:])
		line.clear()

	if x % 3 != 0:
		for row in range(0, max_row, 3):
			i += 1
			room[row][column] = str(i)
			room[row + 1][column] = str(i)
			room[row + 2][column] = str(i)

			if column == -2:
				i += 1
				room[row][column + 1] = str(i)
				room[row + 1][column + 1] = str(i)
				room[row + 2][column + 1] = str(i)

	result = '\n'.join([' '.join(line) for line in room])
	return result

def level3(file_path):
	input = parser(file_path)
	with open(get_outfile_name(file_path), 'w') as file:
		for room in input:
			file.write(create_room(int(room[0]), int(room[1])))
			file.write("\n\n")


# level3("input/level3_example.in")

level3("input/level3_1.in")
level3("input/level3_2.in")
level3("input/level3_3.in")
level3("input/level3_4.in")
level3("input/level3_5.in")