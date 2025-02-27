"""
Wrapper for aiobotocore FraudDetector service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_frauddetector/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore FraudDetector client
    async with session.frauddetector.create_client() as frauddetector_client:
        frauddetector_client: types_aiobotocore_frauddetector.client.FraudDetectorClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_frauddetector.client import FraudDetectorClient

from boto34.aiobotocore.service_factory import ServiceFactory


class FraudDetectorService(ServiceFactory[FraudDetectorClient]):
    SERVICE_NAME = "frauddetector"
    _SERVICE_PROP = "frauddetector"
