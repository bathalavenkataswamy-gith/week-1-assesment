
1. Create a virtual environment: `python -m venv .venv`
2. Activate it on Windows: `.venv\Scripts\Activate.ps1`
3. Install dependencies: `python -m pip install -r requirements.txt`
4. Run Task 1: `python src/task1_core.py`
5. Run Task 2: `python src/task2_files_api.py`
6. Run Task 3: `python src/task3_analysis.py`
7. Launch the notebook: `jupyter notebook notebooks/analysis.ipynb`

The `.env` file contains a demo API key and is excluded by `.gitignore`.

Feature branch: analysis implementation and findings documented.

## Findings

- IT has the largest employee headcount at three.
- Sales and HR both have two employees; Finance has one.
- Chennai has four employees in the source data.
- The Finance department has the highest individual and average salary.
- Operations is the department in the outer join that has no employees.

Assessment status: feature complete
