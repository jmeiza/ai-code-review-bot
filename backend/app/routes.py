from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from typing import List
import os, json
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter()

#Pydantic model for request body
class CodeReviewRequest(BaseModel):
    code: str

class ReviewItem(BaseModel):
    issue: str
    severity: str
    suggestions: str

class CodeReviewResponse(BaseModel):
    bugs: List[ReviewItem]
    optimizations: List[ReviewItem]
    style: List[ReviewItem]


@router.post("/review", response_model=CodeReviewResponse)
async def review_code(request: CodeReviewRequest):

    try:
        prompt = f"""
            You are an expert Python code reviewer.
            Your task is to review the following code and return ONLY a JSON object with these four keys:
            - "bugs": a list of detected bugs or potentail errors. Consider syntax errors, runtime errors, edge cases, and logical mistakes
            - "optimizations": a list of performance improvements
            - "style": a list of style/readablity improvements
            - "suggestions": a list of general best practice tips

            For each item in the lists, provide:
            - "issue": short description
            - "severity": one of ["low", "medium", "high"]
            - "suggestions":actionable recommendation

            Rules:
            1. Return ONLY valid JSON. No extra text or explanations outside the JSON.
            2. If a category has no items, return an empty list
            3. Be concise but specific.
            4. Focus on code correctness, performance, readablitiy, and best practices

            Code to review:
            {request.code}
        """
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        review_json = response.choices[0].message.content
        return json.loads(review_json)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))