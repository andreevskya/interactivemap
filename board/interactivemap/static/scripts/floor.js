Floor.prototype.highlightedStyle = "fill: #FF9955";

Floor.prototype.highlightElement = function(element, removeHighlight) {
	var self = this;
	if(!element.children.length) {
		this.highlightSingleElement(element, removeHighlight);
		this.lastHighlighted = element;
	} else {
		Array.prototype.forEach.call(element.children, function(ec) {
			self.highlightSingleElement(ec, removeHighlight);
		});
		this.lastHighlighted = element;
	}
}

Floor.prototype.highlightSingleElement = function(element, removeHighlight) {
	if(removeHighlight) {
		if(element.prevStyle) {
			element.style = element.prevStyle;
			element.prevStyle = null;
		}
	} else {
		if(!element.prevStyle) {
			this.lastHighlighted = element;
			element.prevStyle = element.style.cssText;
			element.style = Floor.prototype.highlightedStyle;
		}
	}
}

Floor.prototype.resetLastHighlightedElement = function() {

	if(this.lastHighlighted) {
		this.highlightElement(this.lastHighlighted, true);
	}
}

Floor.prototype.getElementById = function(base) {
	var result = null;
	Array.prototype.forEach.call(this.g.children, function(c) {
		if(c.id === base) {
			result = c;
			return true;
		}
	});
	return result;
}

Floor.prototype.highlightEmployeeById = function(id) {
	var self = this;
	this.resetLastHighlightedElement();
	this.highlightElement(this.getElementById(this.getEmployeeById(id).visualizationBase));
}

Floor.prototype.getEmployeeById = function(id) {
	var result = null;
	this.floorData.rooms.forEach(function(room) {
		room.employees.forEach(function(employee) {
			if(employee.id === id) {
				result = employee;
				return true;
			}
		});
	});
	return result;
}

Floor.prototype.getRoomById = function(id) {
	var result = null;
	this.floorData.rooms.forEach(function(room) {
		if(room.id === id) {
			result = room;
			return true;
		}
	});
	return result;
}

Floor.prototype.highlightRoomById = function(id) {
	var self = this;
	this.resetLastHighlightedElement();
	this.highlightElement(this.getElementById(this.getRoomById(id).base));
}


function Floor(svgId, floorData, groupIndex) {
	groupIndex = groupIndex || 1;
	this.floorData = floorData;
	this.svgMapId = svgId;
	this.svgMap = document.getElementById(this.svgMapId);
	if(!this.svgMap) {
		console.log("Unabled to find element with id ", this.svgMapId);
		return;
	}
	// svgPan&Zoom ставит поверх изображения свой g, поэтому берём второй.
	this.g = this.svgMap.contentDocument.getElementsByTagName('g')[groupIndex];
	
	var self = this;
	
	Array.prototype.forEach.call(this.g.children, function(c) {
		floorData.rooms.forEach(function(r) {
			if(c.id === r.base) {
				c.addEventListener("click", function(e) {
					if(self.onRoomClick) {
						self.onRoomClick(r);
					}
					self.resetLastHighlightedElement();
					self.highlightElement(e.currentTarget);
				});
			}	
		});
	});
	
	Array.prototype.forEach.call(this.g.children, function(c) {
		floorData.rooms.forEach(function(r) {
			r.employees.forEach(function(employee) {
				if(!employee.visualizationBase) {
					return;
				}
				if(c.id === employee.visualizationBase) {
					c.addEventListener("mouseover", function(e) {
						//self.highlightElement(e.currentTarget);
					});
					c.addEventListener("mouseleave", function(e) {
						//self.highlightElement(e.currentTarget, true);
					});
					c.addEventListener("click", function(e) {
        				if(self.onWorkspaceClick) {
							self.onWorkspaceClick(employee);
						}
						self.resetLastHighlightedElement();
						self.highlightElement(e.currentTarget);
					});
				}
			});
		});
	});
}
