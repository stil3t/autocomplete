import re
import sys

file = sys.argv[1]

def main(file):

	try:
		input_file = open(file, 'r')

	except IOError as e:
		print('Error: Unable to read the file')
		exit()

	lits = {}
	line_number = 0

	for line in input_file:
		for lit in re.findall(r'[\']\w+[\']', line)+re.findall(r'[\"]\w+[\"]', line):
			lit = lit[1:-1]

			if not lit in lits.keys():
				lits[lit] = [str(line_number)]

			else:
				if str(line_number) not in lits[lit]:
					lits[lit].append(str(line_number))
		
		line_number+=1

	for i in lits.keys():
		if len(lits[i])>1:
			print('Lines with \'{0}\': {1}'.format(i, ', '.join(lits[i])))

	input_file.close()

main(file)