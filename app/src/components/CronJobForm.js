import React, { useState } from 'react';
import axios from 'axios';

// Use window.location para construir a URL base dinamicamente
const backendUrl = `${window.location.protocol}//${window.location.hostname}:${window.location.port}`;

function CronJobForm() {
  const [minutes, setMinutes] = useState('');

  const scheduleSpeedtest = () => {
    axios.post(`${backendUrl}/schedule_test_custom/${minutes}`)
      .then(response => alert(response.data.message))
      .catch(error => console.error('There was an error scheduling the speedtest!', error));
  };

  return (
    <div>
      <h2>Schedule Speedtest</h2>
      <input
        type="number"
        value={minutes}
        onChange={(e) => setMinutes(e.target.value)}
        placeholder="Enter minutes"
      />
      <button onClick={scheduleSpeedtest}>Schedule Speedtest</button>
    </div>
  );
}

export default CronJobForm;
