"""
Wrapper for boto3 Omics service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_omics/)

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
    # Returns type annotated boto3 Omics client
    omics_client = session.omics.client()
    omics_client: types_boto3_omics.client.OmicsClient
    ```
"""

from __future__ import annotations

from types_boto3_omics.client import OmicsClient

from boto34.boto3.service_factory import ServiceFactory


class OmicsService(ServiceFactory[OmicsClient]):
    SERVICE_NAME = "omics"
    _SERVICE_PROP = "omics"
