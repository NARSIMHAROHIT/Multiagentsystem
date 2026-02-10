from utils.model_loader import ModelLoader
from tools.weatherinformationtool import WeatherInformationTool
from tools.calculation import CalculationTool
from tools.currency_conversion_tools import CurrencyConversionTool
from prompts.prompt import SYSTEM_PROMPT, USER_PROMPT, ASSISTANT_PROMPT
from langgraph.graph import StateGraph,MessageState,END,START
from langgraph.prebuilt import ToolNode,tools_condition
class GraphBuilder():
    def __init__(self):
        pass

    def agent_function(self):
        pass

    def build_graph(self):
        pass
    def __call__(self):
        pass 