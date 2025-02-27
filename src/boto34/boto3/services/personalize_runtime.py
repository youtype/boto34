"""
Wrapper for boto3 PersonalizeRuntime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_personalize_runtime/)

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
    # Returns type annotated boto3 PersonalizeRuntime client
    personalize_runtime_client = session.personalize_runtime.client()
    personalize_runtime_client: types_boto3_personalize_runtime.client.PersonalizeRuntimeClient
    ```
"""

from __future__ import annotations

from types_boto3_personalize_runtime.client import PersonalizeRuntimeClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_personalize_runtime.client import PersonalizeRuntimeClient
except ImportError:
    PersonalizeRuntimeClient = object  # type: ignore[misc,assignment]


class PersonalizeRuntimeService(
    ServiceFactory[PersonalizeRuntimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "personalize-runtime"
    _SERVICE_PROP = "personalize_runtime"
