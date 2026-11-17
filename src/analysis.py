"""Analyse the student AI dataset with Pandas, NumPy and Matplotlib.

Run from the project root:
    python src/analysis.py

Outputs are saved to:
    outputs/tables/  (CSV summary tables)
    outputs/charts/  (PNG visualizations)
    outputs/insights.md
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "student_ai_dataset.csv"
TABLE_DIR = PROJECT_ROOT / "outputs" / "tables"
CHART_DIR = PROJECT_ROOT / "outputs" / "charts"
INSIGHTS_PATH = PROJECT_ROOT / "outputs" / "insights.md"

try:
    plt.style.use("seaborn-v0_8-whitegrid")
except OSError:
    plt.style.use("ggplot")


def save_bar_chart(series: pd.Series, title: str, xlabel: str, ylabel: str, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(9, 4.8))
    series.plot(kind="bar", ax=ax, color="#2f81f7", edgecolor="white")
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=25)
    for label in ax.get_xticklabels():
        label.set_ha("right")
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def main() -> None:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    CHART_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH)

    # Basic cleaning and feature engineering with Pandas.
    df = df.drop_duplicates().copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
    df["ai_user"] = np.where(df["ai_tool"] == "None", "No AI tool", "AI user")
    df["ai_usage_level"] = pd.cut(
        df["ai_usage_hours_per_week"],
        bins=[-0.1, 0, 3, 7, 12, 30],
        labels=["No use", "Low", "Moderate", "High", "Very high"],
    )

    # Summary tables.
    df.describe(include="all").round(2).to_csv(TABLE_DIR / "summary_statistics.csv")

    by_tool = (
        df.groupby("ai_tool")
        .agg(
            students=("student_id", "count"),
            avg_ai_hours=("ai_usage_hours_per_week", "mean"),
            avg_creativity_score=("creativity_score", "mean"),
            avg_final_score=("final_score", "mean"),
            avg_attendance=("attendance_percentage", "mean"),
        )
        .round(2)
        .sort_values("avg_final_score", ascending=False)
    )
    by_tool.to_csv(TABLE_DIR / "average_scores_by_ai_tool.csv")

    by_department = (
        df.groupby("department")
        .agg(
            students=("student_id", "count"),
            avg_ai_hours=("ai_usage_hours_per_week", "mean"),
            avg_creativity_score=("creativity_score", "mean"),
            avg_final_score=("final_score", "mean"),
        )
        .round(2)
        .sort_values("avg_final_score", ascending=False)
    )
    by_department.to_csv(TABLE_DIR / "average_scores_by_department.csv")

    by_usage_level = (
        df.groupby("ai_usage_level", observed=False)
        .agg(
            students=("student_id", "count"),
            avg_creativity_score=("creativity_score", "mean"),
            avg_final_score=("final_score", "mean"),
        )
        .round(2)
    )
    by_usage_level.to_csv(TABLE_DIR / "average_scores_by_ai_usage_level.csv")

    corr_cols = [
        "ai_usage_hours_per_week",
        "study_hours_per_week",
        "attendance_percentage",
        "assignment_completion_percentage",
        "previous_gpa",
        "creativity_score",
        "final_score",
    ]
    corr = df[corr_cols].corr(numeric_only=True).round(2)
    corr.to_csv(TABLE_DIR / "correlation_matrix.csv")

    # Chart 1: AI usage vs final score with a NumPy trend line.
    fig, ax = plt.subplots(figsize=(9, 5))
    for label, colour in [("AI user", "#2f81f7"), ("No AI tool", "#f778ba")]:
        subset = df[df["ai_user"] == label]
        ax.scatter(
            subset["ai_usage_hours_per_week"],
            subset["final_score"],
            color=colour,
            alpha=0.68,
            edgecolor="white",
            linewidth=0.4,
            label=label,
        )
    slope, intercept = np.polyfit(df["ai_usage_hours_per_week"], df["final_score"], 1)
    x_line = np.linspace(df["ai_usage_hours_per_week"].min(), df["ai_usage_hours_per_week"].max(), 100)
    ax.plot(x_line, slope * x_line + intercept, color="#111111", linewidth=1.6, label="Trend line")
    ax.set_title("AI Usage Hours vs Final Score", fontweight="bold")
    ax.set_xlabel("AI usage hours per week")
    ax.set_ylabel("Final score")
    ax.legend()
    fig.tight_layout()
    fig.savefig(CHART_DIR / "ai_usage_vs_final_score.png", dpi=160)
    plt.close(fig)

    # Chart 2 and 4: clean bar charts from grouped Pandas results.
    save_bar_chart(
        by_tool["avg_final_score"],
        "Average Final Score by AI Tool",
        "AI tool",
        "Average final score",
        CHART_DIR / "average_final_score_by_ai_tool.png",
    )
    save_bar_chart(
        by_department["avg_final_score"],
        "Average Final Score by Department",
        "Department",
        "Average final score",
        CHART_DIR / "average_final_score_by_department.png",
    )

    # Chart 3: creativity score distribution.
    fig, ax = plt.subplots(figsize=(9, 4.8))
    ax.hist(df["creativity_score"], bins=18, color="#8250df", edgecolor="white")
    ax.axvline(df["creativity_score"].mean(), color="#111111", linestyle="--", linewidth=1.5, label="Mean")
    ax.set_title("Distribution of Creativity Scores", fontweight="bold")
    ax.set_xlabel("Creativity score")
    ax.set_ylabel("Number of students")
    ax.legend()
    fig.tight_layout()
    fig.savefig(CHART_DIR / "creativity_score_distribution.png", dpi=160)
    plt.close(fig)

    # Chart 5: grouped bars for AI usage level.
    fig, ax = plt.subplots(figsize=(9, 5))
    x = np.arange(len(by_usage_level.index))
    width = 0.38
    ax.bar(x - width / 2, by_usage_level["avg_final_score"], width, label="Final score", color="#2f81f7")
    ax.bar(x + width / 2, by_usage_level["avg_creativity_score"], width, label="Creativity score", color="#f778ba")
    ax.set_xticks(x, by_usage_level.index.astype(str))
    ax.set_title("Performance by AI Usage Level", fontweight="bold")
    ax.set_xlabel("AI usage level")
    ax.set_ylabel("Average score")
    ax.legend()
    fig.tight_layout()
    fig.savefig(CHART_DIR / "performance_by_ai_usage_level.png", dpi=160)
    plt.close(fig)

    # Chart 6: correlation heatmap made with Matplotlib imshow.
    fig, ax = plt.subplots(figsize=(9, 7))
    image = ax.imshow(corr.values, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr.columns)), corr.columns, rotation=35, ha="left")
    ax.set_yticks(range(len(corr.index)), corr.index)
    ax.set_title("Correlation Heatmap", fontweight="bold")
    for i in range(len(corr.index)):
        for j in range(len(corr.columns)):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", fontsize=8)
    fig.colorbar(image, ax=ax, shrink=0.85)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "correlation_heatmap.png", dpi=160)
    plt.close(fig)

    top_tool = by_tool.index[0]
    top_department = by_department.index[0]
    best_usage_level = by_usage_level["avg_final_score"].idxmax()
    ai_final_corr = corr.loc["ai_usage_hours_per_week", "final_score"]
    ai_creativity_corr = corr.loc["ai_usage_hours_per_week", "creativity_score"]
    attendance_final_corr = corr.loc["attendance_percentage", "final_score"]

    insights = f"""# Key Insights — Student AI Impact Analysis

> This project uses synthetic practice data generated with NumPy. The patterns below are for learning the workflow only; they are not real research findings.

- Dataset size: **{len(df)} students** and **{len(df.columns)} columns** after feature engineering.
- The AI tool group with the highest average final score is **{top_tool}** ({by_tool.loc['' + top_tool, 'avg_final_score'] if False else by_tool.loc[top_tool, 'avg_final_score']:.2f}).
- The department with the highest average final score is **{top_department}** ({by_department.loc[top_department, 'avg_final_score']:.2f}).
- The strongest average final score appears in the **{best_usage_level}** AI usage level ({by_usage_level.loc[best_usage_level, 'avg_final_score']:.2f}).
- Correlation between AI usage hours and final score: **{ai_final_corr:.2f}**.
- Correlation between AI usage hours and creativity score: **{ai_creativity_corr:.2f}**.
- Correlation between attendance and final score: **{attendance_final_corr:.2f}**.

## Charts

- `charts/ai_usage_vs_final_score.png`
- `charts/average_final_score_by_ai_tool.png`
- `charts/creativity_score_distribution.png`
- `charts/average_final_score_by_department.png`
- `charts/performance_by_ai_usage_level.png`
- `charts/correlation_heatmap.png`

## Important note

Correlation does not prove causation. For a real project, replace the synthetic CSV with real survey data and document the sampling method, consent process and limitations.
"""
    INSIGHTS_PATH.write_text(insights, encoding="utf-8")

    print("Analysis complete.")
    print(f"Tables saved to: {TABLE_DIR}")
    print(f"Charts saved to: {CHART_DIR}")
    print(f"Insights saved to: {INSIGHTS_PATH}")
    print(f"Top AI tool by average final score: {top_tool}")
    print(f"AI hours vs final score correlation: {ai_final_corr:.2f}")


if __name__ == "__main__":
    main()
