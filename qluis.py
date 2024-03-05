import tkinter as tk
import tkinter.ttk as ttk
import requests
from PIL import Image
import urllib

url = "https://any-anime.p.rapidapi.com/v1/anime/png/1"


class GuiApp:
    count = 0
    headers = {}
    def __init__(self, master=None):
        self.count = 1
        self.headers = {
            "X-RapidAPI-Key": "e92da39f38msh9c7e4b7b4d98fc9p1cb968jsnf74d12c3fa29",
            "X-RapidAPI-Host": "any-anime.p.rapidapi.com"
        }

        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.configure(height=278, width=226)
        self.toplevel1.resizable(False, False)
        self.gen_button = ttk.Button(self.toplevel1, name="gen_button")
        self.gen_button.configure(text='GENERATE', command=self.gen)
        self.gen_button.pack(anchor="n", fill="both", side="top")
        self.canvas1 = tk.Canvas(self.toplevel1)
        self.canvas1.configure(background="#747474", height=225, width=225)
        self.canvas1.pack(side="bottom")
        self.button2 = ttk.Button(self.toplevel1, name="button2")
        self.button2.configure(text='DOWNLOAD', command=self.download)
        self.button2.pack(anchor="n", fill="both", side="top")
        self.toplevel1.pack_propagate(False)

        # Main widget
        self.mainwindow = self.toplevel1

    def gen(self):
        global response
        response = requests.get(url, headers=self.headers).json()['images'][0]
        print(response)

        image_url = response
        resp = requests.get(image_url)

        image_format = 'png'
        image_data = resp.content

        img = tk.PhotoImage(data=image_data, format=image_format)
        self.canvas1.create_image(0, 0, anchor=tk.NW, image=img)
        self.canvas1.image = img

    def download(self):
        res = requests.get(response)

        print(f'{self.count}')
        with open(f'avatar{self.count}.png', 'wb') as f:
            self.count = self.count + 1
            f.write(res.content)







    def run(self):

        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = GuiApp()
    app.run()
