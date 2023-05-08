from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
from PIL import Image, ImageTk
import random



class Application():
    def __init__(self, root):
        self.root = root
        self.root.title("Hello Accenture!")
        self.root.geometry("400x400")
        self.current_slide = 0
        self.animation_canvas = Canvas(self.root, width=100, height=100)
        self.slides = [
            {
                'text': 'Hello! my name is Juniper James, but my friends call me June :]',
                'image': None,
                'widget': None
            },
            {'text': "I'm a software developer from Northampton massachusetts. I have experience in Javascript, React, Django, Postgresql, Mongoose, and more! I believe interacting with computers should be engaging and easy, and I love working on my craft.",
             "image":None,
             "widget": None},
            {
                'text': 'Today, I\'d Like to show you tkinter, a fantastic GUI library for python. I built this app in python, using TkInter and PIL (the python image library.)',
                'image': None,
                'widget': None
            },
            {
                'text': " First, Why Don't we Adjust the background color? PC gray is kind of boring:",
                'image': None,
                'widget': ttk.Button(self.root, text="pick a background color", command=self.update_color)           },
            {
                'text': "It's really easy to add images or other media. Here's an acorn I drew! ",
                'image': ImageTk.PhotoImage(Image.open("acorn128.png")),
                'widget': None
            },
            {
                'text': f"we can even add dynamic UI elements! There is now a button at the bottom of the screen that tells the current slide number.",
                'image': None,
                'widget': ttk.Button(self.root, text="DISPLAY CURRENT SLIDE #", command=self.show_slide_number)
            },
            {
                'text': 'Check out this cool animation! This ball is not an image, it was drawn by tkinter, and I wrote a little algorithm to randomize the direction.',
                'image': None,
                'widget': self.animation_canvas,
            },
            {
                'text': "overall, we've barely scratched the surface. Tkinter is one of the most widely used GUI libraries for python, so the community support is outstanding. It's very easy to learn and incredibly versatile. Since it is native to python, it plays very well with other libraries such as matplotlib, numpy, and pandas. Because it uses your OS display assets, it is very easy to write cross-platform applications. ",
                'image':None,
                'widget':None

            },
            {
                'text': "Thanks for inviting me today! I'm very excited to meet you and to learn more about the company and the Internship.",
                'image': None,
                'widget': None
            },
               
        ]

        self.color_picker = None
        self.label = ttk.Label(self.root, text=self.slides[self.current_slide]["text"], wraplength=325, justify='center')
        self.label.pack(pady=50)
        self.image_label=None
        self.previous_button = ttk.Button(self.root, text="Previous", command=self.show_previous, state=DISABLED)
        self.previous_button.pack(side=LEFT, padx=10)
        self.next_button = ttk.Button(self.root, text="Next", command=self.show_next)
        self.next_button.pack(side=RIGHT, padx=10)



         # Set up the  animation
        
        self.ball = self.animation_canvas.create_oval(10, 10, 30, 30, fill='red', tags="ball")
        self.animation_canvas.move(self.ball, 0, 0)
        self.animation_direction = 1
        

    def animate(self):
        # Move the ball back and forth on the canvas
        if self.ball is not None:
            x, y, x2, y2 = self.animation_canvas.coords(self.ball)
            if x2 > self.animation_canvas.winfo_width():
                self.animation_direction = -1
            elif x < 0:
                self.animation_direction = 1
            if y2 > self.animation_canvas.winfo_height():
                self.animation_direction_y = -1
            elif y < 0:
                self.animation_direction_y = 1
            if random.random() < 0.01:
                self.animation_direction_x = random.choice([-1, 0, 1])
                self.animation_direction_y = random.choice([-1, 0, 1])

            self.animation_canvas.move(self.ball, self.animation_direction, self.animation_direction_y)
            self.root.after(30, self.animate)
            
    def handle_slide(self):
        

        slide = self.slides[self.current_slide]
        
        # Remove the previous image label from the screen
        if self.image_label is not None:
            self.image_label.destroy()

        # Set the text label
        self.label.config(text=slide['text'])

        # If there is an image, create a new label for it and pack it in
        if slide['image'] is not None:
            self.image_label = ttk.Label(self.root, image=slide['image'])
            self.image_label.pack()
        if self.current_slide!=6:
            self.animation_canvas.delete('ball')
            self.ball=None
            self.animation_canvas.forget()
        else:
            self.ball = self.animation_canvas.create_oval(10, 10, 30, 30, fill='red', tags=["ball"])
            self.animate()
        if slide['widget'] is not None:
            self.widget_label=slide['widget']
            self.widget_label.pack(side=BOTTOM, pady=10)

        #Disable the previous button if we've reached the first slide
        if self.current_slide == 0:
            self.previous_button.config(state=DISABLED)
        else:
            self.previous_button.config(state=NORMAL)

        # Disable the next button if we've reached the end of the slides
        if self.current_slide >= len(self.slides)-1:
            self.next_button.config(state=DISABLED)
        else:
            self.next_button.config(state=NORMAL)
   

    def update_color(self):
        color_code = colorchooser.askcolor()
        root.configure(background=color_code[1])
   
 
    def show_previous(self):
        self.current_slide -= 1
        self.handle_slide()

    def show_next(self):
        self.current_slide += 1
        self.handle_slide()

    def show_slide_number(self):
        slide_number = self.current_slide + 1
        messagebox.showinfo(title="Current Slide Number", message=f"You are on slide {slide_number}")

root = Tk()
app = Application(root)
root.mainloop()