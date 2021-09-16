import json
import math

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

		if(int(result[x][z]) >= 500):
			colors.append(int(result_colors[x][z+g]) / 255.0)
			colors.append(int(result_colors[x][z+1+g]) / 255.0)
			colors.append(int(result_colors[x][z+2+g]) / 255.0)
			colors.append(1)
		else:
			colors.append(0.5)
			colors.append(0)
			colors.append(0)
			colors.append(0)
		g += 2

indi = []

l1 = len(result[0])
l2 = 1
for j in range(len(result)-1):
	for k in range(1,len(result[j])):
		indi.append(l2)
		indi.append(l2-1)
		indi.append(l1)

		indi.append(l2)
		indi.append(l1)
		l1 += 1
		indi.append(l1)
		l2 += 1

x = 0
y = 1
z = 2
ns = [None]*len(coord)*3
v1 = [1]*len(coord)*3
v2 = [1]*len(coord)*3
normal = [1]*len(coord)*3
nn = [None]*len(coord)*3

for i in range(0,len(coord),3):
	ns[i + x] = 0.0
	ns[i + y] = 0.0
	ns[i + z] = 0.0
	v1[i + x] = 0.0
	v1[i + y] = 0.0
	v1[i + z] = 0.0
	v2[i + x] = 0.0
	v2[i + y] = 0.0
	v2[i + z] = 0.0
	normal[i + x] = 0.0
	normal[i + y] = 0.0
	normal[i + z] = 0.0
	nn[i + x] = 0.0
	nn[i + y] = 0.0
	nn[i + z] = 0.0

for i in range(0, len(coord), 3):
	v1[x] = coord[3 * indi[i + 2] + x] - coord[3 * indi[i + 1] + x]
	v1[y] = coord[3 * indi[i + 2] + y] - coord[3 * indi[i + 1] + y]
	v1[z] = coord[3 * indi[i + 2] + z] - coord[3 * indi[i + 1] + z]

	v2[x] = coord[3 * indi[i] + x] - coord[3 * indi[i + 1] + x]
	v2[y] = coord[3 * indi[i] + y] - coord[3 * indi[i + 1] + y]
	v2[z] = coord[3 * indi[i] + z] - coord[3 * indi[i + 1] + z]

	normal[x] = v1[y] * v2[z] - v1[z] * v2[y]
	normal[y] = v1[z] * v2[x] - v1[x] * v2[z]
	normal[z] = v1[x] * v2[y] - v1[y] * v2[x]

	for j in range(3):
		ns[3 * indi[i + j] + x] = ns[3 * indi[i + j] + x] + normal[x]
		ns[3 * indi[i + j] + y] = ns[3 * indi[i + j] + y] + normal[y]
		ns[3 * indi[i + j] + z] = ns[3 * indi[i + j] + z] + normal[z]


for i in range(0,len(coord),3):
	nn[x] = ns[i + x]
	nn[y] = ns[i + y]
	nn[z] = ns[i + z]

	leng = math.sqrt((nn[x] * nn[x]) + (nn[y] * nn[y]) + (nn[z] * nn[z]))
	if leng == 0:
		 leng = 1.0

	nn[x] = nn[x] / leng
	nn[y] = nn[y] / leng
	nn[z] = nn[z] / leng

	ns[i + x] = nn[x]
	ns[i + y] = nn[y]
	ns[i + z] = nn[z]

image = './Textures/texture-file.png'

texcoord = [
    0.0,
    0.0,
    1.0,
    0.0,
    1.0,
    1.0,
    0.0,
    1.0,
    1.0,
    0.0,
    1.0,
    1.0,
    0.0,
    1.0,
    0.0,
    0.0,
    0.0,
    1.0,
    0.0,
    0.0,
    1.0,
    0.0,
    1.0,
    1.0,
    1.0,
    1.0,
    0.0,
    1.0,
    0.0,
    0.0,
    1.0,
    0.0,
    1.0,
    0.0,
    1.0,
    1.0,
    0.0,
    1.0,
    0.0,
    0.0,
    0.0,
    0.0,
    1.0,
    0.0,
    1.0,
    1.0,
    0.0,
    1.0
  ]

json_dict = {
	'textureCoords': texcoord,
	'image': image,
	'vertices': coord,
	'indices': indi,
	'scalars': colors,
}

with open('../Models/Maps/mnt_TRIANGLES.map.json', 'w') as json_file:
	json.dump(json_dict, json_file)
