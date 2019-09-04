// var w = document.getElementById("barAre").offsetWidth;
// var height = width / 3.236;
//console.log("width", w);
//var w="400"
//var h="100"
// var h =document.getElementById("barAre").offsetHeight;


function onclick_bar(){
console.log("hello bar how are you")
    d3.select('#barAre').selectAll("svg").remove();
console.log("bar after remove");
var w = d3.select("#barAre").node().getBoundingClientRect().width
var h  = d3.select("#barAre").node().getBoundingClientRect().height
console.log(w)
console.log(h)

w1 = w+120
h1 = h+120

var svg = d3.select("#barAre") //container class to make it responsive
.append("svg")
.attr("style","position: absolute;")
//responsive SVG needs these 2 attributes and no width and height attr
.attr("preserveAspectRatio", "xMidYMid meet")
.attr("viewBox", "0 0 " +w1 + " " +h1 )
//class to make it responsive
.classed("svg-content-responsive", true),  
        margin = 20,
        width = w - margin,
        height = h - margin;



    // svg.append("text")
    //    .attr("transform", "translate(300,0)")
    //    .attr("x", 50)
    //    .attr("y", 50)
    //    .attr("font-size", "24px")
    //    .text("Eye Movement Data")   

    var x = d3.scaleBand().range([0, width]).padding(0.4);
        y = d3.scaleLinear().range([height, 0]);

    var g = svg.append("g").attr("style","overflow:scroll")
            .attr("transform","translate(" + 60 + "," + 50 + ")") 
            .attr("style","position:absolute;");

    d3.csv("2011top20.csv", function(error, data) {
        if (error) {
            throw error;
        }

        x.domain(data.map(function(d) { return d.Medicinename; }));
        y.domain([0,d3.max(data, function(d) { return +d.UnitCount2011; })]);
        
        g.append("g")   // g does not have "x" and "y" attributes, but  svg has .------------------------------
         .attr("transform", "translate(0," + height + ")")  
         .call(d3.axisBottom(x))
         .append("text")
         .attr("y", 50)
         .attr("x", 590)
         .attr("text-anchor", "end")
         .attr("stroke", "black")
         .text("Medicine Name");

        g.append("g").attr("style","overflow: scroll;")
         .call(d3.axisLeft(y).tickFormat(function(d){
             return  d;
         }).ticks(10))
         .append("text")
         .attr("transform", "rotate(-90)")
         .attr("y", -20)
         .attr("x",-100)
         .attr("dy", "-5.1em")
         .attr("text-anchor", "end")
         .attr("stroke", "black")
         .text("Fixation Duration");

        g.selectAll(".bar")
         .data(data)
         .enter().append("rect")
         .attr("class", "bar") //mouseover event is raised when the mouse cursor is moved over an element
         .on("mouseover", onMouseOver) //On selection of bar elements, two new event handlers added, viz. mouseover and mouseout and we are calling the respective functions to handle mouse events
         .on("mouseout", onMouseOut)   //done to apply animation when mouse hovers over a particular bar and goes out
         
         .attr("x", function(d,i) { return  x(d.Medicinename); })
         .attr("y", function(d) { return y(d.UnitCount2011); })
         .attr("width",x.bandwidth())
         .transition()
         .ease(d3.easeLinear)
         .duration(400)
         .delay(function (d, i) {
             return i * 50;
         })
         .attr("height", function(d) { return height - y(d.UnitCount2011); });
    });

    //mouseover event handler function
    /*most callback functions in d3, `this` refers to
the current node. For example, if you pass a function to `attr`,
`style`, or `each`, when that function is called, `this` will refer to
the current DOM element.*/
    function onMouseOver(d, i) {
        d3.select(this).attr('class', 'highlight'); // this, is the object that "owns" the JavaScript code
         //selected bar (given by the 'this' object) d3.select(this) creates a 1-element selection containing the current node
        d3.select(this)
          .transition()     // adds animation
          .duration(400)
          .attr('width', x.bandwidth() + 5)
          .attr("y", function(d) { return y(d.UnitCount2011) - 10; })
          .attr("height", function(d) { return height - y(d.UnitCount2011) + 10; });

        g.append("text")
         .attr('class', 'val')
         .attr('x', function() {
             return x(d.Medicinename);
         })
         .attr('y', function() {
             return y(d.UnitCount2011) - 15;
         })
         .text(function() {
             return [d.Condition];  // Value of the text
         });
    }

    //mouseout event handler function
    function onMouseOut(d, i) {
        // use the text label class to remove label on mouseout
        d3.select(this).attr('class', 'bar');
        d3.select(this)
          .transition()     // adds animation
          .duration(400)
          .attr('width', x.bandwidth())
          .attr("y", function(d) { return y(d.UnitCount2011); }) // What if we don't again fix this Value ?
          .attr("height", function(d) { return height - y(d.UnitCount2011); }); // Play with changing the Value

        d3.selectAll('.val')
          .remove()
    }


}