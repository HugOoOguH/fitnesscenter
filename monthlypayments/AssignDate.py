#librerias que son necesarias
from datetime import datetime, date, time, timedelta
import calendar


class AssignDate(object):
	
	def __init__(self, fecha):
		self.fecha = fecha


	def asignar_fecha(self):
		if self.fecha.month == 12:

			if self.fecha.day == 31:

				day = 1
				month = 2
				year = self.fecha.year + 1
				self.fecha = self.fecha.replace(year, month, day)
				# return self.fecha

			else:

				month = 1
				year = self.fecha.year + 1
				self.fecha = self.fecha.replace(year, month, self.fecha.day)
				# return self.fecha

		elif self.fecha.day == 31:
			month = self.fecha.month + 2
			day = 1
			self.fecha = self.fecha.replace(self.fecha.year, month, day)
			# return self.fecha

		elif self.fecha.month == 1 and self.fecha.day > 28:

			if self.fecha.day == 29:

				if (self.fecha.year % 4 == 0 and ((self.fecha.year % 100 != 0) or (self.fecha.year % 400 == 0))):

					month = self.fecha.month + 1
					self.fecha = self.fecha.replace(self.fecha.year, month, self.fecha.day)
					# return self.fecha

				else:

					day = 1
					month = self.fecha.month + 2
					self.fecha = self.fecha.replace(self.fecha.year, month, day)
					# return self.fecha

			elif self.fecha.day == 30:
				# if self.fecha.day == 30:
				month = self.fecha.month + 2
				day = 1
				self.fecha = self.fecha.replace(self.fecha.year, month, day)
				# return self.fecha

		else:

			month = self.fecha.month + 1
			self.fecha = self.fecha.replace(self.fecha.year, month, self.fecha.day)
			# return self.fecha