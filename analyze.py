import numpy
import matplotlib.pyplot

#backLegSensorValues = numpy.load('data/bcklegvalfile.npy')
#print(backLegSensorValues)

#frntLegSensorValues = numpy.load('data/frntlegvalfile.npy')
#print(backLegSensorValues)

#matplotlib.pyplot.plot(backLegSensorValues, linewidth=2, label="Backleg Sensor Vals")
#matplotlib.pyplot.plot(frntLegSensorValues, linewidth=2, label="Frontleg Sensor Vals")
#matplotlib.pyplot.legend()

sinVal = numpy.load('data/numpsin.npy')

matplotlib.pyplot.plot(sinVal,linewidth=4, label="sin val")
matplotlib.pyplot.legend()

matplotlib.pyplot.show()