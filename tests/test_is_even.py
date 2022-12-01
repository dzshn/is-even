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

    def test_one_hundred_and_one_is_even(self):
        self.assertTrue(not is_even(101))

    def test_one_hundred_and_two_is_even(self):
        self.assertTrue(is_even(102))

    def test_one_hundred_and_three_is_even(self):
        self.assertTrue(not is_even(103))

    def test_one_hundred_and_four_is_even(self):
        self.assertTrue(is_even(104))

    def test_one_hundred_and_five_is_even(self):
        self.assertTrue(not is_even(105))

    def test_one_hundred_and_six_is_even(self):
        self.assertTrue(is_even(106))

    def test_one_hundred_and_seven_is_even(self):
        self.assertTrue(not is_even(107))

    def test_one_hundred_and_eight_is_even(self):
        self.assertTrue(is_even(108))

    def test_one_hundred_and_nine_is_even(self):
        self.assertTrue(not is_even(109))

    def test_one_hundred_and_ten_is_even(self):
        self.assertTrue(is_even(110))

    def test_one_hundred_and_eleven_is_even(self):
        self.assertTrue(not is_even(111))

    def test_one_hundred_and_twelve_is_even(self):
        self.assertTrue(is_even(112))

    def test_one_hundred_and_thirteen_is_even(self):
        self.assertTrue(not is_even(113))

    def test_one_hundred_and_fourteen_is_even(self):
        self.assertTrue(is_even(114))

    def test_one_hundred_and_fifteen_is_even(self):
        self.assertTrue(not is_even(115))

    def test_one_hundred_and_sixteen_is_even(self):
        self.assertTrue(is_even(116))

    def test_one_hundred_and_seventeen_is_even(self):
        self.assertTrue(not is_even(117))

    def test_one_hundred_and_eighteen_is_even(self):
        self.assertTrue(is_even(118))

    def test_one_hundred_and_nineteen_is_even(self):
        self.assertTrue(not is_even(119))

    def test_one_hundred_and_twenty_is_even(self):
        self.assertTrue(is_even(120))

    def test_one_hundred_and_twenty_one_is_even(self):
        self.assertTrue(not is_even(121))

    def test_one_hundred_and_twenty_two_is_even(self):
        self.assertTrue(is_even(122))

    def test_one_hundred_and_twenty_three_is_even(self):
        self.assertTrue(not is_even(123))

    def test_one_hundred_and_twenty_four_is_even(self):
        self.assertTrue(is_even(124))

    def test_one_hundred_and_twenty_five_is_even(self):
        self.assertTrue(not is_even(125))

    def test_one_hundred_and_twenty_six_is_even(self):
        self.assertTrue(is_even(126))

    def test_one_hundred_and_twenty_seven_is_even(self):
        self.assertTrue(not is_even(127))

    def test_one_hundred_and_twenty_eight_is_even(self):
        self.assertTrue(is_even(128))

    def test_one_hundred_and_twenty_nine_is_even(self):
        self.assertTrue(not is_even(129))

    def test_one_hundred_and_thirty_is_even(self):
        self.assertTrue(is_even(130))

    def test_one_hundred_and_thirty_one_is_even(self):
        self.assertTrue(not is_even(131))

    def test_one_hundred_and_thirty_two_is_even(self):
        self.assertTrue(is_even(132))

    def test_one_hundred_and_thirty_three_is_even(self):
        self.assertTrue(not is_even(133))

    def test_one_hundred_and_thirty_four_is_even(self):
        self.assertTrue(is_even(134))

    def test_one_hundred_and_thirty_five_is_even(self):
        self.assertTrue(not is_even(135))

    def test_one_hundred_and_thirty_six_is_even(self):
        self.assertTrue(is_even(136))

    def test_one_hundred_and_thirty_seven_is_even(self):
        self.assertTrue(not is_even(137))

    def test_one_hundred_and_thirty_eight_is_even(self):
        self.assertTrue(is_even(138))

    def test_one_hundred_and_thirty_nine_is_even(self):
        self.assertTrue(not is_even(139))

    def test_one_hundred_and_forty_is_even(self):
        self.assertTrue(is_even(140))

    def test_one_hundred_and_forty_one_is_even(self):
        self.assertTrue(not is_even(141))

    def test_one_hundred_and_forty_two_is_even(self):
        self.assertTrue(is_even(142))

    def test_one_hundred_and_forty_three_is_even(self):
        self.assertTrue(not is_even(143))

    def test_one_hundred_and_forty_four_is_even(self):
        self.assertTrue(is_even(144))

    def test_one_hundred_and_forty_five_is_even(self):
        self.assertTrue(not is_even(145))

    def test_one_hundred_and_forty_six_is_even(self):
        self.assertTrue(is_even(146))

    def test_one_hundred_and_forty_seven_is_even(self):
        self.assertTrue(not is_even(147))

    def test_one_hundred_and_forty_eight_is_even(self):
        self.assertTrue(is_even(148))

    def test_one_hundred_and_forty_nine_is_even(self):
        self.assertTrue(not is_even(149))

    def test_one_hundred_and_fifty_is_even(self):
        self.assertTrue(is_even(150))

    def test_one_hundred_and_fifty_one_is_even(self):
        self.assertTrue(not is_even(151))

    def test_one_hundred_and_fifty_two_is_even(self):
        self.assertTrue(is_even(152))

    def test_one_hundred_and_fifty_three_is_even(self):
        self.assertTrue(not is_even(153))

    def test_one_hundred_and_fifty_four_is_even(self):
        self.assertTrue(is_even(154))

    def test_one_hundred_and_fifty_five_is_even(self):
        self.assertTrue(not is_even(155))

    def test_one_hundred_and_fifty_six_is_even(self):
        self.assertTrue(is_even(156))

    def test_one_hundred_and_fifty_seven_is_even(self):
        self.assertTrue(not is_even(157))

    def test_one_hundred_and_fifty_eight_is_even(self):
        self.assertTrue(is_even(158))

    def test_one_hundred_and_fifty_nine_is_even(self):
        self.assertTrue(not is_even(159))

    def test_one_hundred_and_sixty_is_even(self):
        self.assertTrue(is_even(160))

    def test_one_hundred_and_sixty_one_is_even(self):
        self.assertTrue(not is_even(161))

    def test_one_hundred_and_sixty_two_is_even(self):
        self.assertTrue(is_even(162))

    def test_one_hundred_and_sixty_three_is_even(self):
        self.assertTrue(not is_even(163))

    def test_one_hundred_and_sixty_four_is_even(self):
        self.assertTrue(is_even(164))

    def test_one_hundred_and_sixty_five_is_even(self):
        self.assertTrue(not is_even(165))

    def test_one_hundred_and_sixty_six_is_even(self):
        self.assertTrue(is_even(166))

    def test_one_hundred_and_sixty_seven_is_even(self):
        self.assertTrue(not is_even(167))

    def test_one_hundred_and_sixty_eight_is_even(self):
        self.assertTrue(is_even(168))

    def test_one_hundred_and_sixty_nine_is_even(self):
        self.assertTrue(not is_even(169))

    def test_one_hundred_and_seventy_is_even(self):
        self.assertTrue(is_even(170))

    def test_one_hundred_and_seventy_one_is_even(self):
        self.assertTrue(not is_even(171))

    def test_one_hundred_and_seventy_two_is_even(self):
        self.assertTrue(is_even(172))

    def test_one_hundred_and_seventy_three_is_even(self):
        self.assertTrue(not is_even(173))

    def test_one_hundred_and_seventy_four_is_even(self):
        self.assertTrue(is_even(174))

    def test_one_hundred_and_seventy_five_is_even(self):
        self.assertTrue(not is_even(175))

    def test_one_hundred_and_seventy_six_is_even(self):
        self.assertTrue(is_even(176))

    def test_one_hundred_and_seventy_seven_is_even(self):
        self.assertTrue(not is_even(177))

    def test_one_hundred_and_seventy_eight_is_even(self):
        self.assertTrue(is_even(178))

    def test_one_hundred_and_seventy_nine_is_even(self):
        self.assertTrue(not is_even(179))

    def test_one_hundred_and_eighty_is_even(self):
        self.assertTrue(is_even(180))

    def test_one_hundred_and_eighty_one_is_even(self):
        self.assertTrue(not is_even(181))

    def test_one_hundred_and_eighty_two_is_even(self):
        self.assertTrue(is_even(182))

    def test_one_hundred_and_eighty_three_is_even(self):
        self.assertTrue(not is_even(183))

    def test_one_hundred_and_eighty_four_is_even(self):
        self.assertTrue(is_even(184))

    def test_one_hundred_and_eighty_five_is_even(self):
        self.assertTrue(not is_even(185))

    def test_one_hundred_and_eighty_six_is_even(self):
        self.assertTrue(is_even(186))

    def test_one_hundred_and_eighty_seven_is_even(self):
        self.assertTrue(not is_even(187))

    def test_one_hundred_and_eighty_eight_is_even(self):
        self.assertTrue(is_even(188))

    def test_one_hundred_and_eighty_nine_is_even(self):
        self.assertTrue(not is_even(189))

    def test_one_hundred_and_ninety_is_even(self):
        self.assertTrue(is_even(190))

    def test_one_hundred_and_ninety_one_is_even(self):
        self.assertTrue(not is_even(191))

    def test_one_hundred_and_ninety_two_is_even(self):
        self.assertTrue(is_even(192))

    def test_one_hundred_and_ninety_three_is_even(self):
        self.assertTrue(not is_even(193))

    def test_one_hundred_and_ninety_four_is_even(self):
        self.assertTrue(is_even(194))

    def test_one_hundred_and_ninety_five_is_even(self):
        self.assertTrue(not is_even(195))

    def test_one_hundred_and_ninety_six_is_even(self):
        self.assertTrue(is_even(196))

    def test_one_hundred_and_ninety_seven_is_even(self):
        self.assertTrue(not is_even(197))

    def test_one_hundred_and_ninety_eight_is_even(self):
        self.assertTrue(is_even(198))

    def test_one_hundred_and_ninety_nine_is_even(self):
        self.assertTrue(not is_even(199))

    def test_two_hundred_is_even(self):
        self.assertTrue(is_even(200))

    def test_two_hundred_and_one_is_even(self):
        self.assertTrue(not is_even(201))

    def test_two_hundred_and_two_is_even(self):
        self.assertTrue(is_even(202))

    def test_two_hundred_and_three_is_even(self):
        self.assertTrue(not is_even(203))

    def test_two_hundred_and_four_is_even(self):
        self.assertTrue(is_even(204))

    def test_two_hundred_and_five_is_even(self):
        self.assertTrue(not is_even(205))

    def test_two_hundred_and_six_is_even(self):
        self.assertTrue(is_even(206))

    def test_two_hundred_and_seven_is_even(self):
        self.assertTrue(not is_even(207))

    def test_two_hundred_and_eight_is_even(self):
        self.assertTrue(is_even(208))

    def test_two_hundred_and_nine_is_even(self):
        self.assertTrue(not is_even(209))

    def test_two_hundred_and_ten_is_even(self):
        self.assertTrue(is_even(210))

    def test_two_hundred_and_eleven_is_even(self):
        self.assertTrue(not is_even(211))

    def test_two_hundred_and_twelve_is_even(self):
        self.assertTrue(is_even(212))

    def test_two_hundred_and_thirteen_is_even(self):
        self.assertTrue(not is_even(213))

    def test_two_hundred_and_fourteen_is_even(self):
        self.assertTrue(is_even(214))

    def test_two_hundred_and_fifteen_is_even(self):
        self.assertTrue(not is_even(215))

    def test_two_hundred_and_sixteen_is_even(self):
        self.assertTrue(is_even(216))

    def test_two_hundred_and_seventeen_is_even(self):
        self.assertTrue(not is_even(217))

    def test_two_hundred_and_eighteen_is_even(self):
        self.assertTrue(is_even(218))

    def test_two_hundred_and_nineteen_is_even(self):
        self.assertTrue(not is_even(219))

    def test_two_hundred_and_twenty_is_even(self):
        self.assertTrue(is_even(220))

    def test_two_hundred_and_twenty_one_is_even(self):
        self.assertTrue(not is_even(221))

    def test_two_hundred_and_twenty_two_is_even(self):
        self.assertTrue(is_even(222))

    def test_two_hundred_and_twenty_three_is_even(self):
        self.assertTrue(not is_even(223))

    def test_two_hundred_and_twenty_four_is_even(self):
        self.assertTrue(is_even(224))

    def test_two_hundred_and_twenty_five_is_even(self):
        self.assertTrue(not is_even(225))

    def test_two_hundred_and_twenty_six_is_even(self):
        self.assertTrue(is_even(226))

    def test_two_hundred_and_twenty_seven_is_even(self):
        self.assertTrue(not is_even(227))

    def test_two_hundred_and_twenty_eight_is_even(self):
        self.assertTrue(is_even(228))

    def test_two_hundred_and_twenty_nine_is_even(self):
        self.assertTrue(not is_even(229))

    def test_two_hundred_and_thirty_is_even(self):
        self.assertTrue(is_even(230))

    def test_two_hundred_and_thirty_one_is_even(self):
        self.assertTrue(not is_even(231))

    def test_two_hundred_and_thirty_two_is_even(self):
        self.assertTrue(is_even(232))

    def test_two_hundred_and_thirty_three_is_even(self):
        self.assertTrue(not is_even(233))

    def test_two_hundred_and_thirty_four_is_even(self):
        self.assertTrue(is_even(234))

    def test_two_hundred_and_thirty_five_is_even(self):
        self.assertTrue(not is_even(235))

    def test_two_hundred_and_thirty_six_is_even(self):
        self.assertTrue(is_even(236))

    def test_two_hundred_and_thirty_seven_is_even(self):
        self.assertTrue(not is_even(237))

    def test_two_hundred_and_thirty_eight_is_even(self):
        self.assertTrue(is_even(238))

    def test_two_hundred_and_thirty_nine_is_even(self):
        self.assertTrue(not is_even(239))

    def test_two_hundred_and_forty_is_even(self):
        self.assertTrue(is_even(240))

    def test_two_hundred_and_forty_one_is_even(self):
        self.assertTrue(not is_even(241))

    def test_two_hundred_and_forty_two_is_even(self):
        self.assertTrue(is_even(242))

    def test_two_hundred_and_forty_three_is_even(self):
        self.assertTrue(not is_even(243))

    def test_two_hundred_and_forty_four_is_even(self):
        self.assertTrue(is_even(244))

    def test_two_hundred_and_forty_five_is_even(self):
        self.assertTrue(not is_even(245))

    def test_two_hundred_and_forty_six_is_even(self):
        self.assertTrue(is_even(246))

    def test_two_hundred_and_forty_seven_is_even(self):
        self.assertTrue(not is_even(247))

    def test_two_hundred_and_forty_eight_is_even(self):
        self.assertTrue(is_even(248))

    def test_two_hundred_and_forty_nine_is_even(self):
        self.assertTrue(not is_even(249))

    def test_two_hundred_and_fifty_is_even(self):
        self.assertTrue(is_even(250))

    def test_two_hundred_and_fifty_one_is_even(self):
        self.assertTrue(not is_even(251))

    def test_two_hundred_and_fifty_two_is_even(self):
        self.assertTrue(is_even(252))

    def test_two_hundred_and_fifty_three_is_even(self):
        self.assertTrue(not is_even(253))

    def test_two_hundred_and_fifty_four_is_even(self):
        self.assertTrue(is_even(254))

    def test_two_hundred_and_fifty_five_is_even(self):
        self.assertTrue(not is_even(255))

    def test_two_hundred_and_fifty_six_is_even(self):
        self.assertTrue(is_even(256))

    def test_two_hundred_and_fifty_seven_is_even(self):
        self.assertTrue(not is_even(257))

    def test_two_hundred_and_fifty_eight_is_even(self):
        self.assertTrue(is_even(258))

    def test_two_hundred_and_fifty_nine_is_even(self):
        self.assertTrue(not is_even(259))

    def test_two_hundred_and_sixty_is_even(self):
        self.assertTrue(is_even(260))

    def test_two_hundred_and_sixty_one_is_even(self):
        self.assertTrue(not is_even(261))

    def test_two_hundred_and_sixty_two_is_even(self):
        self.assertTrue(is_even(262))

    def test_two_hundred_and_sixty_three_is_even(self):
        self.assertTrue(not is_even(263))

    def test_two_hundred_and_sixty_four_is_even(self):
        self.assertTrue(is_even(264))

    def test_two_hundred_and_sixty_five_is_even(self):
        self.assertTrue(not is_even(265))

    def test_two_hundred_and_sixty_six_is_even(self):
        self.assertTrue(is_even(266))

    def test_two_hundred_and_sixty_seven_is_even(self):
        self.assertTrue(not is_even(267))

    def test_two_hundred_and_sixty_eight_is_even(self):
        self.assertTrue(is_even(268))

    def test_two_hundred_and_sixty_nine_is_even(self):
        self.assertTrue(not is_even(269))

    def test_two_hundred_and_seventy_is_even(self):
        self.assertTrue(is_even(270))

    def test_two_hundred_and_seventy_one_is_even(self):
        self.assertTrue(not is_even(271))

    def test_two_hundred_and_seventy_two_is_even(self):
        self.assertTrue(is_even(272))

    def test_two_hundred_and_seventy_three_is_even(self):
        self.assertTrue(not is_even(273))

    def test_two_hundred_and_seventy_four_is_even(self):
        self.assertTrue(is_even(274))

    def test_two_hundred_and_seventy_five_is_even(self):
        self.assertTrue(not is_even(275))

    def test_two_hundred_and_seventy_six_is_even(self):
        self.assertTrue(is_even(276))

    def test_two_hundred_and_seventy_seven_is_even(self):
        self.assertTrue(not is_even(277))

    def test_two_hundred_and_seventy_eight_is_even(self):
        self.assertTrue(is_even(278))

    def test_two_hundred_and_seventy_nine_is_even(self):
        self.assertTrue(not is_even(279))

    def test_two_hundred_and_eighty_is_even(self):
        self.assertTrue(is_even(280))

    def test_two_hundred_and_eighty_one_is_even(self):
        self.assertTrue(not is_even(281))

    def test_two_hundred_and_eighty_two_is_even(self):
        self.assertTrue(is_even(282))

    def test_two_hundred_and_eighty_three_is_even(self):
        self.assertTrue(not is_even(283))

    def test_two_hundred_and_eighty_four_is_even(self):
        self.assertTrue(is_even(284))

    def test_two_hundred_and_eighty_five_is_even(self):
        self.assertTrue(not is_even(285))

    def test_two_hundred_and_eighty_six_is_even(self):
        self.assertTrue(is_even(286))

    def test_two_hundred_and_eighty_seven_is_even(self):
        self.assertTrue(not is_even(287))

    def test_two_hundred_and_eighty_eight_is_even(self):
        self.assertTrue(is_even(288))

    def test_two_hundred_and_eighty_nine_is_even(self):
        self.assertTrue(not is_even(289))

    def test_two_hundred_and_ninety_is_even(self):
        self.assertTrue(is_even(290))

    def test_two_hundred_and_ninety_one_is_even(self):
        self.assertTrue(not is_even(291))

    def test_two_hundred_and_ninety_two_is_even(self):
        self.assertTrue(is_even(292))

    def test_two_hundred_and_ninety_three_is_even(self):
        self.assertTrue(not is_even(293))

    def test_two_hundred_and_ninety_four_is_even(self):
        self.assertTrue(is_even(294))

    def test_two_hundred_and_ninety_five_is_even(self):
        self.assertTrue(not is_even(295))

    def test_two_hundred_and_ninety_six_is_even(self):
        self.assertTrue(is_even(296))

    def test_two_hundred_and_ninety_seven_is_even(self):
        self.assertTrue(not is_even(297))

    def test_two_hundred_and_ninety_eight_is_even(self):
        self.assertTrue(is_even(298))

    def test_two_hundred_and_ninety_nine_is_even(self):
        self.assertTrue(not is_even(299))

    def test_three_hundred_is_even(self):
        self.assertTrue(is_even(300))

    def test_three_hundred_and_one_is_even(self):
        self.assertTrue(not is_even(301))

    def test_three_hundred_and_two_is_even(self):
        self.assertTrue(is_even(302))

    def test_three_hundred_and_three_is_even(self):
        self.assertTrue(not is_even(303))

    def test_three_hundred_and_four_is_even(self):
        self.assertTrue(is_even(304))

    def test_three_hundred_and_five_is_even(self):
        self.assertTrue(not is_even(305))

    def test_three_hundred_and_six_is_even(self):
        self.assertTrue(is_even(306))

    def test_three_hundred_and_seven_is_even(self):
        self.assertTrue(not is_even(307))

    def test_three_hundred_and_eight_is_even(self):
        self.assertTrue(is_even(308))

    def test_three_hundred_and_nine_is_even(self):
        self.assertTrue(not is_even(309))

    def test_three_hundred_and_ten_is_even(self):
        self.assertTrue(is_even(310))

    def test_three_hundred_and_eleven_is_even(self):
        self.assertTrue(not is_even(311))

    def test_three_hundred_and_twelve_is_even(self):
        self.assertTrue(is_even(312))

    def test_three_hundred_and_thirteen_is_even(self):
        self.assertTrue(not is_even(313))

    def test_three_hundred_and_fourteen_is_even(self):
        self.assertTrue(is_even(314))

    def test_three_hundred_and_fifteen_is_even(self):
        self.assertTrue(not is_even(315))

    def test_three_hundred_and_sixteen_is_even(self):
        self.assertTrue(is_even(316))

    def test_three_hundred_and_seventeen_is_even(self):
        self.assertTrue(not is_even(317))

    def test_three_hundred_and_eighteen_is_even(self):
        self.assertTrue(is_even(318))

    def test_three_hundred_and_nineteen_is_even(self):
        self.assertTrue(not is_even(319))

    def test_three_hundred_and_twenty_is_even(self):
        self.assertTrue(is_even(320))

    def test_three_hundred_and_twenty_one_is_even(self):
        self.assertTrue(not is_even(321))

    def test_three_hundred_and_twenty_two_is_even(self):
        self.assertTrue(is_even(322))

    def test_three_hundred_and_twenty_three_is_even(self):
        self.assertTrue(not is_even(323))

    def test_three_hundred_and_twenty_four_is_even(self):
        self.assertTrue(is_even(324))

    def test_three_hundred_and_twenty_five_is_even(self):
        self.assertTrue(not is_even(325))

    def test_three_hundred_and_twenty_six_is_even(self):
        self.assertTrue(is_even(326))

    def test_three_hundred_and_twenty_seven_is_even(self):
        self.assertTrue(not is_even(327))

    def test_three_hundred_and_twenty_eight_is_even(self):
        self.assertTrue(is_even(328))

    def test_three_hundred_and_twenty_nine_is_even(self):
        self.assertTrue(not is_even(329))

    def test_three_hundred_and_thirty_is_even(self):
        self.assertTrue(is_even(330))

    def test_three_hundred_and_thirty_one_is_even(self):
        self.assertTrue(not is_even(331))

    def test_three_hundred_and_thirty_two_is_even(self):
        self.assertTrue(is_even(332))

    def test_three_hundred_and_thirty_three_is_even(self):
        self.assertTrue(not is_even(333))

    def test_three_hundred_and_thirty_four_is_even(self):
        self.assertTrue(is_even(334))

    def test_three_hundred_and_thirty_five_is_even(self):
        self.assertTrue(not is_even(335))

    def test_three_hundred_and_thirty_six_is_even(self):
        self.assertTrue(is_even(336))

    def test_three_hundred_and_thirty_seven_is_even(self):
        self.assertTrue(not is_even(337))

    def test_three_hundred_and_thirty_eight_is_even(self):
        self.assertTrue(is_even(338))

    def test_three_hundred_and_thirty_nine_is_even(self):
        self.assertTrue(not is_even(339))

    def test_three_hundred_and_forty_is_even(self):
        self.assertTrue(is_even(340))

    def test_three_hundred_and_forty_one_is_even(self):
        self.assertTrue(not is_even(341))

    def test_three_hundred_and_forty_two_is_even(self):
        self.assertTrue(is_even(342))

    def test_three_hundred_and_forty_three_is_even(self):
        self.assertTrue(not is_even(343))

    def test_three_hundred_and_forty_four_is_even(self):
        self.assertTrue(is_even(344))

    def test_three_hundred_and_forty_five_is_even(self):
        self.assertTrue(not is_even(345))

    def test_three_hundred_and_forty_six_is_even(self):
        self.assertTrue(is_even(346))

    def test_three_hundred_and_forty_seven_is_even(self):
        self.assertTrue(not is_even(347))

    def test_three_hundred_and_forty_eight_is_even(self):
        self.assertTrue(is_even(348))

    def test_three_hundred_and_forty_nine_is_even(self):
        self.assertTrue(not is_even(349))

    def test_three_hundred_and_fifty_is_even(self):
        self.assertTrue(is_even(350))

    def test_three_hundred_and_fifty_one_is_even(self):
        self.assertTrue(not is_even(351))

    def test_three_hundred_and_fifty_two_is_even(self):
        self.assertTrue(is_even(352))

    def test_three_hundred_and_fifty_three_is_even(self):
        self.assertTrue(not is_even(353))

    def test_three_hundred_and_fifty_four_is_even(self):
        self.assertTrue(is_even(354))

    def test_three_hundred_and_fifty_five_is_even(self):
        self.assertTrue(not is_even(355))

    def test_three_hundred_and_fifty_six_is_even(self):
        self.assertTrue(is_even(356))

    def test_three_hundred_and_fifty_seven_is_even(self):
        self.assertTrue(not is_even(357))

    def test_three_hundred_and_fifty_eight_is_even(self):
        self.assertTrue(is_even(358))

    def test_three_hundred_and_fifty_nine_is_even(self):
        self.assertTrue(not is_even(359))

    def test_three_hundred_and_sixty_is_even(self):
        self.assertTrue(is_even(360))

    def test_three_hundred_and_sixty_one_is_even(self):
        self.assertTrue(not is_even(361))

    def test_three_hundred_and_sixty_two_is_even(self):
        self.assertTrue(is_even(362))

    def test_three_hundred_and_sixty_three_is_even(self):
        self.assertTrue(not is_even(363))

    def test_three_hundred_and_sixty_four_is_even(self):
        self.assertTrue(is_even(364))

    def test_three_hundred_and_sixty_five_is_even(self):
        self.assertTrue(not is_even(365))

    def test_three_hundred_and_sixty_six_is_even(self):
        self.assertTrue(is_even(366))

    def test_three_hundred_and_sixty_seven_is_even(self):
        self.assertTrue(not is_even(367))

    def test_three_hundred_and_sixty_eight_is_even(self):
        self.assertTrue(is_even(368))

    def test_three_hundred_and_sixty_nine_is_even(self):
        self.assertTrue(not is_even(369))

    def test_three_hundred_and_seventy_is_even(self):
        self.assertTrue(is_even(370))

    def test_three_hundred_and_seventy_one_is_even(self):
        self.assertTrue(not is_even(371))

    def test_three_hundred_and_seventy_two_is_even(self):
        self.assertTrue(is_even(372))

    def test_three_hundred_and_seventy_three_is_even(self):
        self.assertTrue(not is_even(373))

    def test_three_hundred_and_seventy_four_is_even(self):
        self.assertTrue(is_even(374))

    def test_three_hundred_and_seventy_five_is_even(self):
        self.assertTrue(not is_even(375))

    def test_three_hundred_and_seventy_six_is_even(self):
        self.assertTrue(is_even(376))

    def test_three_hundred_and_seventy_seven_is_even(self):
        self.assertTrue(not is_even(377))

    def test_three_hundred_and_seventy_eight_is_even(self):
        self.assertTrue(is_even(378))

    def test_three_hundred_and_seventy_nine_is_even(self):
        self.assertTrue(not is_even(379))

    def test_three_hundred_and_eighty_is_even(self):
        self.assertTrue(is_even(380))

    def test_three_hundred_and_eighty_one_is_even(self):
        self.assertTrue(not is_even(381))

    def test_three_hundred_and_eighty_two_is_even(self):
        self.assertTrue(is_even(382))

    def test_three_hundred_and_eighty_three_is_even(self):
        self.assertTrue(not is_even(383))

    def test_three_hundred_and_eighty_four_is_even(self):
        self.assertTrue(is_even(384))

    def test_three_hundred_and_eighty_five_is_even(self):
        self.assertTrue(not is_even(385))

    def test_three_hundred_and_eighty_six_is_even(self):
        self.assertTrue(is_even(386))

    def test_three_hundred_and_eighty_seven_is_even(self):
        self.assertTrue(not is_even(387))

    def test_three_hundred_and_eighty_eight_is_even(self):
        self.assertTrue(is_even(388))

    def test_three_hundred_and_eighty_nine_is_even(self):
        self.assertTrue(not is_even(389))

    def test_three_hundred_and_ninety_is_even(self):
        self.assertTrue(is_even(390))

    def test_three_hundred_and_ninety_one_is_even(self):
        self.assertTrue(not is_even(391))

    def test_three_hundred_and_ninety_two_is_even(self):
        self.assertTrue(is_even(392))

    def test_three_hundred_and_ninety_three_is_even(self):
        self.assertTrue(not is_even(393))

    def test_three_hundred_and_ninety_four_is_even(self):
        self.assertTrue(is_even(394))

    def test_three_hundred_and_ninety_five_is_even(self):
        self.assertTrue(not is_even(395))

    def test_three_hundred_and_ninety_six_is_even(self):
        self.assertTrue(is_even(396))

    def test_three_hundred_and_ninety_seven_is_even(self):
        self.assertTrue(not is_even(397))

    def test_three_hundred_and_ninety_eight_is_even(self):
        self.assertTrue(is_even(398))

    def test_three_hundred_and_ninety_nine_is_even(self):
        self.assertTrue(not is_even(399))

    def test_four_hundred_is_even(self):
        self.assertTrue(is_even(400))

    def test_four_hundred_and_one_is_even(self):
        self.assertTrue(not is_even(401))

    def test_four_hundred_and_two_is_even(self):
        self.assertTrue(is_even(402))

    def test_four_hundred_and_three_is_even(self):
        self.assertTrue(not is_even(403))

    def test_four_hundred_and_four_is_even(self):
        self.assertTrue(is_even(404))

    def test_four_hundred_and_five_is_even(self):
        self.assertTrue(not is_even(405))

    def test_four_hundred_and_six_is_even(self):
        self.assertTrue(is_even(406))

    def test_four_hundred_and_seven_is_even(self):
        self.assertTrue(not is_even(407))

    def test_four_hundred_and_eight_is_even(self):
        self.assertTrue(is_even(408))

    def test_four_hundred_and_nine_is_even(self):
        self.assertTrue(not is_even(409))

    def test_four_hundred_and_ten_is_even(self):
        self.assertTrue(is_even(410))

    def test_four_hundred_and_eleven_is_even(self):
        self.assertTrue(not is_even(411))

    def test_four_hundred_and_twelve_is_even(self):
        self.assertTrue(is_even(412))

    def test_four_hundred_and_thirteen_is_even(self):
        self.assertTrue(not is_even(413))

    def test_four_hundred_and_fourteen_is_even(self):
        self.assertTrue(is_even(414))

    def test_four_hundred_and_fifteen_is_even(self):
        self.assertTrue(not is_even(415))

    def test_four_hundred_and_sixteen_is_even(self):
        self.assertTrue(is_even(416))

    def test_four_hundred_and_seventeen_is_even(self):
        self.assertTrue(not is_even(417))

    def test_four_hundred_and_eighteen_is_even(self):
        self.assertTrue(is_even(418))

    def test_four_hundred_and_nineteen_is_even(self):
        self.assertTrue(not is_even(419))

    def test_four_hundred_and_twenty_is_even(self):
        self.assertTrue(is_even(420))

    def test_four_hundred_and_twenty_one_is_even(self):
        self.assertTrue(not is_even(421))

    def test_four_hundred_and_twenty_two_is_even(self):
        self.assertTrue(is_even(422))

    def test_four_hundred_and_twenty_three_is_even(self):
        self.assertTrue(not is_even(423))

    def test_four_hundred_and_twenty_four_is_even(self):
        self.assertTrue(is_even(424))

    def test_four_hundred_and_twenty_five_is_even(self):
        self.assertTrue(not is_even(425))

    def test_four_hundred_and_twenty_six_is_even(self):
        self.assertTrue(is_even(426))

    def test_four_hundred_and_twenty_seven_is_even(self):
        self.assertTrue(not is_even(427))

    def test_four_hundred_and_twenty_eight_is_even(self):
        self.assertTrue(is_even(428))

    def test_four_hundred_and_twenty_nine_is_even(self):
        self.assertTrue(not is_even(429))

    def test_four_hundred_and_thirty_is_even(self):
        self.assertTrue(is_even(430))

    def test_four_hundred_and_thirty_one_is_even(self):
        self.assertTrue(not is_even(431))

    def test_four_hundred_and_thirty_two_is_even(self):
        self.assertTrue(is_even(432))

    def test_four_hundred_and_thirty_three_is_even(self):
        self.assertTrue(not is_even(433))

    def test_four_hundred_and_thirty_four_is_even(self):
        self.assertTrue(is_even(434))

    def test_four_hundred_and_thirty_five_is_even(self):
        self.assertTrue(not is_even(435))

    def test_four_hundred_and_thirty_six_is_even(self):
        self.assertTrue(is_even(436))

    def test_four_hundred_and_thirty_seven_is_even(self):
        self.assertTrue(not is_even(437))

    def test_four_hundred_and_thirty_eight_is_even(self):
        self.assertTrue(is_even(438))

    def test_four_hundred_and_thirty_nine_is_even(self):
        self.assertTrue(not is_even(439))

    def test_four_hundred_and_forty_is_even(self):
        self.assertTrue(is_even(440))

    def test_four_hundred_and_forty_one_is_even(self):
        self.assertTrue(not is_even(441))

    def test_four_hundred_and_forty_two_is_even(self):
        self.assertTrue(is_even(442))

    def test_four_hundred_and_forty_three_is_even(self):
        self.assertTrue(not is_even(443))

    def test_four_hundred_and_forty_four_is_even(self):
        self.assertTrue(is_even(444))

    def test_four_hundred_and_forty_five_is_even(self):
        self.assertTrue(not is_even(445))

    def test_four_hundred_and_forty_six_is_even(self):
        self.assertTrue(is_even(446))

    def test_four_hundred_and_forty_seven_is_even(self):
        self.assertTrue(not is_even(447))

    def test_four_hundred_and_forty_eight_is_even(self):
        self.assertTrue(is_even(448))

    def test_four_hundred_and_forty_nine_is_even(self):
        self.assertTrue(not is_even(449))

    def test_four_hundred_and_fifty_is_even(self):
        self.assertTrue(is_even(450))

    def test_four_hundred_and_fifty_one_is_even(self):
        self.assertTrue(not is_even(451))

    def test_four_hundred_and_fifty_two_is_even(self):
        self.assertTrue(is_even(452))

    def test_four_hundred_and_fifty_three_is_even(self):
        self.assertTrue(not is_even(453))

    def test_four_hundred_and_fifty_four_is_even(self):
        self.assertTrue(is_even(454))

    def test_four_hundred_and_fifty_five_is_even(self):
        self.assertTrue(not is_even(455))

    def test_four_hundred_and_fifty_six_is_even(self):
        self.assertTrue(is_even(456))

    def test_four_hundred_and_fifty_seven_is_even(self):
        self.assertTrue(not is_even(457))

    def test_four_hundred_and_fifty_eight_is_even(self):
        self.assertTrue(is_even(458))

    def test_four_hundred_and_fifty_nine_is_even(self):
        self.assertTrue(not is_even(459))

    def test_four_hundred_and_sixty_is_even(self):
        self.assertTrue(is_even(460))

    def test_four_hundred_and_sixty_one_is_even(self):
        self.assertTrue(not is_even(461))

    def test_four_hundred_and_sixty_two_is_even(self):
        self.assertTrue(is_even(462))

    def test_four_hundred_and_sixty_three_is_even(self):
        self.assertTrue(not is_even(463))

    def test_four_hundred_and_sixty_four_is_even(self):
        self.assertTrue(is_even(464))

    def test_four_hundred_and_sixty_five_is_even(self):
        self.assertTrue(not is_even(465))

    def test_four_hundred_and_sixty_six_is_even(self):
        self.assertTrue(is_even(466))

    def test_four_hundred_and_sixty_seven_is_even(self):
        self.assertTrue(not is_even(467))

    def test_four_hundred_and_sixty_eight_is_even(self):
        self.assertTrue(is_even(468))

    def test_four_hundred_and_sixty_nine_is_even(self):
        self.assertTrue(not is_even(469))

    def test_four_hundred_and_seventy_is_even(self):
        self.assertTrue(is_even(470))

    def test_four_hundred_and_seventy_one_is_even(self):
        self.assertTrue(not is_even(471))

    def test_four_hundred_and_seventy_two_is_even(self):
        self.assertTrue(is_even(472))

    def test_four_hundred_and_seventy_three_is_even(self):
        self.assertTrue(not is_even(473))

    def test_four_hundred_and_seventy_four_is_even(self):
        self.assertTrue(is_even(474))

    def test_four_hundred_and_seventy_five_is_even(self):
        self.assertTrue(not is_even(475))

    def test_four_hundred_and_seventy_six_is_even(self):
        self.assertTrue(is_even(476))

    def test_four_hundred_and_seventy_seven_is_even(self):
        self.assertTrue(not is_even(477))

    def test_four_hundred_and_seventy_eight_is_even(self):
        self.assertTrue(is_even(478))

    def test_four_hundred_and_seventy_nine_is_even(self):
        self.assertTrue(not is_even(479))

    def test_four_hundred_and_eighty_is_even(self):
        self.assertTrue(is_even(480))

    def test_four_hundred_and_eighty_one_is_even(self):
        self.assertTrue(not is_even(481))

    def test_four_hundred_and_eighty_two_is_even(self):
        self.assertTrue(is_even(482))

    def test_four_hundred_and_eighty_three_is_even(self):
        self.assertTrue(not is_even(483))

    def test_four_hundred_and_eighty_four_is_even(self):
        self.assertTrue(is_even(484))

    def test_four_hundred_and_eighty_five_is_even(self):
        self.assertTrue(not is_even(485))

    def test_four_hundred_and_eighty_six_is_even(self):
        self.assertTrue(is_even(486))

    def test_four_hundred_and_eighty_seven_is_even(self):
        self.assertTrue(not is_even(487))

    def test_four_hundred_and_eighty_eight_is_even(self):
        self.assertTrue(is_even(488))

    def test_four_hundred_and_eighty_nine_is_even(self):
        self.assertTrue(not is_even(489))

    def test_four_hundred_and_ninety_is_even(self):
        self.assertTrue(is_even(490))

    def test_four_hundred_and_ninety_one_is_even(self):
        self.assertTrue(not is_even(491))

    def test_four_hundred_and_ninety_two_is_even(self):
        self.assertTrue(is_even(492))

    def test_four_hundred_and_ninety_three_is_even(self):
        self.assertTrue(not is_even(493))

    def test_four_hundred_and_ninety_four_is_even(self):
        self.assertTrue(is_even(494))

    def test_four_hundred_and_ninety_five_is_even(self):
        self.assertTrue(not is_even(495))

    def test_four_hundred_and_ninety_six_is_even(self):
        self.assertTrue(is_even(496))

    def test_four_hundred_and_ninety_seven_is_even(self):
        self.assertTrue(not is_even(497))

    def test_four_hundred_and_ninety_eight_is_even(self):
        self.assertTrue(is_even(498))

    def test_four_hundred_and_ninety_nine_is_even(self):
        self.assertTrue(not is_even(499))

    def test_five_hundred_is_even(self):
        self.assertTrue(is_even(500))

    def test_five_hundred_and_one_is_even(self):
        self.assertTrue(not is_even(501))

    def test_five_hundred_and_two_is_even(self):
        self.assertTrue(is_even(502))

    def test_five_hundred_and_three_is_even(self):
        self.assertTrue(not is_even(503))

    def test_five_hundred_and_four_is_even(self):
        self.assertTrue(is_even(504))

    def test_five_hundred_and_five_is_even(self):
        self.assertTrue(not is_even(505))

    def test_five_hundred_and_six_is_even(self):
        self.assertTrue(is_even(506))

    def test_five_hundred_and_seven_is_even(self):
        self.assertTrue(not is_even(507))

    def test_five_hundred_and_eight_is_even(self):
        self.assertTrue(is_even(508))

    def test_five_hundred_and_nine_is_even(self):
        self.assertTrue(not is_even(509))

    def test_five_hundred_and_ten_is_even(self):
        self.assertTrue(is_even(510))

    def test_five_hundred_and_eleven_is_even(self):
        self.assertTrue(not is_even(511))

    def test_five_hundred_and_twelve_is_even(self):
        self.assertTrue(is_even(512))

    def test_five_hundred_and_thirteen_is_even(self):
        self.assertTrue(not is_even(513))

    def test_five_hundred_and_fourteen_is_even(self):
        self.assertTrue(is_even(514))

    def test_five_hundred_and_fifteen_is_even(self):
        self.assertTrue(not is_even(515))

    def test_five_hundred_and_sixteen_is_even(self):
        self.assertTrue(is_even(516))

    def test_five_hundred_and_seventeen_is_even(self):
        self.assertTrue(not is_even(517))

    def test_five_hundred_and_eighteen_is_even(self):
        self.assertTrue(is_even(518))

    def test_five_hundred_and_nineteen_is_even(self):
        self.assertTrue(not is_even(519))

    def test_five_hundred_and_twenty_is_even(self):
        self.assertTrue(is_even(520))

    def test_five_hundred_and_twenty_one_is_even(self):
        self.assertTrue(not is_even(521))

    def test_five_hundred_and_twenty_two_is_even(self):
        self.assertTrue(is_even(522))

    def test_five_hundred_and_twenty_three_is_even(self):
        self.assertTrue(not is_even(523))

    def test_five_hundred_and_twenty_four_is_even(self):
        self.assertTrue(is_even(524))

    def test_five_hundred_and_twenty_five_is_even(self):
        self.assertTrue(not is_even(525))

    def test_five_hundred_and_twenty_six_is_even(self):
        self.assertTrue(is_even(526))

    def test_five_hundred_and_twenty_seven_is_even(self):
        self.assertTrue(not is_even(527))

    def test_five_hundred_and_twenty_eight_is_even(self):
        self.assertTrue(is_even(528))

    def test_five_hundred_and_twenty_nine_is_even(self):
        self.assertTrue(not is_even(529))

    def test_five_hundred_and_thirty_is_even(self):
        self.assertTrue(is_even(530))

    def test_five_hundred_and_thirty_one_is_even(self):
        self.assertTrue(not is_even(531))

    def test_five_hundred_and_thirty_two_is_even(self):
        self.assertTrue(is_even(532))

    def test_five_hundred_and_thirty_three_is_even(self):
        self.assertTrue(not is_even(533))

    def test_five_hundred_and_thirty_four_is_even(self):
        self.assertTrue(is_even(534))

    def test_five_hundred_and_thirty_five_is_even(self):
        self.assertTrue(not is_even(535))

    def test_five_hundred_and_thirty_six_is_even(self):
        self.assertTrue(is_even(536))

    def test_five_hundred_and_thirty_seven_is_even(self):
        self.assertTrue(not is_even(537))

    def test_five_hundred_and_thirty_eight_is_even(self):
        self.assertTrue(is_even(538))

    def test_five_hundred_and_thirty_nine_is_even(self):
        self.assertTrue(not is_even(539))

    def test_five_hundred_and_forty_is_even(self):
        self.assertTrue(is_even(540))

    def test_five_hundred_and_forty_one_is_even(self):
        self.assertTrue(not is_even(541))

    def test_five_hundred_and_forty_two_is_even(self):
        self.assertTrue(is_even(542))

    def test_five_hundred_and_forty_three_is_even(self):
        self.assertTrue(not is_even(543))

    def test_five_hundred_and_forty_four_is_even(self):
        self.assertTrue(is_even(544))

    def test_five_hundred_and_forty_five_is_even(self):
        self.assertTrue(not is_even(545))

    def test_five_hundred_and_forty_six_is_even(self):
        self.assertTrue(is_even(546))

    def test_five_hundred_and_forty_seven_is_even(self):
        self.assertTrue(not is_even(547))

    def test_five_hundred_and_forty_eight_is_even(self):
        self.assertTrue(is_even(548))

    def test_five_hundred_and_forty_nine_is_even(self):
        self.assertTrue(not is_even(549))

    def test_five_hundred_and_fifty_is_even(self):
        self.assertTrue(is_even(550))

    def test_five_hundred_and_fifty_one_is_even(self):
        self.assertTrue(not is_even(551))

    def test_five_hundred_and_fifty_two_is_even(self):
        self.assertTrue(is_even(552))

    def test_five_hundred_and_fifty_three_is_even(self):
        self.assertTrue(not is_even(553))

    def test_five_hundred_and_fifty_four_is_even(self):
        self.assertTrue(is_even(554))

    def test_five_hundred_and_fifty_five_is_even(self):
        self.assertTrue(not is_even(555))

    def test_five_hundred_and_fifty_six_is_even(self):
        self.assertTrue(is_even(556))

    def test_five_hundred_and_fifty_seven_is_even(self):
        self.assertTrue(not is_even(557))

    def test_five_hundred_and_fifty_eight_is_even(self):
        self.assertTrue(is_even(558))

    def test_five_hundred_and_fifty_nine_is_even(self):
        self.assertTrue(not is_even(559))

    def test_five_hundred_and_sixty_is_even(self):
        self.assertTrue(is_even(560))

    def test_five_hundred_and_sixty_one_is_even(self):
        self.assertTrue(not is_even(561))

    def test_five_hundred_and_sixty_two_is_even(self):
        self.assertTrue(is_even(562))

    def test_five_hundred_and_sixty_three_is_even(self):
        self.assertTrue(not is_even(563))

    def test_five_hundred_and_sixty_four_is_even(self):
        self.assertTrue(is_even(564))

    def test_five_hundred_and_sixty_five_is_even(self):
        self.assertTrue(not is_even(565))

    def test_five_hundred_and_sixty_six_is_even(self):
        self.assertTrue(is_even(566))

    def test_five_hundred_and_sixty_seven_is_even(self):
        self.assertTrue(not is_even(567))

    def test_five_hundred_and_sixty_eight_is_even(self):
        self.assertTrue(is_even(568))

    def test_five_hundred_and_sixty_nine_is_even(self):
        self.assertTrue(not is_even(569))

    def test_five_hundred_and_seventy_is_even(self):
        self.assertTrue(is_even(570))

    def test_five_hundred_and_seventy_one_is_even(self):
        self.assertTrue(not is_even(571))

    def test_five_hundred_and_seventy_two_is_even(self):
        self.assertTrue(is_even(572))

    def test_five_hundred_and_seventy_three_is_even(self):
        self.assertTrue(not is_even(573))

    def test_five_hundred_and_seventy_four_is_even(self):
        self.assertTrue(is_even(574))

    def test_five_hundred_and_seventy_five_is_even(self):
        self.assertTrue(not is_even(575))

    def test_five_hundred_and_seventy_six_is_even(self):
        self.assertTrue(is_even(576))

    def test_five_hundred_and_seventy_seven_is_even(self):
        self.assertTrue(not is_even(577))

    def test_five_hundred_and_seventy_eight_is_even(self):
        self.assertTrue(is_even(578))

    def test_five_hundred_and_seventy_nine_is_even(self):
        self.assertTrue(not is_even(579))

    def test_five_hundred_and_eighty_is_even(self):
        self.assertTrue(is_even(580))

    def test_five_hundred_and_eighty_one_is_even(self):
        self.assertTrue(not is_even(581))

    def test_five_hundred_and_eighty_two_is_even(self):
        self.assertTrue(is_even(582))

    def test_five_hundred_and_eighty_three_is_even(self):
        self.assertTrue(not is_even(583))

    def test_five_hundred_and_eighty_four_is_even(self):
        self.assertTrue(is_even(584))

    def test_five_hundred_and_eighty_five_is_even(self):
        self.assertTrue(not is_even(585))

    def test_five_hundred_and_eighty_six_is_even(self):
        self.assertTrue(is_even(586))

    def test_five_hundred_and_eighty_seven_is_even(self):
        self.assertTrue(not is_even(587))

    def test_five_hundred_and_eighty_eight_is_even(self):
        self.assertTrue(is_even(588))

    def test_five_hundred_and_eighty_nine_is_even(self):
        self.assertTrue(not is_even(589))

    def test_five_hundred_and_ninety_is_even(self):
        self.assertTrue(is_even(590))

    def test_five_hundred_and_ninety_one_is_even(self):
        self.assertTrue(not is_even(591))

    def test_five_hundred_and_ninety_two_is_even(self):
        self.assertTrue(is_even(592))

    def test_five_hundred_and_ninety_three_is_even(self):
        self.assertTrue(not is_even(593))

    def test_five_hundred_and_ninety_four_is_even(self):
        self.assertTrue(is_even(594))

    def test_five_hundred_and_ninety_five_is_even(self):
        self.assertTrue(not is_even(595))

    def test_five_hundred_and_ninety_six_is_even(self):
        self.assertTrue(is_even(596))

    def test_five_hundred_and_ninety_seven_is_even(self):
        self.assertTrue(not is_even(597))

    def test_five_hundred_and_ninety_eight_is_even(self):
        self.assertTrue(is_even(598))

    def test_five_hundred_and_ninety_nine_is_even(self):
        self.assertTrue(not is_even(599))

    def test_six_hundred_is_even(self):
        self.assertTrue(is_even(600))

    def test_six_hundred_and_one_is_even(self):
        self.assertTrue(not is_even(601))

    def test_six_hundred_and_two_is_even(self):
        self.assertTrue(is_even(602))

    def test_six_hundred_and_three_is_even(self):
        self.assertTrue(not is_even(603))

    def test_six_hundred_and_four_is_even(self):
        self.assertTrue(is_even(604))

    def test_six_hundred_and_five_is_even(self):
        self.assertTrue(not is_even(605))

    def test_six_hundred_and_six_is_even(self):
        self.assertTrue(is_even(606))

    def test_six_hundred_and_seven_is_even(self):
        self.assertTrue(not is_even(607))

    def test_six_hundred_and_eight_is_even(self):
        self.assertTrue(is_even(608))

    def test_six_hundred_and_nine_is_even(self):
        self.assertTrue(not is_even(609))

    def test_six_hundred_and_ten_is_even(self):
        self.assertTrue(is_even(610))

    def test_six_hundred_and_eleven_is_even(self):
        self.assertTrue(not is_even(611))

    def test_six_hundred_and_twelve_is_even(self):
        self.assertTrue(is_even(612))

    def test_six_hundred_and_thirteen_is_even(self):
        self.assertTrue(not is_even(613))

    def test_six_hundred_and_fourteen_is_even(self):
        self.assertTrue(is_even(614))

    def test_six_hundred_and_fifteen_is_even(self):
        self.assertTrue(not is_even(615))

    def test_six_hundred_and_sixteen_is_even(self):
        self.assertTrue(is_even(616))

    def test_six_hundred_and_seventeen_is_even(self):
        self.assertTrue(not is_even(617))

    def test_six_hundred_and_eighteen_is_even(self):
        self.assertTrue(is_even(618))

    def test_six_hundred_and_nineteen_is_even(self):
        self.assertTrue(not is_even(619))

    def test_six_hundred_and_twenty_is_even(self):
        self.assertTrue(is_even(620))

    def test_six_hundred_and_twenty_one_is_even(self):
        self.assertTrue(not is_even(621))

    def test_six_hundred_and_twenty_two_is_even(self):
        self.assertTrue(is_even(622))

    def test_six_hundred_and_twenty_three_is_even(self):
        self.assertTrue(not is_even(623))

    def test_six_hundred_and_twenty_four_is_even(self):
        self.assertTrue(is_even(624))

    def test_six_hundred_and_twenty_five_is_even(self):
        self.assertTrue(not is_even(625))

    def test_six_hundred_and_twenty_six_is_even(self):
        self.assertTrue(is_even(626))

    def test_six_hundred_and_twenty_seven_is_even(self):
        self.assertTrue(not is_even(627))

    def test_six_hundred_and_twenty_eight_is_even(self):
        self.assertTrue(is_even(628))

    def test_six_hundred_and_twenty_nine_is_even(self):
        self.assertTrue(not is_even(629))

    def test_six_hundred_and_thirty_is_even(self):
        self.assertTrue(is_even(630))

    def test_six_hundred_and_thirty_one_is_even(self):
        self.assertTrue(not is_even(631))

    def test_six_hundred_and_thirty_two_is_even(self):
        self.assertTrue(is_even(632))

    def test_six_hundred_and_thirty_three_is_even(self):
        self.assertTrue(not is_even(633))

    def test_six_hundred_and_thirty_four_is_even(self):
        self.assertTrue(is_even(634))

    def test_six_hundred_and_thirty_five_is_even(self):
        self.assertTrue(not is_even(635))

    def test_six_hundred_and_thirty_six_is_even(self):
        self.assertTrue(is_even(636))

    def test_six_hundred_and_thirty_seven_is_even(self):
        self.assertTrue(not is_even(637))

    def test_six_hundred_and_thirty_eight_is_even(self):
        self.assertTrue(is_even(638))

    def test_six_hundred_and_thirty_nine_is_even(self):
        self.assertTrue(not is_even(639))

    def test_six_hundred_and_forty_is_even(self):
        self.assertTrue(is_even(640))

    def test_six_hundred_and_forty_one_is_even(self):
        self.assertTrue(not is_even(641))

    def test_six_hundred_and_forty_two_is_even(self):
        self.assertTrue(is_even(642))

    def test_six_hundred_and_forty_three_is_even(self):
        self.assertTrue(not is_even(643))

    def test_six_hundred_and_forty_four_is_even(self):
        self.assertTrue(is_even(644))

    def test_six_hundred_and_forty_five_is_even(self):
        self.assertTrue(not is_even(645))

    def test_six_hundred_and_forty_six_is_even(self):
        self.assertTrue(is_even(646))

    def test_six_hundred_and_forty_seven_is_even(self):
        self.assertTrue(not is_even(647))

    def test_six_hundred_and_forty_eight_is_even(self):
        self.assertTrue(is_even(648))

    def test_six_hundred_and_forty_nine_is_even(self):
        self.assertTrue(not is_even(649))

    def test_six_hundred_and_fifty_is_even(self):
        self.assertTrue(is_even(650))

    def test_six_hundred_and_fifty_one_is_even(self):
        self.assertTrue(not is_even(651))

    def test_six_hundred_and_fifty_two_is_even(self):
        self.assertTrue(is_even(652))

    def test_six_hundred_and_fifty_three_is_even(self):
        self.assertTrue(not is_even(653))

    def test_six_hundred_and_fifty_four_is_even(self):
        self.assertTrue(is_even(654))

    def test_six_hundred_and_fifty_five_is_even(self):
        self.assertTrue(not is_even(655))

    def test_six_hundred_and_fifty_six_is_even(self):
        self.assertTrue(is_even(656))

    def test_six_hundred_and_fifty_seven_is_even(self):
        self.assertTrue(not is_even(657))

    def test_six_hundred_and_fifty_eight_is_even(self):
        self.assertTrue(is_even(658))

    def test_six_hundred_and_fifty_nine_is_even(self):
        self.assertTrue(not is_even(659))

    def test_six_hundred_and_sixty_is_even(self):
        self.assertTrue(is_even(660))

    def test_six_hundred_and_sixty_one_is_even(self):
        self.assertTrue(not is_even(661))

    def test_six_hundred_and_sixty_two_is_even(self):
        self.assertTrue(is_even(662))

    def test_six_hundred_and_sixty_three_is_even(self):
        self.assertTrue(not is_even(663))

    def test_six_hundred_and_sixty_four_is_even(self):
        self.assertTrue(is_even(664))

    def test_six_hundred_and_sixty_five_is_even(self):
        self.assertTrue(not is_even(665))

    def test_six_hundred_and_sixty_six_is_even(self):
        self.assertTrue(is_even(666))

    def test_six_hundred_and_sixty_seven_is_even(self):
        self.assertTrue(not is_even(667))

    def test_six_hundred_and_sixty_eight_is_even(self):
        self.assertTrue(is_even(668))

    def test_six_hundred_and_sixty_nine_is_even(self):
        self.assertTrue(not is_even(669))

    def test_six_hundred_and_seventy_is_even(self):
        self.assertTrue(is_even(670))

    def test_six_hundred_and_seventy_one_is_even(self):
        self.assertTrue(not is_even(671))

    def test_six_hundred_and_seventy_two_is_even(self):
        self.assertTrue(is_even(672))

    def test_six_hundred_and_seventy_three_is_even(self):
        self.assertTrue(not is_even(673))

    def test_six_hundred_and_seventy_four_is_even(self):
        self.assertTrue(is_even(674))

    def test_six_hundred_and_seventy_five_is_even(self):
        self.assertTrue(not is_even(675))

    def test_six_hundred_and_seventy_six_is_even(self):
        self.assertTrue(is_even(676))

    def test_six_hundred_and_seventy_seven_is_even(self):
        self.assertTrue(not is_even(677))

    def test_six_hundred_and_seventy_eight_is_even(self):
        self.assertTrue(is_even(678))

    def test_six_hundred_and_seventy_nine_is_even(self):
        self.assertTrue(not is_even(679))

    def test_six_hundred_and_eighty_is_even(self):
        self.assertTrue(is_even(680))

    def test_six_hundred_and_eighty_one_is_even(self):
        self.assertTrue(not is_even(681))

    def test_six_hundred_and_eighty_two_is_even(self):
        self.assertTrue(is_even(682))

    def test_six_hundred_and_eighty_three_is_even(self):
        self.assertTrue(not is_even(683))

    def test_six_hundred_and_eighty_four_is_even(self):
        self.assertTrue(is_even(684))

    def test_six_hundred_and_eighty_five_is_even(self):
        self.assertTrue(not is_even(685))

    def test_six_hundred_and_eighty_six_is_even(self):
        self.assertTrue(is_even(686))

    def test_six_hundred_and_eighty_seven_is_even(self):
        self.assertTrue(not is_even(687))

    def test_six_hundred_and_eighty_eight_is_even(self):
        self.assertTrue(is_even(688))

    def test_six_hundred_and_eighty_nine_is_even(self):
        self.assertTrue(not is_even(689))

    def test_six_hundred_and_ninety_is_even(self):
        self.assertTrue(is_even(690))

    def test_six_hundred_and_ninety_one_is_even(self):
        self.assertTrue(not is_even(691))

    def test_six_hundred_and_ninety_two_is_even(self):
        self.assertTrue(is_even(692))

    def test_six_hundred_and_ninety_three_is_even(self):
        self.assertTrue(not is_even(693))

    def test_six_hundred_and_ninety_four_is_even(self):
        self.assertTrue(is_even(694))

    def test_six_hundred_and_ninety_five_is_even(self):
        self.assertTrue(not is_even(695))

    def test_six_hundred_and_ninety_six_is_even(self):
        self.assertTrue(is_even(696))

    def test_six_hundred_and_ninety_seven_is_even(self):
        self.assertTrue(not is_even(697))

    def test_six_hundred_and_ninety_eight_is_even(self):
        self.assertTrue(is_even(698))

    def test_six_hundred_and_ninety_nine_is_even(self):
        self.assertTrue(not is_even(699))

    def test_seven_hundred_is_even(self):
        self.assertTrue(is_even(700))

    def test_seven_hundred_and_one_is_even(self):
        self.assertTrue(not is_even(701))

    def test_seven_hundred_and_two_is_even(self):
        self.assertTrue(is_even(702))

    def test_seven_hundred_and_three_is_even(self):
        self.assertTrue(not is_even(703))

    def test_seven_hundred_and_four_is_even(self):
        self.assertTrue(is_even(704))

    def test_seven_hundred_and_five_is_even(self):
        self.assertTrue(not is_even(705))

    def test_seven_hundred_and_six_is_even(self):
        self.assertTrue(is_even(706))

    def test_seven_hundred_and_seven_is_even(self):
        self.assertTrue(not is_even(707))

    def test_seven_hundred_and_eight_is_even(self):
        self.assertTrue(is_even(708))

    def test_seven_hundred_and_nine_is_even(self):
        self.assertTrue(not is_even(709))

    def test_seven_hundred_and_ten_is_even(self):
        self.assertTrue(is_even(710))

    def test_seven_hundred_and_eleven_is_even(self):
        self.assertTrue(not is_even(711))

    def test_seven_hundred_and_twelve_is_even(self):
        self.assertTrue(is_even(712))

    def test_seven_hundred_and_thirteen_is_even(self):
        self.assertTrue(not is_even(713))

    def test_seven_hundred_and_fourteen_is_even(self):
        self.assertTrue(is_even(714))

    def test_seven_hundred_and_fifteen_is_even(self):
        self.assertTrue(not is_even(715))

    def test_seven_hundred_and_sixteen_is_even(self):
        self.assertTrue(is_even(716))

    def test_seven_hundred_and_seventeen_is_even(self):
        self.assertTrue(not is_even(717))

    def test_seven_hundred_and_eighteen_is_even(self):
        self.assertTrue(is_even(718))

    def test_seven_hundred_and_nineteen_is_even(self):
        self.assertTrue(not is_even(719))

    def test_seven_hundred_and_twenty_is_even(self):
        self.assertTrue(is_even(720))

    def test_seven_hundred_and_twenty_one_is_even(self):
        self.assertTrue(not is_even(721))

    def test_seven_hundred_and_twenty_two_is_even(self):
        self.assertTrue(is_even(722))

    def test_seven_hundred_and_twenty_three_is_even(self):
        self.assertTrue(not is_even(723))

    def test_seven_hundred_and_twenty_four_is_even(self):
        self.assertTrue(is_even(724))

    def test_seven_hundred_and_twenty_five_is_even(self):
        self.assertTrue(not is_even(725))

    def test_seven_hundred_and_twenty_six_is_even(self):
        self.assertTrue(is_even(726))

    def test_seven_hundred_and_twenty_seven_is_even(self):
        self.assertTrue(not is_even(727))

    def test_seven_hundred_and_twenty_eight_is_even(self):
        self.assertTrue(is_even(728))

    def test_seven_hundred_and_twenty_nine_is_even(self):
        self.assertTrue(not is_even(729))

    def test_seven_hundred_and_thirty_is_even(self):
        self.assertTrue(is_even(730))

    def test_seven_hundred_and_thirty_one_is_even(self):
        self.assertTrue(not is_even(731))

    def test_seven_hundred_and_thirty_two_is_even(self):
        self.assertTrue(is_even(732))

    def test_seven_hundred_and_thirty_three_is_even(self):
        self.assertTrue(not is_even(733))

    def test_seven_hundred_and_thirty_four_is_even(self):
        self.assertTrue(is_even(734))

    def test_seven_hundred_and_thirty_five_is_even(self):
        self.assertTrue(not is_even(735))

    def test_seven_hundred_and_thirty_six_is_even(self):
        self.assertTrue(is_even(736))

    def test_seven_hundred_and_thirty_seven_is_even(self):
        self.assertTrue(not is_even(737))

    def test_seven_hundred_and_thirty_eight_is_even(self):
        self.assertTrue(is_even(738))

    def test_seven_hundred_and_thirty_nine_is_even(self):
        self.assertTrue(not is_even(739))

    def test_seven_hundred_and_forty_is_even(self):
        self.assertTrue(is_even(740))

    def test_seven_hundred_and_forty_one_is_even(self):
        self.assertTrue(not is_even(741))

    def test_seven_hundred_and_forty_two_is_even(self):
        self.assertTrue(is_even(742))

    def test_seven_hundred_and_forty_three_is_even(self):
        self.assertTrue(not is_even(743))

    def test_seven_hundred_and_forty_four_is_even(self):
        self.assertTrue(is_even(744))

    def test_seven_hundred_and_forty_five_is_even(self):
        self.assertTrue(not is_even(745))

    def test_seven_hundred_and_forty_six_is_even(self):
        self.assertTrue(is_even(746))

    def test_seven_hundred_and_forty_seven_is_even(self):
        self.assertTrue(not is_even(747))

    def test_seven_hundred_and_forty_eight_is_even(self):
        self.assertTrue(is_even(748))

    def test_seven_hundred_and_forty_nine_is_even(self):
        self.assertTrue(not is_even(749))

    def test_seven_hundred_and_fifty_is_even(self):
        self.assertTrue(is_even(750))

    def test_seven_hundred_and_fifty_one_is_even(self):
        self.assertTrue(not is_even(751))

    def test_seven_hundred_and_fifty_two_is_even(self):
        self.assertTrue(is_even(752))

    def test_seven_hundred_and_fifty_three_is_even(self):
        self.assertTrue(not is_even(753))

    def test_seven_hundred_and_fifty_four_is_even(self):
        self.assertTrue(is_even(754))

    def test_seven_hundred_and_fifty_five_is_even(self):
        self.assertTrue(not is_even(755))

    def test_seven_hundred_and_fifty_six_is_even(self):
        self.assertTrue(is_even(756))

    def test_seven_hundred_and_fifty_seven_is_even(self):
        self.assertTrue(not is_even(757))

    def test_seven_hundred_and_fifty_eight_is_even(self):
        self.assertTrue(is_even(758))

    def test_seven_hundred_and_fifty_nine_is_even(self):
        self.assertTrue(not is_even(759))

    def test_seven_hundred_and_sixty_is_even(self):
        self.assertTrue(is_even(760))

    def test_seven_hundred_and_sixty_one_is_even(self):
        self.assertTrue(not is_even(761))

    def test_seven_hundred_and_sixty_two_is_even(self):
        self.assertTrue(is_even(762))

    def test_seven_hundred_and_sixty_three_is_even(self):
        self.assertTrue(not is_even(763))

    def test_seven_hundred_and_sixty_four_is_even(self):
        self.assertTrue(is_even(764))

    def test_seven_hundred_and_sixty_five_is_even(self):
        self.assertTrue(not is_even(765))

    def test_seven_hundred_and_sixty_six_is_even(self):
        self.assertTrue(is_even(766))

    def test_seven_hundred_and_sixty_seven_is_even(self):
        self.assertTrue(not is_even(767))

    def test_seven_hundred_and_sixty_eight_is_even(self):
        self.assertTrue(is_even(768))

    def test_seven_hundred_and_sixty_nine_is_even(self):
        self.assertTrue(not is_even(769))

    def test_seven_hundred_and_seventy_is_even(self):
        self.assertTrue(is_even(770))

    def test_seven_hundred_and_seventy_one_is_even(self):
        self.assertTrue(not is_even(771))

    def test_seven_hundred_and_seventy_two_is_even(self):
        self.assertTrue(is_even(772))

    def test_seven_hundred_and_seventy_three_is_even(self):
        self.assertTrue(not is_even(773))

    def test_seven_hundred_and_seventy_four_is_even(self):
        self.assertTrue(is_even(774))

    def test_seven_hundred_and_seventy_five_is_even(self):
        self.assertTrue(not is_even(775))

    def test_seven_hundred_and_seventy_six_is_even(self):
        self.assertTrue(is_even(776))

    def test_seven_hundred_and_seventy_seven_is_even(self):
        self.assertTrue(not is_even(777))

    def test_seven_hundred_and_seventy_eight_is_even(self):
        self.assertTrue(is_even(778))

    def test_seven_hundred_and_seventy_nine_is_even(self):
        self.assertTrue(not is_even(779))

    def test_seven_hundred_and_eighty_is_even(self):
        self.assertTrue(is_even(780))

    def test_seven_hundred_and_eighty_one_is_even(self):
        self.assertTrue(not is_even(781))

    def test_seven_hundred_and_eighty_two_is_even(self):
        self.assertTrue(is_even(782))

    def test_seven_hundred_and_eighty_three_is_even(self):
        self.assertTrue(not is_even(783))

    def test_seven_hundred_and_eighty_four_is_even(self):
        self.assertTrue(is_even(784))

    def test_seven_hundred_and_eighty_five_is_even(self):
        self.assertTrue(not is_even(785))

    def test_seven_hundred_and_eighty_six_is_even(self):
        self.assertTrue(is_even(786))

    def test_seven_hundred_and_eighty_seven_is_even(self):
        self.assertTrue(not is_even(787))

    def test_seven_hundred_and_eighty_eight_is_even(self):
        self.assertTrue(is_even(788))

    def test_seven_hundred_and_eighty_nine_is_even(self):
        self.assertTrue(not is_even(789))

    def test_seven_hundred_and_ninety_is_even(self):
        self.assertTrue(is_even(790))

    def test_seven_hundred_and_ninety_one_is_even(self):
        self.assertTrue(not is_even(791))

    def test_seven_hundred_and_ninety_two_is_even(self):
        self.assertTrue(is_even(792))

    def test_seven_hundred_and_ninety_three_is_even(self):
        self.assertTrue(not is_even(793))

    def test_seven_hundred_and_ninety_four_is_even(self):
        self.assertTrue(is_even(794))

    def test_seven_hundred_and_ninety_five_is_even(self):
        self.assertTrue(not is_even(795))

    def test_seven_hundred_and_ninety_six_is_even(self):
        self.assertTrue(is_even(796))

    def test_seven_hundred_and_ninety_seven_is_even(self):
        self.assertTrue(not is_even(797))

    def test_seven_hundred_and_ninety_eight_is_even(self):
        self.assertTrue(is_even(798))

    def test_seven_hundred_and_ninety_nine_is_even(self):
        self.assertTrue(not is_even(799))

    def test_eight_hundred_is_even(self):
        self.assertTrue(is_even(800))

    def test_eight_hundred_and_one_is_even(self):
        self.assertTrue(not is_even(801))

    def test_eight_hundred_and_two_is_even(self):
        self.assertTrue(is_even(802))

    def test_eight_hundred_and_three_is_even(self):
        self.assertTrue(not is_even(803))

    def test_eight_hundred_and_four_is_even(self):
        self.assertTrue(is_even(804))

    def test_eight_hundred_and_five_is_even(self):
        self.assertTrue(not is_even(805))

    def test_eight_hundred_and_six_is_even(self):
        self.assertTrue(is_even(806))

    def test_eight_hundred_and_seven_is_even(self):
        self.assertTrue(not is_even(807))

    def test_eight_hundred_and_eight_is_even(self):
        self.assertTrue(is_even(808))

    def test_eight_hundred_and_nine_is_even(self):
        self.assertTrue(not is_even(809))

    def test_eight_hundred_and_ten_is_even(self):
        self.assertTrue(is_even(810))

    def test_eight_hundred_and_eleven_is_even(self):
        self.assertTrue(not is_even(811))

    def test_eight_hundred_and_twelve_is_even(self):
        self.assertTrue(is_even(812))

    def test_eight_hundred_and_thirteen_is_even(self):
        self.assertTrue(not is_even(813))

    def test_eight_hundred_and_fourteen_is_even(self):
        self.assertTrue(is_even(814))

    def test_eight_hundred_and_fifteen_is_even(self):
        self.assertTrue(not is_even(815))

    def test_eight_hundred_and_sixteen_is_even(self):
        self.assertTrue(is_even(816))

    def test_eight_hundred_and_seventeen_is_even(self):
        self.assertTrue(not is_even(817))

    def test_eight_hundred_and_eighteen_is_even(self):
        self.assertTrue(is_even(818))

    def test_eight_hundred_and_nineteen_is_even(self):
        self.assertTrue(not is_even(819))

    def test_eight_hundred_and_twenty_is_even(self):
        self.assertTrue(is_even(820))

    def test_eight_hundred_and_twenty_one_is_even(self):
        self.assertTrue(not is_even(821))

    def test_eight_hundred_and_twenty_two_is_even(self):
        self.assertTrue(is_even(822))

    def test_eight_hundred_and_twenty_three_is_even(self):
        self.assertTrue(not is_even(823))

    def test_eight_hundred_and_twenty_four_is_even(self):
        self.assertTrue(is_even(824))

    def test_eight_hundred_and_twenty_five_is_even(self):
        self.assertTrue(not is_even(825))

    def test_eight_hundred_and_twenty_six_is_even(self):
        self.assertTrue(is_even(826))

    def test_eight_hundred_and_twenty_seven_is_even(self):
        self.assertTrue(not is_even(827))

    def test_eight_hundred_and_twenty_eight_is_even(self):
        self.assertTrue(is_even(828))

    def test_eight_hundred_and_twenty_nine_is_even(self):
        self.assertTrue(not is_even(829))

    def test_eight_hundred_and_thirty_is_even(self):
        self.assertTrue(is_even(830))

    def test_eight_hundred_and_thirty_one_is_even(self):
        self.assertTrue(not is_even(831))

    def test_eight_hundred_and_thirty_two_is_even(self):
        self.assertTrue(is_even(832))

    def test_eight_hundred_and_thirty_three_is_even(self):
        self.assertTrue(not is_even(833))

    def test_eight_hundred_and_thirty_four_is_even(self):
        self.assertTrue(is_even(834))

    def test_eight_hundred_and_thirty_five_is_even(self):
        self.assertTrue(not is_even(835))

    def test_eight_hundred_and_thirty_six_is_even(self):
        self.assertTrue(is_even(836))

    def test_eight_hundred_and_thirty_seven_is_even(self):
        self.assertTrue(not is_even(837))

    def test_eight_hundred_and_thirty_eight_is_even(self):
        self.assertTrue(is_even(838))

    def test_eight_hundred_and_thirty_nine_is_even(self):
        self.assertTrue(not is_even(839))

    def test_eight_hundred_and_forty_is_even(self):
        self.assertTrue(is_even(840))

    def test_eight_hundred_and_forty_one_is_even(self):
        self.assertTrue(not is_even(841))

    def test_eight_hundred_and_forty_two_is_even(self):
        self.assertTrue(is_even(842))

    def test_eight_hundred_and_forty_three_is_even(self):
        self.assertTrue(not is_even(843))

    def test_eight_hundred_and_forty_four_is_even(self):
        self.assertTrue(is_even(844))

    def test_eight_hundred_and_forty_five_is_even(self):
        self.assertTrue(not is_even(845))

    def test_eight_hundred_and_forty_six_is_even(self):
        self.assertTrue(is_even(846))

    def test_eight_hundred_and_forty_seven_is_even(self):
        self.assertTrue(not is_even(847))

    def test_eight_hundred_and_forty_eight_is_even(self):
        self.assertTrue(is_even(848))

    def test_eight_hundred_and_forty_nine_is_even(self):
        self.assertTrue(not is_even(849))

    def test_eight_hundred_and_fifty_is_even(self):
        self.assertTrue(is_even(850))

    def test_eight_hundred_and_fifty_one_is_even(self):
        self.assertTrue(not is_even(851))

    def test_eight_hundred_and_fifty_two_is_even(self):
        self.assertTrue(is_even(852))

    def test_eight_hundred_and_fifty_three_is_even(self):
        self.assertTrue(not is_even(853))

    def test_eight_hundred_and_fifty_four_is_even(self):
        self.assertTrue(is_even(854))

    def test_eight_hundred_and_fifty_five_is_even(self):
        self.assertTrue(not is_even(855))

    def test_eight_hundred_and_fifty_six_is_even(self):
        self.assertTrue(is_even(856))

    def test_eight_hundred_and_fifty_seven_is_even(self):
        self.assertTrue(not is_even(857))

    def test_eight_hundred_and_fifty_eight_is_even(self):
        self.assertTrue(is_even(858))

    def test_eight_hundred_and_fifty_nine_is_even(self):
        self.assertTrue(not is_even(859))

    def test_eight_hundred_and_sixty_is_even(self):
        self.assertTrue(is_even(860))

    def test_eight_hundred_and_sixty_one_is_even(self):
        self.assertTrue(not is_even(861))

    def test_eight_hundred_and_sixty_two_is_even(self):
        self.assertTrue(is_even(862))

    def test_eight_hundred_and_sixty_three_is_even(self):
        self.assertTrue(not is_even(863))

    def test_eight_hundred_and_sixty_four_is_even(self):
        self.assertTrue(is_even(864))

    def test_eight_hundred_and_sixty_five_is_even(self):
        self.assertTrue(not is_even(865))

    def test_eight_hundred_and_sixty_six_is_even(self):
        self.assertTrue(is_even(866))

    def test_eight_hundred_and_sixty_seven_is_even(self):
        self.assertTrue(not is_even(867))

    def test_eight_hundred_and_sixty_eight_is_even(self):
        self.assertTrue(is_even(868))

    def test_eight_hundred_and_sixty_nine_is_even(self):
        self.assertTrue(not is_even(869))

    def test_eight_hundred_and_seventy_is_even(self):
        self.assertTrue(is_even(870))

    def test_eight_hundred_and_seventy_one_is_even(self):
        self.assertTrue(not is_even(871))

    def test_eight_hundred_and_seventy_two_is_even(self):
        self.assertTrue(is_even(872))

    def test_eight_hundred_and_seventy_three_is_even(self):
        self.assertTrue(not is_even(873))

    def test_eight_hundred_and_seventy_four_is_even(self):
        self.assertTrue(is_even(874))

    def test_eight_hundred_and_seventy_five_is_even(self):
        self.assertTrue(not is_even(875))

    def test_eight_hundred_and_seventy_six_is_even(self):
        self.assertTrue(is_even(876))

    def test_eight_hundred_and_seventy_seven_is_even(self):
        self.assertTrue(not is_even(877))

    def test_eight_hundred_and_seventy_eight_is_even(self):
        self.assertTrue(is_even(878))

    def test_eight_hundred_and_seventy_nine_is_even(self):
        self.assertTrue(not is_even(879))

    def test_eight_hundred_and_eighty_is_even(self):
        self.assertTrue(is_even(880))

    def test_eight_hundred_and_eighty_one_is_even(self):
        self.assertTrue(not is_even(881))

    def test_eight_hundred_and_eighty_two_is_even(self):
        self.assertTrue(is_even(882))

    def test_eight_hundred_and_eighty_three_is_even(self):
        self.assertTrue(not is_even(883))

    def test_eight_hundred_and_eighty_four_is_even(self):
        self.assertTrue(is_even(884))

    def test_eight_hundred_and_eighty_five_is_even(self):
        self.assertTrue(not is_even(885))

    def test_eight_hundred_and_eighty_six_is_even(self):
        self.assertTrue(is_even(886))

    def test_eight_hundred_and_eighty_seven_is_even(self):
        self.assertTrue(not is_even(887))

    def test_eight_hundred_and_eighty_eight_is_even(self):
        self.assertTrue(is_even(888))

    def test_eight_hundred_and_eighty_nine_is_even(self):
        self.assertTrue(not is_even(889))

    def test_eight_hundred_and_ninety_is_even(self):
        self.assertTrue(is_even(890))

    def test_eight_hundred_and_ninety_one_is_even(self):
        self.assertTrue(not is_even(891))

    def test_eight_hundred_and_ninety_two_is_even(self):
        self.assertTrue(is_even(892))

    def test_eight_hundred_and_ninety_three_is_even(self):
        self.assertTrue(not is_even(893))

    def test_eight_hundred_and_ninety_four_is_even(self):
        self.assertTrue(is_even(894))

    def test_eight_hundred_and_ninety_five_is_even(self):
        self.assertTrue(not is_even(895))

    def test_eight_hundred_and_ninety_six_is_even(self):
        self.assertTrue(is_even(896))

    def test_eight_hundred_and_ninety_seven_is_even(self):
        self.assertTrue(not is_even(897))

    def test_eight_hundred_and_ninety_eight_is_even(self):
        self.assertTrue(is_even(898))

    def test_eight_hundred_and_ninety_nine_is_even(self):
        self.assertTrue(not is_even(899))

    def test_nine_hundred_is_even(self):
        self.assertTrue(is_even(900))

    def test_nine_hundred_and_one_is_even(self):
        self.assertTrue(not is_even(901))

    def test_nine_hundred_and_two_is_even(self):
        self.assertTrue(is_even(902))

    def test_nine_hundred_and_three_is_even(self):
        self.assertTrue(not is_even(903))

    def test_nine_hundred_and_four_is_even(self):
        self.assertTrue(is_even(904))

    def test_nine_hundred_and_five_is_even(self):
        self.assertTrue(not is_even(905))

    def test_nine_hundred_and_six_is_even(self):
        self.assertTrue(is_even(906))

    def test_nine_hundred_and_seven_is_even(self):
        self.assertTrue(not is_even(907))

    def test_nine_hundred_and_eight_is_even(self):
        self.assertTrue(is_even(908))

    def test_nine_hundred_and_nine_is_even(self):
        self.assertTrue(not is_even(909))

    def test_nine_hundred_and_ten_is_even(self):
        self.assertTrue(is_even(910))

    def test_nine_hundred_and_eleven_is_even(self):
        self.assertTrue(not is_even(911))

    def test_nine_hundred_and_twelve_is_even(self):
        self.assertTrue(is_even(912))

    def test_nine_hundred_and_thirteen_is_even(self):
        self.assertTrue(not is_even(913))

    def test_nine_hundred_and_fourteen_is_even(self):
        self.assertTrue(is_even(914))

    def test_nine_hundred_and_fifteen_is_even(self):
        self.assertTrue(not is_even(915))

    def test_nine_hundred_and_sixteen_is_even(self):
        self.assertTrue(is_even(916))

    def test_nine_hundred_and_seventeen_is_even(self):
        self.assertTrue(not is_even(917))

    def test_nine_hundred_and_eighteen_is_even(self):
        self.assertTrue(is_even(918))

    def test_nine_hundred_and_nineteen_is_even(self):
        self.assertTrue(not is_even(919))

    def test_nine_hundred_and_twenty_is_even(self):
        self.assertTrue(is_even(920))

    def test_nine_hundred_and_twenty_one_is_even(self):
        self.assertTrue(not is_even(921))

    def test_nine_hundred_and_twenty_two_is_even(self):
        self.assertTrue(is_even(922))

    def test_nine_hundred_and_twenty_three_is_even(self):
        self.assertTrue(not is_even(923))

    def test_nine_hundred_and_twenty_four_is_even(self):
        self.assertTrue(is_even(924))

    def test_nine_hundred_and_twenty_five_is_even(self):
        self.assertTrue(not is_even(925))

    def test_nine_hundred_and_twenty_six_is_even(self):
        self.assertTrue(is_even(926))

    def test_nine_hundred_and_twenty_seven_is_even(self):
        self.assertTrue(not is_even(927))

    def test_nine_hundred_and_twenty_eight_is_even(self):
        self.assertTrue(is_even(928))

    def test_nine_hundred_and_twenty_nine_is_even(self):
        self.assertTrue(not is_even(929))

    def test_nine_hundred_and_thirty_is_even(self):
        self.assertTrue(is_even(930))

    def test_nine_hundred_and_thirty_one_is_even(self):
        self.assertTrue(not is_even(931))

    def test_nine_hundred_and_thirty_two_is_even(self):
        self.assertTrue(is_even(932))

    def test_nine_hundred_and_thirty_three_is_even(self):
        self.assertTrue(not is_even(933))

    def test_nine_hundred_and_thirty_four_is_even(self):
        self.assertTrue(is_even(934))

    def test_nine_hundred_and_thirty_five_is_even(self):
        self.assertTrue(not is_even(935))

    def test_nine_hundred_and_thirty_six_is_even(self):
        self.assertTrue(is_even(936))

    def test_nine_hundred_and_thirty_seven_is_even(self):
        self.assertTrue(not is_even(937))

    def test_nine_hundred_and_thirty_eight_is_even(self):
        self.assertTrue(is_even(938))

    def test_nine_hundred_and_thirty_nine_is_even(self):
        self.assertTrue(not is_even(939))

    def test_nine_hundred_and_forty_is_even(self):
        self.assertTrue(is_even(940))

    def test_nine_hundred_and_forty_one_is_even(self):
        self.assertTrue(not is_even(941))

    def test_nine_hundred_and_forty_two_is_even(self):
        self.assertTrue(is_even(942))

    def test_nine_hundred_and_forty_three_is_even(self):
        self.assertTrue(not is_even(943))

    def test_nine_hundred_and_forty_four_is_even(self):
        self.assertTrue(is_even(944))

    def test_nine_hundred_and_forty_five_is_even(self):
        self.assertTrue(not is_even(945))

    def test_nine_hundred_and_forty_six_is_even(self):
        self.assertTrue(is_even(946))

    def test_nine_hundred_and_forty_seven_is_even(self):
        self.assertTrue(not is_even(947))

    def test_nine_hundred_and_forty_eight_is_even(self):
        self.assertTrue(is_even(948))

    def test_nine_hundred_and_forty_nine_is_even(self):
        self.assertTrue(not is_even(949))

    def test_nine_hundred_and_fifty_is_even(self):
        self.assertTrue(is_even(950))

    def test_nine_hundred_and_fifty_one_is_even(self):
        self.assertTrue(not is_even(951))

    def test_nine_hundred_and_fifty_two_is_even(self):
        self.assertTrue(is_even(952))

    def test_nine_hundred_and_fifty_three_is_even(self):
        self.assertTrue(not is_even(953))

    def test_nine_hundred_and_fifty_four_is_even(self):
        self.assertTrue(is_even(954))

    def test_nine_hundred_and_fifty_five_is_even(self):
        self.assertTrue(not is_even(955))

    def test_nine_hundred_and_fifty_six_is_even(self):
        self.assertTrue(is_even(956))

    def test_nine_hundred_and_fifty_seven_is_even(self):
        self.assertTrue(not is_even(957))

    def test_nine_hundred_and_fifty_eight_is_even(self):
        self.assertTrue(is_even(958))

    def test_nine_hundred_and_fifty_nine_is_even(self):
        self.assertTrue(not is_even(959))

    def test_nine_hundred_and_sixty_is_even(self):
        self.assertTrue(is_even(960))

    def test_nine_hundred_and_sixty_one_is_even(self):
        self.assertTrue(not is_even(961))

    def test_nine_hundred_and_sixty_two_is_even(self):
        self.assertTrue(is_even(962))

    def test_nine_hundred_and_sixty_three_is_even(self):
        self.assertTrue(not is_even(963))

    def test_nine_hundred_and_sixty_four_is_even(self):
        self.assertTrue(is_even(964))

    def test_nine_hundred_and_sixty_five_is_even(self):
        self.assertTrue(not is_even(965))

    def test_nine_hundred_and_sixty_six_is_even(self):
        self.assertTrue(is_even(966))

    def test_nine_hundred_and_sixty_seven_is_even(self):
        self.assertTrue(not is_even(967))

    def test_nine_hundred_and_sixty_eight_is_even(self):
        self.assertTrue(is_even(968))

    def test_nine_hundred_and_sixty_nine_is_even(self):
        self.assertTrue(not is_even(969))

    def test_nine_hundred_and_seventy_is_even(self):
        self.assertTrue(is_even(970))

    def test_nine_hundred_and_seventy_one_is_even(self):
        self.assertTrue(not is_even(971))

    def test_nine_hundred_and_seventy_two_is_even(self):
        self.assertTrue(is_even(972))

    def test_nine_hundred_and_seventy_three_is_even(self):
        self.assertTrue(not is_even(973))

    def test_nine_hundred_and_seventy_four_is_even(self):
        self.assertTrue(is_even(974))

    def test_nine_hundred_and_seventy_five_is_even(self):
        self.assertTrue(not is_even(975))

    def test_nine_hundred_and_seventy_six_is_even(self):
        self.assertTrue(is_even(976))

    def test_nine_hundred_and_seventy_seven_is_even(self):
        self.assertTrue(not is_even(977))

    def test_nine_hundred_and_seventy_eight_is_even(self):
        self.assertTrue(is_even(978))

    def test_nine_hundred_and_seventy_nine_is_even(self):
        self.assertTrue(not is_even(979))

    def test_nine_hundred_and_eighty_is_even(self):
        self.assertTrue(is_even(980))

    def test_nine_hundred_and_eighty_one_is_even(self):
        self.assertTrue(not is_even(981))

    def test_nine_hundred_and_eighty_two_is_even(self):
        self.assertTrue(is_even(982))

    def test_nine_hundred_and_eighty_three_is_even(self):
        self.assertTrue(not is_even(983))

    def test_nine_hundred_and_eighty_four_is_even(self):
        self.assertTrue(is_even(984))

    def test_nine_hundred_and_eighty_five_is_even(self):
        self.assertTrue(not is_even(985))

    def test_nine_hundred_and_eighty_six_is_even(self):
        self.assertTrue(is_even(986))

    def test_nine_hundred_and_eighty_seven_is_even(self):
        self.assertTrue(not is_even(987))

    def test_nine_hundred_and_eighty_eight_is_even(self):
        self.assertTrue(is_even(988))

    def test_nine_hundred_and_eighty_nine_is_even(self):
        self.assertTrue(not is_even(989))

    def test_nine_hundred_and_ninety_is_even(self):
        self.assertTrue(is_even(990))

    def test_nine_hundred_and_ninety_one_is_even(self):
        self.assertTrue(not is_even(991))

    def test_nine_hundred_and_ninety_two_is_even(self):
        self.assertTrue(is_even(992))

    def test_nine_hundred_and_ninety_three_is_even(self):
        self.assertTrue(not is_even(993))

    def test_nine_hundred_and_ninety_four_is_even(self):
        self.assertTrue(is_even(994))

    def test_nine_hundred_and_ninety_five_is_even(self):
        self.assertTrue(not is_even(995))

    def test_nine_hundred_and_ninety_six_is_even(self):
        self.assertTrue(is_even(996))

    def test_nine_hundred_and_ninety_seven_is_even(self):
        self.assertTrue(not is_even(997))

    def test_nine_hundred_and_ninety_eight_is_even(self):
        self.assertTrue(is_even(998))

    def test_nine_hundred_and_ninety_nine_is_even(self):
        self.assertTrue(not is_even(999))

    def test_one_thousand_is_even(self):
        self.assertTrue(is_even(1000))
