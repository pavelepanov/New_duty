from fastapi import FastAPI

from defection.router import router as router_duty

app = FastAPI(
    title="New defection"
)

app.include_router(router_duty)
