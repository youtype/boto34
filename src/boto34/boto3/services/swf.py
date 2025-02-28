"""
Wrapper for boto3 SWF service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_swf/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_swf.client import SWFClient

from boto34.boto3.service_factory import ServiceFactory


class SWFService(ServiceFactory[SWFClient]):
    """
    SWF service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_swf/)
    """
