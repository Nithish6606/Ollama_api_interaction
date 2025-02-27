from fastapi import FastAPI,Depends,HTTPException,Header
import os
import ollama
from dotenv import load_dotenv
load_dotenv()
API_KEY_CREDITS = {os.getenv("API_KEY"):5}
DEFAULT_CREDITS = 5
app = FastAPI()

def verify_api_key(api_key: str = Header(None)):
    if api_key not in API_KEY_CREDITS:
        raise HTTPException(status_code=401, detail="Invalid API key")
    credits = API_KEY_CREDITS.get(api_key)
    if credits <= 0:
        raise HTTPException(status_code=403, detail="No API credits available")

    return api_key

@app.get("/")
def welcome():
    return {"Message":"Welcome to API INTERACTION."}

@app.post("/generate")
def generate(prompt:str,api_key:str = Depends(verify_api_key)):
    API_KEY_CREDITS[api_key] -= 1
    response = ollama.chat(model="gemma:2b",messages=[{"role":"user","content":prompt}])
    return {"response":response["message"]["content"]}
