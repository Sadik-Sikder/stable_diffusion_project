from tkinter import Tk, Label, Entry, Button, PhotoImage
from PIL import Image, ImageTk
import io
import requests

API_URL = "https://api-inference.huggingface.co/models/your model"
HEADERS = {"Authorization": "api key"}
def display_image_from_bytes(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes))
        photo = ImageTk.PhotoImage(image)

        image_label.configure(image=photo)
        image_label.image = photo
    except Exception as e:
        print(f"Error displaying the image: {e}")

def generate_image():
    text_input = entry.get()
    payload = {"inputs": text_input}

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        image_bytes = response.content
        display_image_from_bytes(image_bytes)
    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")

window = Tk()
window.title("Image Generator")

window.geometry("600x500")

label = Label(window, text="Enter Text:")
label.pack()

entry = Entry(window)
entry.pack()

generate_button = Button(window, text="Generate Image", command=generate_image)
generate_button.pack()

image_label = Label(window)
image_label.pack(pady=20) 

window.mainloop()
