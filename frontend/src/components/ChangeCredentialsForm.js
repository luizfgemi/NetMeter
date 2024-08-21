import React, { useState } from 'react';
import axios from 'axios';

const backendUrl = `${window.location.protocol}//${window.location.hostname}:${window.location.port}`;

function ChangeCredentialsForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const changeCredentials = () => {
    axios.post(`${backendUrl}/change_credentials`, { username, password })
      .then(response => alert(response.data.message))
      .catch(error => console.error('There was an error changing the credentials!', error));
  };

  return (
    <div>
      <h2>Change Credentials</h2>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Enter new username"
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Enter new password"
      />
      <button onClick={changeCredentials}>Update Credentials</button>
    </div>
  );
}

export default ChangeCredentialsForm;
