from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Body, Depends, Request
from fastapi_restful.cbv import cbv
from pydantic.schema import UUID

from src.api.request_models.request import RequestDeclineRequest, Status
from src.api.response_models.request import (
    RequestResponse,
    RequestWithUserStatusResponse,
)
from src.core.services.request_service import RequestService

router = APIRouter(prefix="/requests", tags=["Request"])


@cbv(router)
class RequestCBV:
    request_service: RequestService = Depends()

    @router.patch(
        "/{request_id}/approve",
        response_model=RequestResponse,
        status_code=HTTPStatus.OK,
        summary="Одобрить заявку на участие.",
    )
    async def approve_request_status(
        self,
        request_id: UUID,
        request: Request,
    ) -> RequestResponse:
        """Одобрить заявку на участие в акции."""
        return await self.request_service.approve_request(request_id, request.app.state.bot_instance)

    @router.patch(
        "/{request_id}/decline",
        response_model=RequestResponse,
        status_code=HTTPStatus.OK,
        summary="Отклонить заявку на участие.",
    )
    async def decline_request_status(
        self,
        request_id: UUID,
        request: Request,
        decline_request_data: RequestDeclineRequest | None = Body(None),
    ) -> RequestResponse:
        """Отклонить заявку на участие в акции."""
        return await self.request_service.decline_request(
            request_id, request.app.state.bot_instance, decline_request_data
        )

    @router.get(
        '/',
        response_model=list[RequestWithUserStatusResponse],
        status_code=HTTPStatus.OK,
        summary='Получить список заявок на участие',
    )
    async def get_requests_list(self, status: Optional[Status] = None) -> list[RequestWithUserStatusResponse]:
        return await self.request_service.get_requests_list(status)
