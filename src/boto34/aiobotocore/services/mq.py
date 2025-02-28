"""
Wrapper for aiobotocore MQ service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mq/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mq.client import MQClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MQService(ServiceFactory[MQClient]):
    """
    MQ service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mq/)
    """
