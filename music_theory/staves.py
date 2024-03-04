import os
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from music21 import stream, metadata
from PIL import Image, ImageTk
import tkinter as tk
from music21 import environment

environment.set("musescoreDirectPNGPath", "/Applications/MuseScore 4.app/Contents/MacOS/mscore")


def generate_pdf(pdf_filename):
    # Create a PDF with 12 staves
    c = canvas.Canvas(pdf_filename, pagesize=LETTER)
    stave_stream = stream.Stream()
    for _ in range(12):
        stave_stream.append(stream.Measure())
    stave_stream.insert(0, metadata.Metadata())
    stave_stream.metadata.title = "12 Staves"
    # Generate and place stave images on the PDF
    for i, stave in enumerate(stave_stream):
        stave_image_path = f"stave_{i}.png"
        stave.write(fmt="musicxml.png", fp=stave_image_path)
        c.drawImage(stave_image_path, 50, 750 - i * 50, width=500, height=40)
        os.remove(stave_image_path)  # Clean up the temporary image file
    c.save()

def display_preview(window, pdf_filename):
    # Convert the first page of the PDF to an image for preview
    os.system(f"magick convert -density 150 {pdf_filename}[0] preview.png")
    # Display the preview image in the Tkinter window
    img = Image.open("preview.png")
    img = img.resize((300, 400), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=photo)
    label.image = photo
    label.pack()

def main():
    pdf_filename = "staves.pdf"
    generate_pdf(pdf_filename)
    
    # Create a Tkinter window for preview
    window = tk.Tk()
    window.title("PDF Preview")
    display_preview(window, pdf_filename)
    window.mainloop()

if __name__ == "__main__":
    main()
