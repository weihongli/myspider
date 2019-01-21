import os


def build_dir(source_path, cur_path):
	fir_name = ""
	sec_name = ""
	thi_name = ""
	cur_path = r"C:\Users\YiFan\Desktop\软件工程目录"
	with open("./SoftwareEngine.txt", "r", encoding="utf-8") as file:
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


def get_files_list(rootpath):
	files = []


def walk_dir(root_path):
	files = []
	for dir_path, dir_names, file_names in os.walk(root_path):
			for dir_name in dir_names:
				print(os.path.join(dir_path, dir_name))
			for file_name in file_names:
				print(os.path.join(dir_path, file_name))


walk_dir(r"C:\Users\YiFan\Desktop\软件工程目录")
