import is_even
import unittest


class TestIsEven(unittest.TestCase):
    def test_implodes(self):
        with self.assertRaises(TypeError):
            is_even(0.0)
        with self.assertRaises(RuntimeError):
            is_even(__build_class__(
                lambda: locals().update(__index__=lambda *_: 0.0),
                "::<>"))

    def test_one_is_even(self):
        self.assertEqual(is_even(1), False)

    def test_two_is_even(self):
        self.assertEqual(is_even(2), True)

    def test_three_is_even(self):
        self.assertEqual(is_even(3), False)

    def test_four_is_even(self):
        self.assertEqual(is_even(4), True)

    def test_five_is_even(self):
        self.assertEqual(is_even(5), False)

    def test_six_is_even(self):
        self.assertEqual(is_even(6), True)

    def test_seven_is_even(self):
        self.assertEqual(is_even(7), False)

    def test_eight_is_even(self):
        self.assertEqual(is_even(8), True)

    def test_nine_is_even(self):
        self.assertEqual(is_even(9), False)

    def test_ten_is_even(self):
        self.assertEqual(is_even(10), True)

    def test_eleven_is_even(self):
        self.assertEqual(is_even(11), False)

    def test_twelve_is_even(self):
        self.assertEqual(is_even(12), True)

    def test_thirteen_is_even(self):
        self.assertEqual(is_even(13), False)

    def test_fourteen_is_even(self):
        self.assertEqual(is_even(14), True)

    def test_fifteen_is_even(self):
        self.assertEqual(is_even(15), False)

    def test_sixteen_is_even(self):
        self.assertEqual(is_even(16), True)

    def test_seventeen_is_even(self):
        self.assertEqual(is_even(17), False)

    def test_eighteen_is_even(self):
        self.assertEqual(is_even(18), True)

    def test_nineteen_is_even(self):
        self.assertEqual(is_even(19), False)

    def test_twenty_is_even(self):
        self.assertEqual(is_even(20), True)

    def test_twenty_one_is_even(self):
        self.assertEqual(is_even(21), False)

    def test_twenty_two_is_even(self):
        self.assertEqual(is_even(22), True)

    def test_twenty_three_is_even(self):
        self.assertEqual(is_even(23), False)

    def test_twenty_four_is_even(self):
        self.assertEqual(is_even(24), True)

    def test_twenty_five_is_even(self):
        self.assertEqual(is_even(25), False)

    def test_twenty_six_is_even(self):
        self.assertEqual(is_even(26), True)

    def test_twenty_seven_is_even(self):
        self.assertEqual(is_even(27), False)

    def test_twenty_eight_is_even(self):
        self.assertEqual(is_even(28), True)

    def test_twenty_nine_is_even(self):
        self.assertEqual(is_even(29), False)

    def test_thirty_is_even(self):
        self.assertEqual(is_even(30), True)

    def test_thirty_one_is_even(self):
        self.assertEqual(is_even(31), False)

    def test_thirty_two_is_even(self):
        self.assertEqual(is_even(32), True)

    def test_thirty_three_is_even(self):
        self.assertEqual(is_even(33), False)

    def test_thirty_four_is_even(self):
        self.assertEqual(is_even(34), True)

    def test_thirty_five_is_even(self):
        self.assertEqual(is_even(35), False)

    def test_thirty_six_is_even(self):
        self.assertEqual(is_even(36), True)

    def test_thirty_seven_is_even(self):
        self.assertEqual(is_even(37), False)

    def test_thirty_eight_is_even(self):
        self.assertEqual(is_even(38), True)

    def test_thirty_nine_is_even(self):
        self.assertEqual(is_even(39), False)

    def test_forty_is_even(self):
        self.assertEqual(is_even(40), True)

    def test_forty_one_is_even(self):
        self.assertEqual(is_even(41), False)

    def test_forty_two_is_even(self):
        self.assertEqual(is_even(42), True)

    def test_forty_three_is_even(self):
        self.assertEqual(is_even(43), False)

    def test_forty_four_is_even(self):
        self.assertEqual(is_even(44), True)

    def test_forty_five_is_even(self):
        self.assertEqual(is_even(45), False)

    def test_forty_six_is_even(self):
        self.assertEqual(is_even(46), True)

    def test_forty_seven_is_even(self):
        self.assertEqual(is_even(47), False)

    def test_forty_eight_is_even(self):
        self.assertEqual(is_even(48), True)

    def test_forty_nine_is_even(self):
        self.assertEqual(is_even(49), False)

    def test_fifty_is_even(self):
        self.assertEqual(is_even(50), True)

    def test_fifty_one_is_even(self):
        self.assertEqual(is_even(51), False)

    def test_fifty_two_is_even(self):
        self.assertEqual(is_even(52), True)

    def test_fifty_three_is_even(self):
        self.assertEqual(is_even(53), False)

    def test_fifty_four_is_even(self):
        self.assertEqual(is_even(54), True)

    def test_fifty_five_is_even(self):
        self.assertEqual(is_even(55), False)

    def test_fifty_six_is_even(self):
        self.assertEqual(is_even(56), True)

    def test_fifty_seven_is_even(self):
        self.assertEqual(is_even(57), False)

    def test_fifty_eight_is_even(self):
        self.assertEqual(is_even(58), True)

    def test_fifty_nine_is_even(self):
        self.assertEqual(is_even(59), False)

    def test_sixty_is_even(self):
        self.assertEqual(is_even(60), True)

    def test_sixty_one_is_even(self):
        self.assertEqual(is_even(61), False)

    def test_sixty_two_is_even(self):
        self.assertEqual(is_even(62), True)

    def test_sixty_three_is_even(self):
        self.assertEqual(is_even(63), False)

    def test_sixty_four_is_even(self):
        self.assertEqual(is_even(64), True)

    def test_sixty_five_is_even(self):
        self.assertEqual(is_even(65), False)

    def test_sixty_six_is_even(self):
        self.assertEqual(is_even(66), True)

    def test_sixty_seven_is_even(self):
        self.assertEqual(is_even(67), False)

    def test_sixty_eight_is_even(self):
        self.assertEqual(is_even(68), True)

    def test_sixty_nine_is_even(self):
        self.assertEqual(is_even(69), False)

    def test_seventy_is_even(self):
        self.assertEqual(is_even(70), True)

    def test_seventy_one_is_even(self):
        self.assertEqual(is_even(71), False)

    def test_seventy_two_is_even(self):
        self.assertEqual(is_even(72), True)

    def test_seventy_three_is_even(self):
        self.assertEqual(is_even(73), False)

    def test_seventy_four_is_even(self):
        self.assertEqual(is_even(74), True)

    def test_seventy_five_is_even(self):
        self.assertEqual(is_even(75), False)

    def test_seventy_six_is_even(self):
        self.assertEqual(is_even(76), True)

    def test_seventy_seven_is_even(self):
        self.assertEqual(is_even(77), False)

    def test_seventy_eight_is_even(self):
        self.assertEqual(is_even(78), True)

    def test_seventy_nine_is_even(self):
        self.assertEqual(is_even(79), False)

    def test_eighty_is_even(self):
        self.assertEqual(is_even(80), True)

    def test_eighty_one_is_even(self):
        self.assertEqual(is_even(81), False)

    def test_eighty_two_is_even(self):
        self.assertEqual(is_even(82), True)

    def test_eighty_three_is_even(self):
        self.assertEqual(is_even(83), False)

    def test_eighty_four_is_even(self):
        self.assertEqual(is_even(84), True)

    def test_eighty_five_is_even(self):
        self.assertEqual(is_even(85), False)

    def test_eighty_six_is_even(self):
        self.assertEqual(is_even(86), True)

    def test_eighty_seven_is_even(self):
        self.assertEqual(is_even(87), False)

    def test_eighty_eight_is_even(self):
        self.assertEqual(is_even(88), True)

    def test_eighty_nine_is_even(self):
        self.assertEqual(is_even(89), False)

    def test_ninety_is_even(self):
        self.assertEqual(is_even(90), True)

    def test_ninety_one_is_even(self):
        self.assertEqual(is_even(91), False)

    def test_ninety_two_is_even(self):
        self.assertEqual(is_even(92), True)

    def test_ninety_three_is_even(self):
        self.assertEqual(is_even(93), False)

    def test_ninety_four_is_even(self):
        self.assertEqual(is_even(94), True)

    def test_ninety_five_is_even(self):
        self.assertEqual(is_even(95), False)

    def test_ninety_six_is_even(self):
        self.assertEqual(is_even(96), True)

    def test_ninety_seven_is_even(self):
        self.assertEqual(is_even(97), False)

    def test_ninety_eight_is_even(self):
        self.assertEqual(is_even(98), True)

    def test_ninety_nine_is_even(self):
        self.assertEqual(is_even(99), False)

    def test_one_hundred_is_even(self):
        self.assertEqual(is_even(100), True)
