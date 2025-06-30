 

from utils.model_loader import 
from prompt_lib.prompt import 

from langgraph.graph import StartGraph, MessageState, START, END
from langgraph.prebuilt import ToolNode, tool_condition






class GraphBuilder():

    def __init__(self):
        
        self.tools= []

        self.system_prompt = SYSTEM_PROMPT


    def agent_function(self, state: MessageState):
        """
        main agent function
        """
        user_question = state['message']
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {'message': response}



    def build_graph(self):
        """
        In this method we desinged the architecture of graph.

        """

        graph_builder = StartGraph(MessageState)
        graph_builder.add_node('agent', self.agent_function)
        graph_builder.add_node('tools', ToolNode(tools = self.tools))
        graph_builder.add_edge(START, 'agent')
        graph_builder.add_conditional_edge('agent', tools_condition)
        graph_builder.add_edge('tools', 'agent')
        graph_builder.add_edge('agent', END)
        self.graph = graph_builder.complie()
        return self.graph

    def __call__(self):
        return self.build_graph()
