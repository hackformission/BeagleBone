var url = 'http://localhost:8888';

var submitButton = document.getElementById("createEvent");

submitButton.addEventListener("click", function () {
  //TimeStamp in Coordinated Universal Time (UTC) YYYY-MM-DDThh:mm
  //Add the time zone later *********** (look up format at : https://en.wikipedia.org/wiki/ISO_8601)
  //Should be "YYYY-MM-DDThh:mm" +/- TimeOffset (hh:mm)
  //Ex: 2019-01-01T00:00+01:00 OR 2000-05-31T:07:34-11:00

  var eventData = {
      "eventName" : document.getElementById("eventName").value,
      "eventTimeStamp" : document.getElementById("eventTime").value + " " + document.getElementById("eventDate").value +  ":00",
      "eventFrequency" : document.getElementById("eventFrequency").value,
      "eventDuration" : document.getElementById("eventDuration").value,
      "eventRepeat" : document.getElementById("eventRepeat").value
    };

    fetch(url, {
      method: 'POST', // or 'PUT'
      body: JSON.stringify(eventData), // data can be `string` or {object}!
      headers:{
        'Content-Type': 'application/json'
      }
    }).then(res => res.json())
    .then(response => console.log('Success:', JSON.stringify(response)))
    .catch(error => console.error('Error:', error));
});
