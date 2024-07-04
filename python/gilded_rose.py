# -*- coding: utf-8 -*-

class GildedRose(object):

	def __init__(self, items):
		self.items = items

	def update_item_sell_in(self, item):
		if item.name != "Sulfuras, Hand of Ragnaros":
			item.sell_in -= 1

		# Makes sure sell_in doesn't drop under 0
		item.sell_in = max(0, item.sell_in)

	def update_quality_aged_brie(self, item):
		# Makes sure quality doesn't rise over 50
		item.quality = min(50, item.quality + 1)

	def update_quality_sulfuras(self, item):
		# Sulfuras, Hand of Ragnaros is a legendary item so it's quality doesn't change
		return

	def update_quality_backstage_pass(self, item):
		if item.sell_in > 10:
			item.quality += 1
		elif item.sell_in > 5:
			item.quality += 2
		elif item.sell_in > 0:
			item.quality += 3
		else:
			item.quality = 0

		# Makes sure quality doesn't rise over 50
		item.quality = min(50, item.quality)

	def update_quality_conjured(self, item):
		if item.sell_in > 0:
			item.quality -= 2
		else:
			item.quality -= 4

		# Makes sure quality doesn't drop under 0
		item.quality = max(0, item.quality)

	def update_quality_normal(self, item):
		if item.sell_in > 0:
			item.quality -= 1
		else:
			item.quality -= 2

		# Makes sure quality doesn't drop under 0
		item.quality = max(0, item.quality)

	def update_item_quality(self, item):
		match item.name:
			case "Sulfuras, Hand of Ragnaros":
				self.update_quality_sulfuras(item)
				return
			case "Aged Brie":
				self.update_quality_aged_brie(item)
				return

		if str(item.name).startswith("Backstage passes"):
			self.update_quality_backstage_pass(item)
		elif str(item.name).startswith("Conjured"):
			self.update_quality_conjured(item)
		else:
			self.update_quality_normal(item)

	def update_quality(self):
		for item in self.items:
			self.update_item_quality(item)
			self.update_item_sell_in(item)


class Item:
	def __init__(self, name, sell_in, quality):
		self.name = name
		self.sell_in = sell_in
		self.quality = quality

	def __repr__(self):
		return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
