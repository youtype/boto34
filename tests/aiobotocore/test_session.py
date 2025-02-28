import pytest
from botocore.exceptions import UnknownServiceError

from boto34.aiobotocore import get_session


@pytest.mark.asyncio
async def test_session_client(moto_server_url: str) -> None:
    session = get_session()
    async with session.s3.create_client(
        endpoint_url=moto_server_url,
        aws_secret_access_key="aws_secret_access_key",
        aws_access_key_id="aws_access_key_id",
    ) as s3_client:
        await s3_client.create_bucket(Bucket="test-bucket")
        await s3_client.put_object(Bucket="test-bucket", Key="test-key", Body="test-body")

        response = await s3_client.get_object(Bucket="test-bucket", Key="test-key")
        body = await response["Body"].read()
        assert body == b"test-body"


@pytest.mark.asyncio
async def test_session_proxy_methods() -> None:
    session = get_session()
    assert len(await session.s3.get_available_regions())


@pytest.mark.asyncio
async def test_session_invalid_service(moto_server_url: str) -> None:
    session = get_session()
    s3_session = session.s3
    s3_session.service_name = "invalid"
    with pytest.raises(UnknownServiceError):
        async with s3_session.create_client(
            endpoint_url=moto_server_url,
            aws_secret_access_key="aws_secret_access_key",
            aws_access_key_id="aws_access_key_id",
        ) as s3_client:
            assert s3_client
