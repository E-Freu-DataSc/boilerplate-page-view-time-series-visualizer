import unittest
import matplotlib as mpl
import time_series_visualizer  # Importa tu módulo principal con las funciones

class DataCleaningTestCase(unittest.TestCase):
    def test_data_cleaning(self):
        actual = int(time_series_visualizer.df.count(numeric_only=True))
        expected = 1238
        self.assertEqual(actual, expected, "Expected DataFrame count after cleaning to be 1238.")

class LinePlotTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Acceder directamente al objeto 'Axes'
        cls.ax = time_series_visualizer.draw_line_plot(time_series_visualizer.df)

    def test_line_plot_title(self):
        actual = self.ax.get_title()
        expected = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
        self.assertEqual(actual, expected, "Expected line plot title to be 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019'")

    def test_line_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Date", "Expected line plot xlabel to be 'Date'")
        self.assertEqual(self.ax.get_ylabel(), "Page Views", "Expected line plot ylabel to be 'Page Views'")

class BarPlotTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Acceder directamente al objeto 'Axes'
        cls.ax = time_series_visualizer.draw_bar_plot(time_series_visualizer.df)

    def test_bar_plot_legend_labels(self):
        actual = [label.get_text() for label in self.ax.get_legend().get_texts()]
        expected = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.assertEqual(actual, expected, "Expected bar plot legend labels to be months of the year.")

class BoxPlotTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Obtener los dos ejes de la figura devuelta por draw_box_plot
        cls.fig = time_series_visualizer.draw_box_plot(time_series_visualizer.df)
        cls.ax1, cls.ax2 = cls.fig.axes  # Asignación múltiple de ejes

    def test_box_plot_labels(self):
        self.assertEqual(self.ax1.get_xlabel(), "Year", "Expected box plot 1 xlabel to be 'Year'")
        self.assertEqual(self.ax2.get_xlabel(), "Month", "Expected box plot 2 xlabel to be 'Month'")

    def test_box_plot_titles(self):
        self.assertEqual(self.ax1.get_title(), "Year-wise Box Plot (Trend)", "Expected box plot 1 title to be 'Year-wise Box Plot (Trend)'")
        self.assertEqual(self.ax2.get_title(), "Month-wise Box Plot (Seasonality)", "Expected box plot 2 title to be 'Month-wise Box Plot (Seasonality)'")

if __name__ == "__main__":
    unittest.main()
