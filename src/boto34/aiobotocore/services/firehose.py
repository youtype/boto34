"""
Wrapper for aiobotocore Firehose service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_firehose/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_firehose.client import FirehoseClient

from boto34.aiobotocore.service_factory import ServiceFactory


class FirehoseService(ServiceFactory[FirehoseClient]):
    """
    Firehose service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_firehose/)
    """
