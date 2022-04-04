
'''
GuiZero Example Use Cases
'''

# from enum import auto
# from tkinter import Grid
from guizero import App, Text, PushButton, TextBox, Picture, Combo, Slider, CheckBox, ButtonGroup, info

# methods
def say_my_name():
    intro.value = my_name.value

def counter():
    text.value = int(text.value) + 1

def change_text_size(slider_value):
    intro.size = slider_value

def do_booking():
    info("Booking", "Thank you for booking")
    print( film_choice.value )
    print( vip_seat.value )
    print( row_choice.value )
    
# MAIN

# General stuff
app = App(title="UDP-Client", width=600, height=500, layout="grid") # grid = [x, y, xspan, yspan]

intro = Text(app, text="Hello Worlds!", size=40, font="Times New Roman", color="lightblue", grid=[0,0])
ok = PushButton(app, text="OK", padx=10, pady=10, grid=[0,1])
my_name = TextBox(app, grid=[0,2])

update_text = PushButton(app, command=say_my_name, text="Display my name", grid=[0,3])

# Utilize work task
text = Text(app, text="1", grid=[0,4])
text.repeat(100, counter)  # run counter method every 100ms

text_size = Slider(app, command=change_text_size, start=10, end=80, grid=[0,5])

# my_cat = Picture(app, image="wow.gif", width=100, height=100, grid=[0,6,5,3])

# Ticket agent example
film_description = Text(app, text="Which film?", grid=[0,7], align="left")
film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"], grid=[1,7], align="left")

vip_seat = CheckBox(app, text="VIP seat?", grid=[0,9], align="left")

seat_location = Text(app, text="Seat location?", grid=[0,10], align="left")

row_choice = ButtonGroup(app, options=[ ["Front", "F"], ["Middle", "M"],["Back", "B"] ],
selected="M", horizontal=True, grid=[1,10], align="left")

book_seats = PushButton(app, command=do_booking, text="Book seat", grid=[0,12], align="left")

app.display() # display loop
