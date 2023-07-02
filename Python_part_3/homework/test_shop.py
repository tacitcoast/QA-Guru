import pytest
from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def product_2():
    return Product("cookie", 50, "Юбилейное", 500)

@pytest.fixture
def cart():
    return Cart()


class TestProducts:

    def test_product_check_quantity(self, product):
        assert product.check_quantity(20) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(3452) is False

    def test_product_buy(self, product):
        product.buy(1)
        assert product.quantity == 999
        product.buy(999)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(11000)


class TestCart:

    def test_add_product(self, cart, product):
        cart.add_product(product)
        assert cart.products == {product: 1}

        cart.add_product(product, 5)
        assert cart.products == {product: 6}

    def test_remove_product_without_remove_count(self, cart, product):
        # Проверяем удаление товара которого не существует в корзине
        cart.remove_product(product)
        assert product not in cart.products

        cart.add_product(product, 10)
        assert cart.products == {product: 10}

        cart.remove_product(product)
        assert product not in cart.products

    def test_remove_product_with_remove_count_bigger(self, cart, product):
        cart.add_product(product, 10)
        assert cart.products == {product: 10}

        cart.remove_product(product, remove_count=15)
        assert product not in cart.products

    def test_remove_product_with_remove_count_smaller(self, cart, product):
        cart.add_product(product, 10)
        assert cart.products == {product: 10}

        cart.remove_product(product, remove_count=5)
        assert cart.products == {product: 5}

    def test_remove_product_with_remove_count_same(self, cart, product):
        cart.add_product(product, 10)
        assert cart.products == {product: 10}

        cart.remove_product(product, remove_count=10)
        assert product not in cart.products

    def test_clear(self, cart, product, product_2):
        cart.add_product(product, 1)
        cart.add_product(product_2, 3)

        assert len(cart.products) == 2

        cart.clear()
        assert product not in cart.products
        assert product_2 not in cart.products

    def test_get_total_price(self, cart, product, product_2):
        cart.add_product(product, 5)
        cart.add_product(product_2, 10)

        assert cart.get_total_price() == 1000

    def test_buy_success(self, cart, product, product_2):
        cart.add_product(product, 5)
        cart.add_product(product_2, 10)

        cart.buy()

        assert product.quantity == 995
        assert product_2.quantity == 490

    def test_buy_fail(self, cart, product):
        cart.add_product(product, 1005)
        with pytest.raises(ValueError):
            cart.buy()
