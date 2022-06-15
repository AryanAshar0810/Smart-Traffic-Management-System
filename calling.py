from onnxruntime_predict import main
import json

def emmain():
	emergency=[]

	ev=main('noev.jpg')
	#print(ev)

	if ev==[]:
		emergency.append(0)
	else:
		emergency.append(1)

	ev=main('Side_4+2.png')
	#print(ev)

	if ev==[]:
		emergency.append(0)
	else:
		emergency.append(1)

	ev=main('43.jpg')
	#print(ev)

	if ev==[]:
		emergency.append(0)
	else:
		emergency.append(1)

	ev=main('cars.png')
	#print(ev)

	if ev==[]:
		emergency.append(0)
	else:
		emergency.append(1)


	print(emergency)
	return(emergency)

emmain()
