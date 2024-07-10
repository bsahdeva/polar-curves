import manim as bb
import numpy as np

from polar_utils import plot_polar_curve, sin_lima_looped_pos


class PolarDerivatives(bb.Scene):

    def construct(self):

        self.add(bb.NumberPlane())

        intro1 = bb.Tex(
            "The next topic we'll explore in polar curves is the method for deriving them.",
            font_size=40,
        ).shift(bb.UP * 3)
        intro_rect1 = bb.SurroundingRectangle(intro1, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro2 = bb.Tex(
            r"We can find the rate of change of the magnitude $r$ with respect to the angle $\theta$ like you would with a rectangular function.",
            font_size=36,
        ).move_to(intro1)
        intro_rect2 = bb.SurroundingRectangle(intro2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro3 = bb.Tex(
            r"For example, $r'(theta)$ for the below function would be $\frac{3}{2} \cdot \cos(\theta)$.",
            font_size=38,
        ).move_to(intro1)
        intro_rect3 = bb.SurroundingRectangle(intro3, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        curve = plot_polar_curve(sin_lima_looped_pos)

        side_txt1 = bb.MathTex(
            r"r = \frac{1}{2} + \frac{3}{2} \cdot \sin(\theta)", font_size=30
        )
        side_txt2 = bb.MathTex(
            r"\frac{d}{d\theta}[r] = \frac{d}{d\theta}[\frac{1}{2} + \frac{3}{2} \cdot \sin(\theta)]",
            font_size=30,
        )
        side_txt3 = bb.MathTex(
            r"\frac{dr}{d\theta} = \frac{3}{2} \cdot \cos(\theta)", font_size=30
        )
        side1 = (
            bb.VGroup(side_txt1, side_txt2, side_txt3)
            .arrange(bb.DOWN, buff=0.1)
            .next_to(curve, direction=bb.DOWN)
        )
        side_rect1 = bb.SurroundingRectangle(side1, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.add(intro_rect1)
        self.play(bb.Write(intro1))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, intro_rect2), bb.FadeOut(intro1))
        self.play(bb.Write(intro2))
        self.wait(1)
        self.play(bb.Create(curve))
        self.play(bb.Transform(intro_rect1, intro_rect3), bb.FadeOut(intro2))
        self.play(bb.Write(intro3))
        self.wait(1)

        self.play(
            bb.Create(side_rect1),
            bb.Write(side_txt1),
            bb.Write(side_txt2),
            bb.Write(side_txt3),
        )
        self.wait(3)
        self.play(
            bb.Uncreate(side_rect1),
            bb.FadeOut(side_txt1),
            bb.FadeOut(side_txt2),
            bb.FadeOut(side_txt3),
        )

        slope1 = bb.Tex(
            "However, in order to find the instantaneous rate of change of the curve itself, there are a few more steps.",
            font_size=40,
        ).move_to(intro1)
        slope_rect1 = bb.SurroundingRectangle(slope1, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        slope2 = bb.Tex(
            r"The instantaneous rate of change is described as $\frac{dy}{dx}$, or the rate of change of $y$ with respect to $x$.",
            font_size=38,
        ).move_to(intro1)
        slope_rect2 = bb.SurroundingRectangle(slope2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        slope3 = bb.Tex(
            r"Since polar curves can be described as parametric functions where $x = r \cdot \cos(\theta)$ and $y = r \cdot \sin(\theta)$, we can take the derivative of $x$ and $y$ with respect to $\theta$ and then use that to determine $\frac{dy}{dx}$.",
            font_size=32,
        ).move_to(intro1)
        slope_rect3 = bb.SurroundingRectangle(slope3, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        slope3 = bb.Tex(
            r"First, let's find $\frac{dy}{d\theta}$.",
            font_size=32,
        ).move_to(intro1)
        slope_rect3 = bb.SurroundingRectangle(slope3, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        slope4 = bb.Tex(
            r"Next, let's find $\frac{dx}{d\theta}$.",
            font_size=32,
        ).move_to(intro1)
        slope_rect4 = bb.SurroundingRectangle(slope4, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        slope5 = bb.Tex(
            r"Now that we have $\frac{dy}{d\theta}$ and $\frac{dx}{d\theta}$, we can find $\frac{dy}{dx}$.",
            font_size=32,
        ).move_to(intro1)
        slope_rect5 = bb.SurroundingRectangle(slope5, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        side_txt4 = bb.MathTex(r"y = r \cdot \sin(\theta)", font_size=30)
        side_txt5 = bb.MathTex(
            r"y = (\frac{1}{2} + \frac{3}{2} \cdot \sin(\theta)) \cdot \sin(\theta)",
            font_size=30,
        )
        side_txt6 = bb.MathTex(
            r"\frac{d}{d\theta}[y] = \frac{d}{d\theta}[(\frac{1}{2} + \frac{3}{2} \cdot \sin(\theta)) \cdot \sin(\theta)]",
            font_size=30,
        )
        side_txt7 = bb.MathTex(
            r"\frac{dy}{d\theta} = (\frac{3}{2} \cdot \cos{\theta}) \cdot \sin(\theta) + (\frac{1}{2} + \frac{3}{2} \cdot \sin(\theta)) \cdot \cos(\theta)",
            font_size=30,
        )
        side2 = (
            bb.VGroup(side_txt4, side_txt5, side_txt6, side_txt7)
            .arrange(bb.DOWN, buff=0.1)
            .next_to(curve, direction=bb.DOWN)
        )
        side_rect2 = bb.SurroundingRectangle(side2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.play(bb.Transform(intro_rect1, slope_rect1), bb.FadeOut(intro3))
        self.play(bb.Write(slope1))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, slope_rect2), bb.FadeOut(slope1))
        self.play(bb.Write(slope2))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, slope_rect3), bb.FadeOut(slope2))
        self.play(bb.Write(slope3))
        self.wait(1)

        self.play(
            bb.Create(side_rect2),
            bb.Write(side_txt4),
            bb.Write(side_txt5),
            bb.Write(side_txt6),
            bb.Write(side_txt7),
        )
        self.wait(3)
        self.play(
            bb.Uncreate(side_rect2),
            bb.FadeOut(side_txt4),
            bb.FadeOut(side_txt5),
            bb.FadeOut(side_txt6),
            bb.FadeOut(side_txt7),
        )

        self.play(bb.Transform(intro_rect1, slope_rect4), bb.FadeOut(slope3))
        self.play(bb.Write(slope4))
        self.wait(2)

        side_txt8 = bb.MathTex(r"x = r \cdot \cos(\theta)", font_size=30)
        side_txt9 = bb.MathTex(
            r"x = (\frac{1}{2} + \frac{3}{2} \cdot \sin(\theta)) \cdot \cos(\theta)",
            font_size=30,
        )
        side_txt10 = bb.MathTex(
            r"\frac{d}{d\theta}[x] = \frac{d}{d\theta}[(\frac{1}{2} + \frac{3}{2} \cdot \sin(\theta)) \cdot \cos(\theta)]",
            font_size=30,
        )
        side_txt11 = bb.MathTex(
            r"\frac{dx}{d\theta} = (\frac{3}{2} \cdot \cos{\theta}) \cdot \cos(\theta) - (\frac{1}{2} + \frac{3}{2} \cdot \sin(\theta)) \cdot \sin(\theta)",
            font_size=30,
        )
        side3 = (
            bb.VGroup(side_txt8, side_txt9, side_txt10, side_txt11)
            .arrange(bb.DOWN, buff=0.1)
            .next_to(curve, direction=bb.DOWN)
        )
        side_rect3 = bb.SurroundingRectangle(side3, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.play(
            bb.Create(side_rect3),
            bb.Write(side_txt8),
            bb.Write(side_txt9),
            bb.Write(side_txt10),
            bb.Write(side_txt11),
        )
        self.wait(3)
        self.play(
            bb.Uncreate(side_rect3),
            bb.FadeOut(side_txt8),
            bb.FadeOut(side_txt9),
            bb.FadeOut(side_txt10),
            bb.FadeOut(side_txt11),
        )

        self.play(bb.Transform(intro_rect1, slope_rect5), bb.FadeOut(slope4))
        self.play(bb.Write(slope5))
        self.wait(2)

        side_txt12 = bb.MathTex(
            r"\frac{dy}{dx} = \frac{\frac{dy}{d\theta}}{\frac{dx}{d\theta}}",
            font_size=30,
        )
        side_txt13 = bb.MathTex(
            r"\frac{dy}{dx} = \frac{(\frac{3}{2} \cdot \cos{\theta}) \cdot \sin(\theta) + (\frac{1}{2} + \frac{3}{2} \cdot \sin(\theta)) \cdot \cos(\theta)}{(\frac{3}{2} \cdot \cos{\theta}) \cdot \cos(\theta) - (\frac{1}{2} + \frac{3}{2} \cdot \sin(\theta)) \cdot \sin(\theta)}",
            font_size=30,
        )
        side4 = (
            bb.VGroup(side_txt12, side_txt13)
            .arrange(bb.DOWN, buff=0.1)
            .next_to(curve, direction=bb.DOWN)
        )
        side_rect4 = bb.SurroundingRectangle(side4, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.play(
            bb.Create(side_rect4),
            bb.Write(side_txt12),
            bb.Write(side_txt13),
        )
        self.wait(3)
