"""Task 3: NumPy, Pandas, cleaning, merges, and Matplotlib."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)


def numpy_analysis():
    marks = np.array([
        [78, 82, 74],
        [88, 79, 91],
        [67, 73, 70],
        [92, 85, 89],
    ])
    print("Shape:", marks.shape)
    print("Student averages:", np.mean(marks, axis=1))
    print("Subject averages:", np.mean(marks, axis=0))
    with_grace = marks + 5
    weights = np.array([0.30, 0.30, 0.40])
    weighted_scores = np.dot(with_grace, weights)
    print("Weighted scores:", weighted_scores)
    return marks, with_grace, weighted_scores


def pandas_analysis():
    employees = pd.read_csv(DATA / "employees.csv")
    print("\nEmployee info:")
    employees.info()
    print("\nEmployee description:")
    print(employees.describe())
    print("\nloc example:")
    print(employees.loc[employees["city"] == "Chennai", ["name", "salary"]])
    print("\niloc example:")
    print(employees.iloc[:3, [1, 2, 3]])
    print("\nSalary filtering:")
    print(employees[employees["salary"] > 50000])

    dirty = pd.read_csv(DATA / "employees_dirty.csv")
    dirty["salary"] = pd.to_numeric(dirty["salary"], errors="coerce")
    missing_salary_count = int(dirty["salary"].isna().sum())
    duplicate_count = int(dirty.duplicated().sum())
    dirty["salary"] = dirty["salary"].fillna(dirty["salary"].median())
    dirty = dirty.drop_duplicates()
    dirty["id"] = dirty["id"].astype(int)
    dirty["salary"] = dirty["salary"].astype(float)
    print(f"\nCleaning: imputed {missing_salary_count} salaries; removed {duplicate_count} duplicate rows")

    departments = pd.read_csv(DATA / "departments.csv")
    summary = dirty.groupby("department").agg(
        headcount=("name", "count"),
        average_salary=("salary", "mean"),
        maximum_salary=("salary", "max"),
    ).reset_index()

    inner_join = pd.merge(dirty, departments, on="department", how="inner")
    left_join = pd.merge(dirty, departments, on="department", how="left")
    outer_join = pd.merge(dirty, departments, on="department", how="outer")
    no_employees = outer_join.loc[
        outer_join["name"].isna() & outer_join["department"].notna(),
        "department",
    ].tolist()

    print("\nHeadcount:")
    for _, row in summary.iterrows():
        print(f"{row['department']} {int(row['headcount'])}")
    print(
        "Join row counts:",
        f"inner={len(inner_join)}",
        f"left={len(left_join)}",
        f"outer={len(outer_join)}",
    )
    print("\nOuter join: department with no employees:", no_employees)

    dirty.to_csv(REPORTS / "cleaned_employees.csv", index=False)
    summary.to_csv(REPORTS / "department_summary.csv", index=False)
    return employees, dirty, departments, summary, inner_join, left_join, outer_join


def create_charts(employees, departments, summary):
    plt.figure(figsize=(8, 5))
    employee_counts = employees.groupby("department").size()
    employee_counts.plot(kind="bar", color="steelblue", legend=False)
    plt.title("Employees by Department")
    plt.xlabel("Department")
    plt.ylabel("Employee Count")
    plt.tight_layout()
    plt.savefig(REPORTS / "department_headcount.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.hist(employees["salary"], bins=5, color="orange", edgecolor="black")
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(REPORTS / "salary_histogram.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    department_codes = employees["department"].astype("category").cat.codes
    plt.scatter(department_codes, employees["salary"], c="green", label="Employees")
    plt.xticks(range(len(employees["department"].astype("category").cat.categories)),
               employees["department"].astype("category").cat.categories, rotation=30)
    plt.title("Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Salary")
    plt.legend()
    plt.tight_layout()
    plt.savefig(REPORTS / "salary_scatter.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    sorted_summary = summary.sort_values("department")
    plt.plot(sorted_summary["department"], sorted_summary["average_salary"],
             marker="o", color="purple", label="Average Salary")
    plt.title("Average Salary Trend by Department")
    plt.xlabel("Department")
    plt.ylabel("Average Salary")
    plt.legend()
    plt.tight_layout()
    plt.savefig(REPORTS / "salary_line.png", dpi=150)
    plt.close()

    employee_counts = employees.groupby("department").size()
    largest_department = employee_counts.idxmax()
    below_70000 = int((employees["salary"] < 70000).sum())
    highest_paid = employees.loc[employees["salary"].idxmax()]
    highest_average = summary.loc[summary["average_salary"].idxmax()]
    insights = [
        f"Insight: {largest_department} has the largest original headcount "
        f"({employee_counts.max()} employees).",
        f"Insight: {below_70000} of {len(employees)} employees earn below 70,000.",
        f"Insight: {highest_paid['name']} has the highest individual salary "
        f"({highest_paid['salary']:,}).",
        f"Insight: {highest_average['department']} has the highest cleaned average salary "
        f"({highest_average['average_salary']:,.0f}).",
    ]
    return insights


def main():
    numpy_analysis()
    employees, dirty, departments, summary, _, _, outer_join = pandas_analysis()
    insights = create_charts(employees, departments, summary)
    print("\n".join(insights))


if __name__ == "__main__":
    main()
