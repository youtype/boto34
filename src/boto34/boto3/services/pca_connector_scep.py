"""
Wrapper for boto3 PrivateCAConnectorforSCEP service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pca_connector_scep/)

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
    # Returns type annotated boto3 PrivateCAConnectorforSCEP client
    pca_connector_scep_client = session.pca_connector_scep.client()
    pca_connector_scep_client: types_boto3_pca_connector_scep.client.PrivateCAConnectorforSCEPClient
    ```
"""

from __future__ import annotations

from types_boto3_pca_connector_scep.client import PrivateCAConnectorforSCEPClient

from boto34.boto3.service_factory import ServiceFactory


class PrivateCAConnectorforSCEPService(ServiceFactory[PrivateCAConnectorforSCEPClient]):
    SERVICE_NAME = "pca-connector-scep"
    _SERVICE_PROP = "pca_connector_scep"
