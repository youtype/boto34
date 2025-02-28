"""
Wrapper for boto3 ACMPCA service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm_pca/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_acm_pca.client import ACMPCAClient

from boto34.boto3.service_factory import ServiceFactory


class ACMPCAService(ServiceFactory[ACMPCAClient]):
    """
    ACMPCA service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm_pca/)
    """
