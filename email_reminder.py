import json
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
TO_EMAIL = "your_email@gmail.com"
TASK_FILE = "tasks.json"

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def check_tasks_and_remind():
    try:
        with open(TASK_FILE, 'r') as f:
            tasks = json.load(f)
    except:
        tasks = []

    tomorrow = datetime.today().date() + timedelta(days=1)
    reminder_tasks = []

    for task in tasks:
        try:
            deadline = datetime.strptime(task['deadline'], "%Y-%m-%d").date()
            if deadline == tomorrow:
                reminder_tasks.append(f"- {task['task']} (due: {task['deadline']})")
        except:
            continue

    if reminder_tasks:
        body = "Yeh tasks kal due hain:

" + "\n".join(reminder_tasks)
        send_email("⏰ Kal ke Deadline Reminder", body)

check_tasks_and_remind()
