"""
Wrapper for aioboto3 Inspector2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_inspector2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_inspector2.client import Inspector2Client

from boto34.aioboto3.service_factory import ServiceFactory


class Inspector2Service(ServiceFactory[Inspector2Client]):
    """
    Inspector2 service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_inspector2/)
    """
