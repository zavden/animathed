from manim import *

class VMob1(Scene):
  def construct(self):
    svg = SVGMobject("./vmob.svg")
    svg.set_stroke(width=10, color=RED, opacity=1)
    svg.set(height=config.frame_height-1)

    self.add(svg)
    self.wait()


class VMob2(Scene):
  def construct(self):
    svg = SVGMobject("./vmob.svg")
    svg.set_stroke(width=10, color=RED, opacity=1)
    svg.set(height=config.frame_height-2)

    submob = svg.submobjects[0]
    points = VGroup(*[
      Dot(coord, color=YELLOW)
      for coord in submob.get_start_anchors()
    ])

    r_submob = Rectangle(
      width=submob.width,
      height=submob.height,
      color=YELLOW
    ).move_to(submob)

    pmobs = PMobject(
      stroke_width=25,
      color=PURPLE
    ).add_points(submob.get_all_points())
    
    r_pmob = Rectangle(
      width=pmobs.width,
      height=pmobs.height,
      color=PURPLE
    ).move_to(pmobs)

    self.add(svg)
    self.wait()
    self.play(FadeIn(pmobs, r_pmob, scale=1.3))
    self.wait()
    self.play(FadeIn(points, r_submob, scale=1.3))
    self.wait()

class VMob3(Scene):
  def construct(self):
    svg = SVGMobject("./vmob.svg")
    svg.set_stroke(width=10, color=RED, opacity=1)
    svg.set(height=config.frame_height-2)

    submob = svg.submobjects[0]

    radius = 0.1
    dots = VGroup(*[
      Dot(color=YELLOW, radius=radius)
        .next_to(submob, direction, buff=-radius)
      for direction in [
        LEFT , DL, DOWN, DR,
        RIGHT, UR, UP  , UL
      ]
    ])

    pmobs = PMobject(
      stroke_width=25,
      color=PURPLE
    ).add_points(submob.get_start_anchors())
    
    r_pmob = Rectangle(
      width=pmobs.width,
      height=pmobs.height,
      color=PURPLE
    ).move_to(pmobs)

    self.add(submob, pmobs, r_pmob, dots)
    self.wait()


class VMob4(Scene):
  def construct(self):
    r = Rectangle(
      width=10,
      height=6,
      fill_color=PURE_GREEN,
      fill_opacity=0.5,
      stroke_color=PURPLE,
      stroke_opacity=1,
      stroke_width=20,
      background_stroke_color=RED,
      background_stroke_opacity=1,
      background_stroke_width=40,
    )

    self.add(r)
    self.wait()
