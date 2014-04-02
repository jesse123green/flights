
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

var circles = svg.append("svg:g")
    .attr("id", "circles");
	
var ports = svg.append("svg:g")
    .attr("id", "ports");

var texts = svg.append("svg:g")
    .attr("id", "texts");

var cells = svg.append("svg:g")
    .attr("id", "cells");

var vectors = svg.append("svg:g")
    .attr("id", "vectors");

var flightdata;

var portnames = [];	

var currentday = 2;
var currentport;
var airportData;



function loadmap(finished_loading){

	console.log('loading map')

	d3.json("../static/data/us-states.json", function(collection) {
		states.selectAll("path")
		.data(collection.features)
		.enter().append("svg:path")
		.attr("d", path);
	});

	d3.json("../static/data/thanks2.json", function(json) {
		flightdata = json;
	});

	finished_loading();
}

$(document).ready(

	loadmap(function(){
		console.log('finished loading!')
	})

);




