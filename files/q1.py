from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
points = None

@test_case(points=None, hidden=False)
def test_cat_1(Cat):
  my_cat = Cat("Mimi", "black", 6)
  assert my_cat.make_noise() == "meow!"
  assert my_cat.get_info() == "Mimi is 6 years old. Its colour is black."
  my_cat.age_one_year()
  assert my_cat.get_info() == "Mimi is 7 years old. Its colour is black."

@test_case(points=None, hidden=False)
def test_cat_2(Cat):
  my_cat2 = Cat("Cookie", "grey", 8, has_bell=True)
  assert my_cat2.make_noise() == "ding!"
  my_cat2.age_one_year()
  assert my_cat2.get_info() == "Cookie is 9 years old. Its colour is grey."

@test_case(points=None, hidden=False)
def test_dog_1(Dog):
  my_dog = Dog("Buddy", "brown", 4)
  my_dog.age_one_year()
  my_dog.age_one_year()
  my_dog.age_one_year()
  assert my_dog.make_noise() == "woof!"
  assert my_dog.get_info() == "Buddy is 7 years old. Its colour is brown."
  my_dog.age_one_year()
  assert my_dog.get_info() == "Buddy is 8 years old. Its colour is brown."
  assert my_dog.lead_colour == "brown"

@test_case(points=None, hidden=False)
def test_dog_2(Dog):
  my_dog2 = Dog("Linus", "black", 5, lead_colour="red")
  assert my_dog2.get_info() == "Linus is 5 years old. Its colour is black."
  assert my_dog2.lead_colour == "red"


