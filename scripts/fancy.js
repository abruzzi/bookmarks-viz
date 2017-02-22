$(function() {
    var margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = 960 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    var parseDate = d3.time.format("%Y-%m-%d").parse;

    var x = d3.time.scale()
        .range([0, width]);

    var y = d3.scale.linear()
        .range([height, 0]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .innerTickSize(-width)
        .outerTickSize(0)
        .tickPadding(10);

    var line = d3.svg.line()
        .x(function(d) { return x(d.date); })
        .y(function(d) { return y(d.close); });

    var svg = d3.select("#chart").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    $.get('/bookmarks.count.json').done(function(data) {
      data.forEach(function(d) {
        d.date = parseDate(d.created);
        d.close = +d.count;
      });

      x.domain(d3.extent(data, function(d) { return d.date; }));
      y.domain([0, d3.max(data, function(d) {return d.close;})]);

      // svg.append("path")
      //         .datum(data)
      //         .attr("class", "line")
      //         .attr("d", line);

      svg.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xAxis);

      svg.selectAll(".dot")
        .data(data)
        .enter()
        .append("circle")
          .attr("class", function(d) {
            var year = d.date.getFullYear();
            console.log(year);
            if(year <= 2013) {
              return "circle-2013";
            } else if (year > 2013 && year <= 2014) {
              return "circle-2014";
            } else if (year > 2014 && year <= 2016) {
              return "circle-2015";
            } else {
              return "circle-2016";
            }
          })
          .attr("r", function(d) {return d.close/2;})
          .attr("opacity", function(d) {return d.close*0.05;})
          .attr("cx", function(d) {return x(d.date)})
          .attr("cy", function(d) {return y(d.close)});

      svg.append("g")
          .attr("class", "y axis")
          .call(yAxis)
        .append("text")
          .attr("transform", "rotate(-90)")
          .attr("y", 6)
          .attr("dy", ".71em")
          .style("text-anchor", "end")
          .text("Bookmarks Count");
    });
});