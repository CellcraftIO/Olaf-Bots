from Tkinter import *
from tkFileDialog import *
import os, sys, json, subprocess

def relpath(p):
	if getattr(sys, 'frozen', False):
		return sys._MEIPASS;
	else:
		return p;

def setProxyFile():
	proxyFile.set(askopenfilename());

def downloadProxies():
	#os.chdir(askdirectory());
	CREATE_NO_WINDOW = 0x08000000;
	startinfo = subprocess.STARTUPINFO();
	#startinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW;
	#startinfo.wShowWindow = subprocess.SW_HIDE;
	subprocess.Popen([relpath('.') + '\\node.exe', relpath('.') + '\\u.js'], startupinfo=startinfo, creationflags=CREATE_NO_WINDOW);
	#os.chdir(sys._MEIPASS);

def startBots():
	global c;
	global started;
	with open(relpath('.') + '\\GUI.conf', 'w') as GUIconfig:
		data = {
			'botName': botName.get(),
			'proxies': proxyFile.get(),
			'maxBots': maxBots.get()
		}
		json.dump(data, GUIconfig);
	if started:
		started = False
		start.config(text='Start Bots');
		c.terminate();
	else:
		started = True;
		start.config(text='Stop Bots');
		CREATE_NO_WINDOW = 0x08000000;
		startinfo = subprocess.STARTUPINFO();
		#startinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW;
		#startinfo.wShowWindow = subprocess.SW_HIDE;
		c = subprocess.Popen([relpath('.') + '\\node.exe', relpath('.') + '\\c.js'], startupinfo=startinfo, creationflags=CREATE_NO_WINDOW);

os.chdir(relpath('.'));

root = Tk();
root.wm_title('Olaf4Snow');
root.iconbitmap(relpath('.') + '\\icon.ico');
root.resizable(width=False, height=False);

root.clipboard_clear();
root.clipboard_append('// ==UserScript==\n// @name         Olaf Bots-Client\n// @namespace    Beta!@!\n// @version      1.0\n// @description  New Bots\n// @author       Olaf\n// @match       *.astr.io/*\n// @match       *.agarup.us/*\n// @match       *.gaver.io/*\n// @match       *.agar.bio/*\n// @match       *.nbk.io/*\n// @match       *.rata.io/*\n// @match       *.cellcraft.io/*\n// @match       *.gota.io/*\n// @match       *.germs.io/*\n// @match       *.galx.io/*\n// @match       *.germs.io/*\n// @match       *.happyfor.win/*\n// @match       *.agarios.org/*\n// @match       *.kralagario.com/*\n// @match       *.agar.red/*\n// @match       *.gkclan.tk/*\n// @require      https://cdnjs.cloudflare.com/ajax/libs/socket.io/1.4.5/socket.io.min.js\n// @grant        none\n// @run-at       document-start\n// ==/UserScript==\n\'use strict\';\nwindow.botServer=\'127.0.0.1:8081\';\nvar script=document.createElement(\"script\");\nscript.src=\"http://www.olaf4snow.com/public/NeyBotsScriptSrc_Olaf4Snow_v1.js\";\ndocument.getElementsByTagName(\"head\")[0].appendChild(script);');

Label(root, text='Proxy-File:').pack(anchor='w', padx=10, pady=(5, 0));
proxyFile = StringVar()
proxyFile.set(relpath('.') + '\\proxy.txt')
Entry(root, width=25, textvariable=proxyFile).pack(fill='x', padx=10, pady=(0, 10));
Button(root, text='Select file', command=setProxyFile).pack(expand=True, fill='x', padx=10, pady=5)
Label(root, text='Bot-Name:').pack(anchor='w', padx=10, pady=(5, 0));
botName = StringVar()
botName.set('[Olaf]4snow.com');
Entry(root, width=25, textvariable=botName).pack(fill='x', padx=10, pady=(0, 10));
Label(root, text='Max bot amount:').pack(anchor='w', padx=10, pady=(0, 5))
maxBots = Scale(root, from_=0, to=10000, orient='horizontal');
maxBots.pack(anchor='w', padx=10, pady=(0, 5), expand=True, fill='x')
maxBots.set(1000);
Button(root, text='Download Proxies', command=downloadProxies, width=20).pack(side='left', expand=True, fill='x', padx=(10, 5), pady=10);
started = False;
start = Button(root, text='Start Bots', command=startBots, width=20);
start.pack(side='left', expand=True, fill='x', padx=(5, 10), pady=10);

root.mainloop();