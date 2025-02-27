"""
Wrapper for boto3 QuickSight service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_quicksight/)

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
    # Returns type annotated boto3 QuickSight client
    quicksight_client = session.quicksight.client()
    quicksight_client: types_boto3_quicksight.client.QuickSightClient
    ```
"""

from __future__ import annotations

from types_boto3_quicksight.client import QuickSightClient

from boto34.boto3.service_factory import ServiceFactory


class QuickSightService(ServiceFactory[QuickSightClient]):
    SERVICE_NAME = "quicksight"
    _SERVICE_PROP = "quicksight"
