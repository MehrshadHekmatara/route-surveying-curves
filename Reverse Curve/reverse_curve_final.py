from tkinter import *
from tkinter import ttk
import math
import matplotlib.pyplot as plt
import numpy as np

window = Tk()

def correct_angle(angle):
    x = angle.split(",")
    return float(x[0]) + float(x[1]) / 60 + float(x[2]) / 3600

def correct_klm(klm):
    x = klm.split("+")
    return float(x[0])*1000 + float(x[1])

def get_values():
    azimuth = EG.get()
    kilm_start = EG2.get()
    azimuth = correct_angle(azimuth)
    kilm_start = correct_klm(kilm_start)
    T1A = float(ED.get())
    T1T2 = float(EQ.get())

    half_curve_intersection_angle = np.rad2deg(math.asin(T1A / T1T2))
    curve_intersection_angle = half_curve_intersection_angle * 2
    
    curve_radius = (T1T2) / (4 * math.sin(math.radians(half_curve_intersection_angle)))

    #first curve
    curve1_lenght_point = curve_radius // 20

    #second curve
    curve2_lenght_point = curve_radius // 20

    curve_length = curve_radius * math.radians(curve_intersection_angle)

    KM_curve1_start = kilm_start
    KM_curve1_end = KM_curve1_start + curve_length
    KM_curve2_start = KM_curve1_end
    KM_curve2_end = KM_curve2_start + curve_length

    curve1_delta = []
    curve1_kilometraj = []

    curve1_next_multiple = math.ceil(KM_curve1_start / curve1_lenght_point) * curve1_lenght_point
    curve1_data = []
    curve1_point_count = 1
    curve1_data.append((curve1_point_count, round(KM_curve1_start, 3), 0, 0, 0, 0))
    
    curve1_L1 = curve1_next_multiple - KM_curve1_start
    curve1_s1 = (curve1_L1 / (2*curve_radius)) * (180 / math.pi)
    curve1_c1 = 2 * curve_radius * math.sin(math.radians(curve1_s1))
    curve1_point_count += 1
    curve1_sum_s = curve1_s1
    curve1_delta.append(curve1_sum_s)
    curve1_data.append((curve1_point_count, round(curve1_next_multiple, 3), round(curve1_s1, 3), round(curve1_sum_s, 4), round(curve1_c1, 3), round(curve1_L1, 4)))

    curve1_c = curve_length - (curve1_next_multiple - KM_curve1_start)
    curve1_x = curve1_c // curve1_lenght_point
    for i in range(int(curve1_x)):
        if curve1_next_multiple > KM_curve1_end:
            break
        curve1_next_multiple += curve1_lenght_point
        curve1_kilometraj.append(curve1_next_multiple)
        curve1_s = (curve1_lenght_point / (2*curve_radius)) * (180 / math.pi)
        curve1_c = 2 * curve_radius * math.sin(math.radians(curve1_s))
        curve1_point_count += 1
        curve1_sum_s += curve1_s
        curve1_delta.append(curve1_sum_s)
        curve1_data.append((curve1_point_count, round(curve1_next_multiple, 3), round(curve1_s, 3), round(curve1_sum_s, 4), round(curve1_c, 3), 50))
    
    curve1_L2 = KM_curve1_end - curve1_next_multiple
    curve1_s2 = (curve1_L2 / (2*curve_radius)) * (180 / math.pi)
    curve1_c2 = 2 * curve_radius * math.sin(math.radians(curve1_s2))
    curve1_sum_s += curve1_s2
    curve1_delta.append(curve1_sum_s)
    curve1_data.append((curve1_point_count + 1, round(KM_curve1_end, 3), round(curve1_s2, 3), round(curve1_sum_s, 4), round(curve1_c2, 3), round(curve1_L2, 4)))

    for row in tree1.get_children():
        tree1.delete(row)

    for row in curve1_data:
        tree1.insert("", "end", values=row)

    curve2_delta = []
    curve2_kilometraj = []

    curve2_next_multiple = math.ceil(KM_curve2_start / curve2_lenght_point) * curve2_lenght_point

    curve2_data = []
    curve2_point_count = 1
    curve2_data.append((curve2_point_count, round(KM_curve2_start, 3), 0, 0, 0, 0))

    curve2_L1 = curve2_next_multiple - KM_curve2_start
    curve2_s1 = (curve2_L1 / (2*curve_radius)) * (180 / math.pi)
    curve2_c1 = 2 * curve_radius * math.sin(math.radians(curve2_s1))
    curve2_point_count += 1
    curve2_sum_s = curve2_s1
    curve2_delta.append(curve2_sum_s)
    curve2_data.append((curve2_point_count, round(curve2_next_multiple, 3), round(curve2_s1, 3), round(curve2_sum_s, 4), round(curve2_c1, 3), round(curve2_L1, 4)))

    curve2_c = curve_length - (curve2_next_multiple - KM_curve2_start)
    curve2_x = curve2_c // curve2_lenght_point
    for i in range(int(curve2_x)):
        if curve2_next_multiple > KM_curve2_end:
            break
        curve2_next_multiple += curve2_lenght_point
        curve2_kilometraj.append(curve2_next_multiple)
        curve2_s = (curve2_lenght_point / (2*curve_radius)) * (180 / math.pi)
        curve2_c = 2 * curve_radius * math.sin(math.radians(curve2_s))
        curve2_point_count += 1
        curve2_sum_s += curve2_s
        curve2_delta.append(curve2_sum_s)
        curve2_data.append((curve2_point_count, round(curve2_next_multiple, 3), round(curve2_s, 3), round(curve2_sum_s, 4), round(curve2_c, 3), 50))
    
    curve2_L2 = KM_curve2_end - curve2_next_multiple
    curve2_s2 = (curve2_L2 / (2*curve_radius)) * (180 / math.pi)
    curve2_c2 = 2 * curve_radius * math.sin(math.radians(curve2_s2))
    curve2_sum_s += curve2_s2
    curve2_delta.append(curve2_sum_s)
    curve2_data.append((curve2_point_count + 1, round(KM_curve2_end, 3), round(curve2_s2, 3), round(curve2_sum_s, 4), round(curve2_c2, 3), round(curve2_L2, 4)))

    for row in tree2.get_children():
        tree2.delete(row)

    for row in curve2_data:
        tree2.insert("", "end", values=row)

    def plot_curve():
        X_T1 = 0
        Y_T1 = 0

        X_T2 = X_T1 + (T1T2 * math.sin(math.radians(azimuth + half_curve_intersection_angle)))
        Y_T2 = Y_T1 + (T1T2 * math.cos(math.radians(azimuth + half_curve_intersection_angle)))

        Y_E =  Y_T1 + (2 * curve_radius * math.sin(math.radians(curve_intersection_angle / 2))) * math.cos(math.radians(azimuth + half_curve_intersection_angle))
        X_E = X_T1 + (2 * curve_radius * math.sin(math.radians(curve_intersection_angle / 2))) * math.sin(math.radians(azimuth + half_curve_intersection_angle))

        impl_points_1 = []
        for i in curve1_delta:
            l = 2 * curve_radius * math.sin(math.radians(i))
            x_pt = X_T1 + (l * math.sin(math.radians(azimuth + i)))
            y_pt = Y_T1 + (l * math.cos(math.radians(azimuth + i)))
            impl_points_1.append((x_pt, y_pt)) 

        impl_points_2 = []
        for i in curve2_delta:
            l = 2 * curve_radius * math.sin(math.radians(i))
            x_pt2 = X_E + (l * math.sin(math.radians(curve_intersection_angle + azimuth - i)))
            y_pt2 = (Y_E + (l * math.cos(math.radians(curve_intersection_angle + azimuth - i))))
            impl_points_2.append((x_pt2, y_pt2))

        plt.figure(figsize=(8, 6))
        plt.plot([X_T1, X_T2], [Y_T1, Y_T2], marker='o', color='black', linestyle='--')
        plt.text(X_T1, Y_T1, 'T1', fontsize=12, ha='right')
        plt.text(X_T2, Y_T2, 'T2', fontsize=12, ha='left')

        plt.plot(X_E, Y_E, marker='o', color='red')

        for (x_pt, y_pt), ang in zip(impl_points_1, curve1_delta):
            plt.scatter(x_pt, y_pt, color="green", zorder=4)
            plt.text(x_pt, y_pt, f"angle:{round(ang, 2)}, len:{round(2*curve_radius*math.sin(math.radians(ang)),2)}", 
                    fontsize=8, color="green", verticalalignment="bottom")
            plt.plot([X_T1, x_pt], [Y_T1, y_pt], color="black", linestyle="--", linewidth=0.8)

        x_vals, y_vals = zip(*impl_points_1)
        plt.plot(x_vals, y_vals, color='blue', linewidth=1.2, zorder=3, label='Curve1')

        for (x_pt, y_pt), ang in zip(impl_points_2, curve2_delta):
            plt.scatter(x_pt, y_pt, color="green", zorder=4)
            plt.text(x_pt, y_pt, f"angle:{round(ang, 2)}, len:{round(2*curve_radius*math.sin(math.radians(ang)),2)}", 
                    fontsize=8, color="green", verticalalignment="bottom")
            plt.plot([X_E, x_pt], [Y_E, y_pt], color="black", linestyle="--", linewidth=0.8)
        
        x_vals, y_vals = zip(*impl_points_2)
        plt.plot(x_vals, y_vals, color='red', linewidth=1.2, zorder=3, label='Curve2')

        plt.grid(True)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Plot of Points T1 and T2')
        plt.axis('equal')
        plt.show()

    plot_curve()

window.title("Reverse Curve")

window.configure(bg="#D3D3D3")

canvas = Canvas(window, bg="#D3D3D3")
canvas.pack(side=LEFT, fill=BOTH, expand=True)

vsb = Scrollbar(window, orient="vertical", command=canvas.yview)
vsb.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=vsb.set)

frame = Frame(canvas, bg="#D3D3D3")
canvas.create_window((0,0), window=frame, anchor="nw")

def onFrameConfigure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", onFrameConfigure)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 600
window_height = 600
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
window.resizable(False, True)

L0 = Label(frame, text="General parameters", font=("Arial", 12, "bold"), fg="blue")
L0.grid(row=0, column=0, columnspan=2, pady=10)

LG = Label(frame, text="Azimuth of road:", font=("Arial", 9, "bold"))
LG.grid(row=1, column=0, pady=5)
EG = Entry(frame)
EG.grid(row=1, column=1, pady=5)
EG.insert(0, "90,0,0") 

LG2 = Label(frame, text="Kilometraj of start point:", font=("Arial", 9, "bold"))
LG2.grid(row=2, column=0, pady=5)
EG2 = Entry(frame)
EG2.grid(row=2, column=1, pady=5)
EG2.insert(0, "14+895.68") 

LD = Label(frame, text="Distance between roads", font=("Arial", 9, "bold"))
LD.grid(row=3, column=0, pady=5)
ED = Entry(frame)
ED.grid(row=3, column=1, pady=5)
ED.insert(0, 30) 

LQ = Label(frame, text="Distance between start point and end point", font=("Arial", 9, "bold"))
LQ.grid(row=4, column=0, pady=5)
EQ = Entry(frame)
EQ.grid(row=4, column=1, pady=5)
EQ.insert(0, 120) 

L0 = Label(frame, text="First Curve Parameters", font=("Arial", 12, "bold"), fg="blue")
L0.grid(row=5, column=0, columnspan=2, pady=10)

L0 = Label(frame, text="second Curve Parameters", font=("Arial", 12, "bold"), fg="blue")
L0.grid(row=8, column=0, columnspan=2, pady=10)

B1_C2 = Button(frame, text="Calculate",command=get_values, fg="white", bg="#2b2b2b", relief="raised", borderwidth=3, font=("Arial", 10, "bold"))
B1_C2.grid(row=11, column=0, columnspan=2, pady=10, sticky="ew")

tree1 = ttk.Treeview(frame, columns=("pointNumber", "Kilometraj", "S Angle", "Stotal", "C Length", "arc"), show="headings")
tree1.heading("arc", text="طول کمان دهنه")
tree1.heading("pointNumber", text="شماره نقاط")
tree1.heading("Stotal", text="زاویه انحراف کل")
tree1.heading("S Angle", text="زاویه انحراف جز")
tree1.heading("C Length", text="طول وتر")
tree1.heading("Kilometraj", text="کیلومتراژ")

tree1.column("pointNumber", width=70, anchor="center")
tree1.column("Kilometraj", width=100, anchor="center")
tree1.column("S Angle", width=100, anchor="center")
tree1.column("Stotal", width=100, anchor="center")
tree1.column("C Length", width=100, anchor="center")
tree1.column("arc", width=100, anchor="center")

tree1.grid(row=7, column=0, columnspan=2, pady=10, sticky="ew")

tree2 = ttk.Treeview(frame, columns=("pointNumber", "Kilometraj", "S Angle", "Stotal", "C Length", "arc"), show="headings")
tree2.heading("arc", text="طول کمان دهنه")
tree2.heading("pointNumber", text="شماره نقاط")
tree2.heading("Stotal", text="زاویه انحراف کل")
tree2.heading("S Angle", text="زاویه انحراف جز")
tree2.heading("C Length", text="طول وتر")
tree2.heading("Kilometraj", text="کیلومتراژ")

tree2.column("pointNumber", width=70, anchor="center")
tree2.column("Kilometraj", width=100, anchor="center")
tree2.column("S Angle", width=100, anchor="center")
tree2.column("Stotal", width=100, anchor="center")
tree2.column("C Length", width=100, anchor="center")
tree2.column("arc", width=100, anchor="center")

tree2.grid(row=10, column=0, columnspan=2, pady=10, sticky="ew")
window.mainloop()
