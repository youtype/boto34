"""
Wrapper for aioboto3 Inspector service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_inspector/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_inspector.client import InspectorClient

from boto34.aioboto3.service_factory import ServiceFactory


class InspectorService(ServiceFactory[InspectorClient]):
    """
    Inspector service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_inspector/)
    """
