"""
Wrapper for boto3 Ivschat service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ivschat/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ivschat.client import IvschatClient

from boto34.boto3.service_factory import ServiceFactory


class IvschatService(ServiceFactory[IvschatClient]):
    """
    Ivschat service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ivschat/)
    """
