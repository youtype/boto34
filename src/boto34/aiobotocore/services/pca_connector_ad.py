"""
Wrapper for aiobotocore PcaConnectorAd service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_pca_connector_ad.client import PcaConnectorAdClient

from boto34.aiobotocore.service_factory import ServiceFactory


class PcaConnectorAdService(ServiceFactory[PcaConnectorAdClient]):
    """
    PcaConnectorAd service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/)
    """
