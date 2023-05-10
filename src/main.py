from fastapi import FastAPI

from duty.router import router as router_duty

app = FastAPI(
    title="New duty"
)

app.include_router(router_duty)
