"""
Wrapper for boto3 Personalize service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_personalize/)

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
    # Returns type annotated boto3 Personalize client
    personalize_client = session.personalize.client()
    personalize_client: types_boto3_personalize.client.PersonalizeClient
    ```
"""

from __future__ import annotations

from types_boto3_personalize.client import PersonalizeClient

from boto34.boto3.service_factory import ServiceFactory


class PersonalizeService(ServiceFactory[PersonalizeClient]):
    SERVICE_NAME = "personalize"
    _SERVICE_PROP = "personalize"
