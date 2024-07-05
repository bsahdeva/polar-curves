import manim as bb
import numpy as np

from polar_utils import polar_ray


class PolarIntro(bb.Scene):

    def construct(self):

        plane1 = bb.NumberPlane()
        self.add(plane1)

        intro1 = bb.Tex(
            "You are likely familiar with the traditional form of mapping coordinates.",
            font_size=38,
        ).shift(bb.UP * 3)
        intro_rect1 = bb.SurroundingRectangle(intro1, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro2 = bb.Tex(
            r"In the rectangular plane, points are defined by $(x, y)$."
        ).move_to(intro1)
        intro_rect2 = bb.SurroundingRectangle(intro2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro3 = bb.Tex(
            'However, there is a different way to define coordinates, using a system called "polar coordinates."',
            font_size=38,
        ).move_to(intro1)
        intro_rect3 = bb.SurroundingRectangle(intro3, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro4 = bb.Tex(r"Polar coordinates are defined by $(r, \theta)$.").move_to(
            intro1
        )
        intro_rect4 = bb.SurroundingRectangle(intro4, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro5 = bb.Tex(
            r"$r$ is the magnitude of the vector that points at the coordinate, and $\theta$ is the angle of the vector.",
            font_size=38,
        ).move_to(intro1)
        intro_rect5 = bb.SurroundingRectangle(intro5, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.add(intro_rect1)
        self.play(bb.Write(intro1))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, intro_rect2), bb.FadeOut(intro1))
        self.play(bb.Write(intro2))

        point_r = bb.Circle(radius=0.06, color=bb.WHITE).move_to([3, 1, 0])
        point_r.set_fill(bb.WHITE, 1)
        point_r.scale(0.01)
        self.add(point_r)
        point_r_txt = bb.MathTex("(3, 1)").next_to(
            point_r, direction=bb.DOWN * 0.3 + bb.RIGHT * 0.3
        )
        self.play(bb.ScaleInPlace(point_r, 100), bb.Write(point_r_txt))
        self.wait(2)

        self.play(bb.Transform(intro_rect1, intro_rect3), bb.FadeOut(intro2))
        self.play(bb.Write(intro3))
        self.wait(1.5)
        self.play(
            bb.Transform(intro_rect1, intro_rect4),
            bb.FadeOut(intro3),
            bb.FadeOut(bb.VGroup(point_r, point_r_txt)),
        )
        self.play(bb.Write(intro4))
        self.wait(2)
        self.play(
            bb.Transform(intro_rect1, intro_rect5),
            bb.FadeOut(intro4),
        )
        self.play(bb.Write(intro5))
        self.wait(0.2)
        ray1 = polar_ray(
            magnitude=2,
            theta=bb.PI / 4,
        )
        r_txt = bb.MathTex("r").next_to(ray1).shift(bb.LEFT * 1.3 + bb.UP * 0.14)
        theta_txt = (
            bb.MathTex(r"\theta", font_size=38)
            .next_to(ray1)
            .shift(bb.DOWN * 0.4 + bb.LEFT * 0.97)
        )
        self.play(bb.Create(ray1))
        self.wait(0.2)
        self.play(bb.Write(r_txt), bb.Write(theta_txt))

        point_p = bb.Circle(radius=0.06, color=bb.WHITE).move_to(
            [2 * np.cos(bb.PI / 4), 2 * np.sin(bb.PI / 4), 0]
        )
        point_p.set_fill(bb.WHITE, 1)
        point_p.scale(0.01)
        self.add(point_p)
        point_p_txt = bb.MathTex(r"(r, \theta) = (2, \frac{\pi}{4})").next_to(
            point_p, direction=bb.DOWN * 0.3 + bb.RIGHT * 0.3
        )
        self.play(bb.ScaleInPlace(point_p, 100), bb.Write(point_p_txt))
        self.wait(3)

        convert1 = bb.Tex(
            "Polar and rectangular coordinates can be converted into each other.",
            font_size=40,
        ).move_to(intro1)
        convert_rect1 = bb.SurroundingRectangle(convert1, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        convert2 = bb.Tex(
            r"In order to convert polar coordinates to rectangular, we can set $x = r \cdot \cos(\theta)$ and $y = r \cdot \sin(\theta)$.",
            font_size=38,
        ).move_to(intro1)
        convert_rect2 = bb.SurroundingRectangle(convert2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        convert3 = bb.Tex(
            "We can use our sine and cosine right triangle identities to derive this.",
            font_size=40,
        ).move_to(intro1)
        convert_rect3 = bb.SurroundingRectangle(convert3, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        side_txt1 = bb.MathTex(r"\cos(\theta) = \frac{x}{r}", font_size=35)
        side_txt2 = bb.MathTex(r"r \cdot \cos(\theta) = x", font_size=35)
        side_txt3 = bb.MathTex(r"\sin(\theta) = \frac{y}{r}", font_size=35)
        side_txt4 = bb.MathTex(r"r \cdot \sin(\theta) = y", font_size=35)
        side1 = (
            bb.VGroup(side_txt1, side_txt2, side_txt3, side_txt4)
            .arrange(bb.DOWN, buff=0.1)
            .shift(bb.RIGHT * 3 + bb.UP * 0.5)
        )
        side_rect1 = bb.SurroundingRectangle(side1, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.play(
            bb.Transform(intro_rect1, convert_rect1),
            bb.FadeOut(intro5),
        )
        self.play(bb.Write(convert1))
        self.wait(2)
        self.play(
            bb.Transform(intro_rect1, convert_rect2),
            bb.FadeOut(convert1),
        )
        self.play(bb.Write(convert2))
        self.wait(2)
        self.play(
            bb.Transform(intro_rect1, convert_rect3),
            bb.FadeOut(convert2),
        )
        self.play(bb.Write(convert3))
        self.wait(0.5)
        self.play(bb.Uncreate(point_p), bb.Uncreate(point_p_txt))
        leg1 = bb.Line([0, 0, 0], [2 * np.cos(bb.PI / 4), 0, 0], color=bb.YELLOW)
        height1 = bb.Line(
            [2 * np.cos(bb.PI / 4), 0, 0],
            [2 * np.cos(bb.PI / 4), 2 * np.sin(bb.PI / 4), 0],
            color=bb.YELLOW,
        )
        self.play(bb.Create(leg1), bb.Create(height1))
        self.wait(1)
        self.play(
            bb.Create(side_rect1),
            bb.Write(side_txt1),
            bb.Write(side_txt2),
            bb.Write(side_txt3),
            bb.Write(side_txt4),
        )
        self.wait(2)
        self.play(
            bb.Uncreate(side_rect1),
            bb.FadeOut(side_txt1),
            bb.FadeOut(side_txt2),
            bb.FadeOut(side_txt3),
            bb.FadeOut(side_txt4),
        )
        self.wait(2)

        convert4 = bb.Tex(
            r"In order to convert rectangular coordinates to polar, we can set $r = \sqrt{x^2 + y^2}$ and $\theta = \arctan(\frac{y}{x})$.",
            font_size=38,
        ).move_to(intro1)
        convert_rect4 = bb.SurroundingRectangle(convert4, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        convert5 = bb.Tex(
            "We can use the Pythagorean Theorem and the tangent right triangle identity to derive these.",
            font_size=39,
        ).move_to(intro1)
        convert_rect5 = bb.SurroundingRectangle(convert5, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        side_txt5 = bb.MathTex(r"\tan(\theta) = \frac{y}{x}", font_size=35)
        side_txt6 = bb.MathTex(r"\theta = \arctan(\frac{y}{x})", font_size=35)
        side_txt7 = bb.MathTex(r"r^2 = x^2 + y^2", font_size=35)
        side_txt8 = bb.MathTex(r"r = \sqrt(x^2 + y^2)", font_size=35)

        side2 = (
            bb.VGroup(side_txt5, side_txt6, side_txt7, side_txt8)
            .arrange(bb.DOWN, buff=0.1)
            .shift(bb.RIGHT * 3 + bb.UP * 0.5)
        )
        side_rect2 = bb.SurroundingRectangle(side2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.play(
            bb.Transform(intro_rect1, convert_rect4),
            bb.FadeOut(convert3),
            bb.Write(convert4),
        )
        self.wait(2)
        self.play(
            bb.Transform(intro_rect1, convert_rect5),
            bb.FadeOut(convert4),
        )
        self.play(bb.Write(convert5))
        self.wait(2)

        self.play(bb.Create(side_rect2))
        self.play(
            bb.Write(side_txt5),
            bb.Write(side_txt6),
            bb.Write(side_txt7),
            bb.Write(side_txt8),
        )
        self.wait(2)
