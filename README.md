# 🧮 Salary Analyzer (Python + NumPy CLI Tool)

A simple command-line project built to analyze employee salary data using NumPy — great for beginners looking to get hands-on with data, scripting, and automation.

---

## 👋 About

Hi, I'm **Saran**, and this is one of my learning projects to practice Python and NumPy.  
This project helped me get familiar with:

- Generating random data with NumPy
- Creating command-line tools using `argparse` *(my first time!)*
- Exporting structured data to `.csv` files
- Writing clean, formatted Python code using **Black**

It's part of my learning journey and also something I’m proud to showcase on my GitHub for recruiters and fellow developers.

---

## 💻 Features

✅ Generate random salary data  
✅ Analyze salary stats overall and by department  
✅ Identify high-earning employees  
✅ Export data to `.csv` for further use  
✅ Simple CLI using `argparse`  
✅ Clean code formatting with `black`

---

## 🚀 How to Use

### 1. Install dependencies

```bash
pip install numpy
```
---

### 2. Run the script

```bash
python salary_analyzer.py --summary --departments --high-earners --export
python salary_analyzer.py --summary
python salary_analyzer.py --export
```
---

### 3. Format code
```bash
python -m black salary_analyzer.py
```
---

### 🗂 Sample .csv Output
``` Employee ID,Department,Salary
1,IT,90522
2,Sales,73921
3,HR,63455
...
```
---

### 🌱 Future Plans
``` I plan to:
- Add a simple web UI to make the tool more interactive
- Integrate charts using matplotlib to visualize salary distribution
- Allow users to upload real .csv employee data
```








