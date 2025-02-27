"""
Wrapper for boto3 MWAA service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mwaa/)

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
    # Returns type annotated boto3 MWAA client
    mwaa_client = session.mwaa.client()
    mwaa_client: types_boto3_mwaa.client.MWAAClient
    ```
"""

from __future__ import annotations

from types_boto3_mwaa.client import MWAAClient

from boto34.boto3.service_factory import ServiceFactory


class MWAAService(ServiceFactory[MWAAClient]):
    SERVICE_NAME = "mwaa"
    _SERVICE_PROP = "mwaa"
