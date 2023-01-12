import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import cm
import tkinter as tk
import random
import scipy.io
import numpy as np
from numpy.fft import fft2


ens_mean=[]
time_mean =0
ACF_arr=[]
ACF_matrix=[]
ACF =0
result = []
time_ACF=[]
X=[]
t=[]
x=[]
PSD_matrix=[]

def read_file():
    global X , t , x
    file= entry.get()
    mat = scipy.io.loadmat(file+'.mat')
    X = mat['X']
    t = mat['t']
    x=t[0]

window = tk.Tk()
window.title("Probabiblty project 2")
window.geometry("900x700")


fig1 = Figure(figsize=(5, 4), dpi=100)
fig2 = Figure(figsize=(5, 4), dpi=100)
fig3 = Figure(figsize=(5, 4), dpi=100)
fig4= Figure(figsize=(5, 4), dpi=100)

ax1 = fig1.add_subplot(111)
ax2 = fig2.add_subplot(111)
ax3 = fig3.add_subplot(111, projection='3d')



fig1.suptitle('M Sample functions')
fig2.suptitle('Ensemble mean')
fig3.suptitle('3D ACF')


mean_box = tk.Label(window, text= "Enter the name of the file:")
mean_box.place(x=10, y=10)
mean_box = tk.Label(window, text= "number of sample function:")
mean_box.place(x=10, y=40)
mean_box = tk.Label(window, text= "Plot ensemble mean:")
mean_box.place(x=500, y=40)

time_mean_text = tk.Label(window, text= "Time mean for nth:")
time_mean_text.place(x=10, y=430)

time_ACF_text = tk.Label(window, text= "Time ACF for nth:")
time_ACF_text.place(x=10, y=580)

value_time_mean = tk.Label(window, text= "Value: ")
value_time_mean.place(x=330, y=400)

i = tk.Label(window, text= "Enter i :")
i.place(x=10, y=480)

j = tk.Label(window, text= "Enter j :")
j.place(x=10, y=530)

taw = tk.Label(window, text= "For alpha = 1")
taw.place(x=350, y=550)

entry = tk.Entry(window)
entry.place(x=170, y=10, width=100, height=25)

entry1 = tk.Entry(window)
entry1.place(x=170, y=40, width=100, height=25)


entry2 = tk.Entry(window)
entry2.place(x=120, y=430, width=100, height=25)

entry3 = tk.Entry(window)
entry3.place(x=60, y=480, width=100, height=25)

entry4 = tk.Entry(window)
entry4.place(x=60, y=530, width=100, height=25)

entry5 = tk.Entry(window)
entry5.place(x=120, y=580, width=100, height=25)

def samples_plot():
    N = int(entry1.get())

    fig1.clf()

    random_rows = random.sample(range(len(X)), N)

    rows = int(np.ceil(np.sqrt(N)))
    cols = int(np.ceil(N / rows))

    for i, j in enumerate(random_rows):
        y = X[j]
        ax1 = fig1.add_subplot(rows, cols, i+1)
        fig1.suptitle("M Sample functions")
        ax1.plot(x, y)

    canvas1.draw()


def calc_ens_mean():
    ax2.cla()
    ens_mean = np.mean(X,axis=0)

    ax2.plot(t[0],ens_mean)
    canvas2.draw()

def calc_time_mean():
    M = int(entry2.get())
    global time_mean
    time_mean = sum(X[M-1]) / len(X[0])
    time_mean_value.set(time_mean)
def calc_ACF_once(I,J):
    ACF =0
    ACF_arr=[]
    for row in X:
        # Multiply the i-th element of the row with the j-th element of the row
        product = row[I] * row[J] * (1/len(X))
        # Append the product to the result list
        ACF_arr.append(product)
    ACF= sum(ACF_arr)
    return ACF

def calc_ACF():
    global time_ACF , ACF_matrix
    ACF_matrix = []
    matrix = []
    I = int(entry3.get())
    J= int(entry4.get())
    print (calc_ACF_once(I-1,J-1))
    ACF_value.set(calc_ACF_once(I-1,J-1))
    matrix = [[0 for x in range(len(X[0]))] for y in range(len(X))]
    for i in range (I,J+1):
        for j in range(I,J+1):
            matrix[i][j] = calc_ACF_once(i-1,j-1)

    N, Y = np.meshgrid(np.arange(0, len(matrix[0])),np.arange(0, len(matrix)))
    Z=np.array(matrix)
    print(len(Z), len(Z[0]))
    ACF_matrix = matrix
    ax3.plot_surface(N, Y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')

    canvas3.draw()


def calc_time_ACF():
    B = int(entry5.get())
    sum = 0
    for i in range (len(X[0])-1):
        sum = sum + (X[B-1][i]*X[B-1][i+1])
    sum = sum *0.1

    time_ACF_value.set(sum)


def calc_PSD():
    global ACF_matrix , PSD_matrix
    ACF_fft = np.fft.fft2(ACF_matrix)
    x_fourier_abs = np.abs(ACF_fft)
    x_fourier_abs_sqr_prob = (x_fourier_abs ** 2) * 1/len(X)
    print(x_fourier_abs_sqr_prob)
    row_sum = x_fourier_abs_sqr_prob.sum(axis=1)
    c = len(X[0])
    print(c)
    row_sum_over_time = row_sum/(x[c-1]-x[0])

    PSD_matrix = row_sum_over_time

def plot_PSD():
    global  PSD_matrix
    plot_window = tk.Toplevel(window)
    ax4 = fig4.add_subplot(111)
    ax4.plot(PSD_matrix)
    canvas4 = FigureCanvasTkAgg(fig4, master=plot_window)
    canvas4.get_tk_widget().pack()


button = tk.Button(window, text="Import", command=read_file)
button.place(x=290, y=10, width=80, height=25)

button1 = tk.Button(window, text="Plot", command=samples_plot)
button1.place(x=290, y=40, width=80, height=25)

button2 = tk.Button(window, text="Plot", command=calc_ens_mean)
button2.place(x=650, y=40, width=80, height=25)

button2 = tk.Button(window, text="Calculate", command=calc_time_mean)
button2.place(x=230, y=430, width=80, height=25)

button3 = tk.Button(window, text="Submit", command=calc_ACF)
button3.place(x=180, y=500, width=80, height=25)

button4 = tk.Button(window, text="Submit", command=calc_time_ACF)
button4.place(x=230, y=580, width=80, height=25)

button5 = tk.Button(window, text="Calculate PSD", command=calc_PSD)
button5.place(x=30, y=620, width=150, height=25)

button6 = tk.Button(window, text="Plot PSD", command=plot_PSD)
button6.place(x=200, y=620, width=100, height=25)

time_mean_value = tk.StringVar()
time_ACF_value = tk.StringVar()
ACF_value = tk.StringVar()

time_mean_label =tk.Entry(window, textvariable=time_mean_value)
time_mean_label.place(x= 330, y = 430)

time_ACF_label =tk.Entry(window, textvariable=time_ACF_value)
time_ACF_label.place(x= 330, y = 580)

ACF_label =tk.Entry(window, textvariable=ACF_value)
ACF_label.place(x= 280, y = 505)



canvas1 = FigureCanvasTkAgg(fig1, master=window)
canvas2 = FigureCanvasTkAgg(fig2, master=window)
canvas3 = FigureCanvasTkAgg(fig3, master=window)

canvas3.get_tk_widget().place(x=480, y=400, width=400, height=300)
canvas1.get_tk_widget().place(x=10, y=75, width=400, height=300)
canvas2.get_tk_widget().place(x=450, y=75, width=400, height=300)

window.mainloop()
