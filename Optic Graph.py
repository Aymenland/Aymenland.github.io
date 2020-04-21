# -*-coding:Latin-1 -*

from tkinter import *
from math import atan, tan, fabs, floor
from time import sleep


class opticGraph:
    def __init__(self, master):
        master.iconbitmap('eye.ico')
        self.master = master

        self.menu = Menu(master)
        self.master.config(menu=self.menu)
        self.File_menu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.File_menu)
        self.File_menu.add_command(label="New Graph ...", command=self.newGraph)

        self.frame = Frame(master, bg="lightgrey", borderwidth=0, bd=0)
        self.frame.grid(row=2, column=1)
        self.can = Canvas(self.frame, highlightthickness=0, width="500", height="350", bg="#606060", bd=2,
                          relief="groove")
        self.can.grid(row=1, pady=5)

        self.can.create_line(250, 350 / 4, 250, 3 * (350 / 4), fill="silver")
        self.can.create_line(0, 350 / 2, 505, 350 / 2, fill="silver")
        self.can.create_line(250, 350 / 4, 255, (350 / 4) + 8, fill="silver")
        self.can.create_line(250, 350 / 4, 245, (350 / 4) + 8, fill="silver")
        self.can.create_line(250, 3 * (350 / 4), 255, 3 * (350 / 4) - 8, fill="silver")
        self.can.create_line(250, 3 * (350 / 4), 245, 3 * (350 / 4) - 8, fill="silver")
        self.F = self.can.create_line(190, (350 / 2) - 2, 190, (350 / 2) + 3, fill="silver")
        self.F1 = self.can.create_line(310, (350 / 2) - 2, 310, (350 / 2) + 3, fill="silver")
        self.can.create_text(240, 185, text="O", fill="silver")
        self.F_text = self.can.create_text(190, 188, text="F", fill="silver")
        self.F1_text = self.can.create_text(310, 188, text="F'", fill="silver")
        self.AB = -1
        self.A_text = self.can.create_text(220, (350 / 2) + 12, text="A", fill="white")
        self.B_text = self.can.create_text(220, (350 / 2) - 42, text="B", fill="white")

        self.frame1 = Frame(self.frame, bd=2, relief="groove", bg="dark grey")
        self.frame1.grid(row=2, padx=8)

        self.OF_dis = Scale(self.frame1, sliderrelief="ridge", length="147", orient=HORIZONTAL,
                            label="Distance Focale (OF) :", troughcolor="#606060", sliderlength=20, showvalue=0,
                            from_=45, to=120, tickinterval=25, bg="dark grey", command=self.updateOf,
                            highlightthickness=0, bd=2, state="normal")
        self.OF_dis.grid(row=1, column=1, ipadx=5, ipady=2, pady=5, padx=3)
        self.OA_dis = Scale(self.frame1, sliderrelief="ridge", length="147", orient=HORIZONTAL,
                            label="Distance Centre - Objet (OA) :", troughcolor="#606060", sliderlength=20,
                            showvalue=0, from_=30, to=150, tickinterval=40, command=self.updateOa, bg="dark grey",
                            highlightthickness=0, bd=2, state="normal")
        self.OA_dis.grid(row=1, column=2, ipadx=5, ipady=2, padx=3)
        self.AB_dis = Scale(self.frame1, sliderrelief="ridge", length="147", orient=HORIZONTAL,
                            label="Longueur de l'Objet (AB) :", troughcolor="#606060", sliderlength=20,
                            showvalue=0, from_=20, to=50, tickinterval=10, bg="dark grey", command=self.updateAb,
                            highlightthickness=0, bd=2, state="normal")
        self.AB_dis.grid(row=1, column=3, ipadx=5, ipady=2, padx=3)

        self.frame2 = Frame(self.frame, bd=2, relief="groove", bg="dark grey")
        self.frame2.grid(row=3, pady=5)

        self.draw = Button(self.frame2, text="Draw", bg="lightgrey", width="8", height="3", relief="groove",
                           command=self.drawIt)
        self.draw.grid(row=1, column=1, padx=3, pady=5)
        self.result = Canvas(self.frame2, width="413", height="52", bg="#F3F3F3", bd=2, relief="sunken")
        self.result.grid(row=1, column=2, padx=4)
        self.result.create_line(-5, 20, 203, 20, fill="#BDBDBD")
        self.result.create_line(-5, 40, 203, 40, fill="#BDBDBD")
        self.result.create_line(215, 20, 417, 20, fill="#BDBDBD")
        self.result.create_line(215, 40, 417, 40, fill="#BDBDBD")
        self.result.create_line(209, -5, 209, 57, fill="#BDBDBD")

    def updateOf(self, x):
        x = 250 - int(x)
        z = self.can.coords(self.F)[0] - x
        self.can.move(self.F, -z, 0)
        self.can.move(self.F_text, -z, 0)
        self.can.move(self.F1, z, 0)
        self.can.move(self.F1_text, z, 0)

    def updateOa(self, x):
        x = 250 - int(x)
        z = self.can.coords(self.A_text)[0] - x
        self.can.move(self.A_text, -z, 0)
        self.can.move(self.B_text, -z, 0)
        self.can.move(self.AB, -z, 0)

    def updateAb(self, x):
        self.can.delete(self.AB)
        x = (350 / 2) - int(x)
        z = self.can.coords(self.B_text)[1] + 12 - x
        self.can.move(self.B_text, 0, -z)
        self.AB = self.can.create_line(self.can.coords(self.A_text)[0], self.can.coords(self.A_text)[1] - 12,
                                       self.can.coords(self.B_text)[0], self.can.coords(self.B_text)[1] + 12,
                                       fill="white")

    def drawIt(self):
        self.OF_dis.configure(state="disabled")
        self.OA_dis.configure(state="disabled")
        self.AB_dis.configure(state="disabled")
        self.draw.configure(state="disabled")
        ab = self.can.coords(self.AB)[1] - self.can.coords(self.AB)[3]
        oa = 250 - self.can.coords(self.AB)[0]
        of = 250 - self.can.coords(self.F)[0]
        a = atan(ab / oa)
        b = atan(ab / of)
        first_time = True
        dx1 = 1
        dx3 = 1
        dy1 = tan(a) * dx1
        dy3 = tan(b) * dx3
        x1 = self.can.coords(self.AB)[2] + dx1
        y1 = self.can.coords(self.AB)[3] + dy1
        x2 = self.can.coords(self.AB)[2] + dx1
        y2 = self.can.coords(self.AB)[3]
        x3 = self.can.coords(self.AB)[2] + oa + dx1
        y3 = self.can.coords(self.AB)[3] + dy3
        line1 = -1
        line2 = -1
        line3 = -1
        x_collision = -1
        y_collision = -1
        image_dis = -1
        y = -1
        if (tan(a) - tan(b)) != 0:
            x_collision = 250 - (ab / (tan(a) - tan(b)))
            y_collision = tan(a) * (x_collision - 250) + 175

        while x1 < 505 and y1 < 355:
            if first_time:
                line1 = self.can.create_line(self.can.coords(self.AB)[2], self.can.coords(self.AB)[3], x1, y1,
                                             fill="orange")
                line2 = self.can.create_line(self.can.coords(self.AB)[2], self.can.coords(self.AB)[3], x2, y2,
                                             fill="orange")
                dx1 += 1
                dy1 = tan(a) * dx1
                x1 = self.can.coords(self.AB)[2] + dx1
                y1 = self.can.coords(self.AB)[3] + dy1
                x2 = self.can.coords(self.AB)[2] + dx1
                y2 = self.can.coords(self.AB)[3]
                first_time = False

                self.master.update()
                sleep(0.007)
            else:
                self.can.delete(line1, line3)
                line1 = self.can.create_line(self.can.coords(self.AB)[2], self.can.coords(self.AB)[3], x1, y1,
                                             fill="orange")
                if x2 < 252:
                    line2 = self.can.create_line(self.can.coords(self.AB)[2], self.can.coords(self.AB)[3], x2, y2,
                                                 fill="orange")

                if self.can.coords(line2)[2] == 251:
                    line3 = self.can.create_line(self.can.coords(self.AB)[2] + oa, self.can.coords(self.AB)[3], x3, y3,
                                                 fill="orange")
                    dx3 += 1
                    dy3 = tan(b) * dx3
                    x3 = self.can.coords(self.AB)[2] + oa + dx3
                    y3 = self.can.coords(self.AB)[3] + dy3
                dx1 += 1
                dy1 = tan(a) * dx1
                x1 = self.can.coords(self.AB)[2] + dx1
                y1 = self.can.coords(self.AB)[3] + dy1
                x2 = self.can.coords(self.AB)[2] + dx1
                y2 = self.can.coords(self.AB)[3]

                self.master.update()
                sleep(0.007)

        first_time = True
        y_new1 = y_collision - 1
        y_new2 = y_collision + 1
        image = -1
        dx1 = -1
        dx3 = -1
        dy1 = tan(a) * dx1
        dy3 = tan(b) * dx3
        x1 = self.can.coords(self.AB)[2] + dx1
        y1 = self.can.coords(self.AB)[3] + dy1
        x3 = self.can.coords(self.AB)[2] + oa + dx1
        y3 = self.can.coords(self.AB)[3] + dy3

        if 352 > y_collision > 0 and 502 > x_collision > 0:
            if x_collision > self.can.coords(self.AB)[0] and y_collision > self.can.coords(self.AB)[1]:
                while y_new1 > 174:
                    if first_time:
                        image = self.can.create_line(x_collision, y_collision, x_collision, y_new1, fill="white")
                        y_new1 -= 1
                        first_time = False
                        self.master.update()
                        sleep(0.01)
                    else:
                        self.can.delete(image)
                        image = self.can.create_line(x_collision, y_collision, x_collision, y_new1, fill="white")
                        y_new1 -= 1
                        self.master.update()
                        sleep(0.01)
                image_dis = fabs(y_collision - y_new1)
                y = - image_dis / ab
                self.can.create_text(x_collision, y_collision + 12, text="B'", fill="white")
                self.can.create_text(x_collision, y_new1 - 12, text="A'", fill="white")
            elif x_collision < self.can.coords(self.AB)[0] and y_collision < self.can.coords(self.AB)[1]:
                while y_new2 < 176 or x1 > x_collision or x3 > x_collision:
                    if first_time:
                        line1 = self.can.create_line(self.can.coords(self.AB)[2], self.can.coords(self.AB)[3], x1,
                                                     y1)
                        line3 = self.can.create_line(self.can.coords(self.AB)[2] + oa, self.can.coords(self.AB)[3],
                                                     x3, y3, fill="orange")
                        image = self.can.create_line(x_collision, y_collision, x_collision, y_new2, fill="white")
                        y_new2 += 1
                        dx1 -= 1
                        dx3 -= 1.51
                        dy1 = tan(a) * dx1
                        dy3 = tan(b) * dx3
                        x1 = self.can.coords(self.AB)[2] + dx1
                        y1 = self.can.coords(self.AB)[3] + dy1
                        x3 = self.can.coords(self.AB)[2] + oa + dx3
                        y3 = self.can.coords(self.AB)[3] + dy3
                        first_time = False
                        self.master.update()
                        sleep(0.01)
                    else:
                        if x1 > x_collision:
                            self.can.delete(line1)
                            line1 = self.can.create_line(self.can.coords(self.AB)[2], self.can.coords(self.AB)[3], x1,
                                                         y1, fill="orange")
                        if x3 > x_collision:
                            self.can.delete(line3)
                            line3 = self.can.create_line(self.can.coords(self.AB)[2] + oa, self.can.coords(self.AB)[3],
                                                         x3, y3, fill="orange")
                        if y_new2 < 176:
                            self.can.delete(image)
                            image = self.can.create_line(x_collision, y_collision, x_collision, y_new2, fill="white")
                            y_new2 += 1
                        dx1 -= 1
                        dx3 -= 1.51
                        dy1 = tan(a) * dx1
                        dy3 = tan(b) * dx3
                        x1 = self.can.coords(self.AB)[2] + dx1
                        y1 = self.can.coords(self.AB)[3] + dy1
                        x3 = self.can.coords(self.AB)[2] + oa + dx3
                        y3 = self.can.coords(self.AB)[3] + dy3
                        self.master.update()
                        sleep(0.01)
                image_dis = fabs(y_collision - y_new2)
                y = image_dis / ab
                self.can.create_text(x_collision, y_collision - 12, text="B'", fill="white")
                self.can.create_text(x_collision, y_new2 + 12, text="A'", fill="white")

        if x_collision > 500 or y_collision > 350 or ((x_collision < 1 or y_collision < 1) and x_collision != -1):
            self.result.create_text(100, 13, text="Collision didn't happen !", fill="#606060")
            self.result.create_text(100, 33, text="At least not on my screen !", fill="#606060")
        elif x_collision == -1 and y_collision == -1:
            self.result.create_text(100, 14, text="Collision will never happen !", fill="#606060")
            self.result.create_text(100, 33, text="Don't try me ! I'm good !", fill="#606060")
        else:
            c = 1 / of
            self.result.create_text(100, 14, text="Collision did happen !", fill="#606060")
            self.result.create_text(100, 33, text="C = " + str(floor(c * 1000) / 1000), fill="#606060")
            self.result.create_text(320, 14, text="A'B' = " + str(image_dis), fill="#606060")
            self.result.create_text(320, 33, text="Y = " + str(floor(y * 1000) / 1000), fill="#606060")

    def newGraph(self):
        i = self.can.find_all()[len(self.can.find_all()) - 1]
        j = self.result.find_all()[len(self.result.find_all()) - 1]
        while i > 15:
            if i in self.can.find_all():
                self.can.delete(i)
            i -= 1
            self.can.delete(self.AB)
            self.AB = self.can.create_line(self.can.coords(self.A_text)[0], self.can.coords(self.A_text)[1] - 12,
                                           self.can.coords(self.B_text)[0], self.can.coords(self.B_text)[1] + 12,
                                           fill="white")

        while j > 5:
            if j in self.result.find_all():
                self.result.delete(j)
            j -= 1

        self.OF_dis.configure(state="normal")
        self.OA_dis.configure(state="normal")
        self.AB_dis.configure(state="normal")
        self.draw.configure(state="normal")


# -----> Game Execute <----- #

if __name__ == "__main__":
    root = Tk()
    root.title('Optic Graph ( By Aymen SAIDI )')
    game = opticGraph(root)
    root.mainloop()
