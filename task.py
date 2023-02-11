#!/usr/bin/python3
import json
import sys
import random
import datetime
from getpass import getuser

data_json='/home/%s/.config/task.json'%getuser()
your_input=sys.argv
degree=[35,31,34,36]
str_all='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

def random_id():
	zero=0
	tid=[]
	while zero<=4:
		tid.append(random.choice(list(str_all)))
		zero+=1
	return ''.join(tid)

def add(info,degree):
	with open(data_json,'r')as file:
		old_data=json.loads(file.read())
		old_data.append({'info':info,'degree':degree,'tid':random_id(),'date':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
	with open(data_json,'w')as new_file:
		new_file.write(json.dumps(old_data,ensure_ascii=False))

def main():
	global your_input
	if '-h' in your_input or len(your_input)==1:
		print('usage(用法): %s [-adhls] [thing ...]\nexample(例子):\n  %s -s 9 -a \'buy beef.\'  --Add a note and set a 9 degree for it(添加一个便条并为它设置9级的优先度).\n  %s -d nbVJx  --Delete the note whose TID is nbVJx(删除一个TID为nbVJx的便条).\n\n  ------- Listing options(参数详情) -------\n  -a note(便条内容)			Add a note(新建一个便条).\n  -d TID(TID)				Delete a note by TID(通过TID删除一个便条).\n  -h					See the help(查看帮助).\n  -l					List all your notes and informations(列出所有便条和相关信息).\n  -s number(等级)			Set the degree you wanna give for the note(为一个便条设置优先级).'%(your_input[0],your_input[0],your_input[0]))
	else:
		if '-d' in your_input:
			del_item(your_input[your_input.index('-d')+1])
		else:
			if '-l' in your_input:
				show()
			else:
				if '-s' not in your_input:
					degree=4
				else:
					degree=int(your_input[your_input.index('-s')+1])
				info=your_input[your_input.index('-a')+1]
				add(info,degree)

def show():
	global your_input
	with open(data_json,'r')as file:
		data=json.loads(file.read())
	highest=[]
	middle=[]
	low=[]
	lowest=[]
	for item in data:
		if item['degree']>=8:
			highest.append(item)
		elif item['degree']>=4 and item['degree']<8:
			middle.append(item)
		elif item['degree']<4 and item['degree']>=1:
			low.append(item)
		elif item['degree']<=0:
			lowest.append(item)
	def show_list(a_list,degree_id):
		for item in a_list:
			if item['degree']<=10 and item['degree']!=0:
				star='⭐'*item['degree']
			elif item['degree']!=0:
				star='⭐'*10+' + ✨ * %s'%(item['degree']-10)
			else:
				star='0'
			print('\033[1;%sm%s │ %s\n└─ TID: %s  [%s]\033[0m'%(degree[degree_id],item['info'],star,item['tid'],item['date']),end='\n\n')
	show_list(highest,0)
	show_list(middle,1)
	show_list(low,2)
	show_list(lowest,3)

def del_item(tid):
	with open(data_json,'r')as file:
		old_data=json.loads(file.read())
	new_data=[]
	for item in old_data:
		if item['tid']!=tid:
			new_data.append(item)
		else:
			pass
	with open(data_json,'w')as new_file:
		new_file.write(json.dumps(new_data,ensure_ascii=False))

if __name__ == '__main__':
	main()