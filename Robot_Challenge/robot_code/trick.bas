main:
	forward A ; go forwards
	forward B
	; test bumpers
	; to see if hit
	if pinC.3 = 1 then doRight
	if pinC.1 = 1 then doLeft
	goto main
	
doLeft:
	gosub goBack
	forward A ; turn for 0.32s
	backward B
	pause 760
	goto main
	
doRight:
	gosub goBack
	backward A ; turn for 0.32s
	forward B
	pause 760
	goto main
	
goBack:
	backward A ; reverse for 0.5s
	backward B
	pause 200
	return

