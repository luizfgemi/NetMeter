import React from 'react';
import axios from 'axios';

// Use window.location para construir a URL base dinamicamente
const backendUrl = `${window.location.protocol}//${window.location.hostname}:${window.location.port}`;

function SpeedtestForm() {
  const runSpeedtest = () => {
    axios.get(`${backendUrl}/speedtest`)
      .then(response => alert(response.data.message))
      .catch(error => console.error('There was an error running the speedtest!', error));
  };

  return (
    <div>
      <h2>Run Speedtest</h2>
      <button onClick={runSpeedtest}>Run Speedtest Now</button>
    </div>
  );
}

export default SpeedtestForm;
