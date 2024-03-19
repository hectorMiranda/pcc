import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import threading

def take_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('photo.jpg', frame)
        show_photo('photo.jpg')
    cap.release()

def show_photo(photo_path):
    img = Image.open(photo_path)
    img = img.resize((640, 480), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img)
    panel.image = img

def record_video():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('video.avi', fourcc, 20.0, (640, 480))

    def recording():
        while recording_btn['text'] == 'Stop Recording':
            ret, frame = cap.read()
            if ret:
                out.write(frame)
            else:
                break

    threading.Thread(target=recording).start()

def toggle_recording():
    if recording_btn['text'] == 'Record Video':
        recording_btn['text'] = 'Stop Recording'
        record_video()
    else:
        recording_btn['text'] = 'Record Video'

app = tk.Tk()
app.title("Webcam Capture")

panel = tk.Label(app)
panel.pack()

photo_btn = tk.Button(app, text="Take Photo", command=take_photo)
photo_btn.pack(side=tk.LEFT, padx=10)

recording_btn = tk.Button(app, text="Record Video", command=toggle_recording)
recording_btn.pack(side=tk.RIGHT, padx=10)

app.mainloop()
