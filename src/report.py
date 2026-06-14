import json 
from collections import Counter
from datetime import datetime

from config import (
    FEEDBACK_RESULTS_PATH,
    EVALUATION_REPORT_PATH
)



def load_feedback_results():
    results = []

    if not FEEDBACK_RESULTS_PATH.exists():
        print(f'feedback file not found: {FEEDBACK_RESULTS_PATH}')
        return results
    
    with open(FEEDBACK_RESULTS_PATH, 'r', encoding='utf-8') as file:
        for line_num, line  in enumerate(file, start=1):
            line = line.strip()

            if not line :
                continue

            try:
                results.append(json.loads(line))
            except json.JSONDecodeError:
                print(f'skipped invalid JSON at line {line_num}')
    
    return results



def create_report(results):
    feedback_lables = [item.get('feedback', 'unknown') for item in results]
    label_counts = Counter(feedback_lables)

    total = len(results)
    good_count = label_counts.get('good', 0)

    if total > 0:
        good_rate = round((good_count / total) * 100, 2)
    else:
        good_rate = 0.0

    issue_count = total - good_count


    report = {
        "generated_at": datetime.now().isoformat(),
        "total_evaluated": total,
        "good_count": good_count,
        "issue_count": issue_count,
        "good_rate_percent": good_rate,
        "label_counts": dict(label_counts),
        "main_issues": {
            "generic": label_counts.get("generic", 0),
            "wrong_language": label_counts.get("wrong_language", 0),
            "unnatural": label_counts.get("unnatural", 0),
            "wrong_intent": label_counts.get("wrong_intent", 0),
            "repetitive": label_counts.get("repetitive", 0),
            "bad": label_counts.get("bad", 0)
        }
    }

    return report


def save_report(report):
    EVALUATION_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(EVALUATION_REPORT_PATH, 'w', encoding='utf-8') as file:
        json.dump(report, file, ensure_ascii=False, indent=2)
        
    print("evaluation report saved successfully.")
    print(f"saved to: {EVALUATION_REPORT_PATH}")


def print_report(report):
    print("\nSahzade AI Evaluation Report")
    print("----------------------------")
    print(f"Total evaluated: {report['total_evaluated']}")
    print(f"Good responses: {report['good_count']}")
    print(f"Issue responses: {report['issue_count']}")
    print(f"Good rate: {report['good_rate_percent']}%")

    print("\nLabel counts:")
    for label, count in report["label_counts"].items():
        print(f"- {label}: {count}")

    print("\nMain issues:")
    for issue, count in report["main_issues"].items():
        print(f"- {issue}: {count}")


def main():
    results = load_feedback_results()

    if not results:
        print("No feedback results found.")
        return

    report = create_report(results)
    save_report(report)
    print_report(report)


if __name__ == "__main__":
    main()