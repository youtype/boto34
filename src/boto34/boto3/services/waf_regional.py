"""
Wrapper for boto3 WAFRegional service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_waf_regional/)

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
    # Returns type annotated boto3 WAFRegional client
    waf_regional_client = session.waf_regional.client()
    waf_regional_client: types_boto3_waf_regional.client.WAFRegionalClient
    ```
"""

from __future__ import annotations

from types_boto3_waf_regional.client import WAFRegionalClient

from boto34.boto3.service_factory import ServiceFactory


class WAFRegionalService(ServiceFactory[WAFRegionalClient]):
    SERVICE_NAME = "waf-regional"
    _SERVICE_PROP = "waf_regional"
