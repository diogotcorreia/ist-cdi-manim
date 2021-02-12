from manim import *
import numpy as np


class Car(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(self,
                            y_axis_label=r"$\Delta x$ [km]",
                            x_axis_label=r"$\Delta t$ [s]",
                            y_min=0,
                            y_max=5,
                            x_min=0,
                            x_max=65,
                            y_labeled_nums=[4.7],
                            x_labeled_nums=[60],
                            x_axis_config={"tick_frequency": 5},
                            **kwargs)

    def construct(self):
        self.setup_axes(animate=True)
        self.wait()

        text = Text("4.7 km\n60 seg\n4.7 km / min", size=0.7,
                    align="right").to_corner(RIGHT + UP)

        self.play(Write(text))
        self.wait()

        constant_graph = self.get_graph(lambda x: (4.7 / 60) * x,
                                        x_min=0,
                                        x_max=60)

        self.play(ShowCreation(constant_graph))
        self.wait()

        rocky_graph = self.get_graph(lambda x: 0.0001 * ((x - 30)**3) + 2.6,
                                     x_min=0,
                                     x_max=60)

        self.play(ReplacementTransform(constant_graph, rocky_graph))
        self.wait()

        point1 = Dot(self.input_to_graph_point(10, rocky_graph))
        point2 = Dot(self.input_to_graph_point(30, rocky_graph))
        line = Line(point1, point2, color=WHITE).set_length(10)
        self.play(ShowCreation(point1), ShowCreation(point2))
        self.play(ShowCreation(line))
        self.wait()

        for x in [20, 15, 12.5, 11, 10.5]:
            new_point = Dot(self.input_to_graph_point(x, rocky_graph))
            line2 = Line(point1, new_point).set_length(10)
            self.play(ReplacementTransform(point2, new_point),
                      ReplacementTransform(line, line2))
            point2, line = new_point, line2

        self.wait()
