"""
Wrapper for aiobotocore CloudFormation service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore CloudFormation client
    async with session.cloudformation.create_client() as cloudformation_client:
        cloudformation_client: types_aiobotocore_cloudformation.client.CloudFormationClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cloudformation.client import CloudFormationClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudFormationService(ServiceFactory[CloudFormationClient]):
    SERVICE_NAME = "cloudformation"
    _SERVICE_PROP = "cloudformation"
