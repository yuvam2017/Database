# 21th video

from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import sqlite3
root= Tk()
root.title("")
root.geometry("400x400")

# Databases

# Create a Database or connect to one
conn = sqlite3.connect('address_book.db')

# Create a Cursor
c = conn.cursor()
#Create table
try:
	c.execute("""CREATE TABLE addresses(
			first_name text,
			last_name text,
			address text,
			city text,
			state text,
			zipcode integer
			)""")
except Exception as e:
	pass

# Funtion to delete a record
def delete():
	# Create a Database or connect to one
	conn = sqlite3.connect('address_book.db')

	# Create a Cursor
	c = conn.cursor()


	# Delete a record
	c.execute("DELETE from addresses WHERE oid="+del_entry.get() )
	c.execute("SELECT *, oid FROM addresses")
	records = c.fetchall()
	# c.fetchmany(50)
	# c.fetchone()
	# print(records)

	print_records = ''
	for record in records:
		print_records += str(record[0])+ " " + str(record[1]) + "\t" + str(record[6]) + "\n"
	query_label.configure(text = " ")
	query_label.configure(text=print_records)

	# Commit Changes
	conn.commit()

	#close connection
	conn.close()
	del_entry.delete(0,END)

#Create Submit Function
def submit():
	# Create a Database or connect to one
	conn = sqlite3.connect('address_book.db')

	# Create a Cursor
	c = conn.cursor()

	# Insert into the table
	c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:add,:city,:state,:zipcode)",
			{
				'f_name':f_name.get(),
				'l_name':l_name.get(),
				'add':add.get(),
				'city':city.get(),
				'state':state.get(),
				'zipcode':zipcode.get()
			})



	# Commit Changes
	conn.commit()

	#close connection
	conn.close()



	# Clear the text boxes
	f_name.delete(0,END)
	l_name.delete(0,END)
	add.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	zipcode.delete(0,END)

# Create a show records funtion
def query():
	# Create a Database or connect to one
	conn = sqlite3.connect('address_book.db')

	# Create a Cursor
	c = conn.cursor()

	#fetch the data from database
	c.execute("SELECT *, oid FROM addresses")
	records = c.fetchall()
	# c.fetchmany(50)
	# c.fetchone()
	# print(records)

	print_records = ''
	for record in records:
		print_records += str(record[0])+ " " + str(record[1]) + "\t" + str(record[6]) + "\n"
	query_label.configure(text = " ")
	query_label.configure(text=print_records)
	


	# Commit Changes
	conn.commit()

	#close connection
	conn.close()


f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=2)
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1)
add = Entry(root,width=30)
add.grid(row=2,column=1)
city = Entry(root,width=30)
city.grid(row=3,column=1)
state = Entry(root,width=30)
state.grid(row=4,column=1)
zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1)

query_label = Label(root)
query_label.grid(row=10,column=0,columnspan=2) 

# Create Text box label
f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0,column=0)
l_name_label = Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
add_label = Label(root,text="Address")
add_label.grid(row=2,column=0)
city_label = Label(root,text="City")
city_label.grid(row=3,column=0)
state_label = Label(root,text="State")
state_label.grid(row=4,column=0)
zipcode_label = Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0)

#Create Submit Button
btn_submit = Button(root,text="Add record to Database",command=submit)
btn_submit.grid(row=6,column=0,columnspan=2,pady=10,ipadx=100)


#create query button 
btn_query = Button(root,text="Show Data",command=query)
btn_query.grid(row=7,column=0,columnspan=2,pady=10,ipadx=143)

# Delete Entry Box 
del_entry = Entry(root,width=30)
del_entry.grid(row=8,column=1)
del_label=Label(root,text="Number to Delete")
del_label.grid(row=8,column=0)

# Delete Button
btn_del = Button(root,text="Delete The Record",command=delete)
btn_del.grid(row=9,column=0,columnspan=2,padx=2,ipadx=120)

# Commit Changes
conn.commit()

#close connection
conn.close()




root.mainloop()