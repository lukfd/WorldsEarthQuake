# Luca Comba

import math
import turtle

def main():
	earthquakes = ReadCsv("earthquakes_2013-2017.csv")
	data = ReadData(earthquakes)
	map = VisualizeQuake(data, earthquakes, DrawCircles)

def VisualizeQuake (data, earthquakes, DrawCircles):
	# colors
	red = '#ff0000'
	orange = '#ff8800'
	green = '#00ac22'
	
	#setting up the map
	turtle.setup(1600, 800)
	turtle.Screen().bgpic("World_Map.gif")
	turtle.Screen().setworldcoordinates(-180, -90, 180, 90)
	t = turtle.Turtle()
	turtle.tracer(0)
	
	# drawing
	for i in range (0, len(earthquakes), 10):
		x = float(earthquakes[i]['Longitude'])
		y = float(earthquakes[i]['Latitude'])
		if float(earthquakes[i]['Depth']) <= 70:
			DrawCircles (x, y, 0.5*float(earthquakes[i]['Magnitude']), green, t)
		elif float(earthquakes[i]['Depth']) > 70 and float(earthquakes[i]['Depth']) <= 300:
			DrawCircles (x, y, 0.5*float(earthquakes[i]['Magnitude']), orange, t)
		elif float(earthquakes[i]['Depth']) > 300 and float(earthquakes[i]['Depth']) <= 700:
			DrawCircles (x, y, 0.5*float(earthquakes[i]['Magnitude']), red, t)
		
	
	turtle.done()

def DrawCircles(x, y, radius, color, t):
	t.up()
	t.speed(10)
	t.goto(x, y)
	t.down()
	t.color(color)
	t.fillcolor(color)
	t.begin_fill()
	t.circle(radius)
	t.end_fill()
	
def ReadData(earthquakes):
		#counter
	total_magnitude = 0
	number_earthquakes = 0
	magnitude = 0
	SD = 0
		#magnitude
	three = 0
	four = 0
	five = 0
	six = 0
	seven = 0
	eight = 0
	nine = 0
		#years
	year1 = 0
	year2 = 0
	year3 = 0
	year4 = 0
	year5 = 0
	for i in earthquakes:
		number_earthquakes = number_earthquakes + 1
		magnitude = float(i['Magnitude'])
		#rounding
		if magnitude < 3.5:
			three = three + 1
		elif magnitude >= 3.5 and magnitude < 4:
			four = four + 1
		elif magnitude < 4.5 and magnitude >= 4:
			four = four + 1
		elif magnitude >= 4.5 and magnitude < 5:
			five = five + 1
		elif magnitude < 5.5 and magnitude >= 5:
			five = five + 1
		elif magnitude >= 5.5 and magnitude < 6:
			six = six + 1
		elif magnitude < 6.5 and magnitude >= 6:
			six = six + 1
		elif magnitude >=6.5 and magnitude < 6:
			seven = seven + 1
		elif magnitude < 7.5 and magnitude >= 7:
			seven = seven + 1
		elif magnitude >= 7.5 and magnitude < 8:
			eight = eight + 1
		elif magnitude < 8.5 and magnitude >= 8:
			eight = eight + 1
		elif magnitude >= 8.5 and magnitude < 9:
			nine = nine + 1
		elif magnitude < 9.5 and magnitude >= 9:
			nine = nine + 1
		elif magnitude >= 9.5 and magnitude < 10:
			nine = nine + 1
		else:
			three = three + 1
		
		if "2013" in i["DateTime"]:
			year1 = year1 + 1
		if "2014" in i["DateTime"]:
			year2 = year2 + 1
		if "2015" in i["DateTime"]:
			year3 = year3 + 1
		if "2016" in i["DateTime"]:
			year4 = year4 + 1
		if "2017" in i["DateTime"]:
			year5 = year5 + 1
		total_magnitude = total_magnitude + magnitude
	
	#calculating average
	
	average = total_magnitude/number_earthquakes
	
	#calculating Standard Deviation
	
	totalx = 0
	for i in earthquakes:
		magnitude1 = float(i['Magnitude'])
		x = (magnitude1 - average)**2
		totalx = totalx + x
	SD = math.sqrt((1/number_earthquakes) * (totalx))
	
	#calculating percentage
	
	three = int((three*100)/number_earthquakes)
	four = int((four*100)/number_earthquakes)
	five = int((five*100)/number_earthquakes)
	six = int((six*100)/number_earthquakes)
	seven = int((seven*100)/number_earthquakes)
	eight = int((eight*100)/number_earthquakes)
	nine = int((nine*100)/number_earthquakes)

	#print(three, four, five, six, seven, eight, nine)
	print("Earthquake magnitude disrtibution: \n3: %s (%d%%)\n4: %s (%d%%)\n5: %s (%d%%)\n6: %s (%d%%)\n7: %s (%d%%)\n8: %s (%d%%)\n9: %s (%d%%)\n" % ('*'* three, three, '*'*four, four,'*'* five, five, '*'*six, six,'*'* seven, seven, '*'*eight, eight, '*'* nine, nine))
	print("Earthquake magnitude: average = %f, stddev = %f\n" % (average, SD))
	print('Total earthquakes per year:\n2013: %d\n2014: %d\n2015: %d\n2016: %d\n2017: %d' % (year1, year2, year3, year4, year5))

		
def ReadCsv(filename):
	file = open(filename, "r")
	list = []
	line_counter=0
	keys=[]
	for line in file:
		data = {}
		if line_counter == 0:
			keys=line.split(",")
		else:
			line2 = line.split(",")
			if len(keys) == len(line2):
				for i in range(len(line2)):
					data[keys[i]]=line2[i]
				list.append(data)
		line_counter=line_counter+1
		
	return list

main()
