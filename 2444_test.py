import unittest
def generate_star_pyramid(count):
  result = []
  for i in range(1, count * 2):
    if i < count + 1:
      blink = " " * (count - i)
      star = "*" * (2 * i - 1)
      result.append(blink + star)
    else:
      blink = " " * (i - count)
      star = "*" * (2 * count - 1 - 2 * (i - count))
      result.append(blink + star)
  return "\n".join(result)
class TestStarPyramid(unittest.TestCase):
  def test_case_1(self):
    expected = "*"
    self.assertEqual(generate_star_pyramid(1), expected)
  def test_case_2(self):
    expected = " *\n***\n *"
    self.assertEqual(generate_star_pyramid(2), expected)
  def test_case_3(self):
    expected = "  *\n ***\n*****\n ***\n  *"
    self.assertEqual(generate_star_pyramid(3), expected)
  def test_case_4(self):
    expected = "   *\n  ***\n *****\n*******\n *****\n  ***\n   *"
    self.assertEqual(generate_star_pyramid(4), expected)
  def test_case_5(self):
    expected = "    *\n   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    *"
    self.assertEqual(generate_star_pyramid(5), expected)
if __name__ == "__main__":
    unittest.main()
