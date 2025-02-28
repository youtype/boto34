"""
Wrapper for aiobotocore ElasticTranscoder service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elastictranscoder/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_elastictranscoder.client import ElasticTranscoderClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ElasticTranscoderService(ServiceFactory[ElasticTranscoderClient]):
    """
    ElasticTranscoder service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elastictranscoder/)
    """
