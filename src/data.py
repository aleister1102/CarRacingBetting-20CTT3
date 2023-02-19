
import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
import os.path
from os import path
import Racing_Game
import menu
#Hàm kiểm tra xem file có tồn tại hay ko
#Nếu file tồn tại thì xét đến pass word trong hàm create_load
#Nếu file ko tồn tại thì tạo một file mới cho các giá trị reset (trong hàm creat_load, hàm này chỉ kiểm tra)
#Tuy nhiên vẫn chưa cho người dùng nhập tên nhân vật, tính sau
def checkfile(username,password):
	print ("file exist:"+str(path.exists(str(username)+'.txt')))
	
	check=path.exists(str(username)+'.txt')
	print(check)
	create_load(check,username,password)
#Hàm này nhận vào các giá trị về username, password
#Nếu file chưa có thì tạo file mới, tức là tạo nhân vật mới
#Nếu file có rồi thì tiến hành load lên và nhập dữ liệu vào class player cho người chơi

def create_load(check,username,password):
	username_file=username+'.txt'
	if check==False:
		with open(username_file,'w',encoding='utf-8') as f:
			name=username
			username+='.txt\n'
			password+='\n'
			buff='0\n'
			data=[username,password,'500\n',buff,name]
			f.writelines(data)
			print('Tao file moi thanh cong')
			import_data(data)
	if check ==True:
		with open(username_file,'r+',encoding='utf-8') as f:
			data=f.readlines()
			if data[1].strip('\n') == password:
				print ('Load file thanh cong')
				import_data(data)
			else: 
				print('Sai mat khau')
				
#Hàm này là hàm nhập dữ liệu vào class player cho người chơi
def import_data(data):
	print('Du lieu load duoc: ',data)
	
	Racing_Game.player.money=int(data[2].strip('\n'))
	Racing_Game.player.buff=int(data[3].strip('\n'))
	Racing_Game.player.path=data[0].strip('\n')
	Racing_Game.player.name=data[4]
	name=os.path.splitext(Racing_Game.player.path)
	#Cắt chuỗi đường dẫn username lấy làm tên
	if Racing_Game.player.name!=name[0]:
		Racing_Game.player.name=name[0]
	print('Ten nguoi choi: ',Racing_Game.player.name)
	print('So tien nguoi choi co: ',Racing_Game.player.money)
	print('Buff nguoi choi so huu: ',Racing_Game.player.buff)
	print('Duong dan cua file: ',Racing_Game.player.path)
#Hàm này để điều phối chương trình chính của đăng nhập
#Trong đó có bao gồm các cách tạo form nhập dữ liệu của tkinter cơ bản, chưa làm cầu kì
#run_login sẽ được gọi trong nút play game. Tạm thời chưa chuyển hướng
def run_login ():
	def validateLogin(username, password):
		user=username.get()
		user=str(user)
		passw=password.get()
		passw=str(passw)
		print("username entered :", user)
		print("password entered :", passw)
		checkfile(user,passw)
		check=path.exists(str(user)+'.txt')		
		username_file=user+'.txt'
		if check ==True:
			with open(username_file,'r+',encoding='utf-8') as f:
				data=f.readlines()
				if data[1].strip('\n') == passw:
					top.destroy()
				else:
					print('Đệ quy')
					validateLogin()
					return
		
	#window
	top = Tk()  
	top.geometry('300x100')  
	top.title('Đăng nhập')
	#username
	username=tk.StringVar()
	U =Label(top,text='Username').grid(row=0,column=3)
	U_field=Entry(top,textvariable=username,width=12).grid(row=0,column=4)
	#password
	password=tk.StringVar()
	P=Label(top,text='Password').grid(row=1,column=3)
	P_field=Entry(top,textvariable=password,width=12,show='*').grid(row=1,column=4)
	def endtkinter(top):
		top.destroy()
		Racing_Game.player.name=='exit'
	def character_limit(username):
		if len(username.get()) > 0:
			username.set(username.get()[-11])

	username.trace("w", lambda *args: character_limit(username))

	validateLogin=partial(validateLogin,username,password)
	endtkinter=partial(endtkinter,top)
	#login button	
	loginButton = Button(top, text="Login", command=validateLogin).grid(row=3,column=3)
	quitButton=Button(top,text='Quit',command=endtkinter).grid(row=4,column=3)
	top.mainloop()
