import plotly.express as px
import plotly.graph_objects as go
from pydantic import BaseModel
from typing import List
import os


class GraphService:
    
    def generate_graph_image(execution_time, input_sizes, algorithm_title, name_file):
        # this is temporary for bubble sort quadratic big o
        big_o_n2 = [0.00001 * (n**2) for n in input_sizes]
        
        # Plot the results using Plotly
        fig = go.Figure()
        
        
        fig.add_trace(go.Scatter(x=input_sizes, y=execution_time, mode="lines+markers", name=algorithm_title))
        fig.add_trace(go.Scatter(x=input_sizes, y=big_o_n2, mode="lines", name="O(n^2)", line=dict(dash="dash")))
        fig.update_layout(
            title="Execution Time of " + algorithm_title.title(),
            xaxis_title="Input Size (n)",
            yaxis_title="Execution Time (seconds)",
            template="plotly_dark",
        )
        
        fig.write_image('generated_graphs/'+ name_file)
        
        
        
        
        
        
        
        
        
        
        
        
        
   
 
    # # O(n2)
    # def __init__(self):
    #     # Determine the root directory (one level up from the 'service' directory)
    #     self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #     self.output_dir = os.path.join(self.root_dir, 'generated_graph')

    #     # Ensure the output directory exists
    #     if not os.path.exists(self.output_dir):
    #         os.makedirs(self.output_dir)
     

