from algorithms.sort import bubble_sort
from service.MeasureService import MeasureService
from service.GraphService import GraphService
import pandas as pd
import os
from weasyprint import HTML

input_sizes = [1,3,2]

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

print(CURRENT_PATH)
# exec_time = MeasureService.measure_exec_time(bubble_sort, input_sizes)
# print(exec_time)
# graph_generated = GraphService.generate_graph(exec_time, input_sizes, 'algo test', 'algo_test.png')

html_file = os.path.join(CURRENT_PATH, "templates/template.html")
css_file = os.path.join(CURRENT_PATH, "templates/template.css")


df_bar = pd.DataFrame({
    'Moth'
})