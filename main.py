# This entrypoint file to be used in development. Start by reading README.md
import time_series_visualizer
from unittest import main
from time_series_visualizer import df

# Test your function by calling it here
time_series_visualizer.draw_line_plot(df)
time_series_visualizer.draw_bar_plot(df)
time_series_visualizer.draw_box_plot(df)


# Run unit tests automatically
main(module='test_module', exit=False)