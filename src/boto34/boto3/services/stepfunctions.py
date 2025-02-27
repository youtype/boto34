"""
Wrapper for boto3 SFN service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_stepfunctions/)

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
    # Returns type annotated boto3 SFN client
    stepfunctions_client = session.stepfunctions.client()
    stepfunctions_client: types_boto3_stepfunctions.client.SFNClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_stepfunctions.client import SFNClient
except ImportError:
    SFNClient = object  # type: ignore[misc,assignment]


class SFNService(
    ServiceFactory[SFNClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "stepfunctions"
    _SERVICE_PROP = "stepfunctions"
