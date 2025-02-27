"""
Wrapper for aioboto3 ElasticTranscoder service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_elastictranscoder/)

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
    # Returns type annotated aioboto3 ElasticTranscoder client
    elastictranscoder_client = session.elastictranscoder.client()
    elastictranscoder_client: types_aiobotocore_elastictranscoder.client.ElasticTranscoderClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_elastictranscoder.client import ElasticTranscoderClient

from boto34.aioboto3.service_factory import ServiceFactory


class ElasticTranscoderService(ServiceFactory[ElasticTranscoderClient]):
    SERVICE_NAME = "elastictranscoder"
    _SERVICE_PROP = "elastictranscoder"
