import json

with open('./raw-files/Mnt.txt') as f:
	lines = f.readlines()

result = []
for line in lines:
	result.append(line.replace("\n", "").split(";"))

with open('./raw-files/Textura.txt') as f:
	lines = f.readlines()

result_colors = []
for line in lines:
	result_colors.append(line.replace("\n", "").replace(
		"\r", "").replace(";", "_").split("_"))

coord = []
indi = []
colors = []
json_dict = {}
part = 1
g = 0
for x in range(len(result)):
	g = 0
	for z in range(len(result[x])):
		coord.append(x - (len(result) / 2))
		coord.append(int(result[x][z])/5)
		coord.append(z - (len(result[x]) / 2))

		if(int(result[x][z]) >= 500 and (int(result[x][z-1]) >= 500 and int(result[x][z+1]) >= 500 and int(result[x-1][z]) >= 500 and int(result[x+1][z]) >= 500) and (int(result[x][z-2]) >= 500 and int(result[x][z+2]) >= 500 and int(result[x-2][z]) >= 500 and int(result[x+2][z]) >= 500) and (int(result[x][z-3]) >= 500 and int(result[x][z+3]) >= 500 and int(result[x-3][z]) >= 500 and int(result[x+3][z]) >= 500) and (int(result[x][z-4]) >= 500 and int(result[x][z+4]) >= 500 and int(result[x-4][z]) >= 500 and int(result[x+4][z]) >= 500) and (int(result[x][z-5]) >= 500 and int(result[x][z+5]) >= 500 and int(result[x-5][z]) >= 500 and int(result[x+5][z]) >= 500) and (int(result[x][z-6]) >= 500 and int(result[x][z+6]) >= 500 and int(result[x-6][z]) >= 500 and int(result[x+6][z]) >= 500) and (int(result[x][z-7]) >= 500 and int(result[x][z+7]) >= 500 and int(result[x-7][z]) >= 500 and int(result[x+7][z]) >= 500) and (int(result[x][z-8]) >= 500 and int(result[x][z+8]) >= 500 and int(result[x-8][z]) >= 500 and int(result[x+8][z]) >= 500) and (int(result[x][z-9]) >= 500 and int(result[x][z+9]) >= 500 and int(result[x-9][z]) >= 500 and int(result[x+9][z]) >= 500) and (int(result[x][z-10]) >= 500 and int(result[x][z+10]) >= 500 and int(result[x-10][z]) >= 500 and int(result[x+10][z]) >= 500) and (int(result[x][z-11]) >= 500 and int(result[x][z+11]) >= 500 and int(result[x-11][z]) >= 500 and int(result[x+11][z]) >= 500) and (int(result[x][z-12]) >= 500 and int(result[x][z+12]) >= 500 and int(result[x-12][z]) >= 500 and int(result[x+12][z]) >= 500) and (int(result[x][z-13]) >= 400 and int(result[x][z+13]) >= 400 and int(result[x-13][z]) >= 400 and int(result[x+13][z]) >= 400) and (int(result[x][z-14]) >= 400 and int(result[x][z+14]) >= 400 and int(result[x-14][z]) >= 400 and int(result[x+14][z]) >= 400) and (int(result[x][z-15]) >= 400 and int(result[x][z+15]) >= 400 and int(result[x-15][z]) >= 400 and int(result[x+15][z]) >= 400)):
			colors.append(int(result_colors[x][z+g]) / 255.0)
			colors.append(int(result_colors[x][z+1+g]) / 255.0)
			colors.append(int(result_colors[x][z+2+g]) / 255.0)
			colors.append(1)
		else:
			colors.append(0)
			colors.append(0.5)
			colors.append(0)
			colors.append(0)
		g += 2

indi = []

l1 = 0
l2 = len(result[0])
for j in range(len(result)):
	for k in range(len(result[j])):
		indi.append(l1)
		indi.append(l2)
		l1 += 1
		l2 += 1


json_dict = {
	'vertices': coord,
	'indices': indi,
	'scalars': colors
}

with open('../Models/Maps/mnt.json', 'w') as json_file:
	json.dump(json_dict, json_file)
