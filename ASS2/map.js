let map;
let markers = [];

// get instent date and transfer into numbers
let now = new Date();
let mouth = now.getMonth();
let day = now.getDate();
let nowdate = mouth * 100 + day;

// infowindow and marker function
function infoCallback(infowindow, marker) {
  infowindow.close();
  return function () {
    infowindow.open(map, marker);
  };
}

function initialize() {
  map = new google.maps.Map(document.getElementById("map_canvas"), {
    center: { lat: 53.8, lng: -1.4 },
    zoom: 10,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
  });
}

function showMarker() {
  for (id in testData) {
    var mycolor = "";
    var icontype = "";
    var starcolor = "";
    var markerLocation = new google.maps.LatLng(
      testData[id].lat,
      testData[id].lng
    );
    var myletter = testData[id].type.substring(0, 1).toUpperCase();
    var opentime = testData[id].reopeningtime;
    // get and split to string of reopen date, then transfer to numbers
    var openmouth = opentime.replace(/[^0-9]/gi, "").substring(4, 5);
    var openday = opentime.replace(/[^0-9]/gi, "").substring(5);
    var opendate = Number(openmouth) * 100 + Number(openday);

    // judge different conditions and output different mark type
    if (myletter == "M") {
      mycolor = "1E90FF";
    } else if (myletter == "G") {
      mycolor = "ff00ff";
    } else {
      mycolor = "FFD700";
    }
    if (opentime == "Opening") {
      icontype = "xpin_letter_withshadow&chld=pin_star|";
      starcolor = "00FF00";
    } else if (opentime == "Undeclared/Closed") {
      icontype = "pin_letter_withshadow&chld=";
    } else if (opendate > nowdate) {
      icontype = "xpin_letter_withshadow&chld=pin_star|";
      starcolor = "B0C4DE";
    } else if (opendate <= nowdate) {
      icontype = "xpin_letter_withshadow&chld=pin_star|";
      starcolor = "00FF00";
    }

    // final info window content
    var info =
      "<div class=infowindow><h1>" +
      testData[id].place +
      "</h1><p>Address: " +
      testData[id].details +
      "</p><p>Link: <a href='http://" +
      testData[id].website +
      "'>" +
      testData[id].website +
      "</a></p><p>Reopening time: " +
      testData[id].reopeningtime +
      "</p></div>";

    //add marker, set properties
    const marker = new google.maps.Marker({
      position: markerLocation,
      map: map,
      draggable: true,
      animation: google.maps.Animation.DROP,
      icon:
        "http://chart.apis.google.com/chart?chst=d_map_" +
        icontype +
        myletter +
        "|" +
        mycolor +
        "|000000|" +
        starcolor,
    });
    markers.push(marker);
    var infowindow = new google.maps.InfoWindow({
      content: info,
    });

    google.maps.event.addListener(
      marker,
      "click",
      infoCallback(infowindow, marker)
    );
  }
}

function setMapOnAll(map) {
  for (let i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
  }
}

function clearMarker() {
  setMapOnAll(null);
}

// function deleteMarkers() {
//   clearMarkers();
//   markers = [];
// }

var isEmpty = function (x) {
  return x === "";
};

var isNumber = function (x) {
  return !isNaN(x - 0);
};

var invalid = function (x) {
  x.style.backgroundColor = "#FFFF7E";
  error = true;
};

var valid = function (x) {
  x.style.backgroundColor = "White";
};

let newarrey = [];

function validate() {
  error = false;
  var allboxes = document.getElementsByClassName("boxes");
  var lat = document.getElementById("lat");
  var lon = document.getElementById("lon");
  var place = document.getElementById("place");
  var website = "http://" + document.getElementById("website");
  var details = document.getElementById("details");
  var reopeningtime = document.getElementById("reopeningtime");
  var type = document.getElementById("type");
  newarrey.push(lat, lon, place, website, details, reopeningtime, type);

  for (var i = 0; i < allboxes.length; i++) {
    valid(allboxes[i]);
  }

  for (var i = 0; i < allboxes.length; i++) {
    if (isEmpty(allboxes[i].value)) {
      invalid(allboxes[i]);
    }
  }

  if (!isNumber(lat.value) || isEmpty(lat.value)) {
    invalid(lat);
  }

  if (!isNumber(lon.value) || isEmpty(lon.value)) {
    invalid(lon);
  }

  if (isEmpty(website.value)) {
    invalid(website);
  }

  if (error) {
    alert("Please check the form for highlighted errors and resubmit");
    return false;
  } else {
    return true;
  }
}

function pushData() {
  testData.push(newarrey);
}
