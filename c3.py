lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())
for line in lines:
	chat = line.split(' ')
	time = chat[0][:5]
	name = chat[0][5:]
	print(time)
	print(name)
	print(chat[1:])