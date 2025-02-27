"""
Wrapper for boto3 WAFV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_wafv2/)

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
    # Returns type annotated boto3 WAFV2 client
    wafv2_client = session.wafv2.client()
    wafv2_client: types_boto3_wafv2.client.WAFV2Client
    ```
"""

from __future__ import annotations

from types_boto3_wafv2.client import WAFV2Client

from boto34.boto3.service_factory import ServiceFactory


class WAFV2Service(ServiceFactory[WAFV2Client]):
    SERVICE_NAME = "wafv2"
    _SERVICE_PROP = "wafv2"
