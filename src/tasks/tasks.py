import smtplib
from email import encoders
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from typing import List

from celery import Celery
from config import SMTP_USER, SMTP_PASSWORD

from os.path import basename

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

celery = Celery("tasks", broker="redis://localhost:6379")


@celery.task
def send_email_report_dashboard(mail: str, table_list: List[str]):
    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = COMMASPACE.join(mail)
    msg["Subject"] = "Таблицы нарушений"

    body = "Здравствуйте! А вот и ваши таблицы."

    msg.attach(MIMEText(body, "plain"))

    for i in range(3):
        with open(f"/home/vismut/school/src/{table_list[i]}", "rb") as f:
            file = MIMEApplication(f.read(), name=basename(f"table_{table_list[i][:-5]}.xlsx"))
            msg.attach(file)
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, mail, msg.as_string())
