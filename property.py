#!/usr/bin/env python3
# -*- coding: utf-8 -*-



class ClassName(object):

	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, value):
		self._birth = value