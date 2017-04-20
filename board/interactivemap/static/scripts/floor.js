Floor.prototype.STYLE_HIGHLIGHTED = "fill: #FF9955";

Floor.prototype.resetLastHighlightedElement = function() {
	if(this.lastHighlightedElement) {
		this.highlightElement(this.lastHighlightedElement, true);
	}
}

Floor.prototype.highlightElement = function(element, removeHighlight) {
	var self = this;
	if(!element) {
		return;
	}
	if(!element.children.length) {
		this.highlightSingleElement(element, removeHighlight);
	} else {
		Array.prototype.forEach.call(element.children, function(ec) {
			self.highlightSingleElement(ec, removeHighlight);
		});
	}
	this.lastHighlightedElement = removeHighlight ? null : element;
};

Floor.prototype.highlightSingleElement = function(element, removeHighlight) {
	if(removeHighlight) {
		if(element.prevStyle) {
			element.style = element.prevStyle;
			element.prevStyle = null;
		}
	} else {
		if(!element.prevStyle) {
			element.prevStyle = element.style.cssText;
			element.style = Floor.prototype.STYLE_HIGHLIGHTED;
		}
	}
};

Floor.prototype.getEmployeeById = function(id) {
	return this.getElementById(this.employees, id);
}

Floor.prototype.getRoomById = function(id) {
	return this.getElementById(this.rooms, id);
}

Floor.prototype.getElementById = function(arr, id) {
	var a = arr || [];
	var result = null;
	a.forEach(function(e){
		if(e.id === id) {
			result = e;
			return true;
		}
	});
	return result;
}

function Floor(svg, floorData, gIndex) {
	gIndex = gIndex || 1; //svgPanAndZoom place it's own g, so we will use the second one.
	this.employees = [];
	this.rooms = [];
	this.svg = svg;
	this.g = svg.contentDocument.getElementsByTagName('g')[gIndex];
	this.lastHighlightedElement = null;
	this.moved = false;
	var self = this;
	floorData.rooms.forEach(function(room) {
		var roomVisualization = self.svg.contentDocument.getElementById(room.base);
		if(!roomVisualization) {
			console.log("Room ", room.id, " has no visualization!");
		} else {
			room.visual = roomVisualization;
			
			room.visual.addEventListener("mousemove", function(e) {
				self.moved = true;
			});
			room.visual.addEventListener("mousedown", function(e) {
				self.moved = false;
			});
			room.visual.addEventListener("mouseup", function(e) {
				if(!self.moved) {
					if(self.onRoomClick) {
						self.onRoomClick(room);
					}
				}
			});
			/*room.visual.addEventListener("click", function(e) {
				if(self.onRoomClick) {
					self.onRoomClick(room);
				}
			});*/
			self.rooms.push(room);
		}
		room.employees.forEach(function(employee) {
			var employeeVisualization = null;
			if(employee.visualizationBase) {
				employeeVisualization = self.svg.contentDocument.getElementById(employee.visualizationBase);
			} else {
				if(!employee.deskX || !employee.deskY) {
					console.log("Employee ", employee.id, " has neither visualizationBase or desk coordinates!");
					return; // continue;
				}
				employeeVisualization = self.createWorkplace(employee);
				self.g.appendChild(employeeVisualization);
			}
			if(!employeeVisualization) {
				console.log("Employee ", employee.id, " has no visualization!");
				return; // continue;
			} else {
				employee.visual = employeeVisualization;
				employee.visual.addEventListener("click", function(e) {
					if(self.onEmployeeClick) {
						self.onEmployeeClick(employee);
					}
				});
				self.employees.push(employee);
			}
		});
	});
}

Floor.prototype.createWorkplace = function(employee) {
	if( !employee.deskX || !employee.deskY ) {
		console.log("Unable to create workplace for employee ", employee.id, " with coordinates (", employee.deskX, ", ", employee.deskY);
		return null;
	}
	var circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
	circle.setAttribute("id", "employee" + employee.id.toString());
	circle.employeeId = employee.id;
	circle.setAttribute("cx", employee.deskX);
	circle.setAttribute("cy", employee.deskY);
	circle.setAttribute("r", 80);
	circle.setAttribute("stroke", "#000000");
	circle.setAttribute("stroke-width", 15);
	circle.setAttribute("stroke-miterlimit", 4);
	circle.setAttribute("style", "fill: #00FF00");
	circle.setAttribute("stroke-opacity", 1);
	return circle;
}
