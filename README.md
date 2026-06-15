# Sahzade AI Feedback Evaluator V4

A lightweight feedback and evaluation tool for the Sahzade AI local assistant.

## Overview

Sahzade AI Feedback Evaluator V4 is the fourth step of the Sahzade AI project.

In earlier versions, the assistant was fine-tuned, served through a local API, and connected to a simple chat interface.
In V4, the focus is on evaluating assistant responses and identifying weak response patterns.

The goal of this project is to create a simple feedback workflow that helps improve the assistant over time.

## Project Goals

* Read saved chat logs from the local assistant API
* Show user and assistant messages one by one
* Allow manual feedback labeling
* Save feedback results in JSONL format
* Generate a simple evaluation report
* Detect common response problems
* Prepare better data for future improvements

## What This Version Includes

* Chat log reader
* Manual response evaluator
* Feedback label system
* Feedback result saving
* Evaluation report generator
* Local JSONL-based workflow
* Simple terminal-based usage

## What This Version Does Not Include

* Automatic AI-based grading
* Web interface
* Database storage
* Model retraining
* Production monitoring
* Advanced analytics dashboard

These features can be added in later versions.

## Feedback Labels

The evaluator supports these labels:

```text
good
bad
generic
wrong_language
unnatural
wrong_intent
repetitive
```

These labels help identify whether an assistant response is useful, natural, relevant, and consistent with the expected style.

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

## Main Components

### `src/config.py`

Stores project paths and available feedback labels.

Main responsibilities:

* Define input and output paths
* Define chat log path
* Define feedback result path
* Define evaluation report path
* Store feedback label options

### `src/evaluator.py`

Reads chat logs and allows manual feedback labeling.

Main responsibilities:

* Load `chat_logs.jsonl`
* Show each conversation sample
* Ask the evaluator to choose a feedback label
* Optionally collect a short note
* Save feedback into `feedback_results.jsonl`

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

### `src/report.py`

Reads feedback results and creates a summary report.

Main responsibilities:

* Count feedback labels
* Calculate good response rate
* Count issue responses
* Save the evaluation report
* Print a summary in the terminal

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

## How to Run

### 1. Copy chat logs

```bash
chmod +x scripts/copy_logs.sh
./scripts/copy_logs.sh
```

### 2. Start the evaluator

```bash
chmod +x scripts/run_evaluator.sh
./scripts/run_evaluator.sh
```

### 3. Check output files

Feedback results:

```text
data/output/feedback_results.jsonl
```

Evaluation report:

```text
data/output/evaluation_report.json
```

## Why This Project Matters

Fine-tuning and building an assistant is not enough by itself.

A useful AI assistant also needs:

* response testing
* quality evaluation
* feedback collection
* weak pattern detection
* better data for future training

This project adds the first simple evaluation layer to the Sahzade AI system.

## Future Improvements

* Add more detailed feedback labels
* Add better reporting
* Add automatic issue detection
* Add a small dashboard
* Connect feedback results to future dataset improvement
* Use feedback data for later fine-tuning experiments

## Project Status

Completed as V4 feedback evaluation experiment.
