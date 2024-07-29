document.addEventListener('DOMContentLoaded', function () {
  var latField = document.getElementById('id_lat');
  var lngField = document.getElementById('id_lng');
  var map = L.map('map').setView([41.3275, 69.2817], 12);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  var marker = L.marker([latField.value || 41.3275, lngField.value || 69.2817]).addTo(map);

  map.on('click', function (e) {
      marker.setLatLng(e.latlng);
      latField.value = e.latlng.lat;
      lngField.value = e.latlng.lng;
  });

  latField.addEventListener('change', function () {
      var lat = parseFloat(latField.value);
      var lng = parseFloat(lngField.value);
      marker.setLatLng([lat, lng]);
      map.setView([lat, lng], 12);
  });

  lngField.addEventListener('change', function () {
      var lat = parseFloat(latField.value);
      var lng = parseFloat(lngField.value);
      marker.setLatLng([lat, lng]);
      map.setView([lat, lng], 12);
  });
});
