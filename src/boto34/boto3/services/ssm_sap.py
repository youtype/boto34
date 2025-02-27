"""
Wrapper for boto3 SsmSap service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm_sap/)

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
    # Returns type annotated boto3 SsmSap client
    ssm_sap_client = session.ssm_sap.client()
    ssm_sap_client: types_boto3_ssm_sap.client.SsmSapClient
    ```
"""

from __future__ import annotations

from types_boto3_ssm_sap.client import SsmSapClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_ssm_sap.client import SsmSapClient
except ImportError:
    SsmSapClient = object  # type: ignore[misc,assignment]


class SsmSapService(
    ServiceFactory[SsmSapClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ssm-sap"
    _SERVICE_PROP = "ssm_sap"
