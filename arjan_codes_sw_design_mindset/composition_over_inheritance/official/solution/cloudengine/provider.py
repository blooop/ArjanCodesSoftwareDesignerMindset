from typing import Any

QueryResult = dict[str, dict[str, list[str]]]


class CloudProvider:
    def __init__(self, region: str, http_auth: Any, secure: bool):
        self.region = region
        self.http_auth = http_auth
        self.secure = secure

    def filter_by_query(self, bucket: str, query: str, max: int) -> QueryResult:
        return {"result": {"data": ["some data"]}}
