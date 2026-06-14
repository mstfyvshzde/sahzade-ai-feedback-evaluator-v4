from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_DIR = BASE_DIR / "data" / "input"
OUTPUT_DIR = BASE_DIR / "data" / "output"

CHAT_LOGS_PATH = INPUT_DIR / "chat_logs.jsonl"
FEEDBACK_RESULTS_PATH = OUTPUT_DIR / "feedback_results.jsonl"
EVALUATION_REPORT_PATH = OUTPUT_DIR / "evaluation_report.json"


FEEDBACK_LABELS = {
    "1": "good",
    "2": "bad",
    "3": "generic",
    "4": "wrong_language",
    "5": "unnatural",
    "6": "wrong_intent",
    "7": "repetitive"
}