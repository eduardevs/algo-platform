from pydantic import BaseModel
from utils.measure_execution_time import measure_execution_time
from typing import List


class MeasureService(BaseModel):
    input_sizes: List[int]
    algorithm: str
    
    def measure_exec_time(algorithm, input_sizes):
        execution_times = measure_execution_time(algorithm, input_sizes)
        return execution_times