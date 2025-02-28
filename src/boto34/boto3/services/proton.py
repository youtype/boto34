"""
Wrapper for boto3 Proton service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_proton/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_proton.client import ProtonClient

from boto34.boto3.service_factory import ServiceFactory


class ProtonService(ServiceFactory[ProtonClient]):
    """
    Proton service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_proton/)
    """
