import pytest

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
