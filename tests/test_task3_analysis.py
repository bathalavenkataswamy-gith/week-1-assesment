import contextlib
import io
import unittest

import numpy as np

from src.task3_analysis import create_charts, numpy_analysis, pandas_analysis


class Task3AnalysisTests(unittest.TestCase):
    def test_numpy_analysis_returns_expected_dimensions_and_scores(self):
        marks, adjusted_marks, weighted_scores = numpy_analysis()

        self.assertEqual(marks.shape, (4, 3))
        self.assertTrue((adjusted_marks == marks + 5).all())
        np.testing.assert_allclose(weighted_scores, [82.6, 91.5, 75.0, 93.7])

    def test_cleaning_grouping_and_all_join_types(self):
        with contextlib.redirect_stdout(io.StringIO()):
            employees, cleaned, departments, summary, inner, left, outer = pandas_analysis()

        self.assertEqual(len(employees), 8)
        self.assertEqual(len(cleaned), 8)
        self.assertFalse(cleaned["salary"].isna().any())
        self.assertEqual(cleaned["id"].nunique(), 8)
        self.assertEqual(
            dict(zip(summary["department"], summary["headcount"])),
            {"Finance": 1, "HR": 2, "IT": 3, "Sales": 2},
        )
        self.assertEqual((len(inner), len(left), len(outer)), (8, 8, 9))
        self.assertIn("Operations", set(departments["department"]))
        self.assertEqual(
            outer.loc[outer["name"].isna(), "department"].tolist(),
            ["Operations"],
        )

    def test_create_charts_writes_all_four_pngs(self):
        from src.task3_analysis import REPORTS

        with contextlib.redirect_stdout(io.StringIO()):
            employees, _, departments, summary, *_ = pandas_analysis()
        create_charts(employees, departments, summary)

        for filename in (
            "department_headcount.png",
            "salary_histogram.png",
            "salary_scatter.png",
            "salary_line.png",
        ):
            with self.subTest(filename=filename):
                chart = REPORTS / filename
                self.assertTrue(chart.is_file())
                self.assertGreater(chart.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
