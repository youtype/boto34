"""
Wrapper for boto3 Signer service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_signer/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_signer.client import SignerClient

from boto34.boto3.service_factory import ServiceFactory


class SignerService(ServiceFactory[SignerClient]):
    """
    Signer service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_signer/)
    """
