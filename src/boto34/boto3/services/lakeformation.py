"""
Wrapper for boto3 LakeFormation service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lakeformation/)

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
    # Returns type annotated boto3 LakeFormation client
    lakeformation_client = session.lakeformation.client()
    lakeformation_client: types_boto3_lakeformation.client.LakeFormationClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_lakeformation.client import LakeFormationClient
except ImportError:
    LakeFormationClient = object  # type: ignore[misc,assignment]


class LakeFormationService(
    ServiceFactory[LakeFormationClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lakeformation"
    _SERVICE_PROP = "lakeformation"
