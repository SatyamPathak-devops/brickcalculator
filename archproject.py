import tkinter as tk

class BrickCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Brick Calculator")

        # Create labels and entry fields for length, breadth and height
        self.length_label = tk.Label(master, text="Length (in meters):")
        self.length_label.grid(row=0, column=0)
        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1)

        self.breadth_label = tk.Label(master, text="Breadth (in meters):")
        self.breadth_label.grid(row=1, column=0)
        self.breadth_entry = tk.Entry(master)
        self.breadth_entry.grid(row=1, column=1)

        self.height_label = tk.Label(master, text="Height (in meters):")
        self.height_label.grid(row=2, column=0)
        self.height_entry = tk.Entry(master)
        self.height_entry.grid(row=2, column=1)

        # Create radio buttons for selecting brick type
        self.brick_type_label = tk.Label(master, text="Select Brick Type:")
        self.brick_type_label.grid(row=3, column=0)

        self.brick_type = tk.StringVar()
        self.brick_type.set("Clay Bricks")

        self.clay_bricks = tk.Radiobutton(master, text="Clay Bricks", variable=self.brick_type, value="Clay Bricks")
        self.clay_bricks.grid(row=4, column=0)

        self.concrete_bricks = tk.Radiobutton(master, text="Concrete Bricks", variable=self.brick_type, value="Concrete Bricks")
        self.concrete_bricks.grid(row=4, column=1)

        self.fly_ash_bricks = tk.Radiobutton(master, text="Fly Ash Bricks", variable=self.brick_type, value="Fly Ash Bricks")
        self.fly_ash_bricks.grid(row=5, column=0)

        self.engineering_bricks = tk.Radiobutton(master, text="Engineering Bricks", variable=self.brick_type, value="Engineering Bricks")
        self.engineering_bricks.grid(row=5, column=1)

        # Create button for calculating total bricks and cost
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=6, column=0)

        # Create labels for displaying total bricks and cost
        self.total_bricks_label = tk.Label(master, text="Total Bricks:")
        self.total_bricks_label.grid(row=7, column=0)
        self.total_bricks_value = tk.Label(master, text="")
        self.total_bricks_value.grid(row=7, column=1)

        self.total_cost_label = tk.Label(master, text="Approximate Total Cost:")
        self.total_cost_label.grid(row=8, column=0)
        self.total_cost_value = tk.Label(master, text="")
        self.total_cost_value.grid(row=8, column=1)

    def calculate(self):
        # Get the values of length, breadth and height from entry fields
        length = float(self.length_entry.get())
        breadth = float(self.breadth_entry.get())
        height = float(self.height_entry.get())

        # Calculate the total number of bricks required
        if self.brick_type.get() == "Clay Bricks":
            brick_length = 0.222 # in meters
            brick_breadth = 0.106 # in meters
            brick_height = 0.073 # in meters
            brick_cost = 7 # in rupees
        elif self.brick_type.get() == "Concrete Bricks":
            brick_length = 0.225 # in meters
            brick_breadth = 0.113 # in meters
            brick_height = 0.075 # in meters
            brick_cost = 6 # in rupees
        elif self.brick_type.get() == "Fly Ash Bricks":
            brick_length = 0.230 # in meters
            brick_breadth = 0.110 # in meters
            brick_height = 0.070 # in meters
            brick_cost = 5 # in rupees
        elif self.brick_type.get() == "Engineering Bricks":
            brick_length = 0.215 # in meters
            brick_breadth = 0.103 # in meters
            brick_height = 0.065 # in meters
            brick_cost = 10 # in rupees

        total_brick_length = length + 0.01 # in meters
        total_brick_breadth = breadth + 0.01 # in meters
        total_brick_height = height + 0.01 # in rupees

        bricks_per_row = int(total_brick_length / brick_length)
        rows = int(total_brick_breadth / brick_breadth)
        total_bricks = rows * bricks_per_row

        # Calculate the total cost of bricks
        total_cost = total_bricks * brick_cost

        # Display the total number of bricks and cost
        self.total_bricks_value.config(text=str(total_bricks))
        self.total_cost_value.config(text=str(total_cost))

root = tk.Tk()
my_gui = BrickCalculator(root)
root.mainloop()