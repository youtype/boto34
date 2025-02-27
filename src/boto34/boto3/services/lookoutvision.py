"""
Wrapper for boto3 LookoutforVision service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lookoutvision/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 LookoutforVision client
    lookoutvision_client = session.lookoutvision.client()
    lookoutvision_client: types_boto3_lookoutvision.client.LookoutforVisionClient
    ```
"""

from __future__ import annotations

from types_boto3_lookoutvision.client import LookoutforVisionClient

from boto34.boto3.service_factory import ServiceFactory


class LookoutforVisionService(ServiceFactory[LookoutforVisionClient]):
    SERVICE_NAME = "lookoutvision"
    _SERVICE_PROP = "lookoutvision"
