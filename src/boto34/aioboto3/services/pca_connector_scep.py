"""
Wrapper for aioboto3 PrivateCAConnectorforSCEP service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pca_connector_scep/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_pca_connector_scep.client import PrivateCAConnectorforSCEPClient

from boto34.aioboto3.service_factory import ServiceFactory


class PrivateCAConnectorforSCEPService(ServiceFactory[PrivateCAConnectorforSCEPClient]):
    """
    PrivateCAConnectorforSCEP service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pca_connector_scep/)
    """
