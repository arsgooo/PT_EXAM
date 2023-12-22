import unittest
import pawnshop as ps

class TestGoodsFunctions(unittest.TestCase):
    def setUp(self):
        self.goods = {
            "Radio": 200,
            "Headphones": 300,
            "Watch": 499.55555,
            "Ring": 749.47755,
        }

    def test_add_good_normal(self):
        ps.add_good(self.goods, "Laptop", 1000)
        self.assertIn("Laptop", self.goods)

    @unittest.expectedFailure
    def test_add_good_wrong(self):
        self.assertTrue(ps.add_good(self.goods, 700, "Necklace"))
        self.assertTrue(ps.add_good(self.goods, "Phone", "900"))
        self.assertTrue(ps.add_good(self.goods, 500, 400))

    def test_remove_good(self):
        ps.remove_good(
            self.goods, "Radio"
        )  # removing radio and checking that it doesn't exist anymore
        self.assertNotIn("Radio", self.goods)

        with self.assertRaises(
            ValueError
        ):  # trying to remove radio again and facing error
            ps.remove_good(self.goods, "Radio")

    def test_get_good(self):
        result = ps.get_good(self.goods, "Headphones")
        self.assertEqual(
            result, ("Headphones", 300)
        )  # checking that the correct good is returned

        with self.assertRaises(ValueError):
            result = ps.get_good(
                self.goods, "Laptop"
            )  # trying to get the good that is absent in the dictionary

    def test_get_goods_amount(self):
        amount = ps.get_goods_amount(self.goods)
        self.assertEqual(amount, 4)

    def test_get_total_cost(self):
        expected_total_cost = round(sum(self.goods.values()), 2)
        total_cost = ps.get_total_cost(self.goods)
        self.assertAlmostEqual(total_cost, expected_total_cost, places=2)


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(TestGoodsFunctions))
