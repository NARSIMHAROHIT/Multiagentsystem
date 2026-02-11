from utils.model_loader import ModelLoader
from tools.weatherinformationtool import WeatherInformationTool
from tools.calculation import CalculationTool
from tools.currency_conversion_tools import CurrencyConversionTool
from prompts.prompt import SYSTEM_PROMPT, USER_PROMPT, ASSISTANT_PROMPT
from langgraph.graph import StateGraph,MessageState,END,START
from langgraph.prebuilt import ToolNode,tools_condition
class GraphBuilder():
    def __init__(self):
        self.tools = [

        ]
        self.system_prompt = SYSTEM_PROMPT

    def agent_function(self,state:MessageState):
        """This is the main agent function"""
        user_question  = state["messages"]
        input_question = [self.system_prompt]+user_question
        response =  self.llm_with_tools.invoke(input_question)
        return {"message":response}

    def build_graph(self):
        graph_builder = StateGraph(MessageState)

        graph_builder.add_node("agent",self.agent_function)
        graph_builder.add_node("tools",ToolNode(tools=self.tools))
        graph_builder.add_edge(START,"agent")           
        graph_builder.add_conditional_edges("agents",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)
        self.graph = graph_builder.compile()
        return self.graph
    def __call__(self):
        self.build_graph