from langchain.chat_models import init_chat_model
from typing import Optional
from pydantic import BaseModel, Field

class equation_info(BaseModel):
	name_description: str = Field(
		description="The name and description of the equation")
	eq_proper: str = Field(
		description="The equation written in LaTex format, preceeded by the meaning of each term")
	uses: str = Field(
		description="Examples of where and when the equation is used")
	trivia: Optional[str] = Field(default=None, 
		description="Trivia or curious facts about the equation if there are any")

llm = init_chat_model("gemini-2.5-flash", 
	model_provider="google_genai", 
	api_key="AIzaSyDou-bz7lBLsYKxrqyfTscNcE9myVeg9-Q")

structured_llm = llm.with_structured_output(equation_info)