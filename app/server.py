from fastapi import FastAPI
from langserve import add_routes

from pirate_speak.chain import chain as pirate_speak_chain

app = FastAPI()

# Edit this to add the chain you want to add
add_routes(app, pirate_speak_chain, path="/pirate-speak")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
