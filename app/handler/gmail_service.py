import smtplib
import logging.config
from app.config import GmailServiceConfig
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


log = logging.getLogger(__name__)


def send_email(notify_receiver_email):
    
    sender_email = GmailServiceConfig.Sender_eamil # 設定寄信者及收件者的 Email 地址
    receiver_email = notify_receiver_email

    smtp_server = GmailServiceConfig.Smtp_Server
    port = GmailServiceConfig.Port 

    
    password = GmailServiceConfig.App_Password # 應用程式專用密碼（注意：這不是你的 Gmail 密碼）

    
    message = MIMEMultipart()             # 設定郵件內容
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "即將到站通知"

    
    body = "公車即將抵達目的地 !!"            # 郵件主體
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        
    except Exception as e:
        send_email()
        log.error(f"gmail_service send_email error: {e}")

    finally:
        server.quit()
