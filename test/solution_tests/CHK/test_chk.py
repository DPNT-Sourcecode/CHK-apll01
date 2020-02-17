from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('KK') == 120
        assert checkout_solution.checkout('TSXYZ') == 82
        assert checkout_solution.checkout('AAAAASTX') == 245
        assert checkout_solution.checkout('') == 0
        assert checkout_solution.checkout('a') == -1
        assert checkout_solution.checkout('LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH') == 1602