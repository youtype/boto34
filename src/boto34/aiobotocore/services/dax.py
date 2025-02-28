"""
Wrapper for aiobotocore DAX service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_dax.client import DAXClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DAXService(ServiceFactory[DAXClient]):
    """
    DAX service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/)
    """
