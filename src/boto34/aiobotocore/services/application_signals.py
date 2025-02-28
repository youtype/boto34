"""
Wrapper for aiobotocore CloudWatchApplicationSignals service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_signals/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_application_signals.client import CloudWatchApplicationSignalsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudWatchApplicationSignalsService(ServiceFactory[CloudWatchApplicationSignalsClient]):
    """
    CloudWatchApplicationSignals service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_signals/)
    """
