"""
Wrapper for boto3 Inspector2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_inspector2/)

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
    # Returns type annotated boto3 Inspector2 client
    inspector2_client = session.inspector2.client()
    inspector2_client: types_boto3_inspector2.client.Inspector2Client
    ```
"""

from __future__ import annotations

from types_boto3_inspector2.client import Inspector2Client

from boto34.boto3.service_factory import ServiceFactory


class Inspector2Service(ServiceFactory[Inspector2Client]):
    SERVICE_NAME = "inspector2"
    _SERVICE_PROP = "inspector2"
