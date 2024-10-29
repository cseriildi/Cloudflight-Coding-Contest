def parser(file_path):

	with open(file_path, 'r') as file:
		lines = int(file.readline())
		result = [file.readline().split() for _ in range(lines)]
		return result

def get_outfile_name(file_path):
	result = file_path.split(".")[0] + ".out"
	return result

def count_desks(x, y):
	return str(x // 3 * y)


def level1(file_path):
	input = parser(file_path)
	print(input)
	with open(get_outfile_name(file_path), 'w') as file:
		for room in input:
			file.write(count_desks(int(room[0]), int(room[1])))
			file.write("\n")

level1("input/level1_1.in")
level1("input/level1_2.in")
level1("input/level1_3.in")
level1("input/level1_4.in")
level1("input/level1_5.in")