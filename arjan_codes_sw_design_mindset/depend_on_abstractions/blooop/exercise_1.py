from dataclasses import dataclass
from typing import Protocol


class Credientials:
    pass


class AuthProvider(Protocol):
    def retrieve_credentials(self) -> Credientials:
        ...


class ServiceContext:
    pass


class ServiceProvider(Protocol):
    def get_context(self) -> ServiceContext:
        ...

    def connect(self, credential: Credientials) -> None:
        ...


class StorageManger(Protocol):
    def initialize(self, context: ServiceContext):
        ...


@dataclass
class CloudService:
    auth_provider: AuthProvider
    service: ServiceProvider
    storage_manager: StorageManger

    def connect(self) -> None:
        print("Connecting to the cloud service.")
        credentials = self.auth_provider.retrieve_credentials()
        self.service.connect(credentials)
        context = self.service.get_context()
        self.storage_manager.initialize(context)
        print("Cloud service connected.")
