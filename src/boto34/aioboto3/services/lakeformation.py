"""
Wrapper for aioboto3 LakeFormation service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lakeformation/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 LakeFormation client
    lakeformation_client = session.lakeformation.client()
    lakeformation_client: types_aiobotocore_lakeformation.client.LakeFormationClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_lakeformation.client import LakeFormationClient
except ImportError:
    LakeFormationClient = object  # type: ignore[misc,assignment]


class LakeFormationService(
    ServiceFactory[LakeFormationClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lakeformation"
    _SERVICE_PROP = "lakeformation"
