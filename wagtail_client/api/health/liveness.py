from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.liveness_response_200 import LivenessResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/liveness".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[LivenessResponse200]:
    if response.status_code == 200:
        response_200 = LivenessResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[LivenessResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[LivenessResponse200]:
    """Liveness

     Liveness

    Returns:
        Response[LivenessResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[LivenessResponse200]:
    """Liveness

     Liveness

    Returns:
        Response[LivenessResponse200]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[LivenessResponse200]:
    """Liveness

     Liveness

    Returns:
        Response[LivenessResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[LivenessResponse200]:
    """Liveness

     Liveness

    Returns:
        Response[LivenessResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
