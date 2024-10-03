from otter.test_files import test_case

OK_FORMAT = False

name = "q4"
points = None

@test_case(points=None, hidden=False)
def test_weighted_edit_distance(WeightedEditDistance, sub_cost_matrix):
  dist_w = WeightedEditDistance(sub_costs = sub_cost_matrix)
  assert dist_w.compute_edit_distance("bar", "bsr") == 0.25
  assert dist_w.compute_edit_distance("bar", "bfr") == 0.75
  assert (dist_w.compute_edit_distance("bwr", "bar") - 0.353453) < 0.01
  assert dist_w.compute_edit_distance("bpr", "bar") == 2
  assert dist_w.compute_edit_distance("power", "pow") == 2
  assert dist_w.compute_edit_distance("deary", "deary") == 0

