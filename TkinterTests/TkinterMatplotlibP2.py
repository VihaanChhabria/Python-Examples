import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from PIL import Image

class Plotter:
    def __init__(self):
        self.fig = plt.Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.points = []

    def plot_data(self, event):
        # Get the coordinates of the clicked point
        x = event.xdata
        y = event.ydata

        if x is not None and y is not None:
            # Get the current marker
            marker = self.marker_var.get()

            # Plot the clicked point with the current marker and the same color
            self.ax.plot(x, y, marker=marker, color='lime')
            self.points.append((x, y, marker))
            self.canvas.draw()

    def clear_plot(self):
        # Clear the current plot
        self.ax.clear()
        self.points = []  # Reset the points
        self.canvas.draw()

    def create_gui(self):
        # Create a Tkinter window
        window = tk.Tk()
        window.title("Matplotlib Graph in Tkinter")

        # Load and resize the image background
        img = plt.imread(r"C:\Users\vihaa\FTC-Autonomous-Planner\FTC_Auto_Planner\MatPlotLibTests\background.jpg")

        # Set the image as the background
        self.ax.imshow(img, extent=[-10, 10, -10, 10])

        # Create a canvas widget to display the graph
        self.canvas = FigureCanvasTkAgg(self.fig, master=window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create a toolbar for the graph
        toolbar = NavigationToolbar2Tk(self.canvas, window)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create buttons to interact with the plot
        self.marker_var = tk.StringVar()
        self.marker_var.set('o')  # Default marker

        circle_button = tk.Radiobutton(window, text="Circle", variable=self.marker_var, value='o')
        circle_button.pack(side=tk.LEFT, padx=10)

        square_button = tk.Radiobutton(window, text="Square", variable=self.marker_var, value='s')
        square_button.pack(side=tk.LEFT, padx=10)

        triangle_button = tk.Radiobutton(window, text="Triangle", variable=self.marker_var, value='^')
        triangle_button.pack(side=tk.LEFT, padx=10)

        clear_button = tk.Button(window, text="Clear", command=self.clear_plot)
        clear_button.pack(side=tk.LEFT, padx=10)

        # Bind the plot_data function to mouse clicks on the canvas
        self.canvas.mpl_connect('button_press_event', self.plot_data)

        # Run the Tkinter event loop
        window.mainloop()


# Create an instance of the Plotter class and run the GUI
plotter = Plotter()
plotter.create_gui()
