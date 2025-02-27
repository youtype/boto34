"""
Wrapper for aiobotocore LakeFormation service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lakeformation/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore LakeFormation client
    async with session.lakeformation.create_client() as lakeformation_client:
        lakeformation_client: types_aiobotocore_lakeformation.client.LakeFormationClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_lakeformation.client import LakeFormationClient
except ImportError:
    LakeFormationClient = object  # type: ignore[misc,assignment]


class LakeFormationService(
    ServiceFactory[LakeFormationClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lakeformation"
    _SERVICE_PROP = "lakeformation"
