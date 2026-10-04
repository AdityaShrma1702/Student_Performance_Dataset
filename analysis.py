import numpy as np
import pandas as pd


SUBJECTS = ["Python", "DAA", "AIP", "DBMS"]


def load_data(file_path):
    return pd.read_csv(file_path)


def prepare_data(data):
    data = data.copy()

    data["Calculated_Average"] = (
        data[SUBJECTS].mean(axis=1)
    )

    data["Calculated_Result"] = np.where(
        data[SUBJECTS].min(axis=1) >= 40,
        "Pass",
        "Fail"
    )

    conditions = [
        data["Calculated_Average"] >= 90,
        data["Calculated_Average"] >= 80,
        data["Calculated_Average"] >= 70,
        data["Calculated_Average"] >= 60,
        data["Calculated_Average"] >= 50
    ]

    grades = [
        "A+",
        "A",
        "B",
        "C",
        "D"
    ]

    data["Calculated_Grade"] = np.select(
        conditions,
        grades,
        default="F"
    )

    return data


def numpy_analysis(data):
    marks = data[SUBJECTS].to_numpy()

    return {
        "overall_average": np.mean(marks),
        "highest_mark": np.max(marks),
        "lowest_mark": np.min(marks),
        "median_mark": np.median(marks),
        "standard_deviation": np.std(marks)
    }


def get_topper(data):
    index = data["Calculated_Average"].idxmax()

    return data.loc[index]


def get_lowest_performer(data):
    index = data["Calculated_Average"].idxmin()

    return data.loc[index]


def get_subject_averages(data):
    return data[SUBJECTS].mean()


def get_top_10(data):
    return data.nlargest(
        10,
        "Calculated_Average"
    )


def get_bottom_10(data):
    return data.nsmallest(
        10,
        "Calculated_Average"
    )


def get_low_attendance(data):
    return data[
        data["Attendance"] < 75
    ]


def get_high_performers(data):
    return data[
        data["Calculated_Average"] > 80
    ]


def get_high_study_students(data):
    return data[
        data["Study_Hours_Per_Day"] > 5
    ]


def get_failed_students(data):
    return data[
        data["Calculated_Result"] == "Fail"
    ]


def get_best_students(data):
    return data[
        (data["Attendance"] > 85)
        &
        (data["Calculated_Average"] > 80)
    ]


def get_correlation_matrix(data):

    columns = [
        "Attendance",
        "Study_Hours_Per_Day",
        "Assignment_Score",
        "Python",
        "DAA",
        "AIP",
        "DBMS",
        "Calculated_Average"
    ]

    return data[columns].corr()


def get_correlations(data):

    attendance_corr = data[
        "Attendance"
    ].corr(
        data["Calculated_Average"]
    )

    study_corr = data[
        "Study_Hours_Per_Day"
    ].corr(
        data["Calculated_Average"]
    )

    assignment_corr = data[
        "Assignment_Score"
    ].corr(
        data["Calculated_Average"]
    )

    return {
        "attendance": attendance_corr,
        "study_hours": study_corr,
        "assignment_score": assignment_corr
    }