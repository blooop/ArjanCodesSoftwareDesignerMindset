class GoogleCredentials:
    def retrieve_credentials(self) -> str:
        return "ADSFGKJASADFLK345098SDFSDFLKJ"


class GoogleServiceProvider:
    def connect(self, credentials: str) -> None:
        print("Connecting to Google Cloud.")

    def get_context(self) -> str:
        return "my_project"


class GoogleStorage:
    def initialize(self, context: str) -> None:
        print(f"Initializing storage with context {context}.")
