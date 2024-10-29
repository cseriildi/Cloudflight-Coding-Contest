def parser(file_path):

	with open(file_path, 'r') as file:
		lines = int(file.readline())
		result = [file.readline().split() for _ in range(lines)]
		return result

def get_outfile_name(file_path):
	result = file_path.split(".")[0] + ".out"
	return result

def	create_room(x, y):
	room = ""
	line = []
	i = 1

	for _ in range(y):
		for _ in range(0, x, 3):
			line.append(str(i))
			line.append(str(i))
			line.append(str(i))
			i += 1
		room += ' '.join(line)
		room += "\n"
		line.clear()

	return room

def level2(file_path):
	input = parser(file_path)
	with open(get_outfile_name(file_path), 'w') as file:
		for room in input:
			file.write(create_room(int(room[0]), int(room[1])))
			file.write("\n")


#level2("input/level2_example.in")

level2("input/level2_1.in")
level2("input/level2_2.in")
level2("input/level2_3.in")
level2("input/level2_4.in")
level2("input/level2_5.in")