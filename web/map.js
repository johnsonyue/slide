var map_width = 1400;
var map_height = 1200;
var map_svg = d3.select(".map svg")
    .attr("width", map_width)
    .attr("height", map_height);

var xmlHttpRequest;
get_map_func();

function get_map_func(){
    var url = "./caida.json";
    xmlHttpRequest = new XMLHttpRequest();
    xmlHttpRequest.onreadystatechange = map_places_ready;
    xmlHttpRequest.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    xmlHttpRequest.send();
}

var map_places;
var map_world;
function map_places_ready() {
    if(xmlHttpRequest.readyState == 4 && xmlHttpRequest.status == 200) {
        var text = xmlHttpRequest.responseText;
        map_places = JSON.parse(text);

        xmlHttpRequest = d3.json("./world-50m.json", map_world_ready);
    }
}

function map_world_ready(error, json) {
    if (error) return console.warn(error);
    map_world = json;

    //projection, path function for svg <d> data
    var projection = d3.geo.mercator()
        .scale(200)
        .translate([map_width / 2, map_height / 2])
        .precision(.1);

    var map_path = d3.geo.path()
        .projection(projection);

    var nodes = [];

    //convert places to designated format.
    map_places.forEach(function(e, i, a){
        var feature = { "type": "Feature", "properties": {"index": i}, "geometry": { "type": "Point", "coordinates": [e.lon,e.lat] }};
        nodes.push(feature);
    });

    //draw the world map
    map_svg.select("#frame")
        .attr("width", map_width)
        .attr("height", map_height);

    map_svg.append("path")
        .datum(topojson.object(map_world, map_world.objects.land))
        .attr("class", "land noclicks")
        .attr("d", map_path);

    //draw points.
    var g = map_svg.append("g").attr("class","circles")
        .selectAll("path").data(nodes)
        .enter().append("circle")
        .attr("cx", function(d){
            return projection(d.geometry.coordinates)[0];
        })
        .attr("cy",function(d){
            return projection(d.geometry.coordinates)[1];
        })
        .attr("r", 1);
}
