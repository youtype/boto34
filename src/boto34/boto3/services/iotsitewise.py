"""
Wrapper for boto3 IoTSiteWise service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotsitewise/)

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
    # Returns type annotated boto3 IoTSiteWise client
    iotsitewise_client = session.iotsitewise.client()
    iotsitewise_client: types_boto3_iotsitewise.client.IoTSiteWiseClient
    ```
"""

from __future__ import annotations

from types_boto3_iotsitewise.client import IoTSiteWiseClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_iotsitewise.client import IoTSiteWiseClient
except ImportError:
    IoTSiteWiseClient = object  # type: ignore[misc,assignment]


class IoTSiteWiseService(
    ServiceFactory[IoTSiteWiseClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotsitewise"
    _SERVICE_PROP = "iotsitewise"
