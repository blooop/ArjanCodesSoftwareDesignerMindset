from dataclasses import dataclass
from enum import StrEnum


class Camera(StrEnum):
    FRONT = "front"
    BACK = "back"


@dataclass
class QRScanner:
    camera: Camera = Camera.FRONT

    def choose_camera(self, camera: Camera) -> None:
        print(f"Choosing camera {camera.value}.")
        self.camera = camera

    def scan(self) -> str:
        print(f"Scanning QR code with {self.camera.value} camera.")
        return "https://www.arjancodes.com"


class Browser:
    def open(self, url: str) -> None:
        print(f"Opening {url} in the browser.")

    def open_from_qr_code(self) -> None:
        qr = QRScanner()
        qr.choose_camera(Camera.BACK)
        url = qr.scan()
        self.open(url)


def main() -> None:
    print("Navigating to website on device.")
    browser = Browser()
    browser.open_from_qr_code()


if __name__ == "__main__":
    main()
