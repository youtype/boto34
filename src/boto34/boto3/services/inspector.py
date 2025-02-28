"""
Wrapper for boto3 Inspector service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_inspector/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_inspector.client import InspectorClient

from boto34.boto3.service_factory import ServiceFactory


class InspectorService(ServiceFactory[InspectorClient]):
    """
    Inspector service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_inspector/)
    """
