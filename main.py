import uvicorn
from decouple import config

# ENV Variables
PORT = config("PORT")

if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=int(PORT), reload=True)
   
