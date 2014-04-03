
var projection = d3.geo.azimuthal()
    .mode("equidistant")
    .origin([-99, 38])
    .scale(1350)
    .translate([540, 330]);

var path = d3.geo.path()
    .projection(projection);

var margin = {top: 20, right: 0, bottom: 20, left: 0};

var width = 1200 - margin.left - margin.right,
    height = 670 - margin.top - margin.bottom;

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


var states = svg.append("svg:g")
    .attr("id", "states");

var vectors = svg.append("svg:g")
    .attr("id", "vectors");
	
var ports = svg.append("svg:g")
    .attr("id", "ports");

var texts = svg.append("svg:g")
    .attr("id", "texts");

var cells = svg.append("svg:g")
    .attr("id", "cells");

var circles = svg.append("svg:g")
    .attr("id", "circles");


var flightdata;

var portnames = [];	

var currentday = 'Thu';
var currentport;
var airportData;

function scaledCoords(x0,y0,x1,y1,c){
	var dx = x1-x0;
	var dy = y1-y0;
	var r = Math.sqrt(Math.pow(dx,2) + Math.pow(dy,2));
	theta = Math.atan2(dy,dx);
	var x = x0 + r*c*Math.cos(theta);
	var y = y0 + r*c*Math.sin(theta);
	return [x,y,theta];
}

function loadMap(finished_loading){

	console.log('loading map')

	d3.json("../static/data/us-states.json", function(collection) {
		states.selectAll("path")
		.data(collection.features)
		.enter().append("svg:path")
		.attr("d", path);
		console.log('map loaded')
	});

	d3.json("../static/data/thanksgiving_flights.json", function(json) {
		flightdata = json;
		console.log('flight data loaded')
		finished_loading();
	});

	
}


function loadCities(){
	d3.csv("../static/data/AirportGPS.csv", function(airports) {
		airportData = airports;
		createCities();
		console.log('gps loaded')
	});
}

function createCities(){

	var positions = [];
	names = [];
	airportData.forEach(function(d) {
		var location = [+d.Long, +d.Lat];
		positions.push(projection(location));
		portnames.push(d.Airport);
		names.push(d.Airport);
		flightdata[d.Airport]['location'] = projection(location);
	});


	// node = root = airportData;

	texts.selectAll("texts")
	.data(airportData)
	.enter().append("svg:text")
	.text(function(d,i) {
		return names[i];
	})
	.attr("x", function(d, i) {return positions[i][0]+5; })
	.attr("y", function(d, i) { return positions[i][1]-10; });

	circles.selectAll("circle")
		.data(airportData)
		.enter().append("svg:circle")
		.attr("cx", function(d, i) {return positions[i][0]; })
		.attr("cy", function(d, i) { return positions[i][1]; })
		.attr("r", 6)
		.attr("id",function(d,i) {return names[i];})
		.style("fill","steelblue")
		.style("fill-opacity",.8)
		.style("stroke","#707070")
		.on("click", function(d, i) {
		selectDest(d,i) 
		});

	vectors.selectAll("line")
		.data(airportData)
		.enter().append("svg:line")
		.attr("x1", function(d, i) {return positions[i][0]; })
		.attr("y1", function(d, i) { return positions[i][1]; })
		.attr("x2", function(d, i) {return positions[i][0]; })
		.attr("y2", function(d, i) { return positions[i][1]; })
		.attr("id",function(d,i) {return names[i];})
		.style("stroke","gray")
		.style("stroke-width",3)
		.style("fill-opacity",.95);		
		
	ports.selectAll("circle")
		.data(airportData)
		.enter().append("svg:circle")
		.attr("cx", function(d, i) {return positions[i][0]; })
		.attr("cy", function(d, i) { return positions[i][1]; })
		.attr("r", 3)
		.attr("id",function(d,i) {return names[i];})
		.style("fill","#303030")
		.style("fill-opacity",.8)
		.on("click", function(d, i) {
		currentport = names[i];
		selectDest(d,i) 
		});


}

function selectDay(cday){
	var ratio;
	currentday = cday;
	if (currentport){
		
		for (i=0;i<portnames.length;i++){
		
			if (!(portnames[i] == currentport)){ // && currentport.hasOwnProperty('7')

				try{
					ratio = flightdata[currentport][portnames[i]][currentday]['ratio'];

					xy = scaledCoords(flightdata[currentport]['location'][0],flightdata[currentport]['location'][1],flightdata[portnames[i]]['location'][0],flightdata[portnames[i]]['location'][1],ratio)
					circles.selectAll("circle#"+portnames[i]).transition().duration(500).delay(0)
					.attr("r", Math.sqrt(flightdata[currentport][portnames[i]][currentday]['numFlights']))
					// .attr("r", Math.min(flightdata[currentport][portnames[i]][currentday]['numFlights']*8,8))
					.attr("cx", xy[0])
					.attr("cy", xy[1]); 
				}
				catch (e){
					// xy = scaledCoords(flightdata[currentport]['location'][0],flightdata[currentport]['location'][1],flightdata[portnames[i]]['location'][0],flightdata[portnames[i]]['location'][1],ratio)
					circles.selectAll("circle#"+portnames[i]).transition().duration(500).delay(0)
					.attr("r", 0);
					// .attr("r", Math.min(flightdata[currentport][portnames[i]][currentday]['numFlights']*8,8))
					// .attr("cx", xy[0])
					// .attr("cy", xy[1]); 
				}
			}
		}
	}
}

function selectDest(d,i1){

	currentport = names[i1];

	ports.selectAll("circle#"+names[i1])
		.transition().duration(500).delay(0)
		.style("fill-opacity",0);
	
	vectors.selectAll("line#"+names[i1])
		.transition().duration(500).delay(0)
		.attr("x1", flightdata[names[i1]]['location'][0])
		.attr("y1", flightdata[names[i1]]['location'][1])
		.attr("x2", flightdata[names[i1]]['location'][0])
		.attr("y2", flightdata[names[i1]]['location'][1]);

	circles.selectAll("circle#"+names[i1])
		.transition().duration(500).delay(0)
		.style("fill", "black")
		.attr("cx", flightdata[names[i1]]['location'][0])
		.attr("cy", flightdata[names[i1]]['location'][1])
		.attr("r", 5);

	ports.selectAll("circle#"+names[i1])
		.transition().duration(500).delay(0)
		.style("fill-opacity",0);

	for (i=0;i<names.length;i++){
		
		if (!(names[i] == names[i1])){

			// v = vectors.selectAll("line#"+names[i]);
			// console.log(flightdata[names[i1]]['location'])

			try{

			xy = scaledCoords(flightdata[names[i1]]['location'][0],flightdata[names[i1]]['location'][1],flightdata[names[i]]['location'][0],flightdata[names[i]]['location'][1],flightdata[names[i1]][names[i]]['rmin'])
			xy2 = scaledCoords(flightdata[names[i1]]['location'][0],flightdata[names[i1]]['location'][1],flightdata[names[i]]['location'][0],flightdata[names[i]]['location'][1],flightdata[names[i1]][names[i]]['rmax'])

			vectors.selectAll("line#"+names[i])
				.transition().duration(500).delay(0)
				.attr("x1", xy[0])
				.attr("y1", xy[1])
				.attr("x2", xy2[0])
				.attr("y2", xy2[1]);
			}

			catch (e){

				vectors.selectAll("line#"+names[i])
				.transition().duration(500).delay(0)
				.attr("x1", flightdata[names[i]]['location'][0])
				.attr("y1", flightdata[names[i]]['location'][1])
				.attr("x2", flightdata[names[i]]['location'][0])
				.attr("y2", flightdata[names[i]]['location'][1]);
			}
	
			ports.selectAll("circle#"+names[i])
				.transition().duration(500).delay(0)
				.style("fill-opacity",.8);
			
			try{

			xy = scaledCoords(flightdata[names[i1]]['location'][0],flightdata[names[i1]]['location'][1],flightdata[names[i]]['location'][0],flightdata[names[i]]['location'][1],flightdata[names[i1]][names[i]][currentday]['ratio'])

			circles.selectAll("circle#"+names[i]).transition().duration(500).delay(250)
				.attr("r", Math.sqrt(flightdata[names[i1]][names[i]][currentday]['numFlights']))
				.attr("cx", xy[0])
				.attr("cy", xy[1])
				.style("fill", "steelblue")
				.style("fill-opacity",.8);
			}
			catch (e){
				circles.selectAll("circle#"+names[i]).transition().duration(500).delay(250)
					.attr("r", 0)
					.attr("cx", flightdata[names[i]]['location'][0])
					.attr("cy", flightdata[names[i]]['location'][1]);
			}

		
	  }
	  }

		
}

$(document).ready(

	loadMap(function(){
		console.log('done loading')
		loadCities();
	})

);
