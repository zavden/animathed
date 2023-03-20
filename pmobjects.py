from manim import *


class PointMobject1(Scene):
  def construct(self):
    pmob = PMobject().add_points([ORIGIN])
    self.add(pmob)
    self.play(
        pmob.animate.shift(RIGHT*3)
    )
    self.wait()


class PointMobject2(Scene):
  def construct(self):
    pmob = PMobject(stroke_width=10)
    pmob.add_points([ORIGIN])
    self.add(pmob)
    self.play(
        pmob.animate.shift(RIGHT*3)
    )
    self.wait()


class PointMobject3(Scene):
  def construct(self):
    pmob = PMobject(stroke_width=10)
    pmob.add_points([LEFT, RIGHT, UP])
    self.add(pmob)
    self.play(
        pmob.animate.shift(RIGHT*3)
    )
    self.wait()


class PointMobject4(Scene):
  def construct(self):
    pmob = PMobject(stroke_width=10)
    pmob.add_points([LEFT*2, RIGHT*2, UP*2])
    d1 = Dot(pmob.get_center(), color=RED)
    d2 = Dot(pmob.get_center_of_mass(), color=BLUE)
    self.add(pmob, d1, d2)


class PointMobject5(Scene):
  def construct(self):
    pmob1 = PMobject(color=RED, stroke_width=10)\
      .add_points([DL * 2, UL * 2, UR * 2, DR * 2])
    pmob2 = PMobject(color=TEAL, stroke_width=10)\
      .add_points([LEFT * 1.5, RIGHT * 1.5, UP * 1.5])

    self.add(pmob1)
    self.play(
        Transform(pmob1, pmob2),
        run_time=4
    )
    self.wait()


class PointMobject6(Scene):
  # WARNING: This don't work
  def construct(self):  
    pmob1 = PMobject(color=RED, stroke_width=10)\
      .add_points([DL * 2, UL * 2, UR * 2, DR * 2])
    pmob2 = Square()
    self.add(pmob1)
    self.play(
        Transform(pmob1, pmob2),
        run_time=4
    )
    self.wait()


class PointMobject7(Scene):
  def construct(self):
    from pprint import pprint as print
    pmob = PMobject(stroke_width=10)
    print( pmob.points)

    pmob.add_points([LEFT])
    print(pmob.points)

    pmob.add_points([RIGHT])
    print(pmob.points)

    pmob.add_points([UP])
    print(pmob.points)

    self.add(pmob)

