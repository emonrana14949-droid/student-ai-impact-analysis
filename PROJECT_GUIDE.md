# Project Guide — Student AI Impact Analysis

**A complete, beginner-friendly explanation of this whole project.**

Read this file from top to bottom. After reading it, you will understand:
what this project is, what every file does, how the code works line by line,
how to run it yourself, and how to answer viva questions about it.

---

## 1. What is this project?

This is a **Data Science practice project** made with Python.

**Topic:** How do students use AI tools (like ChatGPT), and how is that use
connected to their study habits, creativity, and exam results?

The project takes data about **500 students** and studies it with three
famous Python libraries:

- **NumPy** — creates the data and does number work.
- **Pandas** — cleans the data and makes summary tables.
- **Matplotlib** — draws the charts.

### Questions this project answers

1. Which AI tool's users have the highest average final score?
2. Does using AI *more* always give better results — or is *moderate* use best?
3. Which department performs best?
4. How are attendance and study hours related to the final score?
5. Is AI usage related to creativity score?

### ⚠️ Very important: the data is NOT real

The dataset is **synthetic data**. That means a computer program invented it,
using random numbers and some simple rules. No real student was surveyed.

Why? So that anyone can practise the full Data Science workflow —
generate → clean → analyse → visualize → explain — before working with
real survey data.

So all results in this project are **for learning only**. They are not real
research findings.

---

## 2. What is inside the project?

Here is every folder and file, one by one.

```text
student-ai-impact-analysis/
├── README.md
├── PROJECT_GUIDE.md          ← you are reading this file
├── requirements.txt
├── .gitignore
├── data/
│   └── student_ai_dataset.csv
├── src/
│   ├── generate_dataset.py
│   └── analysis.py
├── notebooks/
│   └── student_ai_analysis.ipynb
└── outputs/
    ├── insights.md
    ├── tables/   (5 CSV files)
    └── charts/   (6 PNG images)
```

| File / folder | What it is, in simple words |
|---|---|
| `README.md` | The front page of the project. A short summary: topic, questions, structure, how to run. Read it first for a quick overview. |
| `PROJECT_GUIDE.md` | This guide. The full, slow explanation of everything. |
| `requirements.txt` | A shopping list of Python libraries the project needs: `pandas`, `numpy`, `matplotlib`. The computer reads this file to install them all in one command. |
| `.gitignore` | A small file for Git (version control). It lists things Git should *not* upload, like `__pycache__/` folders and virtual environments. You can ignore it safely. |
| `data/student_ai_dataset.csv` | The dataset. A CSV file is a simple table saved as text. This one has 500 rows (one per student) and 13 columns. It is created by `generate_dataset.py`. |
| `src/generate_dataset.py` | Python code #1. It **creates** the dataset and saves it as the CSV file. |
| `src/analysis.py` | Python code #2. It **reads** the CSV, cleans it, makes tables and charts, and writes the key results. |
| `notebooks/student_ai_analysis.ipynb` | A Jupyter notebook version of the analysis. A notebook lets you run small pieces of code one by one and see each result under the code — good for learning and for presenting. |
| `outputs/tables/` | 5 summary tables (CSV files) made by `analysis.py`. |
| `outputs/charts/` | 6 chart images (PNG files) made by `analysis.py`. |
| `outputs/insights.md` | A short report written automatically by `analysis.py`. It contains the main results in plain sentences and numbers. |

**One idea to remember:** files in `data/`, `outputs/` are *made by the code*.
If you delete them, just run the two Python files again and they come back.

---

## 3. The dataset, column by column

The CSV file has **500 rows** (students) and **13 columns**.
Each row is one student. Each column is one fact about that student.

Here is one real example row from the file:

```text
STU-002, Male, EEE, 1, ChatGPT, 3.36, 12.21, 88.11, 83.46, 3.61, 73.84, 89.19, Excellent
```

| # | Column name | What it means | Example values |
|---|---|---|---|
| 1 | `student_id` | A code name for the student. Not a real ID — just a label. | `STU-001`, `STU-002` |
| 2 | `gender` | The student's gender. | `Female`, `Male` |
| 3 | `department` | The subject the student studies. | `CSE`, `EEE`, `Business`, `English`, `Pharmacy`, `Architecture` |
| 4 | `study_year` | Which year of study, from 1 to 4. | `1`, `2`, `3`, `4` |
| 5 | `ai_tool` | The main AI tool the student uses. `None` means the student does not use AI. | `ChatGPT`, `Gemini`, `Claude`, `Perplexity`, `DeepSeek`, `None` |
| 6 | `ai_usage_hours_per_week` | How many hours per week the student uses AI for study. | `3.36` hours |
| 7 | `study_hours_per_week` | How many hours per week the student studies (normal study). | `12.21` hours |
| 8 | `attendance_percentage` | How much class the student attends, out of 100%. | `88.11` |
| 9 | `assignment_completion_percentage` | How much of the assignment work the student finishes, out of 100%. | `83.46` |
| 10 | `previous_gpa` | The student's GPA from before, on a 4.00 scale. | `3.61` |
| 11 | `creativity_score` | A creativity score, out of 100. | `73.84` |
| 12 | `final_score` | The final exam/result score, out of 100. This is the main result we study. | `89.19` |
| 13 | `performance_level` | A word-label made from `final_score` (see the rule below). | `Excellent`, `Good`, `Average`, `Needs Improvement` |

**The rule for `performance_level`:**

- 85 or more → `Excellent`
- 70 to 84.99 → `Good`
- 55 to 69.99 → `Average`
- below 55 → `Needs Improvement`

So STU-002 scored 89.19, and that is why the label is `Excellent`.

> Note: when `analysis.py` runs, it adds **2 extra columns** inside its own
> working copy (`ai_user` and `ai_usage_level`, explained in section 6).
> That is why `insights.md` says "15 columns after feature engineering".
> The CSV file itself still has 13 columns.

---

## 4. How to run the project from zero

Follow these steps in order. You need a computer with internet (only for
Step 2, to download the libraries).

### Step 0 — Install Python

Install **Python 3** from [python.org](https://www.python.org/downloads/)
if your computer does not have it. Check that it works:

```bash
python --version
```

You should see something like `Python 3.11` or higher.

### Step 1 — Open a terminal in the project folder

Open your terminal / command prompt and go inside the project folder:

```bash
cd student-ai-impact-analysis
```

### Step 2 — Install the libraries

```bash
pip install -r requirements.txt
```

This one command reads `requirements.txt` and installs **pandas**,
**numpy**, and **matplotlib**.

### Step 3 — Create the dataset

```bash
python src/generate_dataset.py
```

You will see:

```text
Dataset created: .../data/student_ai_dataset.csv
Rows: 500 | Columns: 13
```

Now the file `data/student_ai_dataset.csv` exists.

### Step 4 — Run the analysis

```bash
python src/analysis.py
```

You will see:

```text
Analysis complete.
Tables saved to: .../outputs/tables
Charts saved to: .../outputs/charts
Insights saved to: .../outputs/insights.md
Top AI tool by average final score: Claude
AI hours vs final score correlation: 0.09
```

### Step 5 — See the results

Open these files:

- `outputs/insights.md` — the main results, in words and numbers.
- `outputs/charts/` — the 6 chart images.
- `outputs/tables/` — the 5 summary tables (they open in Excel or any text editor).
- `notebooks/student_ai_analysis.ipynb` — if you want to run the analysis
  step by step in Jupyter.

**Good news:** because the random seed is fixed (see section 5), you will
get the **same dataset and the same results every time** you run the code.

---

## 5. Code explanation: `src/generate_dataset.py`

This file **creates fake but realistic student data**. Let us walk through
it in the same order as the code.

### 5.1 Imports and file path

```python
from pathlib import Path
import numpy as np
import pandas as pd
```

- `numpy` (short name `np`) — for random numbers and maths.
- `pandas` (short name `pd`) — for building the table and saving the CSV.
- `Path` — for working with file locations safely.

```python
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "student_ai_dataset.csv"
```

This finds the project folder from the location of the script itself.
So the CSV is always saved to `data/student_ai_dataset.csv`, no matter
from where you run the command.

### 5.2 The `performance_level` function

```python
def performance_level(score: float) -> str:
    if score >= 85:
        return "Excellent"
    if score >= 70:
        return "Good"
    if score >= 55:
        return "Average"
    return "Needs Improvement"
```

A small helper. Give it a score, it gives back a word label.
This is the rule you saw in section 3.

### 5.3 The random seed — why 42?

```python
rng = np.random.default_rng(42)
n = 500
```

- `rng` is a **random number generator** — a machine that produces
  random-looking numbers.
- The number **42** is the **seed**. The seed is like a starting point.

Why fix the seed? Without a seed, the data would be different on every run,
and nobody could check or repeat the results. With seed 42, **every run
creates exactly the same 500 students**. This is called *reproducibility*,
and it is very important in Data Science.

(Any number could be the seed. 42 is just a popular choice.)

- `n = 500` means the dataset will have 500 students.

### 5.4 Choosing categories: department, gender, study year, AI tool

```python
departments = rng.choice(
    ["CSE", "EEE", "Business", "English", "Pharmacy", "Architecture"],
    size=n,
    p=[0.34, 0.16, 0.18, 0.10, 0.12, 0.10],
)
```

`rng.choice` picks one item from the list, 500 times.
The list `p` gives the **probability** of each item. So about 34% of
students are from CSE, 16% from EEE, and so on. The probabilities add
up to 1.00.

The same idea is used for:

- `gender` — Female 46%, Male 54%.
- `ai_tools` — ChatGPT 34%, Gemini 22%, Claude 16%, Perplexity 8%,
  DeepSeek 7%, and `None` (no AI) 13%.

Study year is different — it is a whole number, not a choice from words:

```python
study_year = rng.integers(1, 5, size=n)
```

This gives random integers from 1 to 4 (the end value 5 is not included).

### 5.5 Normal distribution numbers: GPA, attendance, study hours

```python
previous_gpa = np.clip(rng.normal(3.25, 0.35, size=n), 2.00, 4.00)
```

- `rng.normal(3.25, 0.35, ...)` makes numbers that gather around a
  **mean of 3.25**, with a **standard deviation of 0.35**. Most students
  are near 3.25; very few are far away. This bell-curve shape is called a
  **normal distribution**, and it looks like real life (most people are
  average, few are extreme).
- `np.clip(..., 2.00, 4.00)` cuts off anything outside the range.
  A GPA cannot be above 4.00 or below 2.00 in this dataset.

The same pattern makes:

- `attendance_percentage` — mean 82, spread 10, clipped to 45–100.
- `study_hours_per_week` — mean 11, spread 4, clipped to 1–30.

### 5.6 AI usage hours — two different rules

```python
ai_usage_hours = np.where(
    ai_tools == "None",
    rng.choice([0.0, 0.5, 1.0], size=n, p=[0.70, 0.20, 0.10]),
    np.clip(rng.gamma(shape=2.0, scale=2.3, size=n), 0.2, 18),
)
```

`np.where(condition, A, B)` means: "if the condition is true use A,
otherwise use B", for every student at the same time.

- If the student's tool is `None`, they get 0, 0.5, or 1 hour
  (mostly 0 — they do not use AI).
- Otherwise, hours come from a **gamma distribution**. Gamma gives
  positive numbers where small values are common and big values are rare —
  like real life: most students use AI a little, a few use it a lot.
  The result is clipped to 0.2–18 hours.

### 5.7 Scores built from formulas

Now the interesting part. Three scores are **built from other columns**
using simple formulas, plus a little random noise.

**Assignment completion:**

```python
assignment_completion = (
    48
    + attendance_percentage * 0.32
    + study_hours_per_week * 0.85
    + np.log1p(ai_usage_hours) * 4.0
    + rng.normal(0, 6, size=n)
)
```

Read it like a recipe: start at 48, add points for attending class,
add points for studying, add a smaller bonus for AI use.
`np.log1p(x)` means log(1 + x) — it makes the AI bonus grow *slowly*:
the first hour of AI helps more than the tenth hour.
The last part, `rng.normal(0, 6, ...)`, is **noise** — random ups and
downs, because real students are not perfect formulas.
Finally the result is clipped to 20–100.

**Creativity score** uses the same idea:

```python
creativity_score = (
    45
    + (previous_gpa - 2.0) * 9
    + np.log1p(ai_usage_hours) * 5.2
    + study_hours_per_week * 0.55
    + rng.normal(0, 7, size=n)
)
```

Higher previous GPA, AI use, and study time all push creativity up.
Clipped to 20–100.

**Final score** is the most careful formula:

```python
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
```

Two special ideas live here:

1. **`ai_benefit`** is a bell-shaped curve with its peak at **5 hours**.
   It gives up to +10 points, and the bonus is biggest when AI use is
   around 5 hours per week — not zero, and not very high.
   This is how the data says: *moderate use helps most.*
2. **`overuse_penalty`** is 0 up to 10 hours. After 10 hours, every extra
   hour *removes* 1.15 points. This is how the data says:
   *too much AI use hurts.*

The rest is simple: previous GPA is the biggest part, then attendance,
study hours, and creativity add smaller parts. Noise is added, and the
score is clipped to 30–100.

> Remember: these formulas are the *opinion of the person who made the
> practice data*. The analysis in the next file "discovers" these patterns.
> With real data, nobody knows the formula — that is the real challenge.

### 5.8 Building the table and saving the CSV

```python
df = pd.DataFrame({ "student_id": ..., "gender": gender, ... })
df["performance_level"] = df["final_score"].apply(performance_level)
df.to_csv(DATA_PATH, index=False)
```

- `pd.DataFrame({...})` puts all the columns together into one table.
  This table is called a **DataFrame** — the main object in Pandas.
- Student IDs are made as text: `STU-001` to `STU-500`.
- Numbers are rounded to 2 decimals with `np.round(..., 2)`.
- `.apply(performance_level)` runs the small function from 5.2 on every
  final score, to create the label column.
- `df.to_csv(..., index=False)` saves the table as the CSV file.
  `index=False` means "do not save the row numbers as an extra column".

The last lines print a message: where the file was saved, and
"Rows: 500 | Columns: 13".

---

## 6. Code explanation: `src/analysis.py`

This file **reads the dataset and produces all tables, charts, and the
insights report**. Again, in the order of the code.

### 6.1 Setup

The imports add `matplotlib.pyplot` (short name `plt`) for drawing charts.
The paths point to the CSV file and to the `outputs/tables/` and
`outputs/charts/` folders.

```python
try:
    plt.style.use("seaborn-v0_8-whitegrid")
except OSError:
    plt.style.use("ggplot")
```

This chooses a chart style (colours and grid). If the first style is not
available on the computer, it safely falls back to the second one.
The `try / except` pattern means: "try this; if it fails, do that instead —
do not crash."

### 6.2 A helper for bar charts: `save_bar_chart`

Two of the charts are simple bar charts with the same look.
Instead of writing the same drawing code twice, the file defines one
function that takes a data series, a title, axis labels, and a file path,
draws the bar chart, and saves it as a PNG image. It is used for the
"by AI tool" chart and the "by department" chart.

### 6.3 Loading and cleaning the data

```python
df = pd.read_csv(DATA_PATH)
df = df.drop_duplicates().copy()
```

- `pd.read_csv` loads the CSV into a DataFrame.
- `drop_duplicates()` removes any repeated rows — a basic cleaning step.

```python
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
```

This finds all number columns and makes sure they are really stored as
numbers. If any bad value appears, `errors="coerce"` turns it into a
missing value instead of crashing the program.

### 6.4 Two new columns (feature engineering)

Making useful new columns from old ones is called **feature engineering**.

```python
df["ai_user"] = np.where(df["ai_tool"] == "None", "No AI tool", "AI user")
```

Every student becomes either `AI user` or `No AI tool`. This is used to
colour the scatter chart (blue vs pink dots).

```python
df["ai_usage_level"] = pd.cut(
    df["ai_usage_hours_per_week"],
    bins=[-0.1, 0, 3, 7, 12, 30],
    labels=["No use", "Low", "Moderate", "High", "Very high"],
)
```

`pd.cut` chops a number column into groups:

| Hours per week | Label |
|---|---|
| 0 | `No use` |
| above 0 to 3 | `Low` |
| above 3 to 7 | `Moderate` |
| above 7 to 12 | `High` |
| above 12 | `Very high` |

This lets us ask: "which *level* of use is best?" — not just "more or less?"

### 6.5 The five summary tables

**Table 1 — `summary_statistics.csv`**

```python
df.describe(include="all").round(2).to_csv(...)
```

`describe()` gives a quick health report of every column: count, mean,
standard deviation, minimum, maximum, and quartiles for numbers;
count, unique values, and the most common value for text columns.

**Table 2 — `average_scores_by_ai_tool.csv`**

```python
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
```

This is the most important pattern in the whole project:

- `groupby("ai_tool")` — split the 500 students into one group per AI tool.
- `.agg(...)` — for each group, calculate: how many students (`count`),
  and the **average** (`mean`) of hours, creativity, final score, attendance.
- `.round(2)` — round to 2 decimals.
- `.sort_values(..., ascending=False)` — biggest average final score first.

So the **first row of this table is the answer to Question 1**.

**Table 3 — `average_scores_by_department.csv`** — the same groupby pattern,
grouped by `department` instead of tool. Its first row answers Question 3.

**Table 4 — `average_scores_by_ai_usage_level.csv`** — the same pattern,
grouped by the `ai_usage_level` column made in 6.4. It answers Question 2:
which level of AI use has the highest average score.
(`observed=False` simply tells Pandas to keep all five level labels,
even if one group were empty.)

**Table 5 — `correlation_matrix.csv`**

```python
corr = df[corr_cols].corr(numeric_only=True).round(2)
```

`.corr()` calculates the **correlation** between every pair of number
columns. Correlation is a number from **−1 to +1**:

- near **+1** → when one goes up, the other usually goes up too.
- near **0** → no clear connection.
- near **−1** → when one goes up, the other usually goes down.

Only 7 columns are used here — the ones that matter for the questions.

### 6.6 The six charts

**Chart 1 — `ai_usage_vs_final_score.png` (scatter plot)**

Each dot is one student: x-position = AI hours, y-position = final score.
Blue dots are AI users, pink dots are the `No AI tool` group.
Then a **trend line** is drawn:

```python
slope, intercept = np.polyfit(df["ai_usage_hours_per_week"], df["final_score"], 1)
```

`np.polyfit(..., 1)` finds the straight line that best fits the cloud of
dots. If the line goes up, the general direction is "more hours → higher
score". If it is almost flat, there is no strong general direction.

**Chart 2 — `average_final_score_by_ai_tool.png` (bar chart)**

Made by `save_bar_chart` from Table 2. One bar per AI tool, showing its
average final score. The tallest bar = the top tool.

**Chart 3 — `creativity_score_distribution.png` (histogram)**

```python
ax.hist(df["creativity_score"], bins=18, ...)
ax.axvline(df["creativity_score"].mean(), ...)
```

A **histogram** shows how scores are spread out: it cuts the range into
18 bins and counts how many students fall in each bin. The dashed line
marks the **mean** (average) creativity score.

**Chart 4 — `average_final_score_by_department.png` (bar chart)**

Made by `save_bar_chart` from Table 3. One bar per department.

**Chart 5 — `performance_by_ai_usage_level.png` (grouped bar chart)**

For each usage level (No use → Very high) there are **two bars side by
side**: average final score (blue) and average creativity score (pink).
This is the chart that answers Question 2 visually.

**Chart 6 — `correlation_heatmap.png` (heatmap)**

The correlation matrix from Table 5, drawn as coloured squares with
`ax.imshow(...)`. Red = positive correlation, blue = negative, and the
exact number is written inside every square. It is the same data as
Table 5 — just in picture form, so patterns are easy to see.

Every chart ends with the same steps: `fig.tight_layout()` (fix spacing),
`fig.savefig(path, dpi=160)` (save as a clear PNG image), `plt.close(fig)`
(close it, to free memory).

### 6.7 Writing `insights.md` automatically

At the end, the code picks the key answers out of the tables:

```python
top_tool = by_tool.index[0]          # first row = highest average score
top_department = by_department.index[0]
best_usage_level = by_usage_level["avg_final_score"].idxmax()
ai_final_corr = corr.loc["ai_usage_hours_per_week", "final_score"]
```

- `.index[0]` takes the label of the first row (tables were sorted).
- `.idxmax()` finds the label of the biggest value.
- `corr.loc[row, column]` picks one correlation number out of the matrix.

These values are placed into a ready-made text template (an f-string),
and the text is saved as `outputs/insights.md` with
`INSIGHTS_PATH.write_text(...)`.

So the report you read in `insights.md` was **written by the program**,
not typed by a person. Change the data, re-run, and the report updates
itself. Finally, the code prints "Analysis complete." and the top results.

---

## 7. How to read the outputs

Do not just look at the charts — know what to *look for* in each one.

### The charts

**1. `ai_usage_vs_final_score.png` — scatter plot**
Look at the cloud of dots and the black trend line.
- Is the line going up, down, or almost flat?
- Are the dots tightly packed around the line, or spread far away?
In this project the line rises only a little and the dots are very spread
out. Meaning: in general, AI hours alone do not decide the final score.

**2. `average_final_score_by_ai_tool.png` — bar chart**
Compare the bar heights. The tallest bar is the tool whose users scored
highest *on average*. Also notice: if all bars are almost the same height,
the tool itself matters less than how the student studies.

**3. `creativity_score_distribution.png` — histogram**
Look at the shape. A hill shape in the middle means most students are
average, with few very low or very high. The dashed line is the mean —
check whether the hill is balanced around it or pushed to one side.

**4. `average_final_score_by_department.png` — bar chart**
Same idea as chart 2, but for departments. Tallest bar = best average.

**5. `performance_by_ai_usage_level.png` — grouped bars**
This is the most interesting chart. Follow the blue bars (final score)
from left to right: No use → Low → Moderate → High → Very high.
If the middle bar is the tallest, the pattern is "moderate use is best" —
which is exactly what this dataset shows.

**6. `correlation_heatmap.png` — heatmap**
Find the `final_score` row or column and read across it.
The biggest positive numbers show which factors move together with the
final score most strongly. Dark red squares near +1 are strong links;
pale squares near 0 are weak links.

### The tables

- **`summary_statistics.csv`** — read the `mean` and `std` (standard
  deviation) rows first. Mean = the typical value. Std = how spread out
  the values are. A big std means students differ a lot.
- **`average_scores_by_ai_tool.csv`** — already sorted: best tool first.
  Also compare the `students` column — a result from 158 students
  (ChatGPT) is more trustworthy than one from 40 (DeepSeek).
- **`average_scores_by_department.csv`** — sorted: best department first.
- **`average_scores_by_ai_usage_level.csv`** — read the levels in order
  (No use, Low, Moderate, High, Very high) and watch the average final
  score go up and then come down. That up-then-down shape is the main
  story of this project.
- **`correlation_matrix.csv`** — pick one row and one column; the number
  where they cross is their correlation. The diagonal is always 1.00,
  because every column is perfectly correlated with itself.

---

## 8. Key results of this project

These are the actual numbers from `outputs/insights.md`
(the analysis of the 500-student synthetic dataset):

- Dataset size: **500 students**, 13 columns in the CSV
  (15 columns inside the analysis, after the 2 new columns are added).
- 🏆 AI tool with the highest average final score: **Claude — 74.88**
  (from `average_scores_by_ai_tool.csv`: Claude users averaged 74.88,
  just above ChatGPT users at 74.64).
- 🏆 Department with the highest average final score:
  **Architecture — 75.17**
- ⭐ Best AI usage level: **Moderate** (more than 3 and up to 7 hours per
  week) — average final score **76.85**. Higher than both the "No use"
  group and the "Very high" group. This matches the design of the data:
  a benefit that peaks near 5 hours, and a penalty after 10 hours.
- Correlation, AI usage hours vs final score: **0.09**
  → very weak. More AI hours alone barely move with the final score.
- Correlation, AI usage hours vs creativity score: **0.45**
  → a moderate positive link. Students who use AI more tend to have
  higher creativity scores in this data.
- Correlation, attendance vs final score: **0.22**
  → a weak-to-moderate positive link. Attending class matters,
  but it is not the whole story.

**The one-sentence conclusion:**
In this practice dataset, *how* a student uses AI matters more than
*how much* — moderate use (3–7 hours/week) is linked with the best
results, AI use is clearly linked with creativity, but AI hours alone
have only a weak link with the final score.

**And the honest warning:** this data was invented by a program.
These results show how the *workflow* works. They do not prove anything
about real students.

---

## 9. Viva / presentation help

Questions a teacher may ask — with short model answers.
Learn the ideas, then say them in your own words.

**Q1. What is this project about?**
It studies how students' AI tool usage, study habits, attendance, and
creativity are related to their academic performance, using Pandas,
NumPy, and Matplotlib on a dataset of 500 students.

**Q2. Why did you use Pandas?**
Pandas is made for table data. It loads a CSV into a DataFrame in one
line, and it gives easy tools to clean data, group it (`groupby`),
calculate averages, and find correlations. Doing this by hand in plain
Python would be much longer and easier to get wrong.

**Q3. What did NumPy do in this project?**
Three jobs: it generated the random dataset (with a fixed seed), it did
fast maths on whole columns at once (like `np.clip`, `np.where`,
`np.log1p`), and it calculated the trend line with `np.polyfit`.

**Q4. Why is the random seed fixed at 42?**
So the results are *reproducible*. With the same seed, anyone who runs
the code gets exactly the same data and the same results, so the work
can be checked and repeated.

**Q5. What is correlation?**
Correlation is a number between −1 and +1 that says whether two things
tend to move together. +1 means they rise together perfectly, 0 means
no clear link, and −1 means one rises when the other falls. For example,
AI hours vs creativity is 0.45 here — a moderate positive link.

**Q6. AI hours vs final score correlation is only 0.09. What does that mean?**
It means there is almost no straight-line relationship between them.
Simply using AI for more hours does not come with higher scores in this
data. Other things — like previous GPA, attendance, and *moderate* use —
matter more.

**Q7. Does this project prove that AI improves student results?**
No. Two reasons: (1) correlation is not causation — two things moving
together does not prove one causes the other; (2) this dataset is
synthetic practice data, not real students. The project demonstrates
the *method*, not a real-world truth.

**Q8. What does the trend line in the scatter chart mean?**
It is the best-fit straight line through the dots, made by
`np.polyfit`. It shows the general direction of the relationship.
Here it rises only slightly, which matches the weak correlation of 0.09.

**Q9. What is `groupby`, and where did you use it?**
`groupby` splits data into groups and calculates something for each
group. I used it to find the average final score for each AI tool, each
department, and each AI usage level — for example, that Claude users
averaged 74.88 and the Moderate usage group averaged 76.85.

**Q10. What is the difference between the histogram and the bar chart here?**
A bar chart compares *categories* (tools, departments) using averages.
A histogram shows the *distribution* of one number column — how the
500 creativity scores are spread out, and where most students sit.

**Q11. If you had real data, what would you change?**
I would replace the generated CSV with real survey data collected with
students' consent, describe how participants were chosen (the sampling
method), check the data quality carefully, and only then run the same
analysis — the code would stay almost the same.

---

## 10. What to learn next / how to extend this project

1. **Use real survey data.** Collect answers through a questionnaire
   (with permission), save them in the same CSV format, and run the same
   two scripts. This turns the practice project into a real study —
   but remember to write down the sampling method and limitations.

2. **Add a Machine Learning model.** Use **scikit-learn** to *predict*
   the final score from GPA, attendance, study hours, and AI usage
   (for example, with Linear Regression or a Random Forest), and check
   how accurate the prediction is.

3. **Make an interactive dashboard.** Use **Streamlit** to turn the
   charts into a small web app where a user can filter by department or
   AI tool and see the results update live.

4. **Go deeper with statistics.** Add hypothesis tests (for example,
   comparing two groups with a t-test) and confidence intervals, so
   results are reported with their uncertainty — not just averages.

---

*End of the guide. Good luck — and remember: understand the story the
data tells, not just the code that draws it.* 📊
