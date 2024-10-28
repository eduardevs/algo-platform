# on va écrire l'algo graph in a pdf
from fastapi import FastAPI
from algorithms.sort import bubble_sort
from pydantic import BaseModel
from typing import List
from service.MeasureService import MeasureService
from service.GraphService import GraphService

app = FastAPI()


class AlgorithmRequest(BaseModel):
    input_sizes: List[int]
    # algorithm: str # FIXME -> Add this in a subclass for name


@app.post("/bubble_sort")
def process_algo(request: AlgorithmRequest):
    input_sizes = request.input_sizes
    #algorithm_selection = request.algorithm

    # match algorithm_selection:
    #     case "bubble_sort":
    # solve algo
    algo_solution = bubble_sort(input_sizes)

    # graph process
    exec_time = MeasureService.measure_exec_time(bubble_sort, input_sizes)

    try:
        graph = GraphService.generate_graph_image(
            exec_time, input_sizes, "bubble sort", "bubble_sort.png"
        )

    except Exception as e:
        print(e)
        # case "linear_search":

    return {"response": exec_time, "algo_solution": algo_solution}
