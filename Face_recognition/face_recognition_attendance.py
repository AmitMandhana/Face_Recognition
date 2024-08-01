from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        
        # Create a Label for the heading
        heading_label = Label(self.root, text="SMART ATTENDANCE SYSTEM", font=("Impact", 40, "bold"), bg="navy blue", fg="white")
        heading_label.pack(side="top", fill="x")
        
        img = Image.open(r"C:\Users\BISHNU KANTA\Desktop\Face_recognition\image1.jpg")

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Resize the image to match the screen dimensions
        img = img.resize((screen_width, screen_height), Image.ANTIALIAS)

        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.pack(fill="both", expand=True)
        
        author_label = Label(self.root, text="Amit Mandhana", font=("Arial", 16, "bold"), fg="white")
        author_label.pack(side="top", fill="x")
        # Define button data with images and names
        button_data = [
            {"image_path": r"C:\Users\BISHNU KANTA\Desktop\Face_recognition\imagesss\student_details.jpg", "name": "Student Details"},
            {"image_path": r"C:\Users\BISHNU KANTA\Desktop\Face_recognition\imagesss\train_data.jpg", "name": "Face Detector"},
            {"image_path": r"C:\Users\BISHNU KANTA\Desktop\Face_recognition\imagesss\Attendance.jpg", "name": "Attendance"},
            {"image_path": r"C:\Users\BISHNU KANTA\Desktop\Face_recognition\imagesss\Help_desk.jpg", "name": "Help Desk"},
            {"image_path": r"C:\Users\BISHNU KANTA\Desktop\Face_recognition\imagesss\train_data.jpg", "name": "Train Data"},
            {"image_path": r"C:\Users\BISHNU KANTA\Desktop\Face_recognition\imagesss\photos.jpg", "name": "Photos"},
            {"image_path": r"C:\Users\BISHNU KANTA\Desktop\Face_recognition\imagesss\developer.jpg", "name": "Developer"},
            {"image_path": r"C:\Users\BISHNU KANTA\Desktop\Face_recognition\imagesss\exit.jpg", "name": "Exit"},           
        ]

        button_width = 250
        button_height = 260
        gap_x = 50
        gap_y = 50
        padx_value = 40  # Increase the padding in the X-axis

        for i, button_info in enumerate(button_data):
            image_path = button_info["image_path"]
            name = button_info["name"]

            img_button = Image.open(image_path)
            img_button = img_button.resize((button_width, button_height), Image.ANTIALIAS)
            photoimg_button = ImageTk.PhotoImage(img_button)

            col = i % 4
            row = i // 4
            
            x_pos = 100 + col * (button_width + gap_x)
            y_pos = 10 + row * (button_height + gap_y)
            
            button = Button(f_lbl, image=photoimg_button, cursor="hand2", text=name, font=("Arial", 12, "bold"), compound="top", bg="dark blue", fg="white", padx=padx_value, anchor="s")

            button.image = photoimg_button  # To keep a reference to the image
            button.place(x=x_pos, y=y_pos, width=button_width, height=button_height)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()


