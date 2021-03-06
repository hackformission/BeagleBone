var url = 'http://localhost:8888';

var submitButton = document.getElementById("createEvent");

submitButton.addEventListener("click", function () {
  //TimeStamp in Coordinated Universal Time (UTC) YYYY-MM-DDThh:mm
  //Add the time zone later *********** (look up format at : https://en.wikipedia.org/wiki/ISO_8601)
  //Should be "YYYY-MM-DD hh:mm" +/- TimeOffset (hh:mm)
  //Ex: 2019-01-01 00:00+01:00 OR 2000-05-31 :07:34-11:00

  var eventData = {
      "filename" : document.getElementById("eventName").value,
      "timestamp" : document.getElementById("eventDate").value + " " + document.getElementById("eventHours").value + ":" + document.getElementById("eventMinutes").value,
      "frequency" : document.getElementById("eventFrequency").value,
      "hostname" : document.getElementById("ipAddr").value,
      "port" : document.getElementById("eventPort").value,
      "band" : document.getElementById("eventBand").value,
      "duration" : (60 * document.getElementById("eventDurationMinutes").value) + (1 * document.getElementById("eventDurationSeconds").value)
    };
	console.log(eventData);
	
    fetch(url, {
      method: 'POST', // or 'PUT'
      body: JSON.stringify(eventData), // data can be `string` or {object}!
      headers:{
        'Content-Type': 'application/json'
      }
    }).then(res => console.log(res))
    .then(response => console.log('Success:', JSON.stringify(response)))
    .catch(error => console.error('Error:', error));
});
