from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('BB') == 45
        assert checkout_solution.checkout('C') == 20
        assert checkout_solution.checkout('D') == 15
        assert checkout_solution.checkout('') == 0
        assert checkout_solution.checkout('DA') == -1