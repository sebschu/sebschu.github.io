from otter.test_files import test_case

OK_FORMAT = False

name = "qA"
points = None

@test_case(points=None, hidden=False)
# Test cases

def alignment_edit_distance_test(AlignmentEditDistance):

  a_dist = AlignmentEditDistance()
  c, B = a_dist.compute_edit_distance("musing", "hissing")
  assert c == 3
  l1, l2, l3 = a_dist.compute_alignment(B)
  assert l1[-3:] == "ing"
  assert l2[-3:] == "ing"
  assert l3[-3:] == "   "

  c, B = a_dist.compute_edit_distance("cat", "dog")
  assert c == 3
  l1, l2, l3 = a_dist.compute_alignment(B)
  assert l1 == "cat"
  assert l2 == "dog"
  assert l3 == "sss"

  c, B = a_dist.compute_edit_distance("fan", "spam")
  assert c == 3
  l1, l2, l3 = a_dist.compute_alignment(B)
  assert l1[-2:] == "an"
  assert l2[-2:] == "am"
  assert l3[-2:] == " s"


