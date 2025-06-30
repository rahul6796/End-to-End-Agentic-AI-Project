


import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq


class ConfigLoader:

    def __init__(self):
        pritn('load config......')
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]



class ModelLoader(BaseModel):

    # validation checker.
    model_provider: Literal['openai', 'groq'] = 'groq'
    config: Optional[ConfigLoader] = Field(default = None, exclue= True)

    def model_post_init(self, __context: Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_model(self):
        """
        load and return the llm model.
        """

        print('loading the llm model')

        if self.model_provider = 'groq':
            groq_api_key = os.getenv('GROQ_API_KEY')
            model_name = self.config['llm']['groq']['model_name']
            llm=ChatGroq(model=model_name, api_key=groq_api_key)

        elif self.model_provider = 'openai':
            pass
        
        else:
            pass

        return llm

        


    









