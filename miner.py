"""Miner."""

import tkinter as tk

FILE_VERSION = '0.0.1'


class Application(tk.Tk):
    """Application."""

    def __init__(self):
        """Create form."""
        tk.Tk.__init__(self)
        self.geometry('192x208')  # Ширина х высота
        self.attributes('-alpha', 1)  # Прозрачность формы (0..1)
        self.attributes('-topmost', True)  # Поверх всех окон
        self.resizable(False, False)  # Изменение размеров окна
        self.title('Miner')
        self.buts = []
        self.col = 8
        self.row = 8
        for i in range(self.row):
            self.buts.append([])
        self.set_ui()  # Наполнение виджетами

    def set_ui(self):
        """Create widgets."""
        for i in range(self.row):
            for j in range(self.col):
                self.buts[i].append(tk.Button(self,
                                              text='',
                                              command=self.press_but,
                                              width=2, height=1))
                self.buts[i][j].grid(row=i, column=j)

    def press_but(self):
        """Press button."""
        print(self.buts)


def main():
    """Basic_function."""
    root = Application()
    root.mainloop()


if __name__ == '__main__':
    main()
