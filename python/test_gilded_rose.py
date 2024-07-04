# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
	def test_basic_add(self):
		items = [Item("foo", 0, 0)]
		gilded_rose = GildedRose(items)
		gilded_rose.update_quality()
		self.assertEqual("foo", items[0].name)

	def test_items_correctly_added(self):
		items = [Item("foo", 0, 0), Item("bar", 0, 0),
				 Item("fizz", 0, 0), Item("buzz", 0, 0),
				 Item("bing", 0, 0), Item("bang", 0, 0),
				 Item("bong", 0, 0)]
		gilded_rose = GildedRose(items)
		gilded_rose.update_quality()
		self.assertEqual("foo", items[0].name)
		self.assertEqual("bar", items[1].name)
		self.assertEqual("fizz", items[2].name)
		self.assertEqual("buzz", items[3].name)
		self.assertEqual("bing", items[4].name)
		self.assertEqual("bang", items[5].name)
		self.assertEqual("bong", items[6].name)

	def test_a_lot_of_items_correctly_added(self):
		items = []
		for i in range(10000):
			items.append(Item(str(i), 0, 0))
		gilded_rose = GildedRose(items)
		gilded_rose.update_quality()
		for i in range(10000):
			self.assertEqual(str(i), items[i].name)

	def test_update_quality_once(self):
		items = [Item("Aged Brie", 100, 30),
				 Item("Sulfuras, Hand of Ragnaros", 30, 80), Item("Chips", 5, 10),
				 Item("Elixir of the Mongoose", 0, 10)]
		gilded_rose = GildedRose(items)
		gilded_rose.update_quality()
		self.assertEqual("Aged Brie", items[0].name)
		self.assertEqual(99, items[0].sell_in)
		self.assertEqual(31, items[0].quality)
		self.assertEqual("Sulfuras, Hand of Ragnaros", items[1].name)
		self.assertEqual(30, items[1].sell_in)
		self.assertEqual(80, items[1].quality)
		self.assertEqual("Chips", items[2].name)
		self.assertEqual(4, items[2].sell_in)
		self.assertEqual(9, items[2].quality)
		self.assertEqual("Elixir of the Mongoose", items[3].name)
		self.assertEqual(0, items[3].sell_in)
		self.assertEqual(8, items[3].quality)

	def test_update_quality_multiple(self):
		items = [Item("Aged Brie", 100, 30),
				 Item("Sulfuras, Hand of Ragnaros", 30, 80), Item("Chips", 5, 10)]
		gilded_rose = GildedRose(items)
		for i in range(10):
			gilded_rose.update_quality()
		self.assertEqual("Aged Brie", items[0].name)
		self.assertEqual(90, items[0].sell_in)
		self.assertEqual(40, items[0].quality)
		self.assertEqual("Sulfuras, Hand of Ragnaros", items[1].name)
		self.assertEqual(30, items[1].sell_in)
		self.assertEqual(80, items[1].quality)
		self.assertEqual("Chips", items[2].name)
		self.assertEqual(0, items[2].sell_in)
		self.assertEqual(0, items[2].quality)

	def test_quality_upper_limit(self):
		items = [Item("Aged Brie", 100, 30),
				 Item("Backstage passes to a TAFKAL80ETC concert", 100, 10)]
		gilded_rose = GildedRose(items)
		for i in range(50):
			gilded_rose.update_quality()
		self.assertEqual("Aged Brie", items[0].name)
		self.assertEqual(50, items[0].sell_in)
		self.assertEqual(50, items[0].quality)
		self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[1].name)
		self.assertEqual(50, items[1].sell_in)
		self.assertEqual(50, items[1].quality)

	def test_quality_lower_limit(self):
		items = [Item("Elixir of the Mongoose", 5, 10)]
		gilded_rose = GildedRose(items)
		for i in range(50):
			gilded_rose.update_quality()
		self.assertEqual("Elixir of the Mongoose", items[0].name)
		self.assertEqual(0, items[0].sell_in)
		self.assertEqual(0, items[0].quality)

	def test_quality_expired(self):
		items = [Item("Elixir of the Mongoose", 5, 50)]
		gilded_rose = GildedRose(items)
		for i in range(15):
			gilded_rose.update_quality()
		self.assertEqual("Elixir of the Mongoose", items[0].name)
		self.assertEqual(0, items[0].sell_in)
		self.assertEqual(25, items[0].quality)

	def test_backstage_pass(self):
		items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 10),
				 Item("Backstage passes to a Eminem concert", 11, 10),
				 Item("Backstage passes to a Kendrick Lamar concert", 11, 10), ]
		gilded_rose = GildedRose(items)
		for i in range(10):
			gilded_rose.update_quality()
		self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
		self.assertEqual(1, items[0].sell_in)
		self.assertEqual(33, items[0].quality)
		self.assertEqual("Backstage passes to a Eminem concert", items[1].name)
		self.assertEqual(1, items[1].sell_in)
		self.assertEqual(33, items[1].quality)
		self.assertEqual("Backstage passes to a Kendrick Lamar concert", items[2].name)
		self.assertEqual(1, items[2].sell_in)
		self.assertEqual(33, items[2].quality)

	def test_backstage_pass_increase(self):
		items = [Item("Backstage passes to a TAFKAL80ETC concert", 26, 10),
				 Item("Backstage passes to a TAFKAL80ETC concert", 16, 10),
				 Item("Backstage passes to a TAFKAL80ETC concert", 11, 10),
				 Item("Backstage passes to a TAFKAL80ETC concert", 10, 10),
				 Item("Backstage passes to a TAFKAL80ETC concert", 9, 10)]
		gilded_rose = GildedRose(items)
		for i in range(10):
			gilded_rose.update_quality()
		self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
		self.assertEqual(16, items[0].sell_in)
		self.assertEqual(20, items[0].quality)
		self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[1].name)
		self.assertEqual(6, items[1].sell_in)
		self.assertEqual(24, items[1].quality)
		self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[2].name)
		self.assertEqual(1, items[2].sell_in)
		self.assertEqual(33, items[2].quality)
		self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[3].name)
		self.assertEqual(0, items[3].sell_in)
		self.assertEqual(35, items[3].quality)
		self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[4].name)
		self.assertEqual(0, items[4].sell_in)
		self.assertEqual(0, items[4].quality)

	def test_conjured_items(self):
		items = [Item("Conjured Mana Cake", 10, 40),
				 Item("Conjured Mana Cake", 0, 40)]
		gilded_rose = GildedRose(items)
		for i in range(5):
			gilded_rose.update_quality()
		self.assertEqual("Conjured Mana Cake", items[0].name)
		self.assertEqual(5, items[0].sell_in)
		self.assertEqual(30, items[0].quality)
		self.assertEqual("Conjured Mana Cake", items[1].name)
		self.assertEqual(0, items[1].sell_in)
		self.assertEqual(20, items[1].quality)


if __name__ == '__main__':
	unittest.main()
