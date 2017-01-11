document["dispatchMouseDownEvent"] = function (x, y, target) {

	var mouseMoveEvent = document.createEvent("MouseEvents");

	mouseMoveEvent.initMouseEvent(
           "mousedown",  
           true,
           false, 
           window,  
           1,  
           x,
           y, 
           x,
           y,
           false,
           false,
           false, 
           false, 
           0,  
           null
	);

	console.log (target);

	target.dispatchEvent(mouseMoveEvent)
}

document["dispatchMouseUpEvent"] = function (x, y, target) {

	var mouseMoveEvent = document.createEvent("MouseEvents");

	mouseMoveEvent.initMouseEvent(
           "mouseup",  
           true,
           false, 
           window,
           1,  
           x,
           y, 
           x,
           y,
           false,
           false,
           false, 
           false, 
           0,  
           null
	);

	console.log (target);

	target.dispatchEvent(mouseMoveEvent)
}

document["dispatchMouseMoveEvent"] = function (xstart, ystart, xend, yend, target) {

	var mouseMoveEvent = document.createEvent("MouseEvents");

	mouseMoveEvent.initMouseEvent(
           "mousemove",  
           true,
           false, 
           window,  
           1,  
           xstart,
           ystart, 
           xstart,
           ystart,
           false,
           false,
           false, 
           false, 
           0,  
           null
	);

	target.dispatchEvent(mouseMoveEvent)

	var mouseMoveEvent = document.createEvent("MouseEvents");

	mouseMoveEvent.initMouseEvent(
           "mousemove",  
           true,
           false,
           window, 
           1, 
           xend,
           yend,
           xend,
           yend,
           false,
           false,
           false,
           false, 
           0,  
           null
	);

	console.log (target);

	target.dispatchEvent(mouseMoveEvent)
}
