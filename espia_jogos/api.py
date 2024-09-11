from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from espia_jogos.ludopedia import Ludopedia

app = FastAPI()

class CollectionRequest(BaseModel):
    id_usuario: str
    nome_jogo: str

@app.post("/request-collection/")
async def request_collection(data: CollectionRequest):
    print("Starting request to collection")
    collection = Ludopedia.request_collection(data.id_usuario, data.nome_jogo)
    print("finished request to collection")
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found or error fetching data")
    return {"collection": collection}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)