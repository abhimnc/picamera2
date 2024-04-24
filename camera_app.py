import tkinter as tk
from picamera2 import Picamera2
from PIL import Image, ImageTk
import numpy as np

def capture_image():
    # Preview configuration and start the camera
    picam2.start_preview()
    # Give the camera some time to adjust to conditions
    picam2.wait(2)
    # Capture the image
    image = picam2.capture_array()
    # Stop the camera
    picam2.stop_preview()
    # Convert the image to a PIL format and display
    image = Image.fromarray(image)
    image.save("captured_image.jpg")
    # Update the GUI with the captured image
    tk_image = ImageTk.PhotoImage(image)
    image_label.config(image=tk_image)
    image_label.image = tk_image  # Keep a reference!
    print("Image captured and saved as 'captured_image.jpg'")

# Initialize the camera
picam2 = Picamera2()
picam2.configure(picam2.preview_configuration(main={"size": (640, 480)}))

# Setup the Tkinter window
root = tk.Tk()
root.title("Camera Capture")
root.geometry("650x500")

# Button to capture the image
capture_button = tk.Button(root, text="Capture Image", command=capture_image)
capture_button.pack()

# Label to display the image
image_label = tk.Label(root)
image_label.pack()

root.mainloop()
