from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")

    response.raise_for_status()

    # print(response)
    #get a 200 so okay 

    #get the data at a json format
    data = response.json()
    # print(data) => data print okay 
    kanye_quote = data["quote"]
    
    canvas.itemconfig(quote_text, text= kanye_quote)
    #=> print the quote OK
    #Write your code here.



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=300, height=414, bg="white", highlightthickness=0)
background_img = PhotoImage(file="./kanye-quotes-start/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye once says...", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="./kanye-quotes-start/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()