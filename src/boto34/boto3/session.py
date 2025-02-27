"""
Type annotated wrapper for boto3 Session.

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session
    ```
"""

from boto3.session import Session as _Session

from boto34.boto3.services.acm import ACMService
from boto34.boto3.services.s3 import S3Service


class Session(_Session):
    @property
    def s3(self) -> S3Service:
        return S3Service(self)

    @property
    def acm(self) -> ACMService:
        return ACMService(self)
