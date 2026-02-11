import os
from dotenv import load_dotenv
from typing import Any, Optional, Literal
from pydantic import BaseModel, Field

from utils.config_loader import load_config
from langchain_groq import ChatGroq
from lagchain_openai import ChatOpenAI

load_dotenv()
class ModelLoader(BaseModel):
    def __init__(self):
        pass
    model_provider: Literal["openai", "groq"] = "groq"    
    config: Optional[ConfigLoader] = Field(default =None,exclude = True)                                                                           
    def model_post_init(self,__context:Any)-> None:
        self.config = ConfigLoader()
    class Config:
        arbitrary_types_allowed = True
    def load_llm(self):
        """
        Docstring for load_llm
        
        load and return the llm model based on the model_provider
        """
        print(f"Loading LLM model from provider: {self.model_provider}")
        if self.model_provider == "groq":
            print("Loading Groq LLM model...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(api_key=groq_api_key, model=model_name, temperature=0)
        elif self.model_provider == "openai":   
            print("Loading OpenAI LLM model...")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            llm = ChatOpenAI(api_key=openai_api_key, model=model_name, temperature=0)

        return llm