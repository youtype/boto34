"""
Wrapper for aiobotocore PrometheusService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_amp.client import PrometheusServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class PrometheusServiceService(ServiceFactory[PrometheusServiceClient]):
    """
    PrometheusService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/)
    """
