"""Generate a synthetic student dataset for the AI impact analysis project.

The dataset is practice data only. It is designed to look like a student
survey/analysis dataset so the Pandas, NumPy and visualization workflow can be
practised before using real survey data.
"""

from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "student_ai_dataset.csv"


def performance_level(score: float) -> str:
    if score >= 85:
        return "Excellent"
    if score >= 70:
        return "Good"
    if score >= 55:
        return "Average"
    return "Needs Improvement"


def main() -> None:
    rng = np.random.default_rng(42)
    n = 500

    departments = rng.choice(
        ["CSE", "EEE", "Business", "English", "Pharmacy", "Architecture"],
        size=n,
        p=[0.34, 0.16, 0.18, 0.10, 0.12, 0.10],
    )
    gender = rng.choice(["Female", "Male"], size=n, p=[0.46, 0.54])
    study_year = rng.integers(1, 5, size=n)

    ai_tools = rng.choice(
        ["ChatGPT", "Gemini", "Claude", "Perplexity", "DeepSeek", "None"],
        size=n,
        p=[0.34, 0.22, 0.16, 0.08, 0.07, 0.13],
    )

    previous_gpa = np.clip(rng.normal(3.25, 0.35, size=n), 2.00, 4.00)
    attendance_percentage = np.clip(rng.normal(82, 10, size=n), 45, 100)
    study_hours_per_week = np.clip(rng.normal(11, 4, size=n), 1, 30)

    ai_usage_hours = np.where(
        ai_tools == "None",
        rng.choice([0.0, 0.5, 1.0], size=n, p=[0.70, 0.20, 0.10]),
        np.clip(rng.gamma(shape=2.0, scale=2.3, size=n), 0.2, 18),
    )

    assignment_completion = (
        48
        + attendance_percentage * 0.32
        + study_hours_per_week * 0.85
        + np.log1p(ai_usage_hours) * 4.0
        + rng.normal(0, 6, size=n)
    )
    assignment_completion = np.clip(assignment_completion, 20, 100)

    creativity_score = (
        45
        + (previous_gpa - 2.0) * 9
        + np.log1p(ai_usage_hours) * 5.2
        + study_hours_per_week * 0.55
        + rng.normal(0, 7, size=n)
    )
    creativity_score = np.clip(creativity_score, 20, 100)

    # Moderate AI use helps in this synthetic data; very heavy use has a penalty.
    ai_benefit = 10 * np.exp(-((ai_usage_hours - 5) ** 2) / (2 * 3.5**2))
    overuse_penalty = np.maximum(0, ai_usage_hours - 10) * 1.15

    final_score = (
        (previous_gpa / 4) * 42
        + attendance_percentage * 0.20
        + study_hours_per_week * 0.62
        + creativity_score * 0.13
        + ai_benefit
        - overuse_penalty
        + rng.normal(0, 5.5, size=n)
    )
    final_score = np.clip(final_score, 30, 100)

    df = pd.DataFrame(
        {
            "student_id": [f"STU-{i:03d}" for i in range(1, n + 1)],
            "gender": gender,
            "department": departments,
            "study_year": study_year,
            "ai_tool": ai_tools,
            "ai_usage_hours_per_week": np.round(ai_usage_hours, 2),
            "study_hours_per_week": np.round(study_hours_per_week, 2),
            "attendance_percentage": np.round(attendance_percentage, 2),
            "assignment_completion_percentage": np.round(assignment_completion, 2),
            "previous_gpa": np.round(previous_gpa, 2),
            "creativity_score": np.round(creativity_score, 2),
            "final_score": np.round(final_score, 2),
        }
    )
    df["performance_level"] = df["final_score"].apply(performance_level)

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_PATH, index=False)
    print(f"Dataset created: {DATA_PATH}")
    print(f"Rows: {len(df)} | Columns: {len(df.columns)}")


if __name__ == "__main__":
    main()
