"""
Wrapper for aiobotocore ElasticTranscoder service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elastictranscoder/)

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
    # Returns type annotated aiobotocore ElasticTranscoder client
    async with session.elastictranscoder.create_client() as elastictranscoder_client:
        elastictranscoder_client: types_aiobotocore_elastictranscoder.client.ElasticTranscoderClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_elastictranscoder.client import ElasticTranscoderClient
except ImportError:
    ElasticTranscoderClient = object  # type: ignore[misc,assignment]


class ElasticTranscoderService(
    ServiceFactory[ElasticTranscoderClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "elastictranscoder"
    _SERVICE_PROP = "elastictranscoder"
