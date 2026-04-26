from fastapi import APIRouter, HTTPException
from ..schemas import AIRequest
import openai

router = APIRouter()

@router.post("/analyze")
async def analyze(request: AIRequest):
    try:
        client = openai.OpenAI(api_key=request.api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.prompt}]
        )
        return {"result": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))