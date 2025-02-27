"""
Wrapper for boto3 ComprehendMedical service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_comprehendmedical/)

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
    # Returns type annotated boto3 ComprehendMedical client
    comprehendmedical_client = session.comprehendmedical.client()
    comprehendmedical_client: types_boto3_comprehendmedical.client.ComprehendMedicalClient
    ```
"""

from __future__ import annotations

from types_boto3_comprehendmedical.client import ComprehendMedicalClient

from boto34.boto3.service_factory import ServiceFactory


class ComprehendMedicalService(ServiceFactory[ComprehendMedicalClient]):
    SERVICE_NAME = "comprehendmedical"
    _SERVICE_PROP = "comprehendmedical"
