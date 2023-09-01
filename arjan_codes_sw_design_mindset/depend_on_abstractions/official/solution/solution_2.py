from typing import Protocol

DEFAULT_EMAIL = "support@arjancodes.com"
LOGIN = "test"
PASSWORD = "my_password"
HOST = "smtp.arjancodes.com"
PORT = 19584


class EmailServer(Protocol):
    def connect(self, host: str, port: int) -> None:
        ...

    def login(self, user: str, password: str) -> None:
        ...

    def quit(self) -> None:
        ...

    def sendmail(
        self,
        from_address: str,
        to_address: str,
        message: str,
    ) -> None:
        ...


def send_email(
    server: EmailServer,
    message: str,
    to_address: str,
    from_address: str = DEFAULT_EMAIL,
) -> None:
    server.connect(HOST, PORT)
    server.login(LOGIN, PASSWORD)
    server.sendmail(from_address, to_address, message)
    server.quit()
