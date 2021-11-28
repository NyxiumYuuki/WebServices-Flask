var globalCurrent = null;
var globalForecast = null;

var WEATHER_METEOCONCEPT = {
    0: "Soleil",
    1: "Peu nuageux",
    2: "Ciel voilé",
    3: "Nuageux",
    4: "Très nuageux",
    5: "Couvert",
    6: "Brouillard",
    7: "Brouillard givrant",
    10: "Pluie faible",
    11: "Pluie modérée",
    12: "Pluie forte",
    13: "Pluie faible verglaçante",
    14: "Pluie modérée verglaçante",
    15: "Pluie forte verglaçante",
    16: "Bruine",
    20: "Neige faible",
    21: "Neige modérée",
    22: "Neige forte",
    30: "Pluie et neige mêlées faibles",
    31: "Pluie et neige mêlées modérées",
    32: "Pluie et neige mêlées fortes",
    40: "Averses de pluie locales et faibles",
    41: "Averses de pluie locales",
    42: "Averses locales et fortes",
    43: "Averses de pluie faibles",
    44: "Averses de pluie",
    45: "Averses de pluie fortes",
    46: "Averses de pluie faibles et fréquentes",
    47: "Averses de pluie fréquentes",
    48: "Averses de pluie fortes et fréquentes",
    60: "Averses de neige localisées et faibles",
    61: "Averses de neige localisées",
    62: "Averses de neige localisées et fortes",
    63: "Averses de neige faibles",
    64: "Averses de neige",
    65: "Averses de neige fortes",
    66: "Averses de neige faibles et fréquentes",
    67: "Averses de neige fréquentes",
    68: "Averses de neige fortes et fréquentes",
    70: "Averses de pluie et neige mêlées localisées et faibles",
    71: "Averses de pluie et neige mêlées localisées",
    72: "Averses de pluie et neige mêlées localisées et fortes",
    73: "Averses de pluie et neige mêlées faibles",
    74: "Averses de pluie et neige mêlées",
    75: "Averses de pluie et neige mêlées fortes",
    76: "Averses de pluie et neige mêlées faibles et nombreuses",
    77: "Averses de pluie et neige mêlées fréquentes",
    78: "Averses de pluie et neige mêlées fortes et fréquentes",
    100: "Orages faibles et locaux",
    101: "Orages locaux",
    102: "Orages fort et locaux",
    103: "Orages faibles",
    104: "Orages",
    105: "Orages forts",
    106: "Orages faibles et fréquents",
    107: "Orages fréquents",
    108: "Orages forts et fréquents",
    120: "Orages faibles et locaux de neige ou grésil",
    121: "Orages locaux de neige ou grésil",
    122: "Orages locaux de neige ou grésil",
    123: "Orages faibles de neige ou grésil",
    124: "Orages de neige ou grésil",
    125: "Orages de neige ou grésil",
    126: "Orages faibles et fréquents de neige ou grésil",
    127: "Orages fréquents de neige ou grésil",
    128: "Orages fréquents de neige ou grésil",
    130: "Orages faibles et locaux de pluie et neige mêlées ou grésil",
    131: "Orages locaux de pluie et neige mêlées ou grésil",
    132: "Orages fort et locaux de pluie et neige mêlées ou grésil",
    133: "Orages faibles de pluie et neige mêlées ou grésil",
    134: "Orages de pluie et neige mêlées ou grésil",
    135: "Orages forts de pluie et neige mêlées ou grésil",
    136: "Orages faibles et fréquents de pluie et neige mêlées ou grésil",
    137: "Orages fréquents de pluie et neige mêlées ou grésil",
    138: "Orages forts et fréquents de pluie et neige mêlées ou grésil",
    140: "Pluies orageuses",
    141: "Pluie et neige mêlées à caractère orageux",
    142: "Neige à caractère orageux",
    210: "Pluie faible intermittente",
    211: "Pluie modérée intermittente",
    212: "Pluie forte intermittente",
    220: "Neige faible intermittente",
    221: "Neige modérée intermittente",
    222: "Neige forte intermittente",
    230: "Pluie et neige mêlées",
    231: "Pluie et neige mêlées",
    232: "Pluie et neige mêlées",
    235: "Averses de grêle",
}

// Maps the API's icons to the ones from https://erikflowers.github.io/weather-icons/
var weatherIconsMap = {
    0: "wi-day-sunny",
    1: "wi-day-cloudy",
    2: "wi-day-cloudy-high",
    3: "wi-cloud",
    4: "wi-cloudy",
    5: "wi-day-cloudy",
    6: "wi-fog",
    7: "wi-day-fog",
    10: "wi-day-hail",
    11: "wi-day-rain-mix",
    12: "wi-day-rain",
    13: "wi-day-rain-mix",
    14: "wi-day-showers",
    15: "wi-day-rain-mix",
    16: "wi-day-sprinkle",
    20: "wi-day-snow-wind",
    21: "wi-day-snow",
    22: "wi-day-snow",
    30: "wi-rain-mix",
    31: "wi-showers",
    32: "wi-showers",
    40: "wi-day-sleet",
    41: "wi-day-sleet",
    42: "wi-day-showers",
    43: "wi-day-showers",
    44: "wi-day-showers",
    45: "wi-day-showers",
    46: "wi-day-hail",
    47: "wi-day-hail",
    48: "wi-day-rain",
    60: "wi-day-snow-wind",
    61: "wi-day-snow-wind",
    62: "wi-day-snow",
    63: "wi-day-snow",
    64: "wi-day-snow",
    65: "wi-day-snow",
    66: "wi-day-snow",
    67: "wi-day-snow",
    68: "wi-day-snow",
    70: "wi-day-sleet",
    71: "wi-day-sleet",
    72: "wi-day-sleet",
    73: "wi-day-sleet",
    74: "wi-day-sleet",
    75: "wi-day-sleet",
    76: "wi-day-sleet",
    77: "wi-day-sleet",
    78: "wi-day-sleet",
    100: "wi-day-lightning",
    101: "wi-day-lightning",
    102: "wi-day-lightning",
    103: "wi-day-lightning",
    104: "wi-day-lightning",
    105: "wi-day-lightning",
    106: "wi-day-lightning",
    107: "wi-day-lightning",
    108: "wi-day-lightning",
    120: "wi-day-snow-thunderstorm",
    121: "wi-day-snow-thunderstorm",
    122: "wi-day-snow-thunderstorm",
    123: "wi-day-snow-thunderstorm",
    124: "wi-day-snow-thunderstorm",
    125: "wi-day-snow-thunderstorm",
    126: "wi-day-snow-thunderstorm",
    127: "wi-day-snow-thunderstorm",
    128: "wi-day-snow-thunderstorm",
    130: "wi-day-snow-thunderstorm",
    131: "wi-day-snow-thunderstorm",
    132: "wi-day-snow-thunderstorm",
    133: "wi-day-snow-thunderstorm",
    134: "wi-day-snow-thunderstorm",
    135: "wi-day-snow-thunderstorm",
    136: "wi-day-snow-thunderstorm",
    137: "wi-day-snow-thunderstorm",
    138: "wi-day-snow-thunderstorm",
    140: "wi-storm-showers",
    141: "wi-storm-showers",
    142: "wi-thunderstorm",
    210: "wi-hail",
    211: "wi-hail",
    212: "wi-showers",
    220: "wi-sleet",
    221: "wi-sleet",
    222: "wi-snow",
    230: "wi-snow-wind",
    231: "wi-snow-winds",
    232: "wi-snow-wind",
    235: "wi-sprinkle",
}

$(function(){
  startClock();
});


function startClock(){
  setInterval(function(){
    $("#localTime").text(new Date().toLocaleTimeString());
  }, 1000);
}


function getWeatherData(insee){
  $.ajax({
    type: "GET",
    url: "/current"+"?query="+insee,
    cache: true,
    headers: {
      "Access-Control-Allow-Headers": "x-requested-with"
    },
    success: function(current){
      globalCurrent = current;
      updateCurrent(current);
    },
    error: function(error){
      console.log("Error with ajax: "+ error);
    }
  });
}


function getForecastData(insee){
  $.ajax({
    type: "GET",
    url: "/forecast"+"?query="+insee,
    cache: true,
    headers: {
      "Access-Control-Allow-Headers": "x-requested-with"
    },
    success: function(forecast){
      globalForecast = forecast;
      updateForecast(forecast);

      // Stops Refresh button's spinning animation
      $("#refreshButton").html("<i class='fa fa-refresh fa-fw'></i> Refresh");
    },
    error: function(error){
      console.log("Error with ajax: "+ error);
    }
  });
}

// Update view values from current
function updateCurrent(current){
  // Present day
  var today = current.current.METEOCONCEPT.observation;
  $("#humidity").text(today.humidity.value);
  $("#wind").text(today.wind_s.value);
  $("#localDate").text(getFormattedDate(today.time));
  $("#mainTemperature").text(Math.round(today.temperature.value));
}

// Update view values from passed forecast
function updateForecast(forecast){
  // Info City
  var city = forecast.forecast.METEOCONCEPT.city;
  $("#cityName").text(city.name);
  $("#cityCode").text(city.cp);
  var data = forecast.forecast.METEOCONCEPT.forecast;
  console.log(data);

  // Present day
  var today = data[0];
  $("#tempDescription").text(toCamelCase(WEATHER_METEOCONCEPT[today.weather]));
  $("#main-icon").addClass(weatherIconsMap[today.weather]);
  $("#mainTempHot").text(Math.round(today.tmax));
  $("#mainTempLow").text(Math.round(today.tmin));


  // Following days data
  for(var i = 1; i < (data.length); i++){
    var day = data[i];

    // Day short format e.g. Mon
    var dayName = getFormattedDate(day.datetime).substring(0,3);

    // weather icon from map
    var weatherIcon = weatherIconsMap[day.weather];

    $("#forecast-day-" + i + "-name").text(dayName);
    $("#forecast-day-" + i + "-icon").addClass(weatherIcon);
    $("#forecast-day-" + i + "-main").text(Math.round((day.tmax+day.tmin)/2));
    $("#forecast-day-" + i + "-ht").text(Math.round(day.tmax));
    $("#forecast-day-" + i + "-lt").text(Math.round(day.tmin));
  }
}

// Refresh button handler
$("#refreshButton").on("click", function(){
  // Starts Refresh button's spinning animation
  $("#refreshButton").html("<i class='fa fa-refresh fa-spin fa-fw'></i>");
  getWeatherData();
  getForecastData();
});

// Applies the following format to date: WeekDay, Month Day, Year
function getFormattedDate(date){
  var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(date).toLocaleDateString("fr-FR",options);
}


// Formats the text to CamelCase
function toCamelCase(str) {
  var arr = str.split(" ").map(
    function(sentence){
      return sentence.charAt(0).toUpperCase() + sentence.substring(1);
    }
  );
  return arr.join(" ");
}


// Converts to Celcius
function toCelcius(val){
  return Math.round((val - 32) * (5/9));
}