"""
Wrapper for aioboto3 SSMIncidents service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ssm_incidents/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 SSMIncidents client
    ssm_incidents_client = session.ssm_incidents.client()
    ssm_incidents_client: types_aiobotocore_ssm_incidents.client.SSMIncidentsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ssm_incidents.client import SSMIncidentsClient

from boto34.aioboto3.service_factory import ServiceFactory


class SSMIncidentsService(ServiceFactory[SSMIncidentsClient]):
    SERVICE_NAME = "ssm-incidents"
    _SERVICE_PROP = "ssm_incidents"
