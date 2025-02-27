"""
Wrapper for boto3 SWF service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_swf/)

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
    # Returns type annotated boto3 SWF client
    swf_client = session.swf.client()
    swf_client: types_boto3_swf.client.SWFClient
    ```
"""

from __future__ import annotations

from types_boto3_swf.client import SWFClient

from boto34.boto3.service_factory import ServiceFactory


class SWFService(ServiceFactory[SWFClient]):
    SERVICE_NAME = "swf"
    _SERVICE_PROP = "swf"
