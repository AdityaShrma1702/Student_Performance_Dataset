import os

os.makedirs("outputs", exist_ok=True)

from analysis import (
    load_data,
    prepare_data,
    numpy_analysis,
    get_topper,
    get_lowest_performer,
    get_subject_averages,
    get_top_10,
    get_bottom_10,
    get_low_attendance,
    get_high_performers,
    get_high_study_students,
    get_failed_students,
    get_best_students,
    get_correlation_matrix,
    get_correlations
)

from visualization import (
    create_output_folder,
    subject_average_chart,
    pass_fail_chart,
    attendance_histogram,
    attendance_vs_average,
    study_hours_vs_average,
    top_10_chart,
    grade_distribution,
    correlation_matrix_chart
)


# --------------------------------
# 1. CREATE OUTPUT FOLDERS
# --------------------------------

os.makedirs(
    "outputs",
    exist_ok=True
)

create_output_folder()


# --------------------------------
# 2. LOAD DATA
# --------------------------------

data = load_data(
    "C:/Users/hp/OneDrive/Desktop/Python Learning Tutorial Youtube/College Mini Projects/Sem1/Python Student-Performance-Analyzer/Student_performance_dataset.csv"
)


# --------------------------------
# 3. PREPARE DATA
# --------------------------------

data = prepare_data(data)


# --------------------------------
# 4. BASIC INFORMATION
# --------------------------------

print("\nFIRST 5 RECORDS:")

print(
    data.head()
)

print("\nDATASET INFO:")

data.info()

print("\nMISSING VALUES:")

print(
    data.isnull().sum()
)


# --------------------------------
# 5. NUMPY ANALYSIS
# --------------------------------

stats = numpy_analysis(data)

print("\nNUMPY ANALYSIS:")

print(
    "Overall Average:",
    round(
        stats["overall_average"],
        2
    )
)

print(
    "Highest Mark:",
    stats["highest_mark"]
)

print(
    "Lowest Mark:",
    stats["lowest_mark"]
)

print(
    "Median:",
    stats["median_mark"]
)

print(
    "Standard Deviation:",
    round(
        stats["standard_deviation"],
        2
    )
)


# --------------------------------
# 6. TOPPER
# --------------------------------

topper = get_topper(data)

print("\nTOPPER:")

print(
    topper["Name"],
    "-",
    topper["Calculated_Average"]
)


# --------------------------------
# 7. LOWEST PERFORMER
# --------------------------------

lowest = get_lowest_performer(data)

print("\nLOWEST PERFORMER:")

print(
    lowest["Name"],
    "-",
    lowest["Calculated_Average"]
)


# --------------------------------
# 8. SUBJECT AVERAGES
# --------------------------------

subject_average = (
    get_subject_averages(data)
)

print("\nSUBJECT AVERAGES:")

print(subject_average)


# --------------------------------
# 9. FILTERING
# --------------------------------

top_10 = get_top_10(data)

bottom_10 = get_bottom_10(data)

low_attendance = (
    get_low_attendance(data)
)

high_performers = (
    get_high_performers(data)
)

high_study_students = (
    get_high_study_students(data)
)

failed_students = (
    get_failed_students(data)
)

best_students = (
    get_best_students(data)
)


print("\nTOP 10 STUDENTS:")

print(
    top_10[
        [
            "Name",
            "Calculated_Average",
            "Calculated_Grade"
        ]
    ]
)


print("\nLOW ATTENDANCE:")

print(
    low_attendance[
        [
            "Name",
            "Attendance",
            "Calculated_Average"
        ]
    ]
)


print("\nFAILED STUDENTS:")

print(
    failed_students[
        [
            "Name",
            "Calculated_Average",
            "Calculated_Result"
        ]
    ]
)


# --------------------------------
# 10. CORRELATION ANALYSIS
# --------------------------------

correlation_matrix = (
    get_correlation_matrix(data)
)

correlations = (
    get_correlations(data)
)

print("\nCORRELATION MATRIX:")

print(
    correlation_matrix.round(2)
)

print("\nIMPORTANT CORRELATIONS:")

print(
    "Attendance vs Average:",
    round(
        correlations["attendance"],
        3
    )
)

print(
    "Study Hours vs Average:",
    round(
        correlations["study_hours"],
        3
    )
)

print(
    "Assignment Score vs Average:",
    round(
        correlations[
            "assignment_score"
        ],
        3
    )
)


# --------------------------------
# 11. SAVE CSV RESULTS
# --------------------------------

data.to_csv(
    "outputs/student_analysis_results.csv",
    index=False
)

top_10.to_csv(
    "outputs/top_10_students.csv",
    index=False
)

low_attendance.to_csv(
    "outputs/low_attendance_students.csv",
    index=False
)

failed_students.to_csv(
    "outputs/failed_students.csv",
    index=False
)


# --------------------------------
# 12. CREATE CHARTS
# --------------------------------

subject_average_chart(
    subject_average
)

pass_fail_chart(
    data
)

attendance_histogram(
    data
)

attendance_vs_average(
    data
)

study_hours_vs_average(
    data
)

top_10_chart(
    top_10
)

grade_distribution(
    data
)

correlation_matrix_chart(
    correlation_matrix
)


# --------------------------------
# 13. FINAL SUMMARY
# --------------------------------

total_students = len(data)

passed = (
    data[
        "Calculated_Result"
    ]
    .value_counts()
    .get(
        "Pass",
        0
    )
)

failed = (
    data[
        "Calculated_Result"
    ]
    .value_counts()
    .get(
        "Fail",
        0
    )
)

best_subject = (
    subject_average.idxmax()
)

weakest_subject = (
    subject_average.idxmin()
)


print("\n" + "=" * 50)

print(
    "STUDENT PERFORMANCE ANALYSIS SUMMARY"
)

print("=" * 50)

print(
    "Total Students:",
    total_students
)

print(
    "Passed Students:",
    passed
)

print(
    "Failed Students:",
    failed
)

print(
    "Topper:",
    topper["Name"]
)

print(
    "Topper Average:",
    topper["Calculated_Average"]
)

print(
    "Best Subject:",
    best_subject
)

print(
    "Weakest Subject:",
    weakest_subject
)

print(
    "Students Below 75% Attendance:",
    len(low_attendance)
)

print(
    "Students Above 80 Average:",
    len(high_performers)
)

print(
    "Students Studying More Than 5 Hours:",
    len(high_study_students)
)

print(
    "High Attendance + High Performance:",
    len(best_students)
)

print("=" * 50)

print(
    "\nAnalysis completed successfully."
)

print(
    "Check the outputs folder for CSV files and charts."
)