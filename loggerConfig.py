import logging
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class CustomGmailHandler(logging.Handler):
    """
    Custom gmail log handler
    """

    def __init__(self, subject, recipient_email, gmail_user, gmail_pass):
        logging.Handler.__init__(self)
        self.recipient_email = recipient_email
        self.gmail_user = gmail_user
        self.gmail_pass = gmail_pass
        self.mail_subject = subject

    def emit(self, record):
        formated_record = self.format(record)

        to = self.recipient_email
        subj = self.mail_subject

        # Gmail needs a MIME multipart with html and plain text if an html message is to be sent
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subj
        msg['From'] = self.gmail_user
        msg['To'] = to

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(formated_record, 'plain')
        part2 = MIMEText(formated_record, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            # server.set_debuglevel(True)

            server.ehlo()
            server.login(str(self.gmail_user), str(self.gmail_pass))
            server.sendmail(self.gmail_user, to, msg.as_string())
            server.quit()
            print("The email has sent")
        except:
            #Todo: Handle properly ...
            print("Error. Email not sent")


def loggerInit():
    """Initializes loggers for this project"""
    # 1. Init logger
    logger = logging.getLogger("Main")
    logger.setLevel(logging.DEBUG)

    # 2. Create Handlers
    log_stream_handle = logging.StreamHandler(stream=sys.stdout)

    log_file_handle = logging.FileHandler("logfile_corona.log")
    log_file_handle.setLevel(logging.INFO)

    log_mail_handle = CustomGmailHandler(subject="Error Report - FetchWorldometer",
                                         recipient_email="TBD@gmail.com",
                                         gmail_user="TBD@gmail.com",
                                         gmail_pass="TBD")
    log_mail_handle.setLevel(logging.ERROR)

    # 3. Create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s(%(lineno)s) - %(message)s')
    log_stream_handle.setFormatter(formatter)
    log_file_handle.setFormatter(formatter)
    log_mail_handle.setFormatter(formatter)

    # 4. Add Loggers
    logger.addHandler(log_stream_handle)
    logger.addHandler(log_file_handle)
    logger.addHandler(log_mail_handle)
