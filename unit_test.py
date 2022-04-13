import unittest
import hello


class TestIntentFunction(unittest.TestCase):

    def test_intent(self):

        self.assertEqual(hello.find_intent("Hi, Mario's what can I get you?"), "Greeting")
        self.assertEqual(hello.find_intent("I'd like to order a pizza for pickup please."), "HowCanIHelp")
        self.assertEqual(hello.find_intent("OK, what would you like to order?"), "ReadyToReceiveOrder")
        self.assertEqual(hello.find_intent("I'd like a medium supreme pizza."), "OrderItem")
        self.assertEqual(hello.find_intent("Anything more?"), "AnyMoreItems")
        self.assertEqual(hello.find_intent("Also, a garlic bread."), "OrderItem")
        self.assertEqual(hello.find_intent("Is that all?"), "AnyMoreItems")
        self.assertEqual(hello.find_intent("Yes, that is all thanks."), "EndOfOrder")
        self.assertEqual(hello.find_intent("OK, your order is a medium supreme and a garlic bread."), "ConfirmItem")
        self.assertEqual(hello.find_intent("Should be ready in about 30 minutes."), "DurationBeforePickupAnswer")
        self.assertEqual(hello.find_intent("Thank you, goodbye."), "Goodbye")


if __name__ == '__main__':
    unittest.main()
