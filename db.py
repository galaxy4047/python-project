import sqlite3 


class sequel:
	def createtb(self):
		self.conn=sqlite3.connect("Car.db")
        self.ctrl=self.conn.cursor()
		self.UpdatableStringval=""
		self.table="value"
		self.day="timestamp"
		self.accelator="accelerator"
		self.brake="break"
		self.clutch="cluch"
		self.gear="gear"
		self.handbrake="handbrake"
		self.indicator="indicator"
		self.rpm="rpm"
		self.speed="speed"
		#self.ctrl.execute("drop table if exists Driver ")
		self.ctrl.execute("create table if not exists {tn}({d} timestamp not null,{sensorval1} INT not null,{sensorval2} INT not null ,{sensorval3} INT not null,{sensorval4} INT not null,{sensorval5} INT not null,{sensorval6} INT not null,{sensorval7} INT not null,{sensorval8} INT not null ,{sensorval9} INT not null )".format(tn=self.table,d=self.day,sensorval1=self.accelator,sensorval2=self.brake,sensorval3=self.clutch,sensorval4=self.gear,sensorval5=self.handbrake,sensorval6=self.indicator,sensorval7=self.rpm,sensorval8=self.speed,sensorval9=self.turn))

a=sequel()
a.createtb()