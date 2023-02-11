import task
import os
import sys
from getpass import getuser

if os.path.exists(task.data_json):
	print('You have already create a data file, please remove it first(检测到本地存在数据文件, 请先删除再进行安装)')
	sys.exit()
else:
	os.system("echo '[]' >> %s"%task.data_json)
	if not os.path.exists('/usr/bin/task'):
		os.system('chmod +x task.py && sudo cp task.py /usr/bin/task')
	else:
		print('There is a file whose name is as same as \'task\', please try install this program on your own(本地存在一个名为task的文件, 请尝试手动安装此程序).')
		sys.exit()
print('Congratulation! You can now use the command \'task\' to use this program(成功! 现在可以使用task指令使用此程序了).')