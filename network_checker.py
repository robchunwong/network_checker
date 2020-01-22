from tkinter import *
import socket, platform, subprocess, os, sys
import requests, bs4

#functions
def get_ip():
	e.delete(0, END)
	x = socket.gethostbyname(socket.gethostname())
	e.insert(0, str(x))
	return

def get_telnet():
	ports = [80, 443]
	x = os.system("telnet " + str("www.icbc.com.cn") + " " + str(ports[0]))
	e.insert(0, str(x))


def get_hostname():
	e.delete(0, END)
	x = socket.gethostname()
	e.insert(0, str(x))

def get_ping():
	url = "www.icbc.com.cn"
	x = os.system("ping " + url )


def get_trace():
	url = "www.icbc.com.cn"
	x = os.system("tracert " + url)


def webscrape():
	res = requests.get('http://www.icbc.com.cn')
	soup = bs4.BeautifulSoup(res.content, 'html.parser')

	headers = res.headers
	status = res.status_code
	x = soup.find(class_="main")

	if len(headers) == 3 and status == 200:
		text = x.get_text()
		print("VPN = down, Bank = Up")
		print(text)
	elif len(headers) == 3 and status != 200:
		text = x.get_text()
		print("VPN = down, Bank = Down")
		print(text)
	elif len(headers) > 3 and status != 200:
		print("VPN = Up, Bank = Down")
	else:
		print("VPN = Up, Bank = Up")


		
#create a root terminal
root = Tk()
root.title("network checker")
root.geometry("500x500") #You want the size of the app to be 500x500
root.resizable(0, 0) #Don't allow resizing in the x or y direction

#create and use input
e = Entry(root, width=100, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


    

#create a widget
label_ipadd = Button(root, text="Get IP", padx=60, pady=20, command=get_ip)
label_telnet = Button(root, text="telnet", padx=60, pady=20, command=get_telnet)
label_trace = Button(root, text="tracer", padx=60, pady=20, command= get_trace)
label_hostname = Button(root, text="hostname", padx=60, pady=20, command=get_hostname)
label_ping = Button(root, text="ping", padx=60, pady=20, command= get_ping)
label_webscrape = Button(root, text="webscrape", padx=60, pady=20, command= webscrape)

#put the widget on the screen / root terminal
label_ipadd.grid(row=1, column=0)
label_telnet.grid(row=1, column=1)
label_trace.grid(row=2, column=0)
label_hostname.grid(row=2, column=1)
label_ping.grid(row=3, column=0)
label_webscrape.grid(row=3, column=1)


root.mainloop()