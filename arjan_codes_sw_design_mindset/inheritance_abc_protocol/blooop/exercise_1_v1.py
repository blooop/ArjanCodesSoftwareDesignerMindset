from time import time
from dataclasses import dataclass,field



@dataclass
class Post:
    message: str
    timestamp: int


@dataclass
class SocialChannel:
    channel_type: str
    follower: int
    post_dict:dict =field(init=False)

    def __post_init__(self):
        self.post_dict={"youtube":self.post_to_youtube,"facebook":self.post_to_facebook,"twitter":self.post_to_twitter}

    def post_to_youtube(self, message: str) -> None:
        print(f"{self.channel_type} channel: {message}")

    def post_to_facebook(self, message: str) -> None:
        print(f"{self.channel_type} channel: {message}")

    def post_to_twitter(self, message: str) -> None:
        print(f"{self.channel_type} channel: {message}")

    def post_a_message(self, message: str) -> None:
        return self.post_dict[self.channel_type](message)
        


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        message, timestamp = post
        for channel in channels:
            if timestamp <= time():
                channel.post_a_message(message)


def main() -> None:
    posts = [
        (
            "Grandma's carrot cake is available again (limited quantities!)!",
            1568123400,
        ),
        ("Get your carrot cake now, the promotion ends today!", 1568133400),
    ]
    channels = [
        SocialChannel("youtube", 100),
        SocialChannel("facebook", 100),
        SocialChannel("twitter", 100),
    ]
    process_schedule(posts, channels)


if __name__ == "__main__":
    main()
