from manim import *
import array as arr
    
f = open("StockPrices.txt","r")
stocks_array = arr.array('f',[10.0])
i = 0
for stock in f:
    stocks_array.append(float(stock))
    i+=1

    
class StockPriceCurve(Scene):
    def construct(self):  
        ax = Axes(
                x_range=[0, 20, 0.5],
                y_range=[0, 20, 1],
                tips=False,
                axis_config={"include_numbers": True},
            )
        labels = ax.get_axis_labels(
            Tex("Time").scale(0.7), Text("Stock Prices").scale(0.45)
        )
        self.add(ax,labels)
        a = Dot(LEFT * 6)
        b = TracedPath(a.get_center, dissipating_time=5, stroke_opacity=[0, 1])
        self.add(a, b)

        for j in range(1,i):
            variance = stocks_array [j] - stocks_array [j-1]
            self.play(a.animate.shift(RIGHT*0.1+UP*variance*0.1))