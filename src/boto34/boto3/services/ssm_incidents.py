"""
Wrapper for boto3 SSMIncidents service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm_incidents/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 SSMIncidents client
    ssm_incidents_client = session.ssm_incidents.client()
    ssm_incidents_client: types_boto3_ssm_incidents.client.SSMIncidentsClient
    ```
"""

from __future__ import annotations

from types_boto3_ssm_incidents.client import SSMIncidentsClient

from boto34.boto3.service_factory import ServiceFactory


class SSMIncidentsService(ServiceFactory[SSMIncidentsClient]):
    SERVICE_NAME = "ssm-incidents"
    _SERVICE_PROP = "ssm_incidents"
