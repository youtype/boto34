"""
Wrapper for boto3 WAF service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_waf/)

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
    # Returns type annotated boto3 WAF client
    waf_client = session.waf.client()
    waf_client: types_boto3_waf.client.WAFClient
    ```
"""

from __future__ import annotations

from types_boto3_waf.client import WAFClient

from boto34.boto3.service_factory import ServiceFactory


class WAFService(ServiceFactory[WAFClient]):
    SERVICE_NAME = "waf"
    _SERVICE_PROP = "waf"
