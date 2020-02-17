from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('KK') == 120
        assert checkout_solution.checkout('TSXYZ') == 82
        assert checkout_solution.checkout('AAAAASTX') == 245