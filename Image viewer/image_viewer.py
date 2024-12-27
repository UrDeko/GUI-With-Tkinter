import os
import tkinter as tk

IMAGE_PATH = "GUI with Tkinter/Image viewer/Photos"


class ImageViewer():

    def __init__(self, images):
        self.images = images
        self.img_idx = 0

        self.root = tk.Tk()
        self.root.title("Image Viewer")
        self.root.geometry("+800+200")

        self.default_img = tk.PhotoImage(file=self.images[self.img_idx])
        self.expose_img = tk.Label(self.root, image=self.default_img)
        self.expose_img.grid(row=0, column=0, columnspan=2)

        self.btn_backward = tk.Button(self.root, text="<<", width=5, height=2, command=lambda: self._switch_image(-1), state=tk.DISABLED)
        self.btn_backward.grid(row=1, column=0, pady=7, sticky=tk.W+tk.E)
        self.btn_forward = tk.Button(self.root, text=">>", width=5, height=2, command=lambda: self._switch_image(1))
        self.btn_forward.grid(row=1, column=1, pady=7, sticky=tk.W+tk.E)

        self.status_bar = tk.Label(self.root, bd=1, anchor=tk.E, relief=tk.SUNKEN, padx=5, pady=3)
        self.status_bar.grid(row=2, columnspan=3, sticky=tk.E+tk.W)

        self._update_status()

        self.root.mainloop()

    def _switch_image(self, margin):
        """Switch between images"""

        self.img_idx += margin
        self.btn_forward.config(state=tk.NORMAL)
        self.btn_backward.config(state=tk.NORMAL)

        new_image = tk.PhotoImage(file=self.images[self.img_idx])
        self.expose_img.config(image=new_image)
        self.expose_img.image = new_image

        if self.img_idx + 1 == len(self.images):
            self.btn_forward.config(state=tk.DISABLED)
        if self.img_idx - 1 < 0:
            self.btn_backward.config(state=tk.DISABLED)

        self._update_status()

    def _update_status(self):
        """Display current image's sequence number"""

        self.status_bar.config(text="{}/{}".format(self.img_idx + 1, len(self.images)))


if __name__ == "__main__":

    images = []
    for file in os.listdir(IMAGE_PATH):
        if file.endswith(".png"):
            images.append("GUI with Tkinter/Image viewer/Photos/" + file)

    img_vwr = ImageViewer(images=images)