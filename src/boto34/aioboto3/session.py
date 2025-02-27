"""
Type annotated wrapper for aioboto3 Session.

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session
    ```
"""

from aioboto3.session import Session as _Session

from boto34.aioboto3.services.s3 import S3Service


class Session(_Session):
    @property
    def s3(self) -> S3Service:
        return S3Service(self)
