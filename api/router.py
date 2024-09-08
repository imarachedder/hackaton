from fastapi import APIRouter, status


def init(app):
    router = APIRouter(tags=['Site'])

    # ROUTES
    # -------------------------------------------
    router.add_api_route(
        '/upload_file',
        methods=['GET'],
        status_code=status.HTTP_200_OK,
        endpoint=upload_file
    )
    # INCLUDE ROUTER
    # -------------------------------------------
    app.include_router(router)

