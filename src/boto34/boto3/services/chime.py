"""
Wrapper for boto3 Chime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_chime.client import ChimeClient

from boto34.boto3.service_factory import ServiceFactory


class ChimeService(ServiceFactory[ChimeClient]):
    """
    Chime service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime/)
    """
