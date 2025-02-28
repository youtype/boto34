"""
Wrapper for boto3 Keyspaces service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_keyspaces/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_keyspaces.client import KeyspacesClient

from boto34.boto3.service_factory import ServiceFactory


class KeyspacesService(ServiceFactory[KeyspacesClient]):
    """
    Keyspaces service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_keyspaces/)
    """
