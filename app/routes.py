from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os, json
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter()

#Pydantic model for request body
class CodeInput(BaseModel):
    code: str

@router.post("/review")
async def review_code(input: CodeInput):
    """
    Calls OpenAI to review code and returns structurd JSON feedback
    """

    try:
        prompt = f"""
            You are an expert software engineer and code reviewer.
            Review the following code and return results ONLY in this json format:

            {{
                "bugs": [{{ "issue": "<description>", "severity": "critical|minor", "suggestion": "<fix suggestion>" }}],
                "optimizations": [{{ "issue": "<description>", "severity": "high|medium|low", "suggestion": "<improvement suggestion>" }}],
                "style": [{{ "issue": "<description>", "severity": "high|medium|low", "suggestion": "<style improvement>" }}]
            }}

            Rules:
            - Only return JSON. No explanations, text, or comments outside JSON.
            - Leave arrays empty if there are no issues.
            - Be concise but specific in each suggestion.
            - Do not repeat the original code.

            Code to review:
            {input.code}
        """
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        content = response.choices[0].message.content
        return json.loads(content)
    
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="AI returned invalid JSON.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))