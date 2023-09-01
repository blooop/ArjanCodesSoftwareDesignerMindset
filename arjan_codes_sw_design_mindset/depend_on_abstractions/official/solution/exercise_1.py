from dataclasses import dataclass

from google_service import GoogleCredentials, GoogleServiceProvider, GoogleStorage


@dataclass
class CloudService:
    auth_provider: GoogleCredentials
    service: GoogleServiceProvider
    storage_manager: GoogleStorage

    def connect(self) -> None:
        print("Connecting to the cloud service.")
        credentials = self.auth_provider.retrieve_credentials()
        self.service.connect(credentials)
        context = self.service.get_context()
        self.storage_manager.initialize(context)
        print("Cloud service connected.")


def main() -> None:
    credentials = GoogleCredentials()
    service = GoogleServiceProvider()
    storage = GoogleStorage()
    cloud_service = CloudService(credentials, service, storage)
    cloud_service.connect()


if __name__ == "__main__":
    main()
