"""
Wrapper for aiobotocore Outposts service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_outposts.client import OutpostsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class OutpostsService(ServiceFactory[OutpostsClient]):
    """
    Outposts service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/)
    """
