# Route Surveying (Curves)

**Route surveying** is a branch of surveying that focuses on the planning, design, and setting out of routes such as roads, railways, pipelines, and canals. It involves the determination and layout of horizontal and vertical alignments, as well as geometric elements like curves and gradients, to ensure safe and efficient transportation systems.

In this project, we focus on the calculation and implementation of **circular curves**, including:
- **Simple curves**
- **Compound curves**
- **Reverse curves**

These types of curves are fundamental components in route design and are used to connect straight path segments while maintaining smooth transitions and proper alignment in road or railway construction.

## 📁 Simple Circular Curve

### 🔷 What is a Simple Circular Curve?

A **simple circular curve** is a curve with a constant radius that connects two straight (tangent) lines. It is the most basic form of a horizontal curve used in route surveying and ensures a smooth transition between two tangents. This curve is defined by parameters such as the radius (R), central angle (Δ), tangent length (T), and arc length (L), and is widely used in road and railway design to provide gradual change in direction.

---

### 📄 Folder Contents

- **`simple_curve_final.py`**
- 
  This is the main Python file that implements the calculation and visualization of simple circular curves. The program includes a graphical user interface (GUI) built using Tkinter and utilizes mathematical functions for geometric computations.
   
  **Used modules:**
  
  - `tkinter`, `tkinter.ttk`: for GUI design
  - `math`: for mathematical operations 
  - `matplotlib.pyplot`: for plotting the curve
  - `numpy`: for numerical operations

- **`simple_curve_guide.pdf`**
- 
  A PDF guide containing the fundamental formulas and diagrams related to simple circular curves. This serves as a helpful reference for understanding the mathematical background behind the calculations.

---

### ⚙️ Installation

To run the Python script, make sure the following Python modules are installed:

```bash
pip install matplotlib numpy
```

## 📁 Compound Circular Curve

### 🔷 What is a Compound Circular Curve?

A **compound circular curve** consists of two or more simple circular curves of different radius that bend in the same direction and share a common tangent point. These curves are used when space constraints or design requirements do not allow for a single-radius curve. Compound curves provide a smoother and more flexible transition in alignment changes, especially in mountainous or complex terrain.

Key parameters include the radii of each arc (R₁, R₂), their respective central angles, and the tangent lengths. Compound curves are commonly found in advanced road and railway projects where a single curve cannot satisfy all design constraints.

---

### 📄 Folder Contents

- **`compound_curve_final.py`**
- 
  This is the main Python script that calculates and visualizes compound curves using a graphical user interface (GUI) built with Tkinter. It includes support for entering geometric parameters and visual feedback through plotting.
  
  **Used modules:**
  
  - `tkinter`, `tkinter.ttk`: for GUI interface
  - `math`: for geometric and trigonometric calculations
  - `matplotlib.pyplot`: for plotting the compound curve
  - `numpy`: for numerical arrays and operations

- **`compound_curve_guide.pdf`**
- 
  A reference document containing essential formulas and concepts used in compound curve design. This guide supports understanding and manual verification of the calculated values.

---

### ⚙️ Installation

Make sure the required Python modules are installed before running the script:

```bash
pip install matplotlib numpy
```

## 📁 Reverse Circular Curve

### 🔷 What is a Reverse Circular Curve?

A **reverse circular curve** is formed by two simple curves with equal or different radii that turn in opposite directions, connected directly without a tangent in between. This type of curve is used when a change in direction is required within a limited space, often seen in railway switch yards, mountain roads, or transition zones.

In this project, a special case of reverse curves is implemented, where **both paths are parallel**, and the reverse curve allows transitioning smoothly from one path to the other. This geometry requires careful calculation to ensure the tangents align and the movement is smooth and symmetric.

---

### 📄 Folder Contents

- **`reverse_curve_final.py`**
- 
  The main Python script for calculating and visualizing reverse curves in the case of parallel paths. It includes a user-friendly GUI built with Tkinter for entering parameters and displays the resulting geometry graphically.
  
  **Used modules:**
  
  - `tkinter`, `tkinter.ttk`: for creating the graphical interface
  - `math`: for geometric calculations
  - `matplotlib.pyplot`: for plotting the reverse curve
  - `numpy`: for numerical operations and array handling

- **`reverse_curve_guide.pdf`**
- 
  A detailed reference file containing the formulas and geometric principles for reverse curves, specifically tailored to the parallel-path scenario.

---

### ⚙️ Installation

To run the reverse curve script, install the necessary Python modules using the following command:

```bash
pip install matplotlib numpy
```

---

## 📊 Output

✅ Computed parameters of circular curves (R, Δ, T, L, E, M, etc.)

✅ Interactive GUI for inputting and visualizing curve geometry

✅ Plotted diagrams for:

- Simple curves
- Compound curves
- Reverse curves (parallel paths)

These visual and numerical outputs assist in validating design accuracy and understanding geometric behavior in route surveying.

---

## 📍 Applications

- Road and railway design
- Horizontal alignment planning
- Route optimization in transportation projects
- Educational tool for surveying students

---

## 🤝 Contributing

Feel free to fork this repository and contribute by:

- Improving the GUI/UX
- Adding support for spiral (clothoid) curves
- Extending the tool to vertical curves or 3D visualization
- Refactoring code for modularity and testing

Pull requests are very welcome!

---

## 📌 Citation & Usage

If you use this project or parts of its code in your work, please cite the source as follows:

> "This project was developed by Mehrshad Hekmatara as part of a study on circular curve computations in route surveying. Source available at: https://github.com/MehrshadHekmatara/route-surveying-curves"

✅ Usage with proper credit is allowed for educational, academic, and professional purposes.

---

## 👤 Author

**Mehrshad Hekmatara**  

Surveying Engineering, University of Tehran  

GitHub: https://github.com/MehrshadHekmatara
  
Email: hekmataramehrshad532@gmail.com
