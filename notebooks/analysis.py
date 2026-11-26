"""Exported Python analysis for the Week 1 Jupyter notebook."""

import numpy as np
import pandas as pd


marks = np.array([
    [78, 82, 74],
    [88, 79, 91],
    [67, 73, 70],
    [92, 85, 89],
])
print("Shape:", marks.shape)
print("Student averages:", marks.mean(axis=1))
print("Subject averages:", marks.mean(axis=0))

employees = pd.read_csv("../data/employees.csv")
dirty = pd.read_csv("../data/employees_dirty.csv")
dirty["salary"] = pd.to_numeric(dirty["salary"], errors="coerce")
dirty["salary"] = dirty["salary"].fillna(dirty["salary"].median())
dirty = dirty.drop_duplicates()
dirty["id"] = dirty["id"].astype(int)
dirty["salary"] = dirty["salary"].astype(float)

print(employees.info())
print(employees.describe())
print(dirty.groupby("department").agg(
    headcount=("name", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max"),
))

departments = pd.read_csv("../data/departments.csv")
outer_join = pd.merge(dirty, departments, on="department", how="outer")
print(outer_join)
print("Department with no employees:",
      outer_join.loc[outer_join["name"].isna(), "department"].tolist())
