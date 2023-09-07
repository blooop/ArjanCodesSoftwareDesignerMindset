from typing import Callable


Retrieve = Callable[[], str]
Connect = Callable[[], None]
Initialize = Callable[[str], None]


class CloudService:
    def connect(
        self, credentials: Retrieve, connect: Connect, context: Retrieve, initialize: Initialize
    ) -> None:
        print("Connecting to the cloud service.")
        connect(credentials)
        initialize(context)
        print("Cloud service connected.")
