

from fastapi import FastAPI
from pydentic import BaseModel
from agent.agentic_workflow import GraphBuilder


app = FastAPI()



class QueryRequest(BaseModel):
    query: str



@app.post('/query')
async def query(query: QueryRequest):
    
    try:
        
        print(query)
        
        graph = GraphBuilder()
        react_app = graph()

        png_graph = react_app.get_graph().draw_mermid_png()

        with opne('my_graph.png', 'wb') as f:
            f.write(png_graph)

        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")

        message = {'message': [query.question]}

        output = react_app.invoke(message)


        if isinstance(output, dict) and 'message' in outout:
            
            final_output = output['message'][-1].content

        else:

            final_output = str(output)

        return {'answer': final_output}

    except Exception as e:
        print(f'error is raise from query endpoint :: {e}')

