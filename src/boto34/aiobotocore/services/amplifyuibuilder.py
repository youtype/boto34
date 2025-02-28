"""
Wrapper for aiobotocore AmplifyUIBuilder service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_amplifyuibuilder.client import AmplifyUIBuilderClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AmplifyUIBuilderService(ServiceFactory[AmplifyUIBuilderClient]):
    """
    AmplifyUIBuilder service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/)
    """
