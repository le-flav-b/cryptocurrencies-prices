import tkinter as tk
from tkinter import messagebox


def show_error() -> None:
    """Open a messagebox that blocks the window from closing
    """
    messagebox.showerror(title="Please Be Patient", message="You can't delete this window")


class LoadingWindow:

    def __init__(self, number_of_actions: int) -> None:
        """Create a loading window during data recovery

        Parameters
        ----------
        number_of_actions: int
        """

        # window settings
        self.root = tk.Tk()
        self.root.title("Data Recovery")
        self.root.geometry("350x100")
        self.root.resizable(False, False)
        self.root.iconbitmap('assets/wait.ico')
        self.root.protocol("WM_DELETE_WINDOW", show_error)

        # initialization of actions
        self.actual_actions = 0
        self.TOTAL_ACTIONS = number_of_actions

        # creation of the animated gif
        self.gif_frames = [tk.PhotoImage(file='assets/wait_animation.gif', format=f'gif -index {i}') for i in range(8)]
        self.gif_label = tk.Label(self.root)
        self.gif_label.place(x=35, y=17)
        self.root.after(0, self.update, 0)

        # creation of the title
        self.title = tk.Label(self.root, text="Please wait...", font=("Helvetica", 14))
        self.title.place(x=120, y=20)

        # creation of the subtitle
        self.subtitle = tk.Label(self.root, text=f"We are collecting data, "
                                                 f"{self.actual_actions}/{self.TOTAL_ACTIONS} collected.")
        self.subtitle.place(x=120, y=50)

    def run(self):
        """Generate the window
        """
        self.root.mainloop()

    def increment(self) -> None:
        """Increment the actions counter
        """

        self.actual_actions += 1
        self.subtitle['text'] = f"We are collecting data, {self.actual_actions}/{self.TOTAL_ACTIONS} collected."

        # destroy the window when all actions are done
        if self.actual_actions >= self.TOTAL_ACTIONS:
            self.root.destroy()

    def update(self, index: int) -> None:
        """Update the gif

        Parameters
        ----------
        index : int
        """

        self.gif_label.configure(image=self.gif_frames[index])

        index += 1
        if index == 8:
            index = 0

        self.root.after(100, self.update, index)

