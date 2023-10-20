import tkinter as tk

# Your class
class ui_Labels():
    '''This class sets the baseline characteristics 
    for the widgets, including font, font size, and colors
    '''

    # Attributes
    varFont = "Calibri"
    fontSize = 14
    varFG = "#F2F2F2"
    varBG = "#3b3b3b"
    
    # Constructor
    def __init__(self, parent, name, varText):
        self.parent  = parent
        self.name = name
        self.varText = varText

        self.label = tk.Label(
            parent, 
            text = varText, 
            fg = self.varFG, 
            bg = self.varBG, 
            font = (self.varFont, self.fontSize)
            )

    # Allows you to grid as you would normally
    # Can subsitute pack() here or have both class methods
    def grid(self, **kwargs):
        self.label.grid(kwargs)


# Main GUI
root = tk.Tk()



# Create an instance of your class
finalWidget = ui_Labels(root)
finalWidget.grid()

root.mainloop()



hash = {}
hash.update({"Label0" : "Content"})
hash.update({"Label1" : "Content"})
hash.update({"Label2" : "Content"})
hash.update({"Label3" : "Content"})

for key , value in hash:
    finalWidget.grid(key, value)