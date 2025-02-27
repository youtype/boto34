"""
Wrapper for aioboto3 ComprehendMedical service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_comprehendmedical/)

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
    # Returns type annotated aioboto3 ComprehendMedical client
    comprehendmedical_client = session.comprehendmedical.client()
    comprehendmedical_client: types_aiobotocore_comprehendmedical.client.ComprehendMedicalClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_comprehendmedical.client import ComprehendMedicalClient

from boto34.aioboto3.service_factory import ServiceFactory


class ComprehendMedicalService(ServiceFactory[ComprehendMedicalClient]):
    SERVICE_NAME = "comprehendmedical"
    _SERVICE_PROP = "comprehendmedical"
