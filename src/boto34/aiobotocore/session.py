"""
Type annotated wrapper for aiobotocore Session.

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.Session constructor
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session
    ```
"""

from __future__ import annotations

from typing import Mapping

from aiobotocore.session import AioSession as _Session

from boto34.aiobotocore.services.acm import ACMService
from boto34.aiobotocore.services.s3 import S3Service


class Session(_Session):
    @property
    def s3(self) -> S3Service:
        return S3Service(self)

    @property
    def acm(self) -> ACMService:
        return ACMService(self)


def get_session(env_vars: Mapping[str, str] | None = None) -> Session:
    return Session(session_vars=env_vars)
