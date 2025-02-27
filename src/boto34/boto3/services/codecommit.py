"""
Wrapper for boto3 CodeCommit service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codecommit/)

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
    # Returns type annotated boto3 CodeCommit client
    codecommit_client = session.codecommit.client()
    codecommit_client: types_boto3_codecommit.client.CodeCommitClient
    ```
"""

from __future__ import annotations

from types_boto3_codecommit.client import CodeCommitClient

from boto34.boto3.service_factory import ServiceFactory


class CodeCommitService(ServiceFactory[CodeCommitClient]):
    SERVICE_NAME = "codecommit"
    _SERVICE_PROP = "codecommit"
