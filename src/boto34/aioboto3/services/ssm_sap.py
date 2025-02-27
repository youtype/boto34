"""
Wrapper for aioboto3 SsmSap service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ssm_sap/)

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
    # Returns type annotated aioboto3 SsmSap client
    ssm_sap_client = session.ssm_sap.client()
    ssm_sap_client: types_aiobotocore_ssm_sap.client.SsmSapClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ssm_sap.client import SsmSapClient

from boto34.aioboto3.service_factory import ServiceFactory


class SsmSapService(ServiceFactory[SsmSapClient]):
    SERVICE_NAME = "ssm-sap"
    _SERVICE_PROP = "ssm_sap"
