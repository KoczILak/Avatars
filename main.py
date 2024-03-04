import tkinter as tk
import tkinter.ttk as ttk
import requests
from PIL import Image
import urllib

url = "https://any-anime.p.rapidapi.com/v1/anime/png/1"


class GuiApp:
    count = 1
    def __init__(self, master=None):
        headers = {
            "X-RapidAPI-Key": "e92da39f38msh9c7e4b7b4d98fc9p1cb968jsnf74d12c3fa29",
            "X-RapidAPI-Host": "any-anime.p.rapidapi.com"
        }

        def gen():
            global response
            response = requests.get(url, headers=headers).json()['images'][0]
            print(response)

            image_url = response
            resp = requests.get(image_url)

            image_format = 'png'
            image_data = resp.content

            img = tk.PhotoImage(data=image_data, format=image_format)
            canvas1.create_image(0, 0, anchor=tk.NW, image=img)
            canvas1.image = img


        def download():

            res = requests.get(response)

            print(f'{count}')
            with open(f'avatar{count}.png', 'wb') as f:
                f.write(res.content)

                count = count + 1

        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=278, width=226)
        toplevel1.resizable(False, False)
        gen_button = ttk.Button(toplevel1, name="gen_button")
        gen_button.configure(text='GENERATE', command=gen)
        gen_button.pack(anchor="n", fill="both", side="top")
        canvas1 = tk.Canvas(toplevel1)
        canvas1.configure(background="#747474", height=225, width=225)
        canvas1.pack(side="bottom")
        button2 = ttk.Button(toplevel1, name="button2")
        button2.configure(text='DOWNLOAD', command=download)
        button2.pack(anchor="n", fill="both", side="top")
        toplevel1.pack_propagate(0)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):

        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = GuiApp()
    app.run()
