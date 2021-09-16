import json

with open('./raw-files/Mnt.txt') as f:
	lines = f.readlines()

result = []
for line in lines:
	result.append(line.replace("\n", "").split(";"))

coord = []
json_dict = {}

for x in range(int(len(result)/2),int(len(result)/2)+100):
	for z in range(int(len(result[x]))):
		coord.append(x - (len(result) / 2))
		coord.append(int(result[x][z])/5)
		coord.append(z - (len(result[x]) / 2))

json_dict = {
	'vertices': coord
}

with open('../Models/Maps/dem_cacapava_only_points.json', 'w') as json_file:
	json.dump(json_dict, json_file)
