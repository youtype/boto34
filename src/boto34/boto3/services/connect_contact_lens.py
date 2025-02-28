"""
Wrapper for boto3 ConnectContactLens service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connect_contact_lens/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_connect_contact_lens.client import ConnectContactLensClient

from boto34.boto3.service_factory import ServiceFactory


class ConnectContactLensService(ServiceFactory[ConnectContactLensClient]):
    """
    ConnectContactLens service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connect_contact_lens/)
    """
