
# Week 1 Assessment

## Setup

1. Create a virtual environment: `python -m venv .venv`
2. Activate it on Windows: `.venv\Scripts\Activate.ps1`
3. Install dependencies: `python -m pip install -r requirements.txt`
4. Run Tasks 1–3: `python src/task1_core.py`, `python src/task2_files_api.py`, and `python src/task3_analysis.py`
5. Run the focused Task 3 tests: `python -m unittest discover -s tests -v`
6. Launch the notebook: `jupyter notebook notebooks/analysis.ipynb`

The `.env` file is optional for the public JSONPlaceholder API and is excluded by `.gitignore`.

## Task 3: NumPy, Pandas, and Matplotlib

- NumPy reports the marks array shape, student and subject averages, and weighted scores.
- Pandas inspects and filters employee data, imputes missing salaries with the median, removes duplicates, groups salaries by department, and demonstrates inner, left, and outer joins.
- The cleaned employee data and department summary are written to `reports/cleaned_employees.csv` and `reports/department_summary.csv`.
- Four charts are generated under `reports/`: department headcount, salary histogram, salary scatter, and average-salary line chart.
- Data-based findings and join row counts are printed when the analysis runs.

## Task 4: Git and GitHub workflow

The repository history records the Task 1–3 implementation, feature-branch work, a real README merge conflict and its resolution, and the final merge to `main`. For this Task 3/4 completion, `feature/task-3-task-4` was pushed, reviewed in [pull request #1](https://github.com/bathalavenkataswamy-gith/week-1-assesment/pull/1), and merged to `main`. The graph and workflow evidence are in `reports/git_log.txt` and `reports/task4_git_evidence.txt`.

To repeat the feature-branch workflow for new work:

```powershell
git checkout -b feature/<short-description>
git add <files>
git commit -m "Describe the change"
git push -u origin feature/<short-description>
git checkout main
git merge feature/<short-description>
git push origin main
```

For a merge conflict, edit the conflicted file to retain the intended content, then run `git add <file>` and `git commit` to complete the merge.

## Findings

- IT has the largest employee headcount at three.
- Sales and HR both have two employees; Finance has one.
- Chennai has four employees in the source data.
- The Finance department has the highest individual and average salary.
- Operations is the department in the outer join that has no employees.

Assessment status: merged and complete
