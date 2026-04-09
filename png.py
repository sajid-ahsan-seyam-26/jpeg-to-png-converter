from PIL import Image
from tkinter import Tk, filedialog


def convert_jpeg_to_png():
    print("\n--------- JPEG to PNG Converter ---------")

    root = Tk()
    root.withdraw()   

    input_file = filedialog.askopenfilename(
        title="Select a JPEG file",
        filetypes=[("JPEG files", "*.jpg;*.jpeg")]
    )

    if input_file == "":
        print("No file selected.")
        return

    output_file = filedialog.asksaveasfilename(
        title="Save PNG file as",
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")]
    )

    if output_file == "":
        print("No save location selected.")
        return

    try:
        image = Image.open(input_file)
        image.save(output_file, "PNG")
        print("Image converted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)


convert_jpeg_to_png()