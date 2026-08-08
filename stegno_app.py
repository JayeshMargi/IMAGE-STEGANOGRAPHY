from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import os


class Stegno:
    art = r"¯\_(ツ)_/¯"
    art2 = r'''
@(\/)
(\/)-{}-)@
@(={}=)/\)(\/)
(\/(/\)@| (-{}-)
(={}=)@(\/)@(/\)@
(/\)\(={}=)/(\/)
@(\/)\(/\)/(={}=)
(-{}-)""""@/(/\)
|:   |
/::'   \\
/:::     \\
|::'       |
|::        |
\::.       /
':_______.' 
`""""""`
'''

    def main(self, root):
        root.title('Image Steganography')
        root.attributes("-fullscreen", True)
        root.configure(bg="#f5f5f5")

        f = Frame(root, bg="#f5f5f5")
        f.pack(expand=True)

        Label(f, text='Image Steganography', font=('Courier', 40, 'bold'), bg="#f5f5f5").pack(pady=30)
        Button(f, text="Encode", command=lambda: self.frame1_encode(f), font=('Courier', 20), width=15).pack(pady=20)
        Button(f, text="Decode", command=lambda: self.frame1_decode(f), font=('Courier', 20), width=15).pack(pady=20)
        Label(f, text=self.art, font=('Courier', 60), bg="#f5f5f5").pack(pady=10)
        Label(f, text=self.art2, font=('Courier', 12, 'bold'), bg="#f5f5f5", justify=LEFT).pack(pady=10)
        Button(f, text="Exit", font=('Courier', 14), command=root.destroy).pack(pady=30)

    def home(self, frame):
        frame.destroy()
        self.main(root)

    def frame1_encode(self, f):
        f.destroy()
        f2 = Frame(root, bg="#f5f5f5")
        f2.pack(expand=True)
        Label(f2, text='\'\\(°Ω°)/\'', font=('Courier', 70), bg="#f5f5f5").pack(pady=40)
        Label(f2, text='Select the Image in which\nyou want to hide text:', font=('Courier', 20), bg="#f5f5f5").pack(pady=10)
        Button(f2, text='Select', font=('Courier', 18), command=lambda: self.frame2_encode(f2)).pack(pady=10)
        Button(f2, text='Cancel', font=('Courier', 18), command=lambda: self.home(f2)).pack(pady=20)

    def frame2_encode(self, f2):
        f2.destroy()
        ep = Frame(root, bg="#f5f5f5")
        ep.pack(expand=True)

        file_path = filedialog.askopenfilename(filetypes=[('Images', '*.png *.jpeg *.jpg')])
        if not file_path:
            messagebox.showerror("Error", "No file selected.")
            self.home(ep)
            return

        myimg = Image.open(file_path)
        img = ImageTk.PhotoImage(myimg.resize((300, 200)))
        Label(ep, text='Selected Image', font=('Courier', 18), bg="#f5f5f5").pack(pady=10)
        panel = Label(ep, image=img, bg="#f5f5f5")
        panel.image = img
        panel.pack()

        Label(ep, text='Enter the message:', font=('Courier', 18), bg="#f5f5f5").pack(pady=10)
        text_area = Text(ep, width=80, height=10, font=('Courier', 12))
        text_area.pack()

        Button(ep, text='Encode', font=('Courier', 14),
               command=lambda: self.enc_fun(text_area, myimg, file_path, ep)).pack(pady=20)
        Button(ep, text='Cancel', font=('Courier', 14), command=lambda: self.home(ep)).pack()

    def enc_fun(self, text_area, myimg, original_path, frame):
        data = text_area.get("1.0", "end-1c")
        if not data:
            messagebox.showinfo("Alert", "Please enter text to encode.")
            return

        newimg = myimg.copy()
        try:
            self.encode_enc(newimg, data)
        except StopIteration:
            messagebox.showerror("Error", "Image is too small to hold the message.")
            return

        filename = os.path.splitext(os.path.basename(original_path))[0]
        save_path = filedialog.asksaveasfilename(initialfile=f"{filename}_hidden", defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png")])
        if save_path:
            newimg.save(save_path)
            messagebox.showinfo("Success", f"Encoding successful!\nImage saved as:\n{save_path}")
            self.home(frame)

    def genData(self, data):
        return [format(ord(i), '08b') for i in data]

    def modPix(self, pix, data):
        datalist = self.genData(data)
        imdata = iter(pix)
        for i in range(len(datalist)):
            pixels = list(next(imdata)[:3] + next(imdata)[:3] + next(imdata)[:3])
            for j in range(8):
                if datalist[i][j] == '0' and pixels[j] % 2 != 0:
                    pixels[j] -= 1
                elif datalist[i][j] == '1' and pixels[j] % 2 == 0:
                    pixels[j] -= 1
            pixels[-1] = pixels[-1] - 1 if (i == len(datalist) - 1 and pixels[-1] % 2 == 0) or \
                                           (i != len(datalist) - 1 and pixels[-1] % 2 != 0) else pixels[-1]
            yield tuple(pixels[0:3])
            yield tuple(pixels[3:6])
            yield tuple(pixels[6:9])

    def encode_enc(self, newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)
        for pixel in self.modPix(newimg.getdata(), data):
            newimg.putpixel((x, y), pixel)
            x += 1
            if x == w:
                x = 0
                y += 1

    def frame1_decode(self, f):
        f.destroy()
        d_f2 = Frame(root, bg="#f5f5f5")
        d_f2.pack(expand=True)
        Label(d_f2, text='٩(^‿^)۶', font=('Courier', 70), bg="#f5f5f5").pack(pady=40)
        Label(d_f2, text='Select Image with Hidden text:', font=('Courier', 20), bg="#f5f5f5").pack(pady=10)
        Button(d_f2, text='Select', font=('Courier', 18), command=lambda: self.frame2_decode(d_f2)).pack(pady=10)
        Button(d_f2, text='Cancel', font=('Courier', 18), command=lambda: self.home(d_f2)).pack(pady=20)

    def frame2_decode(self, d_f2):
        d_f2.destroy()
        d_f3 = Frame(root, bg="#f5f5f5")
        d_f3.pack(expand=True)
        file_path = filedialog.askopenfilename(filetypes=[('Images', '*.png *.jpeg *.jpg')])
        if not file_path:
            messagebox.showerror("Error", "No file selected.")
            self.home(d_f3)
            return

        myimg = Image.open(file_path)
        img = ImageTk.PhotoImage(myimg.resize((300, 200)))
        Label(d_f3, text='Selected Image:', font=('Courier', 18), bg="#f5f5f5").pack(pady=10)
        panel = Label(d_f3, image=img, bg="#f5f5f5")
        panel.image = img
        panel.pack()

        hidden_data = self.decode(myimg)
        Label(d_f3, text='Hidden Data:', font=('Courier', 18), bg="#f5f5f5").pack(pady=10)
        text_area = Text(d_f3, width=80, height=10, font=('Courier', 12))
        text_area.insert(INSERT, hidden_data)
        text_area.config(state='disabled')
        text_area.pack()

        Button(d_f3, text='Cancel', font=('Courier', 14), command=lambda: self.home(d_f3)).pack(pady=20)

    def decode(self, image):
        data = ''
        imgdata = iter(image.getdata())
        while True:
            pixels = []
            for _ in range(3):
                pixels.extend(next(imgdata)[:3])
            binstr = ''.join(['0' if i % 2 == 0 else '1' for i in pixels[:8]])
            data += chr(int(binstr, 2))
            if pixels[8] % 2 != 0:
                return data


# Launch
if __name__ == '__main__':
    root = Tk()
    app = Stegno()
    app.main(root)
    root.mainloop()
