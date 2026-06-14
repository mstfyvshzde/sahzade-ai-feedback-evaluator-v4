# Sahzade AI — Feedback Evaluator V4

## Overview

**Sahzade AI Feedback Evaluator V4** is a small evaluation tool for the Sahzade AI local assistant project.

In previous versions:

```text
V1 → LoRA fine-tuning experiment
V2 → Local FastAPI chat API
V3 → Browser-based chat UI
```

V4 focuses on evaluating the assistant responses.

The goal of this project is to read saved chat logs, manually label the quality of each assistant response, save feedback results, and generate a simple evaluation report.

---

## Project Goal

The main goal of this project is to create a lightweight feedback system that can:

* read chat logs from the V2 API
* show user and assistant messages one by one
* allow manual feedback labeling
* save feedback results into JSONL format
* generate an evaluation report
* identify weak response patterns
* support future dataset improvement

This project helps understand which responses are good and which responses need improvement.

---

## Project Scope

This version includes:

* chat log reader
* manual response evaluator
* feedback label system
* feedback result saving
* evaluation report generation
* shell scripts for running the evaluator
* local JSONL-based workflow

This version does **not** include:

* automatic AI-based grading
* web interface
* database storage
* model retraining
* production monitoring system
* advanced analytics dashboard

---

## Project Structure

```text
sahzade-ai-feedback-evaluator-v4/
│
├── data/
│   ├── input/
│   │   └── chat_logs.jsonl
│   │
│   └── output/
│       ├── feedback_results.jsonl
│       └── evaluation_report.json
│
├── scripts/
│   ├── copy_logs.sh
│   └── run_evaluator.sh
│
├── src/
│   ├── config.py
│   ├── evaluator.py
│   └── report.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Main Components

### `src/config.py`

Stores project paths and feedback labels.

Main responsibilities:

* define base project directory
* define input and output paths
* define chat logs path
* define feedback results path
* define evaluation report path
* define available feedback labels

Feedback labels:

```text
1 → good
2 → bad
3 → generic
4 → wrong_language
5 → unnatural
6 → wrong_intent
7 → repetitive
```

---

### `src/evaluator.py`

Reads chat logs and allows manual feedback labeling.

Main responsibilities:

* load `chat_logs.jsonl`
* show each conversation sample
* ask the user to choose a feedback label
* optionally collect a note
* save feedback into `feedback_results.jsonl`

Example feedback result:

```json
{
  "evaluated_at": "2026-06-12T17:45:00",
  "time": "2026-06-12T17:35:08",
  "user_message": "ok",
  "assistant_response": "Əla, buradayam.",
  "feedback": "generic",
  "note": "Acceptable but repeated too often."
}
```

---

### `src/report.py`

Reads the feedback results and creates a summary report.

Main responsibilities:

* load `feedback_results.jsonl`
* count feedback labels
* calculate good response rate
* count issue responses
* save report into `evaluation_report.json`
* print report summary in the terminal

Example report structure:

```json
{
  "total_evaluated": 10,
  "good_count": 5,
  "issue_count": 5,
  "good_rate_percent": 50.0,
  "label_counts": {
    "good": 5,
    "generic": 3,
    "wrong_language": 1,
    "unnatural": 1
  }
}
```

---

### `scripts/copy_logs.sh`

Copies chat logs from the V2 API project into this project.

Source:

```text
sahzade-ai-local-chat-mini (v2)/logs/chat_logs.jsonl
```

Target:

```text
data/input/chat_logs.jsonl
```

---

### `scripts/run_evaluator.sh`

Starts the manual evaluator.

```bash
./scripts/run_evaluator.sh
```

---

## Requirements

This project uses only Python standard library modules:

```text
json
pathlib
datetime
collections
```

No external Python package is required.

The `requirements.txt` file can stay empty for this version.

---

## How to Run

### 1. Copy V2 chat logs

```bash
chmod +x scripts/copy_logs.sh
./scripts/copy_logs.sh
```

This copies the V2 API chat logs into:

```text
data/input/chat_logs.jsonl
```

---

### 2. Run the feedback evaluator

```bash
chmod +x scripts/run_evaluator.sh
./scripts/run_evaluator.sh
```

The evaluator shows each sample like this:

```text
User: salam
Assistant: Salam dostum.

Feedback labels:
1. good
2. bad
3. generic
4. wrong_language
5. unnatural
6. wrong_intent
7. repetitive
s. skip
q. quit
```

Choose a label by typing only the number:

```text
1
```

You can also add an optional note.

---

### 3. Generate evaluation report

```bash
python3 src/report.py
```

The report will be saved to:

```text
data/output/evaluation_report.json
```

---

## Output Files

### `feedback_results.jsonl`

Stores manually labeled response evaluations.

Each line is one evaluated sample.

Example:

```json
{"user_message":"salam","assistant_response":"Salam dostum.","feedback":"good","note":"Short and correct greeting."}
```

---

### `evaluation_report.json`

Stores the final summary report.

It includes:

* total evaluated samples
* number of good responses
* number of issue responses
* good response percentage
* feedback label counts
* main issue counts

---

## Feedback Label Meaning

| Label            | Meaning                                     |
| ---------------- | ------------------------------------------- |
| `good`           | The response is correct and natural         |
| `bad`            | The response is generally poor              |
| `generic`        | The response is acceptable but too general  |
| `wrong_language` | The response uses the wrong language        |
| `unnatural`      | The response sounds unnatural               |
| `wrong_intent`   | The response misunderstands the user intent |
| `repetitive`     | The response repeats too much               |

---

## Example Evaluation

| User Message | Assistant Response           | Feedback         | Note                        |
| ------------ | ---------------------------- | ---------------- | --------------------------- |
| `salam`      | `Salam dostum.`              | `good`           | Short and correct           |
| `ok`         | `Əla, buradayam.`            | `generic`        | Repeated response           |
| `bye`        | `Əla, xoşaxşəm.`             | `unnatural`      | Goodbye response is weak    |
| `salam`      | Long wrong-language response | `wrong_language` | Wrong language and too long |

---

## Why This Project Matters

This project is important because fine-tuning alone is not enough.

A local assistant also needs:

* testing
* feedback collection
* response quality evaluation
* weak point detection
* dataset improvement planning

V4 creates a simple feedback loop for improving future Sahzade AI versions.

---

## Main Pipeline

```text
V2 chat logs
    ↓
copy_logs.sh
    ↓
data/input/chat_logs.jsonl
    ↓
manual evaluator
    ↓
feedback_results.jsonl
    ↓
report.py
    ↓
evaluation_report.json
```

---

## Current Status

```text
Status: Completed as V4 feedback evaluation experiment
```

This version successfully adds a simple manual evaluation workflow to the Sahzade AI project.

---

## Limitations

This version is intentionally simple.

Main limitations:

* manual labeling only
* no web dashboard
* no automatic grading
* no database
* no chart visualization
* no direct retraining pipeline
* no advanced metrics like precision or recall

---

## Future Improvements

Possible next improvements:

* add automatic evaluation rules
* add charts for feedback distribution
* create a small dashboard
* convert bad responses into new training examples
* generate improved dataset samples
* connect evaluation results to the next LoRA training dataset
* add RAG evaluation later
* add tool-use evaluation later

---

## Version Summary

```text
V1 → Fine-tuned LoRA adapter
V2 → Served adapter through FastAPI
V3 → Built browser chat UI
V4 → Added feedback and evaluation system
```

Sahzade AI Feedback Evaluator V4 is a small but important step toward improving assistant quality through real testing and structured feedback.
