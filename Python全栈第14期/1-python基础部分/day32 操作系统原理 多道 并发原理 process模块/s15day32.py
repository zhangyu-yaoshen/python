s15day32 线程和进程相关

内容回顾：
	1. 网络基础 
		- OSI 7层
		- 三次握手四次挥手
		- 其他网络知识
			- mac
			- IP
			- 子网掩码
			- 网关 
			- DHCP服务（路由器）
			- 路由器
			- 交换机
			- 广播/单播
			- arp协议
			- DNS 
		- 补充：
			- 私有云/公有云
			- 租服务器/域名
	2. socket 
		- 服务端：
			- 监听IP和端口
			- 等待客户端连接（阻塞）
			- 收（阻塞）
			- 发
			
			import socket 
			sk = socket.socket()
			sk.bind((ip,port))
			sk.listen(5)
			while True:
				# 服务端 sk.accept，如果通过阻塞，则表示有客户端来连接了。
				# 服务端.accept
				conn,addr = sk.accept()
				
				# 服务端.accept
				conn.recv(1028)
			
		- 客户端：
			- 连接服务端IP和端口（阻塞）
			- 收（阻塞）
			- 发
	
		- 黏包 
	3. socketserver
		- 多线程/多进程 + socket 
		- 面向对象多继承
	
今日内容：
	1. 操作系统/应用程序
	
	2. 操作中的"并发"
	
	3. 其他语言线程、进程
	
	4. Python中线程和进程（GIL锁）
	
	5. Python线程编写+锁 
	
	6. 小爬虫
	
内容详细：
	1. 操作系统/应用程序
	
		a. 硬件 
			- 硬盘
			- CPU 
			- 主板 
			- 显卡
			- 内存
			- 电源
			...
		b. 装系统（软件）
			- 系统就是一个由程序员写出来软件，该软件用于控制计算机的硬件，让他们之间进行相互配合。
			
		c. 安软件（安装应用程序）
			- QQ
			- 百度云
			- pycharm
			...
			
	2. 并发和并行
		并发，伪，由于执行速度特别快，人感觉不到停顿。
		并行，真，创建10个人同时操作。
	
	3. 线程、进程
		a. 单进程、单线程的应用程序
			
			print('666')
			
		b. 到底什么是线程？什么是进程？
			Python自己没有这玩意，Python中调用的操作系统的线程和进程。
		
		c. 单进程、多线程的应用程序
			代码：
				import threading
				print('666')

				def func(arg):
					print(arg)
				t = threading.Thread(target=func)
				t.start()

				print('end')
					
		一个应用程序（软件），可以有多个进程（默认只有一个），一个进程中可以创建多个线程（默认一个）。
		
		d. 故事: Alex甄嬛西游传
		
		总结：
			
			1. 操作系统帮助开发者操作硬件。
			2. 程序员写好代码在操作系统上运行（依赖解释器）。
			
			任务特别多。
			3. 以前的你，写代码：
				import threading
				import requests
				import uuid

				url_list = [
					'https://www3.autoimg.cn/newsdfs/g28/M05/F9/98/120x90_0_autohomecar__ChsEnluQmUmARAhAAAFES6mpmTM281.jpg',
					'https://www2.autoimg.cn/newsdfs/g28/M09/FC/06/120x90_0_autohomecar__ChcCR1uQlD6AT4P3AAGRMJX7834274.jpg',
					'https://www2.autoimg.cn/newsdfs/g3/M00/C6/A9/120x90_0_autohomecar__ChsEkVuPsdqAQz3zAAEYvWuAspI061.jpg',
				]

				def task(url):
					""""""

					"""
					1. DNS解析，根据域名解析出IP
					2. 创建socket客户端    sk = socket.socket()
					3. 向服务端发起连接请求 sk.connect()
					4. 发送数据（我要图片） sk.send(...)
					5. 接收数据            sk.recv(8096)

					接收到数据后写入文件。
					"""
					ret = requests.get(url)
					file_name = str(uuid.uuid4()) + '.jpg'
					with open(file_name, mode='wb') as f:
						f.write(ret.content)

				for url in url_list:
					task()
				
				
				"""
				- 你写好代码
				- 交给解释器运行： python s1.py 
				- 解释器读取代码，再交给操作系统去执行，根据你的代码去选择创建多少个线程/进程去执行（单进程/单线程）。
				- 操作系统调用硬件：硬盘、cpu、网卡....
				"""

			4. 现在的你，写代码：
				import threading
				import requests
				import uuid

				url_list = [
					'https://www3.autoimg.cn/newsdfs/g28/M05/F9/98/120x90_0_autohomecar__ChsEnluQmUmARAhAAAFES6mpmTM281.jpg',
					'https://www2.autoimg.cn/newsdfs/g28/M09/FC/06/120x90_0_autohomecar__ChcCR1uQlD6AT4P3AAGRMJX7834274.jpg',
					'https://www2.autoimg.cn/newsdfs/g3/M00/C6/A9/120x90_0_autohomecar__ChsEkVuPsdqAQz3zAAEYvWuAspI061.jpg',
				]

				def task(url):
					""""""

					"""
					1. DNS解析，根据域名解析出IP
					2. 创建socket客户端    sk = socket.socket()
					3. 向服务端发起连接请求 sk.connect()
					4. 发送数据（我要图片） sk.send(...)
					5. 接收数据            sk.recv(8096)

					接收到数据后写入文件。
					"""
					ret = requests.get(url)
					file_name = str(uuid.uuid4()) + '.jpg'
					with open(file_name, mode='wb') as f:
						f.write(ret.content)

				for url in url_list:

					t = threading.Thread(target=task,args=(url,))
					t.start()
			
				
				"""
				- 你写好代码
				- 交给解释器运行： python s2.py 
				- 解释器读取代码，再交给操作系统去执行，根据你的代码去选择创建多少个线程/进程去执行（单进程/4线程）。
				- 操作系统调用硬件：硬盘、cpu、网卡....
				"""
				
				Python多线程情况下：
					- 计算密集型操作：效率低。（GIL锁）
					- IO操作： 效率高 
					
				Python多进程的情况下：
					- 计算密集型操作：效率高（浪费资源）。 不得已而为之。
					- IO操作： 效率高 （浪费资源）。
				
				以后写Python时：
					IO密集型用多线程： 文件/输入输出/socket网络通信
					计算密集型用多进程。
				
				
				扩展：
					Java多线程情况下：
						- 计算密集型操作：效率高。
						- IO操作： 效率高 
					Python多进程的情况下：
						- 计算密集型操作：效率高（浪费资源）。
						- IO操作： 效率高 浪费资源）。
				
	4. Python中线程和进程（GIL锁）
		GIL锁，全局解释器锁。用于限制一个进程中同一时刻只有一个线程被cpu调度。
		
		扩展：默认GIL锁在执行100个cpu指令（过期时间）。
		
		
	5. Python线程编写
				
		# by luffycity.com
		import threading

		# #################### 1. 计算密集型多线程无用 ####################
		# v1 = [11,22,33] # +1
		# v2 = [44,55,66] # 100
		#
		#
		# def func(data,plus):
		#     for i in range(len(data)):
		#         data[i] = data[i] + plus
		#
		# t1 = threading.Thread(target=func,args=(v1,1))
		# t1.start()
		#
		# t2 = threading.Thread(target=func,args=(v2,100))
		# t2.start()


		# #################### 2. IO操作 多线程有用 ####################
		# import threading
		# import requests
		# import uuid
		#
		# url_list = [
		#     'https://www3.autoimg.cn/newsdfs/g28/M05/F9/98/120x90_0_autohomecar__ChsEnluQmUmARAhAAAFES6mpmTM281.jpg',
		#     'https://www2.autoimg.cn/newsdfs/g28/M09/FC/06/120x90_0_autohomecar__ChcCR1uQlD6AT4P3AAGRMJX7834274.jpg',
		#     'https://www2.autoimg.cn/newsdfs/g3/M00/C6/A9/120x90_0_autohomecar__ChsEkVuPsdqAQz3zAAEYvWuAspI061.jpg',
		# ]
		#
		# def task(url):
		#     ret = requests.get(url)
		#     file_name = str(uuid.uuid4()) + '.jpg'
		#     with open(file_name, mode='wb') as f:
		#         f.write(ret.content)
		#
		# for url in url_list:
		#
		#     t = threading.Thread(target=task,args=(url,))
		#     t.start()
		
		
	总结：
		1. 应用程序/进程/线程的关系？ *****（面试题：进程/线程/协程的区别？）
		
		2. 为什么要创建线程？
			由于线程是cpu工作的最小单元，创建线程可以利用多核优势实现并行操作（Java/C#）。
			注意：线程是为了工作。
			
		3. 为什么要创建进程？
			进程和进程之间做数据隔离（Java/C#）。
			
			注意：进程是为了提供环境让线程工作。
			
		4. Python
			a. Python中存在一个GIL锁。 *****
				- 造成：多线程无法利用多核优势。
				- 解决：开多进程处理（浪费资源）
				总结：
					IO密集型：多线程 
					计算密集型：多进程
			b. 线程的创建 
				- Thread 		*****
				- MyThread 
			c. 其他 
				- join 			*****
				- setDeanon		*****
				- setName		*****
				- threading.current_thread()	*****
			d. 锁
				- 获得 
				- 释放 
				
			
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	