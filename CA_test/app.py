import tkinter as tk
from PIL import Image, ImageTk


window = (tk.Tk())
window.title("Reasons Why I Love Oge")
Label = tk.Label(window, text="Welcome my Princess to the reasons why I Love You So So Much",font=("Arial",16),fg="pink")
Label.pack(pady=10)
reasons = ["You always know what to say when I'm down 😍",
    "You make me laugh even when I don’t want to 😄",
    "You believe in me more than I do 💖",
    "Your hugs feel like home 🤗",
    "You’re my favorite person in the whole world 🌍",
    "Your Ass Jiggles when you walk tooooooo 🍑"
]
image_paths = [
    "reason1.png",
    "reason2.png",
    "reason3.png",
    "reason4.png",
    "reason5.png",
    "reason6.png"
]



reason_index = 0
reason_Label = tk.Label(window, text="", font=("Arial", 14), fg="darkred")
reason_Label.pack(pady=10)

image_Label = tk.Label(window)
image_Label.pack(pady=10)
def show_next_reason():
    global reason_index
    if reason_index <len(reasons):
        reason_Label.config(text=reasons[reason_index])
        image = Image.open(image_paths[reason_index])
        image = image.resize((300,350))
        photo = ImageTk.PhotoImage(image)
        image_Label.config(image=photo)
        image_Label.image = photo

        reason_index +=1
    else:
        reason_Label.config(text="That's not even all!!! There's so much more but i can't list them all but"
                                 " just know you're perfect💕")
        image_Label.config(image='')


button = tk.Button(window, text="Show Me a Reason 💌",command=show_next_reason, fg="darkred")
button.pack(pady=5)



window.mainloop()





