# Student Performance Analyzer

## Project Overview

The **Student Performance Analyzer** is a Python-based Data Science mini project designed to analyze student academic performance using **NumPy, Pandas, and Matplotlib**.

The project reads student data from a CSV file, performs statistical and performance analysis, filters students based on different conditions, calculates correlations, generates visualizations, and exports analyzed results into separate CSV files.

This project demonstrates practical usage of Python libraries for data analysis and visualization.

---

## Objectives

The main objectives of this project are:

- To load and analyze student data using Pandas.
- To perform numerical calculations using NumPy.
- To calculate student averages, grades, and pass/fail status.
- To identify top and low-performing students.
- To analyze attendance, study hours, and assignment scores.
- To calculate correlations between academic factors.
- To visualize student performance using Matplotlib.
- To export processed data into CSV files.

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- CSV

---

## Project Structure

```text
Student-Performance-Analyzer/
│
├── main.py
├── analysis.py
├── visualization.py
├── Student_performance_dataset.csv
├── requirements.txt
├── README.md
│
└── outputs/
    │
    ├── student_analysis_results.csv
    ├── top_10_students.csv
    ├── low_attendance_students.csv
    ├── failed_students.csv
    │
    └── charts/
        ├── subject_average.png
        ├── pass_fail_distribution.png
        ├── attendance_distribution.png
        ├── attendance_vs_average.png
        ├── study_hours_vs_average.png
        ├── top_10_students.png
        ├── grade_distribution.png
        └── correlation_matrix.png
```

---

## Dataset

The dataset contains student-related information such as:

- Student ID
- Name
- Gender
- Age
- City
- Attendance
- Study Hours Per Day
- Assignment Score
- Python Marks
- DAA Marks
- AIP Marks
- DBMS Marks

The project also calculates additional columns:

- Calculated Average
- Calculated Grade
- Calculated Result

---

## Libraries Used

### NumPy

NumPy is used for numerical calculations.

Examples:

```python
np.mean()
np.max()
np.min()
np.median()
np.std()
np.where()
np.select()
```

---

### Pandas

Pandas is used for loading, filtering, processing, and exporting data.

Examples:

```python
pd.read_csv()
data.mean()
data.nlargest()
data.nsmallest()
data.value_counts()
data.corr()
data.to_csv()
```

---

### Matplotlib

Matplotlib is used to create data visualizations.

The project includes:

- Bar charts
- Pie charts
- Histograms
- Scatter plots
- Correlation matrix visualization

---

## Main Features

### Student Average Calculation

The average is calculated using marks from:

- Python
- DAA
- AIP
- DBMS

---

### Pass/Fail Calculation

A student is considered to pass only if the student scores at least 40 marks in every subject.

---

### Grade Calculation

The project assigns grades according to average marks.

| Average | Grade |
|---|---|
| 90 and above | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | F |

---

## Performance Analysis

The project calculates:

- Overall average marks
- Highest mark
- Lowest mark
- Median
- Standard deviation
- Subject-wise average marks
- Top-performing student
- Lowest-performing student
- Top 10 students
- Bottom 10 students

---

## Data Filtering

The project filters students based on different conditions.

Examples include:

### Students with low attendance

```python
data[data["Attendance"] < 75]
```

### Students with an average above 80

```python
data[data["Calculated_Average"] > 80]
```

### Students studying more than 5 hours

```python
data[data["Study_Hours_Per_Day"] > 5]
```

### High-performing students with high attendance

```python
data[
    (data["Attendance"] > 85)
    &
    (data["Calculated_Average"] > 80)
]
```

---

## Correlation Analysis

The project analyzes relationships between:

- Attendance and academic performance
- Study hours and academic performance
- Assignment score and academic performance
- Subject marks and overall average

A correlation value ranges between:

```text
-1 and +1
```

A positive value indicates that the variables generally increase together, while a negative value indicates an inverse relationship.

Correlation does not necessarily prove causation.

---

## Visualizations

The project generates the following graphs:

### Subject Average

Shows the average marks obtained in each subject.

### Pass vs Fail Distribution

Shows the percentage of students who passed and failed.

### Attendance Distribution

Shows how attendance percentages are distributed across students.

### Attendance vs Average Marks

Shows the relationship between attendance and academic performance.

### Study Hours vs Average Marks

Shows how study hours relate to student performance.

### Top 10 Students

Displays the top 10 students based on calculated average.

### Grade Distribution

Shows how many students received each grade.

### Correlation Matrix

Displays correlations among important numerical variables.

---

## Output Files

The project automatically generates several output CSV files.

### student_analysis_results.csv

Contains the complete analyzed dataset.

### top_10_students.csv

Contains the top 10 students.

### low_attendance_students.csv

Contains students whose attendance is below 75%.

### failed_students.csv

Contains students who failed according to the project criteria.

---

## Installation

Clone or download the project.

Open the project folder in VS Code or another Python IDE.

Install the required libraries using:

```bash
pip install -r requirements.txt
```

---

## requirements.txt

The project requires:

```text
numpy
pandas
matplotlib
```

---

## How to Run

Open the terminal inside the project folder.

Run:

```bash
python main.py
```

The program will:

1. Load the student dataset.
2. Analyze student performance.
3. Calculate averages and grades.
4. Filter student records.
5. Perform correlation analysis.
6. Generate graphs.
7. Save processed CSV files.
8. Display a final performance summary.

---

## Project Workflow

```text
Start
  ↓
Load CSV Dataset
  ↓
Check Dataset
  ↓
Prepare Data
  ↓
Calculate Average
  ↓
Calculate Grades
  ↓
Calculate Pass / Fail
  ↓
NumPy Statistical Analysis
  ↓
Student Filtering
  ↓
Top / Bottom Performance Analysis
  ↓
Correlation Analysis
  ↓
Matplotlib Visualizations
  ↓
Export CSV Results
  ↓
Generate Final Summary
  ↓
End
```

---

## Learning Outcomes

By completing this project, I learned how to:

- Work with CSV datasets in Python.
- Use Pandas DataFrames.
- Perform data filtering and manipulation.
- Use NumPy for statistical calculations.
- Calculate and interpret correlations.
- Create graphs using Matplotlib.
- Organize Python code into multiple modules.
- Export processed datasets.
- Build a structured mini Data Science project.

---

## Future Improvements

Possible future enhancements include:

- Add a graphical user interface.
- Add Streamlit dashboard.
- Add machine learning for performance prediction.
- Add subject-wise individual student reports.
- Add automated PDF reports.
- Add interactive filters.
- Connect the project to a database.
- Add login and student record management.

---

## Conclusion

The Student Performance Analyzer demonstrates how Python can be used for practical academic data analysis.

The project combines data processing, statistical analysis, filtering, visualization, and CSV export using NumPy, Pandas, and Matplotlib.

It provides a simple and practical foundation for understanding real-world Data Science workflows.