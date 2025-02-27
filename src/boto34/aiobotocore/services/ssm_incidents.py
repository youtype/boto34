"""
Wrapper for aiobotocore SSMIncidents service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_incidents/)

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
    # Returns type annotated aiobotocore SSMIncidents client
    async with session.ssm_incidents.create_client() as ssm_incidents_client:
        ssm_incidents_client: types_aiobotocore_ssm_incidents.client.SSMIncidentsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ssm_incidents.client import SSMIncidentsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SSMIncidentsService(ServiceFactory[SSMIncidentsClient]):
    SERVICE_NAME = "ssm-incidents"
    _SERVICE_PROP = "ssm_incidents"
