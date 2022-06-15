from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .router import post, users, auth, vote

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# private origin specific sites can reach it
# origins = ["https://www.google.com"]

# public origin any site can reach it
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello Mikey, Python is great"}
