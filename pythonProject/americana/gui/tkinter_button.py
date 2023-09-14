import tkinter as tk


class MyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("User Input Panel")

        self.create_user_button = tk.Button(root, text="Create User", command=self.create_user)
        self.create_user_button.pack()


    def create_user(self):
        user_input_text = self.user_input.get("1.0", "end-1c")
        print("User input:", user_input_text)

    def user_text(self):
        self.user_input = tk.Text(root, width=40, height=10)
        self.user_input.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = MyGUI(root)
    root.mainloop()
