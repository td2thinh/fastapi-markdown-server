from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from config import initiate_database

from routes.tag import router as TagRouter
from routes.note import router as NoteRouter

# ENV Variables
PORT = config("PORT")

# APP Object
app = FastAPI()

origins = [
    # "https://localhost:" + str(PORT),
    # "http://localhost:" + str(PORT),
    # "localhost:" + str(PORT),
    # "localhost:5174",
    # "http://localhost:5174",
    # "https://localhost:5174",
    # "127.0.0.1:" + str(PORT),
    # "http://127.0.0.1:" + str(PORT),
    # "https://127.0.01:" + str(PORT),
    # "127.0.0.1:5174",
    # "http://127.0.0.1:5174",
    # "https://127.0.01:5174",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await initiate_database()
    print("Server is running on port " + str(PORT))
    print("At" + " http://localhost:" + str(PORT))


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(TagRouter, tags=["Tag"], prefix="/tags")
app.include_router(NoteRouter, tags=["Note"], prefix="/notes")
