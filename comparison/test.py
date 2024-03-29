# -*- coding: utf-8 -*-
"""Тест нечеткого поиска"""
from unittest import TestCase, main
from comparison import Comparison

# pylint: disable=C0301


class ComparisonTestCase(TestCase):
    "Класс для тестирования нечетких сравнений"

    def test_match(self):
        """Тест1"""
        data = [
            (u'все включено',
             u'скачать все включено сейчас',
             1.0),
            (u'все включено',
             u'All inclusive, или Всё включено',
             1.0),
            (u'все включено',
             u'All inclusive, или Всё включено (2011) &raquo; Новое Кино\
              смотреть онлайн скачать бесплатно', 1.0),
            (u'все включено', u'мотреть фильм Все включено онлайн бесплатно\
             без регистрации', 1.0),
            (u'все включено', u'All inclusive или Все включено (2011). Фильм.', 1.0),
            (u'все включено', u'Все включено&#33; (2011) - All inclusive или Все включено&#33; - информация о фильме -  российские фильмы и сериалы - Кино-Театр.РУ', 1.0),
            (u'все включено', u'ВСЕ ВКЛЮЧЕНО 2011 &raquo; СМОТРЕТЬ ОНЛАЙН БЕСПЛАТНО', 1.0),
            (u'все включено', u'Фильм All inclusive, или Всё включено смотреть онлайн бесплатно в хорошем качестве', 1.0),
            (u'все включено', u'Все включено Онлайн фильм, Смотреть фильмы онлайн бесплатно, Кино онлайн', 1.0),
            (u'все включено', u'Смотреть онлайн All inclusive, или Всё включено | Комедии | Фильм All inclusive, или Всё включено смотреть бесплатно на Films-Online-net.ru', 1.0),
            (u'все включено', u'Фильм «Все включено»,  Эдуард Радзюкевич,  Михаил Беспало', 1.0),
            (u'все включено', u'Фильм All inclusive, или Всё включено отзывы и рецензия', 1.0),
            (u'все включено', u'ильм All inclusive, или Всё включено смотреть онлайн бесплатно в хорошем hd качестве', 1.0)
        ]
        comparison = Comparison()
        for entry in data:
            val = comparison.match(entry[0], entry[1])
            print entry[0], entry[1], val
            self.assertTrue(val >= entry[2])

    def test_match2(self):
        """Тест2"""
        data = [
            (u'восемь с половиной долларов', u'скачать все включено сейчас', 0.75),
            (u'восемь с половиной долларов', u'All inclusive, или Всё включено', 0.75),
            (u'восемь с половиной долларов', u'All inclusive, или Всё включено (2011) &raquo; Новое Кино смотреть онлайн скачать бесплатно', 0.75),
            (u'восемь с половиной долларов', u'мотреть фильм Все включено онлайн бесплатно без регистрации', 0.75),
            (u'восемь с половиной долларов', u'All inclusive или Все включено (2011). Фильм.', 0.75),
            (u'восемь с половиной долларов', u'Все включено&#33; (2011) - All inclusive или Все включено&#33; - информация о фильме -  российские фильмы и сериалы - Кино-Театр.РУ', 0.75),
            (u'восемь с половиной долларов', u'ВСЕ ВКЛЮЧЕНО 2011 &raquo; СМОТРЕТЬ ОНЛАЙН БЕСПЛАТНО', 0.75),
            (u'восемь с половиной долларов', u'Фильм All inclusive, или Всё включено смотреть онлайн бесплатно в хорошем качестве', 0.75),
            (u'восемь с половиной долларов', u'Все включено Онлайн фильм, Смотреть фильмы онлайн бесплатно, Кино онлайн', 0.75),
            (u'восемь с половиной долларов', u'Смотреть онлайн All inclusive, или Всё включено | Комедии | Фильм All inclusive, или Всё включено смотреть бесплатно на Films-Online-net.ru', 0.75),
            (u'восемь с половиной долларов', u'Фильм «Все включено»,  Эдуард Радзюкевич,  Михаил Беспало', 0.75),
            (u'восемь с половиной долларов', u'Фильм All inclusive, или Всё включено отзывы и рецензия', 0.75),
            (u'восемь с половиной долларов', u'ильм All inclusive, или Всё включено смотреть онлайн бесплатно в хорошем hd качестве', 0.75)
        ]
        comparison = Comparison()
        for entry in data:
            val = comparison.match(entry[0], entry[1])
            print entry[0], entry[1], val
            self.assertTrue(val <= entry[2])

    def test_match3(self):
        """Тест3"""
        test = 0.9
        data = [
            (u'восемь франков', u'скачать все включено сейчас', test),
            (u'восемь франков', u'All inclusive, или Всё включено', test),
            (u'восемь франков', u'All inclusive, или Всё включено (2011) &raquo; Новое Кино смотреть онлайн скачать бесплатно', test),
            (u'восемь франков', u'мотреть фильм Все включено онлайн бесплатно без регистрации', test),
            (u'восемь франков', u'All inclusive или Все включено (2011). Фильм.', test),
            (u'восемь франков', u'Все включено&#33; (2011) - All inclusive или Все включено&#33; - информация о фильме -  российские фильмы и сериалы - Кино-Театр.РУ', test),
            (u'восемь франков', u'ВСЕ ВКЛЮЧЕНО 2011 &raquo; СМОТРЕТЬ ОНЛАЙН БЕСПЛАТНО', test),
            (u'восемь франков', u'Фильм All inclusive, или Всё включено смотреть онлайн бесплатно в хорошем качестве', test),
            (u'восемь франков', u'Все включено Онлайн фильм, Смотреть фильмы онлайн бесплатно, Кино онлайн', test),
            (u'восемь франков', u'Смотреть онлайн All inclusive, или Всё включено | Комедии | Фильм All inclusive, или Всё включено смотреть бесплатно на Films-Online-net.ru', test),
            (u'восемь франков', u'Фильм «Все включено»,  Эдуард Радзюкевич,  Михаил Беспало', test),
            (u'восемь франков', u'Фильм All inclusive, или Всё включено отзывы и рецензия', test),
            (u'восемь франков', u'ильм All inclusive, или Всё включено смотреть онлайн бесплатно в хорошем hd качестве', test)
        ]
        comparison = Comparison()
        for entry in data:
            val = comparison.match(entry[0], entry[1])
            print entry[0], entry[1], val
            self.assertTrue(val <= entry[2])

if __name__ == '__main__':
    main()
