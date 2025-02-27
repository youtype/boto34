"""
Wrapper for boto3 Athena service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_athena/)

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
    # Returns type annotated boto3 Athena client
    athena_client = session.athena.client()
    athena_client: types_boto3_athena.client.AthenaClient
    ```
"""

from __future__ import annotations

from types_boto3_athena.client import AthenaClient

from boto34.boto3.service_factory import ServiceFactory


class AthenaService(ServiceFactory[AthenaClient]):
    SERVICE_NAME = "athena"
    _SERVICE_PROP = "athena"
