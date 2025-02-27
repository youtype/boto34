"""
Wrapper for aiobotocore ComprehendMedical service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehendmedical/)

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
    # Returns type annotated aiobotocore ComprehendMedical client
    async with session.comprehendmedical.create_client() as comprehendmedical_client:
        comprehendmedical_client: types_aiobotocore_comprehendmedical.client.ComprehendMedicalClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_comprehendmedical.client import ComprehendMedicalClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_comprehendmedical.client import ComprehendMedicalClient
except ImportError:
    ComprehendMedicalClient = object  # type: ignore[misc,assignment]


class ComprehendMedicalService(
    ServiceFactory[ComprehendMedicalClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "comprehendmedical"
    _SERVICE_PROP = "comprehendmedical"
