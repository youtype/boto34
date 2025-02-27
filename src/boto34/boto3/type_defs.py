from typing import TypedDict

from botocore.config import Config


class ClientKwargs(TypedDict, total=False):
    region_name: str | None
    api_version: str | None
    use_ssl: bool | None
    verify: bool | str | None
    endpoint_url: str | None
    aws_access_key_id: str | None
    aws_secret_access_key: str | None
    aws_session_token: str | None
    config: Config | None
    aws_account_id: str | None


class ResourceKwargs(TypedDict, total=False):
    region_name: str | None
    api_version: str | None
    use_ssl: bool | None
    verify: bool | str | None
    endpoint_url: str | None
    aws_access_key_id: str | None
    aws_secret_access_key: str | None
    aws_session_token: str | None
    config: Config | None
