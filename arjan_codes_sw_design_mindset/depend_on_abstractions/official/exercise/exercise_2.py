from smtplib import SMTP

DEFAULT_EMAIL = "support@arjancodes.com"
LOGIN = "test"
PASSWORD = "my_password"
HOST = "smtp.arjancodes.com"
PORT = 19584


def send_email(
    message: str, to_address: str, from_address: str = DEFAULT_EMAIL
) -> None:
    server = SMTP()
    server.connect(HOST, PORT)
    server.login(LOGIN, PASSWORD)
    server.sendmail(from_address, to_address, message)
    server.quit()
