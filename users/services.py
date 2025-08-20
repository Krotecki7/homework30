import stripe
from config.settings import STRIPE_SECRET_KEY
from lms.models import Course, Lesson

stripe.api_key = STRIPE_SECRET_KEY


def create_product(item):
    product_name = item.course if item.course else item.lesson
    product = stripe.Product.create(name=f"{product_name}")
    return product


def create_price(amount, product):
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        recurring={"interval": "month"},
        product_data={"name": product},
    )


def create_stripe_session(price):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="subscription",
    )
    return session.get("id"), session.get("url")
