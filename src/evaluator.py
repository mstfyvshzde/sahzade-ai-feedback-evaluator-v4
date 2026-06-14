import json
from datetime import datetime

from config import (
    CHAT_LOGS_PATH,
    FEEDBACK_LABELS,
    FEEDBACK_RESULTS_PATH
)




def load_chat_logs():
    logs = []

    if not CHAT_LOGS_PATH.exists():
        print(f'chat log filr not dound: {CHAT_LOGS_PATH}')
        return logs
    
    with open(CHAT_LOGS_PATH, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                logs.append(json.loads(line))
            except json.JSONDecodeError:
                print(f'skipped invalid JSON at line {line_num}')
    
    return logs






def show_label_options():
    print("\nFeedback labels:")
    print("1. good")
    print("2. bad")
    print("3. generic")
    print("4. wrong_language")
    print("5. unnatural")
    print("6. wrong_intent")
    print("7. repetitive")
    print("s. skip")
    print("q. quit")




def get_feedback_from_user():
    label_map = {
        "1": "good",
        "2": "bad",
        "3": "generic",
        "4": "wrong_language",
        "5": "unnatural",
        "6": "wrong_intent",
        "7": "repetitive"
    }

    while True:
        show_label_options()

        choice = input('\nchoose label: ').strip().lower()

        if choice in label_map:
            return label_map[choice]
        
        if choice =='s':
            return 'skipped'
        
        if choice == 'q':
            return 'quit'
        
        if choice is FEEDBACK_LABELS:
            return FEEDBACK_LABELS[choice]
        
        if choice.isdigit():
            number_choice = int(choice)

            if number_choice in FEEDBACK_LABELS:
                return FEEDBACK_LABELS[number_choice]
        
        print('invalid choice. Pls try again')





def save_feedback(log_item, feedback_label, note):
    feedback_data = {
        'evaluated_at': datetime.now().isoformat(),
        'time': log_item.get('time'),
        'user_message': log_item.get('user_message'),
        'assistant_response': log_item.get('assistant_response'),
        'feedback': feedback_label,
        'note': note
    }

    with open(FEEDBACK_RESULTS_PATH, 'a', encoding='utf-8') as file:
        file.write(json.dumps(feedback_data, ensure_ascii=False) + '\n')


def run_evaluator():
    logs = load_chat_logs()

    if not logs:
        print('no chat logs found')   
        return

    FEEDBACK_RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)

    print("Sahzade AI Feedback Evaluator V4")
    print("--------------------------------")
    print(f"Loaded chat logs: {len(logs)}")


    for index, log_item in enumerate(logs, start=1):
        user_message = log_item.get('user_message', '')
        assistant_response = log_item.get('assistant_response', '')

        print("\n================================")
        print(f"sample {index}/{len(logs)}")
        print("--------------------------------")
        print(f"user: {user_message}")
        print(f"assistant: {assistant_response}")

        feedback_label = get_feedback_from_user()

        if feedback_label == 'quit':
            print('evaluation stopped')
            break

        if feedback_label == 'skipped':
            print('sample skipped')
            continue

        note = input('optional note: '). strip()

        save_feedback(log_item, feedback_label, note)

        print('feedback saved')

    print('\nevaluation stopped')



if __name__ == '__main__':
    run_evaluator()


