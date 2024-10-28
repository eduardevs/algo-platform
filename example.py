import time
import random
import plotly.graph_objects as go
from bubble_sort import bubble_sort
from jinja2 import Template
import os


def measure_execution_time(func, sizes):
    times = []
    for size in sizes:
        # Create a random array of the given size
        arr = random.sample(range(size), size)

        # Measure the time taken by the function
        start_time = time.time()
        func(arr)
        end_time = time.time()

        # Calculate the time difference
        times.append(end_time - start_time)

    return times


input_sizes = [10, 100, 500, 1000, 2000, 3000, 4000]
execution_times = measure_execution_time(bubble_sort, input_sizes)

# Theoretical BIg O comparison(O(n^2))
big_o_n2 = [0.00001 * (n**2) for n in input_sizes]

# Plot the results using Plotly
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=input_sizes, y=execution_times, mode="lines+markers", name="Bubble Sort Time"
    )
)
fig.add_trace(
    go.Scatter(
        x=input_sizes, y=big_o_n2, mode="lines", name="O(n^2)", line=dict(dash="dash")
    )
)
fig.update_layout(
    title="Execution Time of Bubble Sort",
    xaxis_title="Input Size (n)",
    yaxis_title="Execution Time (seconds)",
    template="plotly_dark",
)


output_html_path = os.path.join(os.getcwd(), "gui", "output.html")
input_template_path = os.path.join(os.getcwd(), "gui", "index.html")

poltly_jinja_data = {"fig": fig.to_html(full_html=False)}

with open(output_html_path, "w", encoding="utf-8") as output_file:
    with open(input_template_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(poltly_jinja_data))
# fig.show()
