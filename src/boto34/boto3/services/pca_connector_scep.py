"""
Wrapper for boto3 PrivateCAConnectorforSCEP service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pca_connector_scep/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_pca_connector_scep.client import PrivateCAConnectorforSCEPClient

from boto34.boto3.service_factory import ServiceFactory


class PrivateCAConnectorforSCEPService(ServiceFactory[PrivateCAConnectorforSCEPClient]):
    """
    PrivateCAConnectorforSCEP service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pca_connector_scep/)
    """
