from fastapi import FastAPI
from api.user_service.router import router
from fastapi.middleware.cors import CORSMiddleware
from api.db.database import users_engine, Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, or specify like ["GET", "POST"]
    allow_headers=["*"],  # Allows all headers, or specify
)

app.include_router(router=router)


# def startup_event():


# @app.lifespan
# async def lifespan(app: FastAPI):
#     # Code to run at startup
#     Base.metadata.create_all(bind=users_engine)
#     yield  # This will pause the lifespan until the app is shut down
#     # Code to run at shutdown can go here