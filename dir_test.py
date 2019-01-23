import os
from queue import Queue


def build_dir(source_path, cur_path):
	fir_name = ""
	sec_name = ""
	thi_name = ""
	with open(source_path, "r", encoding="utf-8") as file:
		for line in file:
			line = line.replace("\n", "")
			if line.count("\t") == 0:
				fir_name = line
				sec_name = ""
				thi_name = ""
			elif line.count("\t") == 1:
				sec_name = line
				thi_name = ""
			else:
				thi_name = line
			sec_name = sec_name.replace("\t", "")
			thi_name = thi_name.replace("\t", "")
			final_path = os.path.join(cur_path, fir_name, sec_name, thi_name)
			print(final_path)
			os.makedirs(final_path)


def get_dir_names(root_path):
	q = Queue()
	dir_names = []
	for dir_name in os.listdir(root_path):
		q.put(os.path.join(root_path, dir_name))

	while q.qsize() > 0:
		dir_name = q.get()
		tmp_names = os.listdir(dir_name)
		if len(tmp_names) == 0:
			dir_names.append(dir_name)
		else:
			for tmp in tmp_names:
				q.put(os.path.join(dir_name, tmp))
	return dir_names


build_dir("./SoftwareEngine.txt", r"C:\Users\YiFan\Desktop\软件工程目录")


for i in get_dir_names(r"C:\Users\YiFan\Desktop\软件工程目录"):
	print(i)
