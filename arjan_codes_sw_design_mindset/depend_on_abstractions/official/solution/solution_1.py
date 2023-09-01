from dataclasses import dataclass
from typing import Protocol


class CloudCredentials(Protocol):
    def retrieve_credentials(self) -> str:
        ...


class CloudServiceProvider(Protocol):
    def connect(self, credentials: str) -> None:
        ...

    def get_context(self) -> str:
        ...


class CloudStorage(Protocol):
    def initialize(self, context: str) -> None:
        ...


@dataclass
class CloudService:
    auth_provider: CloudCredentials
    service: CloudServiceProvider
    storage_manager: CloudStorage

    def connect(self) -> None:
        print("Connecting to the cloud service.")
        credentials = self.auth_provider.retrieve_credentials()
        self.service.connect(credentials)
        context = self.service.get_context()
        self.storage_manager.initialize(context)
        print("Cloud service connected.")
