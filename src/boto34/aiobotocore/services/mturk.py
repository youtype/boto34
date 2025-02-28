"""
Wrapper for aiobotocore MTurk service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mturk/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mturk.client import MTurkClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MTurkService(ServiceFactory[MTurkClient]):
    """
    MTurk service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mturk/)
    """
