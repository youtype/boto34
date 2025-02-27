"""
Wrapper for aioboto3 SES service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ses/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 SES client
    ses_client = session.ses.client()
    ses_client: types_aiobotocore_ses.client.SESClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ses.client import SESClient

from boto34.aioboto3.service_factory import ServiceFactory


class SESService(ServiceFactory[SESClient]):
    SERVICE_NAME = "ses"
    _SERVICE_PROP = "ses"
