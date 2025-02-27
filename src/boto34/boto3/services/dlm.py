"""
Wrapper for boto3 DLM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dlm/)

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
    # Returns type annotated boto3 DLM client
    dlm_client = session.dlm.client()
    dlm_client: types_boto3_dlm.client.DLMClient
    ```
"""

from __future__ import annotations

from types_boto3_dlm.client import DLMClient

from boto34.boto3.service_factory import ServiceFactory


class DLMService(ServiceFactory[DLMClient]):
    SERVICE_NAME = "dlm"
    _SERVICE_PROP = "dlm"
