"""
Wrapper for boto3 PcaConnectorAd service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pca_connector_ad/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_pca_connector_ad.client import PcaConnectorAdClient

from boto34.boto3.service_factory import ServiceFactory


class PcaConnectorAdService(ServiceFactory[PcaConnectorAdClient]):
    """
    PcaConnectorAd service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pca_connector_ad/)
    """
