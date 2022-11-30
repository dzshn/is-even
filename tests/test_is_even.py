import is_even
import unittest


TurboFish = __build_class__(
    lambda: locals().update(__index__=lambda _: 0.0),
    "::<>")

if not hasattr(TurboFish, "__index__"):  # pragma: no cover
    # polyfill for <3.10
    class TurboFish:
        def __index__(self):
            return 0.0


class TestIsEven(unittest.TestCase):
    def test_implodes(self):
        with self.assertRaises(TypeError):
            is_even(0.0)
        with self.assertRaises(RuntimeError):
            is_even(TurboFish())

    def test_one_is_even(self):
        self.assertTrue(not is_even(1))

    def test_two_is_even(self):
        self.assertTrue(is_even(2))

    def test_three_is_even(self):
        self.assertTrue(not is_even(3))

    def test_four_is_even(self):
        self.assertTrue(is_even(4))

    def test_five_is_even(self):
        self.assertTrue(not is_even(5))

    def test_six_is_even(self):
        self.assertTrue(is_even(6))

    def test_seven_is_even(self):
        self.assertTrue(not is_even(7))

    def test_eight_is_even(self):
        self.assertTrue(is_even(8))

    def test_nine_is_even(self):
        self.assertTrue(not is_even(9))

    def test_ten_is_even(self):
        self.assertTrue(is_even(10))

    def test_eleven_is_even(self):
        self.assertTrue(not is_even(11))

    def test_twelve_is_even(self):
        self.assertTrue(is_even(12))

    def test_thirteen_is_even(self):
        self.assertTrue(not is_even(13))

    def test_fourteen_is_even(self):
        self.assertTrue(is_even(14))

    def test_fifteen_is_even(self):
        self.assertTrue(not is_even(15))

    def test_sixteen_is_even(self):
        self.assertTrue(is_even(16))

    def test_seventeen_is_even(self):
        self.assertTrue(not is_even(17))

    def test_eighteen_is_even(self):
        self.assertTrue(is_even(18))

    def test_nineteen_is_even(self):
        self.assertTrue(not is_even(19))

    def test_twenty_is_even(self):
        self.assertTrue(is_even(20))

    def test_twenty_one_is_even(self):
        self.assertTrue(not is_even(21))

    def test_twenty_two_is_even(self):
        self.assertTrue(is_even(22))

    def test_twenty_three_is_even(self):
        self.assertTrue(not is_even(23))

    def test_twenty_four_is_even(self):
        self.assertTrue(is_even(24))

    def test_twenty_five_is_even(self):
        self.assertTrue(not is_even(25))

    def test_twenty_six_is_even(self):
        self.assertTrue(is_even(26))

    def test_twenty_seven_is_even(self):
        self.assertTrue(not is_even(27))

    def test_twenty_eight_is_even(self):
        self.assertTrue(is_even(28))

    def test_twenty_nine_is_even(self):
        self.assertTrue(not is_even(29))

    def test_thirty_is_even(self):
        self.assertTrue(is_even(30))

    def test_thirty_one_is_even(self):
        self.assertTrue(not is_even(31))

    def test_thirty_two_is_even(self):
        self.assertTrue(is_even(32))

    def test_thirty_three_is_even(self):
        self.assertTrue(not is_even(33))

    def test_thirty_four_is_even(self):
        self.assertTrue(is_even(34))

    def test_thirty_five_is_even(self):
        self.assertTrue(not is_even(35))

    def test_thirty_six_is_even(self):
        self.assertTrue(is_even(36))

    def test_thirty_seven_is_even(self):
        self.assertTrue(not is_even(37))

    def test_thirty_eight_is_even(self):
        self.assertTrue(is_even(38))

    def test_thirty_nine_is_even(self):
        self.assertTrue(not is_even(39))

    def test_forty_is_even(self):
        self.assertTrue(is_even(40))

    def test_forty_one_is_even(self):
        self.assertTrue(not is_even(41))

    def test_forty_two_is_even(self):
        self.assertTrue(is_even(42))

    def test_forty_three_is_even(self):
        self.assertTrue(not is_even(43))

    def test_forty_four_is_even(self):
        self.assertTrue(is_even(44))

    def test_forty_five_is_even(self):
        self.assertTrue(not is_even(45))

    def test_forty_six_is_even(self):
        self.assertTrue(is_even(46))

    def test_forty_seven_is_even(self):
        self.assertTrue(not is_even(47))

    def test_forty_eight_is_even(self):
        self.assertTrue(is_even(48))

    def test_forty_nine_is_even(self):
        self.assertTrue(not is_even(49))

    def test_fifty_is_even(self):
        self.assertTrue(is_even(50))

    def test_fifty_one_is_even(self):
        self.assertTrue(not is_even(51))

    def test_fifty_two_is_even(self):
        self.assertTrue(is_even(52))

    def test_fifty_three_is_even(self):
        self.assertTrue(not is_even(53))

    def test_fifty_four_is_even(self):
        self.assertTrue(is_even(54))

    def test_fifty_five_is_even(self):
        self.assertTrue(not is_even(55))

    def test_fifty_six_is_even(self):
        self.assertTrue(is_even(56))

    def test_fifty_seven_is_even(self):
        self.assertTrue(not is_even(57))

    def test_fifty_eight_is_even(self):
        self.assertTrue(is_even(58))

    def test_fifty_nine_is_even(self):
        self.assertTrue(not is_even(59))

    def test_sixty_is_even(self):
        self.assertTrue(is_even(60))

    def test_sixty_one_is_even(self):
        self.assertTrue(not is_even(61))

    def test_sixty_two_is_even(self):
        self.assertTrue(is_even(62))

    def test_sixty_three_is_even(self):
        self.assertTrue(not is_even(63))

    def test_sixty_four_is_even(self):
        self.assertTrue(is_even(64))

    def test_sixty_five_is_even(self):
        self.assertTrue(not is_even(65))

    def test_sixty_six_is_even(self):
        self.assertTrue(is_even(66))

    def test_sixty_seven_is_even(self):
        self.assertTrue(not is_even(67))

    def test_sixty_eight_is_even(self):
        self.assertTrue(is_even(68))

    def test_sixty_nine_is_even(self):
        self.assertTrue(not is_even(69))

    def test_seventy_is_even(self):
        self.assertTrue(is_even(70))

    def test_seventy_one_is_even(self):
        self.assertTrue(not is_even(71))

    def test_seventy_two_is_even(self):
        self.assertTrue(is_even(72))

    def test_seventy_three_is_even(self):
        self.assertTrue(not is_even(73))

    def test_seventy_four_is_even(self):
        self.assertTrue(is_even(74))

    def test_seventy_five_is_even(self):
        self.assertTrue(not is_even(75))

    def test_seventy_six_is_even(self):
        self.assertTrue(is_even(76))

    def test_seventy_seven_is_even(self):
        self.assertTrue(not is_even(77))

    def test_seventy_eight_is_even(self):
        self.assertTrue(is_even(78))

    def test_seventy_nine_is_even(self):
        self.assertTrue(not is_even(79))

    def test_eighty_is_even(self):
        self.assertTrue(is_even(80))

    def test_eighty_one_is_even(self):
        self.assertTrue(not is_even(81))

    def test_eighty_two_is_even(self):
        self.assertTrue(is_even(82))

    def test_eighty_three_is_even(self):
        self.assertTrue(not is_even(83))

    def test_eighty_four_is_even(self):
        self.assertTrue(is_even(84))

    def test_eighty_five_is_even(self):
        self.assertTrue(not is_even(85))

    def test_eighty_six_is_even(self):
        self.assertTrue(is_even(86))

    def test_eighty_seven_is_even(self):
        self.assertTrue(not is_even(87))

    def test_eighty_eight_is_even(self):
        self.assertTrue(is_even(88))

    def test_eighty_nine_is_even(self):
        self.assertTrue(not is_even(89))

    def test_ninety_is_even(self):
        self.assertTrue(is_even(90))

    def test_ninety_one_is_even(self):
        self.assertTrue(not is_even(91))

    def test_ninety_two_is_even(self):
        self.assertTrue(is_even(92))

    def test_ninety_three_is_even(self):
        self.assertTrue(not is_even(93))

    def test_ninety_four_is_even(self):
        self.assertTrue(is_even(94))

    def test_ninety_five_is_even(self):
        self.assertTrue(not is_even(95))

    def test_ninety_six_is_even(self):
        self.assertTrue(is_even(96))

    def test_ninety_seven_is_even(self):
        self.assertTrue(not is_even(97))

    def test_ninety_eight_is_even(self):
        self.assertTrue(is_even(98))

    def test_ninety_nine_is_even(self):
        self.assertTrue(not is_even(99))

    def test_one_hundred_is_even(self):
        self.assertTrue(is_even(100))
