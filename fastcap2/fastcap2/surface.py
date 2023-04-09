
from typing import Optional
from typing import Tuple

from fastcap2_core import Surface as _Surface

class Surface(_Surface):

  """Describes a FastCap2 surface 

  :param name: The conductor name for conductor-type surfaces.
  :param title: The optional title string.

  This object can be used instead of geometry files to specify 
  conductor or dielectric surfaces. Create this object and use it with
  :py:meth:`fastcap2.problem.Problem.add` to specify 
  the geometry of the problem to solve.

  Details of the surface such as the kind of surface etc. are specified
  upon :py:meth:`fastcap2.problem.Problem.add`.

  :py:meth:`name` is a conductor identifier - surfaces with the same
  name/group combination are considered connected. The name mandatory
  for conductor-type surfaces.

  .. code-block:: python

     import fastcap2 as fc2

     # prepares a Surface object

     surface = fc2.Surface()
     surface.name = "S"
     surface.add_quad_mesh((0, 0, 0), (1, 0, 0), (0, 1, 0), edge_width = 0.01, num = 10)

     # prepares a problem using the meshed quad two times for cap plates 

     problem = fc2.Problem(title = "A sample problem")

     # lower plate: shifted down
     problem.add(surface, d = (0, 0, -0.1))
     # lower plate: shifted up
     problem.add(surface, d = (0, 0, 0.1))

     # solves the problem and returns the cap matrix in MKS units
     cap_matrix = problem.solve()
     print(cap_matrix)
  """

  def __init__(self, name: Optional[str] = None, title: Optional[str] = None):
    kwargs = {}
    if name is not None:
      kwargs["name"] = name
    if title is not None:
      kwargs["title"] = title
    super().__init__(**kwargs)

  @property
  def title(self) -> str:
    """The title string

    The title string is an arbitrary optional string. Surfaces will see
    this title or the project title (see :py:meth:`fastcap2.problem.Problem.title`)
    if no title is given for the surface.
    """
    return super()._get_title()

  @title.setter
  def title(self, value: str):
    return super()._set_title(value)

  @property
  def name(self) -> str:
    """The name string

    The name string specifies the conductor the surface belongs to.
    A conductor-type surface needs to have a name. Together with the 
    group name (see :py:meth:`fastcap2.problem.Problem.add`), the
    conductor name formes an identifier. All surfaces with the same
    conductor identifier are considered connected.

    The name must not contain '%' or ',' characters.
    """
    return super()._get_name()

  @name.setter
  def name(self, value: str):
    return super()._set_name(value)

  def add_quad(self, p1: Tuple[float, float, float], p2: Tuple[float, float, float],
                     p3: Tuple[float, float, float], p4: Tuple[float, float, float]):
    """Adds a quad to the surface"""
    if type(p1) is list:
      p1 = tuple(p1)
    if type(p2) is list:
      p2 = tuple(p2)
    if type(p3) is list:
      p3 = tuple(p3)
    if type(p4) is list:
      p4 = tuple(p4)
    return super()._add_quad(p1, p2, p3, p4)

  def add_tri(self, p1: Tuple[float, float, float], p2: Tuple[float, float, float], p3: Tuple[float, float, float]):
    """Adds a triangle to the surface"""
    if type(p1) is list:
      p1 = tuple(p1)
    if type(p2) is list:
      p2 = tuple(p2)
    if type(p3) is list:
      p3 = tuple(p3)
    return super()._add_tri(p1, p2, p3)
