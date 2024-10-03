from otter.test_files import test_case

OK_FORMAT = False

name = "q2"
points = None

@test_case(points=None, hidden=False)
def test_make_table(make_table):
  assert make_table(2,3) == [[0, 0, 0], [0, 0, 0]]
  assert make_table(7,5) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
  assert make_table(5,7) == [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
  assert make_table(2,0) == [[], []]
  assert make_table(0,2) == []

