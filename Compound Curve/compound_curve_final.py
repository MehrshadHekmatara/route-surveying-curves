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
    kilm_intersection = EG2.get()
    azimuth = correct_angle(azimuth)
    kilm_intersection = correct_klm(kilm_intersection)

    #first curve
    cur1_intersection_angle = E1_C1.get()
    cur1_radius = float(E2_C1.get())
    cur1_lenght_point = cur1_radius // 20
    cur1_intersection_angle = correct_angle(cur1_intersection_angle)

    #second curve
    cur2_intersection_angle = E1_C2.get()
    cur2_radius = float(E2_C2.get())
    cur2_lenght_point = cur2_radius // 20
    cur2_intersection_angle = correct_angle(cur2_intersection_angle)

    intersection_angle = cur1_intersection_angle + cur2_intersection_angle

    #T1t1
    cur1_x = cur1_radius * math.tan(math.radians(cur1_intersection_angle / 2))
    #T2t2
    cur2_x = cur2_radius * math.tan(math.radians(cur2_intersection_angle / 2))

    common_tangent = cur1_x + cur2_x

    #t1I
    cur1_x2 = common_tangent * (math.sin(math.radians(cur2_intersection_angle)) / math.sin(math.radians(intersection_angle)))
    #t2I
    cur2_x2 = common_tangent * (math.sin(math.radians(cur1_intersection_angle)) / math.sin(math.radians(intersection_angle)))

    #tool momas vorodi
    first_tangent = cur1_x + cur1_x2
    second_tangent = cur2_x + cur2_x2

    #curve lenght
    curve1_length = cur1_radius * math.radians(cur1_intersection_angle)
    curve2_length = cur2_radius * math.radians(cur2_intersection_angle)
    curve_length = curve1_length + curve2_length

    #mohasebe kilometraj shoro va payan curve
    start_point_klm = kilm_intersection - first_tangent
    end_point_klm = start_point_klm + curve_length

    #calculations for the first curve
    curve1_klm_start = start_point_klm
    curve1_klm_end = curve1_klm_start + curve1_length

    curve1_delta = []
    curve1_kilometraj = []

    curve1_next_multiple = math.ceil(curve1_klm_start / cur1_lenght_point) * cur1_lenght_point

    curve1_data = []
    curve1_point_count = 1
    curve1_data.append((curve1_point_count, round(curve1_klm_start, 3), 0, 0, 0, 0))
    
    curve1_L1 = curve1_next_multiple - curve1_klm_start
    curve1_s1 = (curve1_L1 / (2*cur1_radius)) * (180 / math.pi)
    curve1_c1 = 2 * cur1_radius * math.sin(math.radians(curve1_s1))
    curve1_point_count += 1
    curve1_sum_s = curve1_s1
    curve1_delta.append(curve1_sum_s)
    curve1_data.append((curve1_point_count, round(curve1_next_multiple, 3), round(curve1_s1, 3), round(curve1_sum_s, 4), round(curve1_c1, 3), round(curve1_L1, 4)))

    curve1_c = curve1_length - (curve1_next_multiple - curve1_klm_start)
    curve1_x = curve1_c // cur1_lenght_point
    for i in range(int(curve1_x)):
        if curve1_next_multiple > curve1_klm_end:
            break
        curve1_next_multiple += cur1_lenght_point
        curve1_kilometraj.append(curve1_next_multiple)
        curve1_s = (cur1_lenght_point / (2*cur1_radius)) * (180 / math.pi)
        curve1_c = 2 * cur1_radius * math.sin(math.radians(curve1_s))
        curve1_point_count += 1
        curve1_sum_s += curve1_s
        curve1_delta.append(curve1_sum_s)
        curve1_data.append((curve1_point_count, round(curve1_next_multiple, 3), round(curve1_s, 3), round(curve1_sum_s, 4), round(curve1_c, 3), 50))

    curve1_L2 = curve1_klm_end - curve1_next_multiple
    curve1_s2 = (curve1_L2 / (2*cur1_radius)) * (180 / math.pi)
    curve1_c2 = 2 * cur1_radius * math.sin(math.radians(curve1_s2))
    curve1_sum_s += curve1_s2
    curve1_delta.append(curve1_sum_s)
    curve1_data.append((curve1_point_count + 1, round(curve1_klm_end, 3), round(curve1_s2, 3), round(curve1_sum_s, 4), round(curve1_c2, 3), round(curve1_L2, 4)))

    for row in tree1.get_children():
        tree1.delete(row)

    for row in curve1_data:
        tree1.insert("", "end", values=row)

    #calculations for the second curve
    curve2_klm_start = curve1_klm_end
    curve2_klm_end = curve2_klm_start + curve2_length

    curve2_delta = []
    curve2_kilometraj = []

    curve2_next_multiple = math.ceil(curve2_klm_start / cur2_lenght_point) * cur2_lenght_point

    curve2_data = []
    curve2_point_count = 1
    curve2_data.append((curve2_point_count, round(curve2_klm_start, 3), 0, 0, 0, 0))
    
    curve2_L1 = curve2_next_multiple - curve2_klm_start
    curve2_s1 = (curve2_L1 / (2*cur2_radius)) * (180 / math.pi)
    curve2_c1 = 2 * cur2_radius * math.sin(math.radians(curve2_s1))
    curve2_point_count += 1
    curve2_sum_s = curve2_s1
    curve2_delta.append(curve2_sum_s)
    curve2_data.append((curve2_point_count, round(curve2_next_multiple, 3), round(curve2_s1, 3), round(curve2_sum_s, 4), round(curve2_c1, 3), round(curve2_L1, 4)))

    curve2_c = curve2_length - (curve2_next_multiple - curve2_klm_start)
    curve2_x = curve2_c // cur2_lenght_point
    for i in range(int(curve2_x)):
        if curve2_next_multiple > curve2_klm_end:
            break
        curve2_next_multiple += cur2_lenght_point
        curve2_kilometraj.append(curve2_next_multiple)
        curve2_s = (cur2_lenght_point / (2*cur2_radius)) * (180 / math.pi)
        curve2_c = 2 * cur2_radius * math.sin(math.radians(curve2_s))
        curve2_point_count += 1
        curve2_sum_s += curve2_s
        curve2_delta.append(curve2_sum_s)
        curve2_data.append((curve2_point_count, round(curve2_next_multiple, 3), round(curve2_s, 3), round(curve2_sum_s, 4), round(curve2_c, 3), 50))

    curve2_L2 = curve2_klm_end - curve2_next_multiple
    curve2_s2 = (curve2_L2 / (2*cur2_radius)) * (180 / math.pi)
    curve2_c2 = 2 * cur2_radius * math.sin(math.radians(curve2_s2))
    curve2_sum_s += curve2_s2
    curve2_delta.append(curve2_sum_s)
    curve2_data.append((curve2_point_count + 1, round(curve2_klm_end, 3), round(curve2_s2, 3), round(curve2_sum_s, 4), round(curve2_c2, 3), round(curve2_L2, 4)))

    for row in tree2.get_children():
        tree2.delete(row)

    for row in curve2_data:
        tree2.insert("", "end", values=row)
    
    def plot_curve():
        x_T1 = 0
        y_T1 = 0

        x_int = x_T1 + (first_tangent * math.sin(math.radians(azimuth)))
        y_int = y_T1 + (first_tangent * math.cos(math.radians(azimuth)))

        x_t = x_T1 + ((2 * cur1_radius * math.sin(math.radians(cur1_intersection_angle / 2))) * math.sin(math.radians(azimuth + (cur1_intersection_angle / 2))))
        y_t = y_T1 + ((2 * cur1_radius * math.sin(math.radians(cur1_intersection_angle / 2))) * math.cos(math.radians(azimuth + (cur1_intersection_angle / 2))))

        impl_points_1 = []
        print(curve1_delta)
        for i in curve1_delta:
            l = 2 * cur1_radius * math.sin(math.radians(i))
            x_pt = x_T1 + (l * math.sin(math.radians(azimuth + i)))
            y_pt = y_T1 + (l * math.cos(math.radians(azimuth + i)))
            impl_points_1.append((x_pt, y_pt)) 

        impl_points_2 = []
        for i in curve2_delta:
            l = 2 * cur2_radius * math.sin(math.radians(i))
            x_pt2 = x_t + (l * math.sin(math.radians(azimuth + cur1_intersection_angle + i)))
            y_pt2 = y_t + (l * math.cos(math.radians(azimuth + cur1_intersection_angle + i)))
            impl_points_2.append((x_pt2, y_pt2))
        
        x_T2, y_T2 = impl_points_2[-1]

        plt.figure(figsize=(6, 6))
        plt.scatter([x_int, x_T1, x_t, x_T2], 
                    [y_int, y_T1, y_t, y_T2], color="black", zorder=3)
        plt.text(x_int, y_int, "Intersection", fontsize=10, color="blue", verticalalignment="bottom", horizontalalignment="center")
        plt.text(x_T1, y_T1, "T1", fontsize=10, color="green", verticalalignment="bottom", horizontalalignment="right")
        plt.text(x_T2, y_T2, "T2", fontsize=10, color="orange", verticalalignment="top", horizontalalignment="left")
        plt.text(x_t, y_t, "t", fontsize=10, color="orange", verticalalignment="top", horizontalalignment="left")

        plt.plot([x_T1, x_int], [y_T1, y_int], linestyle="--", color="black", label="Line T1 - Intersection")
        plt.plot([x_T2, x_int], [y_T2, y_int], linestyle="--", color="black", label="Line T2 - Intersection")

        for (x_pt, y_pt), ang in zip(impl_points_1, curve1_delta):
            plt.scatter(x_pt, y_pt, color="green", zorder=4)
            plt.text(x_pt, y_pt, f"angle:{round(ang, 2)}, len:{round(2*cur1_radius*math.sin(math.radians(ang)),2)}", 
                    fontsize=8, color="green", verticalalignment="bottom")
            plt.plot([x_T1, x_pt], [y_T1, y_pt], color="black", linestyle="--", linewidth=0.8)
        plt.plot([x_T1, x_t], [y_T1, y_t], color="black", linestyle="--", linewidth=.80)

        x_vals, y_vals = zip(*impl_points_1)
        plt.plot(x_vals, y_vals, color='blue', linewidth=1.2, zorder=3, label='Curve1')

        for (x_pt, y_pt), ang in zip(impl_points_2, curve2_delta):
            plt.scatter(x_pt, y_pt, color="green", zorder=4)
            plt.text(x_pt, y_pt, f"angle:{round(ang, 2)}, len:{round(2*cur1_radius*math.sin(math.radians(ang)),2)}", 
                    fontsize=8, color="green", verticalalignment="bottom")
            plt.plot([x_t, x_pt], [y_t, y_pt], color="black", linestyle="--", linewidth=0.8)
        
        x_vals, y_vals = zip(*impl_points_2)
        plt.plot(x_vals, y_vals, color='red', linewidth=1.2, zorder=3, label='Curve2')

        plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
        plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
        plt.xlabel("X (meters)")
        plt.ylabel("Y (meters)")
        plt.title("Curve with Tangents and Intersection")
        plt.legend()
        plt.grid()
        plt.axis("equal")
        plt.show()

    plot_curve()



window.title("Compound Curve")

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

LG2 = Label(frame, text="Kilometraj of PI:", font=("Arial", 9, "bold"))
LG2.grid(row=2, column=0, pady=5)
EG2 = Entry(frame)
EG2.grid(row=2, column=1, pady=5)
EG2.insert(0, "14+895.68") 

L0_C1 = Label(frame, text="First Curve Parameters", font=("Arial", 12, "bold"), fg="blue")
L0_C1.grid(row=3, column=0, columnspan=2, pady=10)

L1_C1 = Label(frame, text="Intersection angle:", font=("Arial", 9, "bold"))
L1_C1.grid(row=4, column=0, pady=5)
E1_C1 = Entry(frame)
E1_C1.grid(row=4, column=1, pady=5, padx=20)
E1_C1.insert(0, "28,17,31.2") 

L2_C1 = Label(frame, text="Radius of curve:", font=("Arial", 9, "bold"))
L2_C1.grid(row=5, column=0, pady=5)
E2_C1 = Entry(frame)
E2_C1.grid(row=5, column=1, pady=5)
E2_C1.insert(0, 200) 

L0_C2 = Label(frame, text="second Curve Parameters", font=("Arial", 12, "bold"), fg="blue")
L0_C2.grid(row=8, column=0, columnspan=2, pady=10)

L1_C2 = Label(frame, text="Intersection angle:", font=("Arial", 9, "bold"))
L1_C2.grid(row=9, column=0, pady=5)
E1_C2 = Entry(frame)
E1_C2.grid(row=9, column=1, pady=5, padx=20)
E1_C2.insert(0, "49,42,28.8") 

L2_C2 = Label(frame, text="Radius of curve:", font=("Arial", 9, "bold"))
L2_C2.grid(row=10, column=0, pady=5)
E2_C2 = Entry(frame)
E2_C2.grid(row=10, column=1, pady=5)
E2_C2.insert(0, 128.16) 

B1_C2 = Button(frame, text="Calculate",command=get_values, fg="white", bg="#2b2b2b", relief="raised", borderwidth=3, font=("Arial", 10, "bold"))
B1_C2.grid(row=12, column=0, columnspan=2, pady=10, sticky="ew")

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

tree2.grid(row=13, column=0, columnspan=2, pady=10, sticky="ew")
window.mainloop()

