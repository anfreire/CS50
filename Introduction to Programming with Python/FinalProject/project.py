from PIL import *
from tkinter import messagebox
from tkinter import *
from pathlib import Path
import warnings
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
import time
from PIL import ImageTk, Image

warnings.simplefilter(action='ignore', category=FutureWarning)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")

def main():
	print_indexs()
	root.protocol("WM_DELETE_WINDOW", lambda:on_closing())
	root.mainloop()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

root = Tk(className='Major World Indices Analyzer')
icon = ImageTk.PhotoImage(Image.open(f"{ASSETS_PATH}/icon.ico"))
root.iconphoto(True, icon)
root.tk.call("wm", "iconphoto", root._w, icon)
root.geometry("800x500")
root.title("Major World Indices Analyzer")
root.resizable(False, False)

f1 = Frame(root, width=800, height=500).pack()
f2 = Frame(root, width=800, height=500).pack()
f3 = Frame(root, width=800, height=500).pack()
f4 = Frame(root, width=800, height=500).pack()


#####################################################
#	MAIN MENU		 -------		DESIGN		    #
#####################################################

canvas_f1 = Canvas(
    f1,
    bg = "#FFFFFF",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas_f1.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("frame0/image_1.png"))
image_1 = canvas_f1.create_image(
    400.0,
    250.0,
    image=image_image_1
)
canvas_f1.create_text(
    122.0,
    75.0,
    anchor="nw",
    text="Major World Indices Analyzer",
    fill="#000000",
    font=("Ubuntu Medium", 40 * -1)
)
canvas_f1.create_rectangle(
    98.0,
    147.0,
    700.0,
    149.0,
    fill="#000000",
    outline="")

button_image_1_f1 = PhotoImage(
    file=relative_to_assets("frame0/button_1.png"))
button_1_f1 = Button(
    image=button_image_1_f1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_1_f1.place(
    x=288.0,
    y=192.0,
    width=225.0,
    height=75.0
)
button_image_2_f1 = PhotoImage(
    file=relative_to_assets("frame0/button_2.png"))
button_2_f1 = Button(
    image=button_image_2_f1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_2_f1.place(
    x=288.0,
    y=287.0,
    width=225.0,
    height=75.0
)
button_image_3_f1 = PhotoImage(
    file=relative_to_assets("frame0/button_3.png"))
button_3_f1 = Button(
    image=button_image_3_f1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_closing(),
    relief="flat"
)
button_3_f1.place(
    x=288.0,
    y=382.0,
    width=225.0,
    height=75.0)
####################################################


#-----------------------//-------------------------#


#####################################################
#	SELECTION		 -------		DESIGN		    #
#####################################################
canvas_f2 = Canvas(
    f2,
    bg = "#FFFFFF",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
image_image_1_f2 = PhotoImage(
    file=relative_to_assets("frame1/image_1.png"))
image_1_f2 = canvas_f2.create_image(
    400.0,
    250.0,
    image=image_image_1
)
canvas_f2.create_text(
    202.0,
    69.0,
    anchor="nw",
    text="Select an Index Fund",
    fill="#000000",
    font=("Ubuntu Medium", 40 * -1)
)
listbox_f2 = Listbox(f2)
scrollbar_f2 = Scrollbar(f2)
listbox_f2.config(
	background= "black",
	foreground="white",
	yscrollcommand= scrollbar_f2.set,
	font=("Ubuntu", 20)
	)
scrollbar_f2.config(command = listbox_f2.yview)
button_image_1_f2 = PhotoImage(
    file=relative_to_assets("frame1/button_1.png"))
button_1_f2 = Button(
    image=button_image_1_f2,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_image_2_f2 = PhotoImage(
    file=relative_to_assets("frame1/button_2.png"))
button_2_f2 = Button(
    image=button_image_2_f2,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
####################################################


#-----------------------//-------------------------#


#####################################################
#		PERIOD		 -------		DESIGN		    #
#####################################################
canvas_f3 = Canvas(
    f3,
    bg = "#FFFFFF",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
image_image_1_f3 = PhotoImage(
    file=relative_to_assets("frame3/image_1.png"))
image_1_f3 = canvas_f3.create_image(
    400.0,
    250.0,
    image=image_image_1
)
canvas_f3.create_text(
    153.0,
    64.0,
    anchor="nw",
    text="Select a period to analzye",
    fill="#000000",
    font=("Ubuntu Medium", 40 * -1)
)
canvas_f3.create_text(
    65.0,
    212.0,
    anchor="nw",
    text="Amount (Number)",
    fill="#000000",
    font=("Ubuntu Medium", 35 * -1)
)
canvas_f3.create_text(
    430.0,
    198.0,
    anchor="nw",
    text="         Season (Text)\nEx: Days, Months, Years",
    fill="#000000",
    font=("Ubuntu Medium", 30 * -1)
)
entry_image_1_f3 = PhotoImage(
    file=relative_to_assets("frame3/entry_1.png"))
entry_bg_1_f3 = canvas_f3.create_image(
    212.5,
    333.5,
    image=entry_image_1_f3
)
entry_1_f3 = Entry(
    bd=0,
    bg="#000000",
    fg="#000716",
    highlightthickness=0,
	background= "black",
	font=("Ubuntu", 50),
	foreground="white",
)
entry_image_2_f3 = PhotoImage(
    file=relative_to_assets("frame3/entry_2.png"))
entry_bg_2_f3 = canvas_f3.create_image(
    593.5,
    333.5,
    image=entry_image_2_f3,
)
entry_2_f3 = Entry(
    bd=0,
    bg="#000000",
    fg="#000716",
	background= "black",
	foreground="white",
	font=("Ubuntu", 50),
    highlightthickness=0
)
canvas_f3.create_rectangle(
    396.0,
    152.0,
    400.0,
    756.0,
    fill="#000000",
    outline="")
canvas_f3.create_rectangle(
    95.0,
    151.0,
    700.0,
    156.0,
    fill="#000000",
    outline="")
button_image_1_f3 = PhotoImage(
    file=relative_to_assets("frame3/button_1.png")
	)
button_1_f3 = Button(
    image=button_image_1_f3,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_image_2_f3 = PhotoImage(
    file=relative_to_assets("frame3/button_2.png"))
button_2_f3 = Button(
    image=button_image_2_f3,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
####################################################


#-----------------------//-------------------------#


#####################################################
#		RESULTS		 -------		DESIGN		    #
#####################################################
canvas_f4 = Canvas(
    f4,
    bg = "#FFFFFF",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

image_image__f41 = PhotoImage(
    file=relative_to_assets("frame2/image_1.png"))
image_1_f4 = canvas_f4.create_image(
    400.0,
    250.0,
    image=image_image_1
)
canvas_f4.create_text(
    305.0,
    29.0,
    anchor="nw",
    text="Results:",
    fill="#000000",
    font=("Ubuntu Medium", 50 * -1)
)
button_image_1_f4 = PhotoImage(
    file=relative_to_assets("frame2/button_1.png"))
button_1_f4 = Button(
    image=button_image_1_f4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)

button_image_2_f4 = PhotoImage(
    file=relative_to_assets("frame2/button_2.png"))
button_2_f4 = Button(
    image=button_image_2_f4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)

button_image_3_f4 = PhotoImage(
    file=relative_to_assets("frame2/button_3.png"))
button_3_f4 = Button(
    image=button_image_3_f4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_image_4_f4 = PhotoImage(
    file=relative_to_assets("frame2/button_4.png"))
button_4_f4 = Button(
    image=button_image_4_f4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_image_5_f4 = PhotoImage(
    file=relative_to_assets("frame2/button_5.png"))
button_5_f4 = Button(
    image=button_image_5_f4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)

button_image_6_f4 = PhotoImage(
    file=relative_to_assets("frame2/button_6.png"))
button_6_f4 = Button(
    image=button_image_6_f4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)

button_image_7_f4 = PhotoImage(
    file=relative_to_assets("frame2/button_7.png"))
button_7_f4 = Button(
    image=button_image_7_f4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_image_8_f4 = PhotoImage(
    file=relative_to_assets("frame2/button_8.png"))
button_8_f4 = Button(
    image=button_image_8_f4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
####################################################


#-----------------------//-------------------------#


#####################################################
#		GLOBAL		 -------		VARIABLES	    #
#####################################################
option_var = 0
period_var = ""
df_var = []
name_var = ""
warning_var = 0

#-----------------------//-------------------------#


#####################################################
#		FUNCTIONS	 -------   HIDE/SHOW WIDGETS    #
#####################################################
def mainmenu():
	canvas_f1.place(x = 0, y = 0)
	button_1_f1.place(
		x=288.0,
		y=192.0,
		width=225.0,
		height=75.0)
	button_2_f1.place(
		x=288.0,
		y=287.0,
		width=225.0,
		height=75.0)
	button_3_f1.place(
		x=288.0,
		y=382.0,
		width=225.0,
		height=75.0)


def analyze():
	canvas_f2.place(x = 0, y = 0)
	button_1_f2.place(
		x=637.0,
		y=441.0,
		width=150.0,
		height=46.0)
	button_2_f2.place(
		x=11.0,
		y=445.0,
		width=150.0,
		height=46.0)
	listbox_f2.place(
		x=140,
    	y=125,
		width=520,
		height=300)
	scrollbar_f2.place()

def period():
	canvas_f3.place(x = 0, y = 0)
	entry_1_f3.place(
		x=50.0,
		y=271.0,
		width=325.0,
		height=123.0)
	entry_2_f3.place(
		x=431.0,
		y=271.0,
		width=325.0,
		height=123.0)
	button_1_f3.place(
		x=11.0,
		y=445.0,
		width=150.0,
		height=46.0)
	button_2_f3.place(
		x=637.0,
		y=441.0,
		width=150.0,
		height=46.0)

def	results():
	canvas_f4.place(x = 0, y = 0)
	button_1_f4.place(
		x=13.0,
		y=441.0,
		width=150.0,
		height=46.0)
	button_2_f4.place(
		x=637.0,
		y=441.0,
		width=150.0,
		height=46.0)
	button_3_f4.place(
		x=325.0,
		y=441.0,
		width=150.0,
		height=46.0)
	button_4_f4.place(
		x=125.0,
		y=138.0,
		width=180.0,
		height=70.0)
	button_5_f4.place(
		x=490.0,
		y=138.0,
		width=180.0,
		height=70.0)
	button_6_f4.place(
		x=125.0,
		y=245.0,
		width=180.0,
		height=70.0)
	button_7_f4.place(
		x=490.0,
		y=245.0,
		width=180.0,
		height=70.0)
	button_8_f4.place(
		x=310.0,
		y=337.0,
		width=180.0,
		height=70.0)

def	forget_mainmenu():
	button_1_f1.place_forget()
	button_2_f1.place_forget()
	button_3_f1.place_forget()
	canvas_f1.place_forget()

def	forget_analyze():
	button_1_f2.place_forget()
	button_2_f2.place_forget()
	canvas_f2.place_forget()
	listbox_f2.place_forget()
	scrollbar_f2.place_forget()

def	forget_period():
	button_1_f3.place_forget()
	button_2_f3.place_forget()
	entry_1_f3.place_forget()
	entry_2_f3.place_forget()
	canvas_f3.place_forget()

def	forget_results():
	button_1_f4.place_forget()
	button_2_f4.place_forget()
	button_3_f4.place_forget()
	button_4_f4.place_forget()
	button_5_f4.place_forget()
	button_6_f4.place_forget()
	button_7_f4.place_forget()
	button_8_f4.place_forget()
	canvas_f4.place_forget()

def	mainmenu_from_analyze():
	mainmenu()
	forget_analyze()

def mainmenu_from_results():
	plt.close('all')
	mainmenu()
	forget_results()

def proceed_analyze():
	analyze()
	forget_mainmenu()

def proceed_period():
	global option_var
	try:
		validate_option(listbox_f2.curselection())
	except:
		messagebox.showerror(title=None, message="Select a Index Fund from the list!")
		return
	option_var = listbox_f2.curselection()[0]
	period()
	forget_analyze()

def proceed_results(entry1, entry2):
	try:
		validate_period(entry1, entry2)
	except:
		raise ValueError

def proceed_results_handler():
	try:
		proceed_results(entry_1_f3.get(), entry_2_f3.get())
	except:
		messagebox.showerror(title=None, message="Enter a number for the amount, and a period for the season. Ex: 5 Days, 15 Months, 30 Years")
		return
	results()
	forget_period()
	process_stocks()

def back_from_period():
	analyze()
	forget_period()

def back_from_results():
	plt.close('all')
	period()
	forget_results()

button_1_f1.config(command=lambda:proceed_analyze())
button_2_f2.config(command=lambda:mainmenu_from_analyze())
button_1_f2.config(command=lambda:proceed_period())
button_1_f3.config(command=lambda:back_from_period())
button_1_f4.config(command=lambda:back_from_results())
button_2_f4.config(command=lambda:mainmenu_from_results())
####################################################


#-----------------------//-------------------------#


#####################################################
#						FUNCTIONS				    #
#####################################################
def open_window(str):
	new_window = Toplevel(root)
	new_window.title("")
	Label(
		new_window,
		text =str,
		font=('Ubuntu', 30),
		padx=20,
		pady=20).pack()
	new_window.after(7000, lambda:root.destroy())

def validate_option(listbox):
	if len(listbox) == 0:
		raise ValueError

def validate_period(number, option):
	global period_var
	try:
		number = int(number)
	except:
		raise ValueError
	option = str.lower(option)
	if option == "day" or option == "days":
		period_var = str(number) + "d"
	elif option == "month" or option == "months":
		period_var = str(number) + "mo"
	elif option == "year" or option == "years":
		period_var = str(number) + "y"
	else:
		raise ValueError

def save_xlsl_data(df, name):
	name = name.replace(' ', '_')
	if len(name) > 31:
		name = name[0:31]
	writer = pd.ExcelWriter(f'{name}.xlsx', engine='xlsxwriter')
	df.to_excel(writer, sheet_name=name, index=False)
	writer.save()
	return (f"{name}.xlsx  Saved!")

def save_xlsl_36indexs(name):
	data = pd.read_html('https://finance.yahoo.com/world-indices/')[0]
	data = data[['Symbol', 'Name', 'Last Price', 'Change', '% Change']]
	df = pd.DataFrame(data)
	today = date.today()
	today = today.strftime("%d_%m_%Y")
	name = name + today
	if len(name) > 31:
		name = name[0:31]
	messagebox.showinfo(title=None, message=save_xlsl_data(df, name))


def print_indexs():
	data = pd.read_html('https://finance.yahoo.com/world-indices/')[0]
	data = data[['Name']]
	i = 1
	for name in data['Name']:
		listbox_f2.insert(i, name)
		i = i + 1

def	process_stocks():
	try:
		option = option_var
		data = pd.read_html('https://finance.yahoo.com/world-indices/')[0]
		data = data[['Symbol', 'Name']]
		name = data['Name'][option]
		index = yf.Ticker(data['Symbol'][option])
		index = index.history(period=period_var)
		get_stock(index, name)
	except:
		messagebox.showerror(title=None, message="Unable to get data from this Stock. Sorry for the Inconvinience. :( Try another one!")
		return

def get_stock(df, name):
	try:
		df['Date'] = df.index.to_pydatetime()
		df['Date'] = df.index.strftime("%d/%m/%Y")
		df = df[['Date','Open','High','Low','Close','Volume']]
	except:
		messagebox.showerror(title=None, message="Unable to get data from this Stock. Sorry for the Inconvinience. :( Try another one!")
		return
	global df_var
	global name_var
	df_var = df
	name_var = name

def print_charts(i):
	global warning_var
	if warning_var == 0:
		messagebox.showinfo(title=None, message="Depending on the period selected, the charts may take some time to render.")
		warning_var = 1
	if (i == 4):
		plt.plot(df_var['Date'], df_var['Open'])
		plt.show()
		plt.close()
	elif(i == 5):
		plt.plot(df_var['Date'], df_var['Close'])
		plt.show()
		plt.close()
	elif(i == 6):
		plt.plot(df_var['Date'], df_var['High'])
		plt.show()
		plt.close()
	elif(i == 7):
		plt.plot(df_var['Date'], df_var['Low'])
		plt.show()
		plt.close()
	elif(i == 8):
		plt.plot(df_var['Date'], df_var['Volume'])
		plt.show()
		plt.close()

def save_xlsx_one_index():
	try:
		save_xlsl_data(df_var, name_var)
		messagebox.showinfo(title=None, message=(f"{name_var}.xlsx  Saved!"))
	except:
		messagebox.showerror(title=None, message="An unknown error occurred.\nPlease restart the program.\nSorry for any inconvenience")
		return

def on_closing():
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		plt.close("all")
		open_window("Thank you so much to Harvard,\nCS50, and Professor David J. Malan\nfor providing this course.")

button_3_f4.config(command=lambda:save_xlsx_one_index())
button_4_f4.config(command=lambda:print_charts(4))
button_5_f4.config(command=lambda:print_charts(5))
button_6_f4.config(command=lambda:print_charts(6))
button_7_f4.config(command=lambda:print_charts(7))
button_8_f4.config(command=lambda:print_charts(8))
button_2_f3.config(command=lambda:proceed_results_handler())
button_2_f1.config(command=lambda: save_xlsl_36indexs("Major_36_Index_Funds_"))

if __name__ == "__main__":
    main()
