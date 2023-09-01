from dataclasses import dataclass

from .google import GoogleCredentials, GoogleServiceProvider, GoogleStorage


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
