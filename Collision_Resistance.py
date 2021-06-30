import hashlib
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def generate_hash(key):
    """
    This method will generate an SHA2 hash on supplied key
    :param key: string to generate hash
    :return: sha2 in string
    """
    return hashlib.new("sha256", key.encode()).hexdigest()

def truncate_hash(hash):
    """
    This method will truncate the hash into a six digit OTP.
    :param hash: sha2
    :return: otp
    """
    truncated = str(int(hash, 16))[-6:]
    return truncated

def plot_cr1(cr1):
    window = Tk()

    # setting the title
    window.title('Plotting in Tkinter')

    # dimensions of the main window
    window.geometry("700x500")

    # the figure that will contain the plot
    fig = Figure(figsize=(7, 7), dpi=100)

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(cr1)

    plot1.set_xlabel('Number of OTPs')
    plot1.set_ylabel('Number of matching OTPs')

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

    window.mainloop()

def plot_cr2(cr2):
    window = Tk()

    # setting the title
    window.title('Plotting in Tkinter')

    # dimensions of the main window
    window.geometry("700x500")

    # the figure that will contain the plot
    fig = Figure(figsize=(7, 7), dpi=100)

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(cr2)

    plot1.set_xlabel('Number of OTPs')
    plot1.set_ylabel('Number of two consecutive OTPs')

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

    window.mainloop()


if __name__ == '__main__':
    # First key supplied to generate otp
    seed = "8EEE70FF00FF080F2"
    count = 0

    # 2 empty lists to save otps and crs
    list_otp = set()
    list_crs = set()

    list_cr1 = []
    list_cr2 = []

    prev_otp = 0

    for i in range(1000000):
        # returned sha2 will become the new seed here
        seed = generate_hash(seed)
        # get otp from seed (i.e. sha2)
        otp = truncate_hash(seed)

        if otp in list_otp:
            list_cr1.append(list_cr1[-1] + 1)
        else:
            list_cr1.append(0 if len(list_cr1) is 0 else list_cr1[-1])
            list_otp.add(otp)

        if prev_otp == otp:
            list_cr2.append(list_cr2[-1] + 1)
        else:
            list_cr2.append(0 if len(list_cr2) is 0 else list_cr2[-1])

        prev_otp = otp

    plot_cr1(list_cr1)
    plot_cr2(list_cr2)
