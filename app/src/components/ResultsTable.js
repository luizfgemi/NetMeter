import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Use window.location para construir a URL base dinamicamente
const backendUrl = `${window.location.protocol}//${window.location.hostname}:${window.location.port}`;

function ResultsTable() {
  const [results, setResults] = useState([]);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchResults(page);
  }, [page]);

  const fetchResults = (page) => {
    setLoading(true);
    axios.get(`${backendUrl}/results?page=${page}`)
      .then(response => {
        setResults(response.data.results);
        setLoading(false);
      })
      .catch(error => {
        console.error('There was an error fetching the results!', error);
        setLoading(false);
      });
  };

  const handleNextPage = () => {
    setPage(page + 1);
  };

  const handlePreviousPage = () => {
    if (page > 1) {
      setPage(page - 1);
    }
  };

  return (
    <div>
      <h2>Speedtest Results</h2>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Timestamp</th>
              <th>Download Speed (Mbps)</th>
              <th>Upload Speed (Mbps)</th>
              <th>Ping (ms)</th>
            </tr>
          </thead>
          <tbody>
            {results.map(result => (
              <tr key={result.id}>
                <td>{result.timestamp}</td>
                <td>{result.download_speed}</td>
                <td>{result.upload_speed}</td>
                <td>{result.ping}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
      <div>
        <button onClick={handlePreviousPage} disabled={page === 1}>Previous</button>
        <button onClick={handleNextPage} disabled={results.length === 0}>Next</button>
      </div>
    </div>
  );
}

export default ResultsTable;
