"""Miner."""

import time
import tkinter as tk
from tkinter import messagebox
from random import randint
from tkinter import font

FILE_VERSION = '1.0.1'


class Application(tk.Tk):
    """Application."""

    def __init__(self):
        """Create form."""
        tk.Tk.__init__(self)
        self.geometry('240x260')  # Ширина х высота
        self.attributes('-alpha', 1)  # Прозрачность формы (0..1)
        self.attributes('-topmost', True)  # Поверх всех окон
        self.resizable(False, False)  # Изменение размеров окна
        self.set_vars()  # Создание переменных
        self.title(f'Miner, {self.bombs}')
        self.set_ui()  # Наполнение виджетами
        self.create_bombs(self.bombs)  # Наполнение бомбами
        self.enumer_bombs()  # Маркировка полей
        self.start()

    def set_vars(self):
        """Create variables."""
        self.buts = []  # Кнопки
        self.labs = []  # Цифры
        self.col = 11  # Колонки
        self.row = 11  # Строки
        self.bombs = 25  # Бомбы
        self.clears = (self.row - 1) * (self.col - 1) - self.bombs
        self.bomb_img = tk.PhotoImage(file=r'files\bomb.gif')

    def set_ui(self):
        """Create widgets."""
        for i in range(self.row):
            self.buts.append([])
            self.labs.append([])
            for j in range(self.col):
                self.buts[i].append(tk.Button(
                    self, text='', width=2, height=1, image=self.bomb_img,
                    command=lambda i=i, j=j: self.left_click(i, j)))
                self.buts[i][j].bind('<Button-2>', self.right_click)
                self.buts[i][j].bind('<Button-3>', self.right_click)
                self.buts[i][j].grid(row=i, column=j)
                if i == self.row - 1 or j == self.col - 1:
                    self.buts[i][j]['state'] = 'disabled'
                self.labs[i].append(tk.Label(
                    text='0', width=2, height=1, font=font.nametofont(
                        "TkDefaultFont").configure(weight=font.BOLD)))

    def left_click(self, i, j):
        """Press button."""
        if self.buts[i][j]['text'] != ' ':
            self.clears -= 1
            self.title(f'Miner, {self.bombs}, {self.clears}')
        self.buts[i][j]['text'] = ' '
        self.buts[i][j].grid_remove()
        self.labs[i][j].grid(row=i, column=j)
        print(self.buts[i][j].cget('font'))
        if self.labs[i][j]['text'] == 'X':
            self.labs[i][j]['bg'] = 'red'
            messagebox.showerror('Конец', 'Вы взорвались')
            exit()
        if self.clears == 0:
            self.time = time.time() - self.time
            messagebox.showinfo(
                'Вы победили',
                f'Ваше время: {int(self.time//60)}м {int(self.time%60)}с')
            exit()

    def right_click(self, event):
        """Mark bomb."""
        if event.widget.cget('text') != '@':
            event.widget['text'] = '@'
            event.widget['bg'] = 'yellow'
            event.widget['state'] = 'disabled'
            self.bombs -= 1
            self.title(f'Miner, {self.bombs}, {self.clears}')
        elif event.widget.cget('text') == '@':
            event.widget['text'] = ''
            event.widget.configure(fg='SystemButtonText')
            event.widget.configure(bg='SystemButtonFace')
            event.widget['state'] = 'active'
            self.bombs += 1
            self.title(f'Miner, {self.bombs}, {self.clears}')

    def create_bombs(self, bombs):
        """Create bombs."""
        count_bombs = bombs
        while count_bombs > 0:
            i = randint(0, self.row-2)
            j = randint(0, self.col-2)
            if self.labs[i][j]['text'] == '0':
                self.labs[i][j]['text'] = 'X'
                count_bombs -= 1

    def enumer_bombs(self):
        """Mark bomb."""

        def minirun(mi, mj):
            count = 0
            # Чтобы не выйти за пределы поля
            mii, mjj = mi, mj
            if mi < 1:
                mi += 1
            if mii > 8:
                mii -= 1
            if mj < 1:
                mj += 1
            if mjj > 8:
                mjj -= 1
            # Пробегаем 8 клеток вокруг
            for i in range(mi-1, mii+2):
                for j in range(mj-1, mjj+2):
                    if self.labs[i][j]['text'] == 'X':
                        count += 1
            return count  # Количество бомб вокруг

        for i in range(self.row-1):
            for j in range(self.col-1):
                if self.labs[i][j]['text'] == '0':
                    self.labs[i][j]['text'] = str(minirun(i, j))
                    if self.labs[i][j]['text'] == '1':
                        self.labs[i][j]['fg'] = 'blue'
                    elif self.labs[i][j]['text'] == '2':
                        self.labs[i][j]['fg'] = 'green'
                    elif self.labs[i][j]['text'] == '3':
                        self.labs[i][j]['fg'] = 'red'
                    elif self.labs[i][j]['text'] == '4':
                        self.labs[i][j]['fg'] = 'navy'
                    elif self.labs[i][j]['text'] == '5':
                        self.labs[i][j]['fg'] = 'maroon'
                    elif self.labs[i][j]['text'] == '6':
                        self.labs[i][j]['fg'] = 'cyan'
                    elif self.labs[i][j]['text'] == '7':
                        self.labs[i][j]['fg'] = 'black'
                    elif self.labs[i][j]['text'] == '8':
                        self.labs[i][j]['fg'] = 'white'

    def start(self):
        """Start."""

        def minirun(mi, mj):
            # Чтобы не выйти за пределы поля
            mii, mjj = mi, mj
            if mi < 1:
                mi += 1
            if mii > 8:
                mii -= 1
            if mj < 1:
                mj += 1
            if mjj > 8:
                mjj -= 1
            # Пробегаем 8 клеток вокруг
            for i in range(mi-1, mii+2):
                for j in range(mj-1, mjj+2):
                    self.left_click(i, j)
        if messagebox.askokcancel('Начало', 'Стартуем?'):
            # Раскрываем пустые поля
            self.time = time.time()
            for i in range(self.row-1):
                for j in range(self.col-1):
                    if self.labs[i][j]['text'] == '0':
                        self.labs[i][j]['text'] = ' '
                        minirun(i, j)
        else:
            exit()


def main():
    """Basic_function."""
    root = Application()
    root.mainloop()


if __name__ == '__main__':
    main()
