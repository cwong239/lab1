"""
    1)
        Signature:  secBig( first, second, third) -> float

        Header:     result = secBig(1, 2, 3)
                    self.assertEqual(result, 2) -> True

                    result = secBig(3, 3, 3)
                    self.assertEqual(result, 3) -> True

                    result = secBig(-1, 10, 2)
                    self.assertEqual(result, 10) -> False

                    result = secBig(0.123, 0.0123123, 0)
                    self.assertEqual(result, 0.0123123) -> True

                    result = secBig(0.123, 0.0123123, 0)
                    self.assertEqual(result, 0.0123123) -> True

        Purpose:    Find the second-largest number given 3 numbers

    2)
        Signature:  cap(str1) -> Boolean

        Header:     result = cap("none")
                    self.assertEqual(result, True) -> True

                    result = cap("Yes")
                    self.assertEqual(result, True) -> False

                    result = cap("uHn")
                    self.assertEqual(result, False) -> True

                    result = cap("okay")
                    self.assertEqual(result, False) -> False

                    result = cap("nOne")
                    self.assertEqual(result, False) -> True

        Purpose:    Return true if there are no capital letters in a string

    3)
        Signature:  north(state1, state2) -> string

        Header:     result = north("Flordia", "Colorado")
                    self.assertEqual(result, "Colorado") -> True

                    result = north("Alaska", "Texas")
                    self.assertEqual(result, "Texas") -> False

                    result = north("California", "California")
                    self.assertEqual(result, "Washington") -> False

                    result = north("Washington", "Georgia")
                    self.assertEqual(result, "Washington") -> True

                    result = north("New York", "New Mexico")
                    self.assertEqual(result, "New York") -> True

        Purpose:    Find the North Most state
"""


