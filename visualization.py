import os
import matplotlib.pyplot as plt


def create_output_folder():

    os.makedirs(
        "outputs/charts",
        exist_ok=True
    )


def subject_average_chart(subject_average):

    plt.figure(figsize=(8, 5))

    plt.bar(
        subject_average.index,
        subject_average.values
    )

    plt.title("Average Marks by Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")

    plt.ylim(0, 100)

    plt.grid(axis="y")

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/subject_average.png"
    )

    plt.show()


def pass_fail_chart(data):

    result_count = (
        data["Calculated_Result"]
        .value_counts()
    )

    plt.figure(figsize=(6, 6))

    plt.pie(
        result_count.values,
        labels=result_count.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title(
        "Pass vs Fail Distribution"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/pass_fail_distribution.png"
    )

    plt.show()


def attendance_histogram(data):

    plt.figure(figsize=(8, 5))

    plt.hist(
        data["Attendance"],
        bins=10,
        edgecolor="black"
    )

    plt.title(
        "Attendance Distribution"
    )

    plt.xlabel(
        "Attendance Percentage"
    )

    plt.ylabel(
        "Number of Students"
    )

    plt.grid(axis="y")

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/attendance_distribution.png"
    )

    plt.show()


def attendance_vs_average(data):

    plt.figure(figsize=(8, 5))

    plt.scatter(
        data["Attendance"],
        data["Calculated_Average"]
    )

    plt.title(
        "Attendance vs Average Marks"
    )

    plt.xlabel(
        "Attendance Percentage"
    )

    plt.ylabel(
        "Average Marks"
    )

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/attendance_vs_average.png"
    )

    plt.show()


def study_hours_vs_average(data):

    plt.figure(figsize=(8, 5))

    plt.scatter(
        data["Study_Hours_Per_Day"],
        data["Calculated_Average"]
    )

    plt.title(
        "Study Hours vs Average Marks"
    )

    plt.xlabel(
        "Study Hours Per Day"
    )

    plt.ylabel(
        "Average Marks"
    )

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/study_hours_vs_average.png"
    )

    plt.show()


def top_10_chart(top_10):

    plt.figure(figsize=(10, 6))

    plt.bar(
        top_10["Name"],
        top_10["Calculated_Average"]
    )

    plt.title(
        "Top 10 Students"
    )

    plt.xlabel(
        "Students"
    )

    plt.ylabel(
        "Average Marks"
    )

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.ylim(0, 100)

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/top_10_students.png"
    )

    plt.show()


def grade_distribution(data):

    grade_order = [
        "A+",
        "A",
        "B",
        "C",
        "D",
        "F"
    ]

    grade_count = (
        data["Calculated_Grade"]
        .value_counts()
        .reindex(
            grade_order,
            fill_value=0
        )
    )

    plt.figure(figsize=(8, 5))

    plt.bar(
        grade_count.index,
        grade_count.values
    )

    plt.title(
        "Grade Distribution"
    )

    plt.xlabel("Grades")
    plt.ylabel(
        "Number of Students"
    )

    plt.grid(axis="y")

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/grade_distribution.png"
    )

    plt.show()


def correlation_matrix_chart(
    correlation_matrix
):

    plt.figure(figsize=(10, 8))

    plt.imshow(
        correlation_matrix,
        aspect="auto"
    )

    plt.colorbar(
        label="Correlation"
    )

    plt.xticks(
        range(
            len(correlation_matrix.columns)
        ),
        correlation_matrix.columns,
        rotation=45,
        ha="right"
    )

    plt.yticks(
        range(
            len(correlation_matrix.index)
        ),
        correlation_matrix.index
    )

    plt.title(
        "Correlation Matrix"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/correlation_matrix.png"
    )

    plt.show()