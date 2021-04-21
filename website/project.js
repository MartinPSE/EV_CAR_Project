// Add map
var map = L.map('map').setView([37.5, 126.99], 11);
13e0af094e2876bdddf3cecf962f51ba
// Add base tiles to the map
var Base = L.tileLayer("https://api.vworld.kr/req/wmts/1.0.0/8842F76A-E2EE-36A3-A466-648DBFC4AEC8/Base/{z}/{y}/{x}.png", {
    attribution: '&copy; <a href="http://api.vwrold.kr">V wrold Map</a>',
    maxZoom: 18
}).addTo(map);

var Hybrid = L.tileLayer("https://api.vworld.kr/req/wmts/1.0.0/8842F76A-E2EE-36A3-A466-648DBFC4AEC8/Hybrid/{z}/{y}/{x}.png", {
    attribution: '&copy; <a href="http://api.vwrold.kr">V wrold Map</a>',
    maxZoom: 18
});

var satelite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: '&copy; <a href="http://www.esri.com/">Esri</a>',
    maxZoom: 18,
});

// Add Icons
var carIcon = L.icon({
    iconUrl: "images/car_icon.png",
    iconSize: [40, 50],
});

var line1icon = L.icon({
    iconUrl: "images/line1.png",
    iconSize: [30, 40],

});
var line2icon = L.icon({
    iconUrl: "images/line2.png",
    iconSize: [30, 40],
});
var line3icon = L.icon({
    iconUrl: "images/line3.png",
    iconSize: [30, 40],
});
var line4icon = L.icon({
    iconUrl: "images/line4.png",
    iconSize: [30, 40],
});
var line5icon = L.icon({
    iconUrl: "images/line5.png",
    iconSize: [30, 40],
});
var line6icon = L.icon({
    iconUrl: "images/line6.png",
    iconSize: [30, 40],
});
var line7icon = L.icon({
    iconUrl: "images/line7.png",
    iconSize: [30, 40],
});
var line8icon = L.icon({
    iconUrl: "images/line8.png",
    iconSize: [30, 40],
});

var line9icon = L.icon({
    iconUrl: "images/line9.png",
    iconSize: [30, 40],
});

var midkyungicon = L.icon({
    iconUrl: "images/kyungeui.png",
    iconSize: [30, 40],
});

var airporticon = L.icon({
    iconUrl: "images/airport.png",
    iconSize: [30, 40],
});

var bundangicon = L.icon({
    iconUrl: "images/bundang.png",
    iconSize: [30, 40],
});

var newbundangicon = L.icon({
    iconUrl: "images/newbundang.png",
    iconSize: [30, 40],
});



// Markercluster
var markers = L.markerClusterGroup();


function createbutton(label, container) {
    var btn = L.DomUtil.create('button', '', container);
    btn.setAttribute('type', 'button');
    btn.innerHTML = label;
    return btn;
}

map.on('click', function (e) {
    var container = L.DomUtil.create('div'),
        startBtn = createbutton('출발 지점', container),
        destBtn = createbutton('도착 지점', container);

    L.DomEvent.on(startBtn, 'click', function () {
        control.spliceWaypoints(0, 1, e.latlng);
        map.closePopup();
    });

    L.DomEvent.on(destBtn, 'click', function () {
        control.spliceWaypoints(control.getWaypoints().length - 1, 1, e.latlng);
        map.closePopup();
    });

    L.popup().setContent(container).setLatLng(e.latlng).openOn(map);
});




var Metroline1 = L.geoJson(metro, {
    filter: function (feature, layer) {
        if (feature.properties.KOR_SBR_NM == '1호선') return true;
    },
    onEachFeature: function (feature, layer, container) {
        layer.setIcon(layer.options.icon = line1icon),
            layer.bindPopup( feature.properties.KOR_SBR_NM + ' : ' + feature.properties.KOR_SUB_NM);
    }
});

var Metroline2 = L.geoJson(metro, {
    filter: function (feature, layer) {
        if (feature.properties.KOR_SBR_NM == '2호선') return true;
    },
    onEachFeature: function (feature, layer) {
        layer.setIcon(layer.options.icon = line2icon),
            layer.bindPopup(feature.properties.KOR_SBR_NM + ' : ' + feature.properties.KOR_SUB_NM);
    }
});

var Metroline3 = L.geoJson(metro, {
    filter: function (feature, layer) {
        if (feature.properties.KOR_SBR_NM == '3호선') return true;
    },
    onEachFeature: function (feature, layer) {
        layer.setIcon(layer.options.icon = line3icon),
            layer.bindPopup(feature.properties.KOR_SBR_NM + ' : ' + feature.properties.KOR_SUB_NM);
    }
});

var Metroline4 = L.geoJson(metro, {
    filter: function (feature, layer) {
        if (feature.properties.KOR_SBR_NM == '4호선') return true;
    },
    onEachFeature: function (feature, layer) {
        layer.setIcon(layer.options.icon = line4icon),
            layer.bindPopup(feature.properties.KOR_SBR_NM + ' : ' + feature.properties.KOR_SUB_NM);
    }
});

var Metroline5 = L.geoJson(metro, {
    filter: function (feature, layer) {
        if (feature.properties.KOR_SBR_NM == '5호선') return true;
    },
    onEachFeature: function (feature, layer) {
        layer.setIcon(layer.options.icon = line5icon),
            layer.bindPopup(feature.properties.KOR_SBR_NM + ' : ' + feature.properties.KOR_SUB_NM);
    }
});

var Metroline6 = L.geoJson(metro, {
    filter: function (feature, layer) {
        if (feature.properties.KOR_SBR_NM == '6호선') return true;
    },
    onEachFeature: function (feature, layer) {
        layer.setIcon(layer.options.icon = line6icon),
            layer.bindPopup(feature.properties.KOR_SBR_NM + ' : ' + feature.properties.KOR_SUB_NM);
    }
});

var Metroline7 = L.geoJson(metro, {
    filter: function (feature, layer) {
        if (feature.properties.KOR_SBR_NM == '7호선') return true;
    },
    onEachFeature: function (feature, layer) {
        layer.setIcon(layer.options.icon = line7icon),
            layer.bindPopup(feature.properties.KOR_SBR_NM + ' : ' + feature.properties.KOR_SUB_NM);
    }
});

var Metroline8 = L.geoJson(metro, {
    filter: function (feature, layer) {
        if (feature.properties.KOR_SBR_NM == '8호선') return true;
    },
    onEachFeature: function (feature, layer) {
        layer.setIcon(layer.options.icon = line8icon),
            layer.bindPopup(feature.properties.KOR_SBR_NM + ' : ' + feature.properties.KOR_SUB_NM);
    }
});

var Metroline9 = L.geoJson(metro, {
    filter: function (feature, layer) {
        if (feature.properties.KOR_SBR_NM == '9호선') return true;
    },
    onEachFeature: function (feature, layer) {
        layer.setIcon(layer.options.icon = line9icon),
            layer.bindPopup(feature.properties.KOR_SBR_NM + ' : ' + feature.properties.KOR_SUB_NM);
    }
});

var AirportLine = L.geoJson(metro, {
    filter: function (feature, layer) {
        if (feature.properties.KOR_SBR_NM == '공항철도') return true;
    },
    onEachFeature: function (feature, layer) {
        layer.setIcon(layer.options.icon = airporticon),
            layer.bindPopup(feature.properties.KOR_SBR_NM + ' : ' + feature.properties.KOR_SUB_NM);
    }
});

var Bundangline = L.geoJson(metro, {
    filter: function (feature, layer) {
        if (feature.properties.KOR_SBR_NM == '분당선') return true;
    },
    onEachFeature: function (feature, layer) {
        layer.setIcon(layer.options.icon = bundangicon),
            layer.bindPopup(feature.properties.KOR_SBR_NM + ' : ' + feature.properties.KOR_SUB_NM);
    }
});

var newbundangline = L.geoJson(metro, {
    filter: function (feature, layer) {
        if (feature.properties.KOR_SBR_NM == '신분당선') return true;
    },
    onEachFeature: function (feature, layer) {
        layer.setIcon(layer.options.icon = newbundangicon),
            layer.bindPopup(feature.properties.KOR_SBR_NM + ' : ' + feature.properties.KOR_SUB_NM);
    }
});

var Middleline = L.geoJson(metro, {
    filter: function (feature, layer) {
        if (feature.properties.KOR_SBR_NM == '중앙선' || feature.properties.KOR_SBR_NM == '경춘선' || feature.properties.KOR_SBR_NM == '경의선') return true;
    },
    onEachFeature: function (feature, layer) {
        layer.setIcon(layer.options.icon = midkyungicon),
            layer.bindPopup(feature.properties.KOR_SBR_NM + ' : ' + feature.properties.KOR_SUB_NM);
    }
});


var baseMaps = {
    "Base": Base,
    "Hybrid": Hybrid,
    "Satelite": satelite,

};

var overlayMaps = {
    '동별 위치보기': markers,
    '1호선': Metroline1,
    '2호선': Metroline2,
    '3호선': Metroline3,
    '4호선': Metroline4,
    '5호선': Metroline5,
    '6호선': Metroline6,
    '7호선': Metroline7,
    '8호선': Metroline8,
    '9호선': Metroline9,
    '분당선': Bundangline,
    '신분당선': newbundangline,
    '경의·중앙·경춘선': Middleline,

};


L.control.layers(baseMaps, overlayMaps, { collapsed: true }).addTo(map);

var ReversablePlan = L.Routing.Plan.extend({

    createGeocoders: function () {
        var container = L.Routing.Plan.prototype.createGeocoders.call(this),
            reverseButton = createbutton('↑↓', container);

        L.DomEvent.on(reverseButton, 'click', function () { var waypoints = this.getWaypoints(); this.setWaypoints(waypoints.reverse()); }, this);

        return container;
    }
});


var plan = new ReversablePlan([
    L.latLng(37.504417, 127.024450),
    L.latLng(37.531829, 127.067072)
], {
        geocoder: L.Control.Geocoder.nominatim(),
        routeWhileDragging: true
    }),
    control = L.Routing.control({
        routeWhileDragging: true,
        plan: plan,
        router: L.Routing.graphHopper('bf505191-5b79-4695-9dd5-0cd5bdedd270'),
    }).addTo(map);


// Find distance!
var dist = control.on('routesfound', function (e) {
    var routes = e.routes;
    document.getElementById('getdistance').innerHTML = Math.floor(routes[0].summary.totalDistance / 10) / 100 + 'km';
});

// Find distance!
var dist = control.on('routesfound', function (e) {
    var routes = e.routes;
    document.getElementById('getdistance').innerHTML = Math.floor(routes[0].summary.totalDistance / 10) / 100 + 'km';
});
// 차종류 선택
$(document).ready(function () {

    // Default dropdown action to show/hide dropdown content
    $('.js-dropp-action').click(function (e) {
        e.preventDefault();
        $(this).toggleClass('js-open');
        $(this).parent().next('.dropp-body').toggleClass('js-open');
    });

    // Using as fake input select dropdown
    $('label').click(function () {
        $(this).addClass('js-open').siblings().removeClass('js-open');
        $('.dropp-body,.js-dropp-action').removeClass('js-open');
    });
    // get the value of checked input radio and display as dropp title
    $('input[name="dropp"]').change(function () {
        var value = $("input[name='dropp']:checked").val();
        $('.js-value').text(value);
    });


    // 자동차 CC선택
    // Default dropdown action to show/hide dropdown content
    $('.js-ch1-action').click(function (e) {
        e.preventDefault();
        $(this).toggleClass('js-open');
        $(this).parent().next('.ch1-body').toggleClass('js-open');
    });

    // Using as fake input select dropdown
    $('label').click(function () {
        $(this).addClass('js-open').siblings().removeClass('js-open');
        $('.ch1-body,.js-ch1-action').removeClass('js-open');
    });
    // get the value of checked input radio and display as dropp title
    $('input[name="ch1"]').change(function () {
        var value1 = $("input[name='ch1']:checked").val();
        $('.ch1-value').text(value1);
    });

    // 동승인원 선택

    // Default dropdown action to show/hide dropdown content
    $('.js-dropp-action').click(function (e) {
        e.preventDefault();
        $(this).toggleClass('js-open');
        $(this).parent().next('.people-body').toggleClass('js-open');
    });

    // Using as fake input select dropdown
    $('label').click(function () {
        $(this).addClass('js-open').siblings().removeClass('js-open');
        $('.people-body,.js-dropp-action').removeClass('js-open');
    });
    // get the value of checked input radio and display as dropp title
    $('input[name="people"]').change(function () {
        var value2 = $("input[name='people']:checked").val();
        $('.people-value').text(value2);
    });

    // 이용 요일 횟수 선택

    // Default dropdown action to show/hide dropdown content
    $('.js-dropp-action').click(function (e) {
        e.preventDefault();
        $(this).toggleClass('js-open');
        $(this).parent().next('.week-body').toggleClass('js-open');
    });

    // Using as fake input select dropdown
    $('label').click(function () {
        $(this).addClass('js-open').siblings().removeClass('js-open');
        $('.week-body,.js-dropp-action').removeClass('js-open');
    });
    // get the value of checked input radio and display as dropp title
    $('input[name="week"]').change(function () {
        var value3 = $("input[name='week']:checked").val();
        $('.week-value').text(value3);
    });


});


var Seoul_dong = L.geoJson(seouldong, {
    onEachFeature: function (feature, layer) {
        layer.bindPopup('동 : ' + feature.properties.EA004_NAM)
    }
});


var geojson = L.geoJson(seouldong, {
    onEachFeature: function (feature, layer) {
        if (feature.geometry.type === 'Polygon') {
            var centroid = turf.centroid(feature);
            var lon = centroid.geometry.coordinates[0];
            var lat = centroid.geometry.coordinates[1];
            var markerinCl = L.marker([lat, lon], { icon: carIcon });
            markerinCl.bindPopup(feature.properties.DONG_NAME);
            markers.addLayer(markerinCl);
            return markerinCl;
        }
    }
});