"""
Wrapper for aiobotocore IoTSiteWise service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iotsitewise.client import IoTSiteWiseClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTSiteWiseService(ServiceFactory[IoTSiteWiseClient]):
    """
    IoTSiteWise service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/)
    """
