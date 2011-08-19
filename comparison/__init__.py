# -*- coding: utf-8 -*-
""" Нечеткий поиск названии фильмов в заголовках интернет страниц """
import trans
import jellyfish
import re

# pylint: disable=R0201,R0903


class Comparison(object):
    """Класс нечеткого сравнения"""
    def _trans(self, name):
        """Транслитерация строки"""
        name = name.replace(u'ё', u'е')
        return trans.trans(name)[0].replace(u'_', '')

    def _split_words(self, old_sort_list):
        """Разбиение строки"""
        return re.sub('[^\w]', ' ', old_sort_list).split()

    def _comparison(self, namelist, sitelist):
        """Подсчет коэффиецента близости строк"""
        total_i = 0
        for name in namelist:
            i = 0
            for site in sitelist:
                dist = jellyfish.jaro_distance(name, site)
                i = max(i, dist)
            total_i += i
        return total_i

    def match(self, name, title):
        """Подсчет вероятности вхождения одной строки в другую"""
        name = self._trans(name.lower())
        title = self._trans(title.lower())
        namelist = self._split_words(name)
        titlelist = self._split_words(title)
        percent = self._comparison(namelist, titlelist)
        return percent / len(name)
