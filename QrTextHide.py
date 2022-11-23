from main1 import *
from main1 import shifr
from main1 import findShifr

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import filedialog as fd
import os.path

class QrTextHide(Tk):

    def __init__(self):
        super(QrTextHide, self).__init__()
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(size=12)
        self.option_add("*Font", default_font)
        self.title("Здесь могла быть ваша реклама")
        self.iconphoto(False, PhotoImage(file='i.png'))

        self.img_file = StringVar()
        self.download_path = StringVar()
        self.save_path = StringVar()
        self.path_to_res = StringVar()
        self.length = IntVar()
        self.length.set(-1)

        self.img_file.set('newtext.png')
        self.download_path.set('cat.png')
        self.save_path.set('catWithQr.png')
        self.path_to_res.set('result.png')

        self.tabControlPack()

    def tabControlPack(self):
        self.tabControl = ttk.Notebook(self)
        self.hide_tab()
        self.define_hide_tab()
        self.tabControl.pack(expand=1, fill="both")

    def hide_tab(self):
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Спрятать')

        Label(self.tab1, text="Задайте необходимые данные: ").grid(sticky="W", row=0, column=0)

        Label(self.tab1, text="Где будем прятать? ").grid(sticky="W", row=1, column=0)
        Entry(self.tab1, textvariable=self.img_file).grid(sticky="W", row=1, column=1)
        button1 = Button(self.tab1, text="Открыть", command=lambda: self.file_get('img_file'), bg="#00BFFF")
        button1.grid(sticky="EW", row=1, column=2)

        Label(self.tab1, text="Путь до qr фона: ").grid(sticky="W", row=2, column=0)
        Entry(self.tab1, textvariable=self.download_path).grid(sticky="W", row=2, column=1)
        button2 = Button(self.tab1, text="Открыть", command=lambda: self.file_get('download_path'), bg="#00BFFF")
        button2.grid(sticky="EW", row=2, column=2)

        Label(self.tab1, text="Куда сохранить qr: ").grid(sticky="W", row=3, column=0)
        Entry(self.tab1, textvariable=self.save_path).grid(sticky="W", row=3, column=1)
        button3 = Button(self.tab1, text="Открыть", command=lambda: self.file_get('save_path'), bg="#00BFFF")
        button3.grid(sticky="EW", row=3, column=2)

        Label(self.tab1, text="Куда результат: ").grid(sticky="W", row=4, column=0)
        Entry(self.tab1, textvariable=self.path_to_res).grid(sticky="W", row=4, column=1)
        button4 = Button(self.tab1, text="Открыть", command=lambda: self.file_get('path_to_res'), bg="#00BFFF")
        button4.grid(sticky="EW", row=4, column=2)

        Label(self.tab1, text="Что будем прятать? ").grid(sticky="W", row=6, column=0)
        self.text = Text(self.tab1, height=10, borderwidth=5)
        self.text.grid(sticky="EW", row=7, columnspan=3)

        buttonHide = Button(self.tab1, text="Спрятать", command=self.shifr, bg="#00BFFF")
        buttonHide.grid(sticky="EW", row=8, columnspan=3)

    def define_hide_tab(self):
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text='Найти шифр')

        Label(self.tab2, text="Где результат?").grid(sticky="W", row=0, column=0, padx=(50, 0), pady=(80, 0))
        Entry(self.tab2, textvariable=self.path_to_res).grid(sticky="W", row=0, column=1, padx=(50, 0), pady=(80, 0))
        Label(self.tab2, text="Примерная длина сообщения: ").grid(sticky="W", row=1, column=0, padx=(50, 0), pady=(80, 0))
        Entry(self.tab2, textvariable=self.length).grid(sticky="W", row=1, column=1, padx=(50, 0), pady=(80, 0))
        button1 = Button(self.tab2, text="Открыть", command=lambda: self.file_get('path_to_res'), bg="#00BFFF")
        button1.grid(sticky="EW", row=0, column=2, padx=(50, 0), pady=(80, 0))

        buttonHide = Button(self.tab2, text="Понять и простить", command=self.find_shifr, bg="#00BFFF")
        buttonHide.grid(sticky="EW", row=2, columnspan=3, padx=(100, 0), pady=(100, 0))

    def shifr(self):
        i_f = self.img_file.get()
        text = self.text.get("1.0", "end")[:-1]
        d_f = self.download_path.get()
        s_f = self.save_path.get()
        r_f = self.path_to_res.get()
        if text == '':
            messagebox.showinfo(title="Ошибка", message="Текст не может быть пустым, так неинтересно)")
        elif i_f == '' or  d_f == '' or s_f == '' or r_f == '':
            messagebox.showinfo(title="Ошибка", message="Проверьте пути ")
        elif i_f[-4:] != '.png' or  d_f[-4:] != '.png' or s_f[-4:] != '.png' or r_f[-4:] != '.png':
            messagebox.showinfo(title="Ошибка", message="Проверьте расширение (нужно png)")
        elif not os.path.exists(i_f) or  not os.path.exists(d_f) \
            or not os.path.exists(s_f) or not os.path.exists(r_f):
            messagebox.showinfo(title="Ошибка", message="Проверьте есть ли такие файлы")
        else:
            shifr(i_f, text, d_f, s_f, r_f)
            messagebox.showinfo(title="Выходной файл", message="Данные записаны в " + self.path_to_res.get())

    def find_shifr(self):
        f = self.path_to_res.get()
        l = self.length.get()
        if f == '':
            messagebox.showinfo(title="Ошибка", message="Проверьте пути")
        elif f[-4:] != '.png':
            messagebox.showinfo(title="Ошибка", message="Проверьте расширение (нужно png)")
        elif not os.path.exists(f):
            messagebox.showinfo(title="Ошибка", message="Проверьте есть ли такие файлы")
        else:
            findShifr(f, l)
            messagebox.showinfo(title="Выходной файл", message="Данные записаны в hiddencode.txt и в hiddentext.txt")

    def file_get(self, file):
        if file == 'img_file':
            self.img_file.set(fd.askopenfilename())
        elif file == 'download_path':
            self.download_path.set(fd.askopenfilename())
        elif file == 'save_path':
            self.save_path.set(fd.askopenfilename())
        elif file == 'path_to_res':
            self.path_to_res.set(fd.askopenfilename())
        else:
            pass

window = QrTextHide()
window.mainloop()
