from otter.test_files import test_case

OK_FORMAT = False

name = "q3"
points = None

@test_case(points=None, hidden=False)
def test_edit_distance_1(EditDistance):
  dist = EditDistance()
  assert dist.compute_edit_distance("cat", "cat") == 0
  assert dist.compute_edit_distance("dog", "cat") == 3
  assert dist.compute_edit_distance("kitten", "mitten") == 1
  assert dist.compute_edit_distance("kissing", "mitten") == 5

@test_case(points=None, hidden=False)
def test_edit_distance_2(EditDistance):
  dist2 = EditDistance(deletion_cost = 1, insertion_cost = 1, substitution_cost = 2)
  assert dist2.compute_edit_distance("cat", "cat") == 0
  assert dist2.compute_edit_distance("dog", "cat") == 6
  assert dist2.compute_edit_distance("kitten", "mitten") == 2
  assert dist2.compute_edit_distance("kissing", "mitten") == 9

