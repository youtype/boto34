"""
Wrapper for boto3 AmplifyUIBuilder service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_amplifyuibuilder/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_amplifyuibuilder.client import AmplifyUIBuilderClient

from boto34.boto3.service_factory import ServiceFactory


class AmplifyUIBuilderService(ServiceFactory[AmplifyUIBuilderClient]):
    """
    AmplifyUIBuilder service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_amplifyuibuilder/)
    """
