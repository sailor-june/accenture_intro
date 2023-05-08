from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
from PIL import Image, ImageTk


class Application():
    def __init__(self, root):
        self.root = root
        self.root.title("Hello Accenture!")
        self.root.geometry("400x400")
        self.current_slide = 0

        self.slides = [
            {
                'text': 'Hello! my name is Juniper James, but my friends call me June :]',
                'image': None,
                'widget': None
            },
            {
                'text': 'Today, I\'d Like to show you tkinter, a fantastic GUI library for python.',
                'image': None,
                'widget': None
            },
            {
                'text': 'It\'s really easy to add images or other media. Check out this cool acorn I drew!',
                'image': ImageTk.PhotoImage(Image.open("acorn128.png")),
                'widget': None
            },
            {
                'text': 'we can even dynamically add UI elements!',
                'image': None,
                'widget': ttk.Button(self.root, text="DISPLAY CURRENT SLIDE NUMBER", command=self.show_slide_number)
            },
            {
                'text': 'Thanks for watching!',
                'image': None,
                'widget': None
            }
        ]

        self.label = ttk.Label(self.root, text=self.slides[self.current_slide]["text"], wraplength=325, justify='center')
        self.label.pack(pady=50)
        self.image_label=None
        self.previous_button = ttk.Button(self.root, text="Previous", command=self.show_previous, state=DISABLED)
        self.previous_button.pack(side=LEFT, padx=10)
        self.next_button = ttk.Button(self.root, text="Next", command=self.show_next)
        self.next_button.pack(side=RIGHT, padx=10)

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

       

        # Disable the previous button if we've reached the first slide
        if self.current_slide == 0:
            self.previous_button.config(state=DISABLED)
        else:
            self.previous_button.config(state=NORMAL)

        # Disable the next button if we've reached the end of the slides
        if self.current_slide >= len(self.slides)-1:
            self.next_button.config(state=DISABLED)
        else:
            self.next_button.config(state=NORMAL)

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
