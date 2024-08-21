import React from 'react';
import SpeedtestForm from './components/SpeedtestForm';
import CronJobForm from './components/CronJobForm';
import ResultsTable from './components/ResultsTable';
import ChangeCredentialsForm from './components/ChangeCredentialsForm';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>NetMeter Dashboard</h1>
      </header>
      <main>
        <section className="form-section">
          <SpeedtestForm />
          <CronJobForm />
          <ChangeCredentialsForm />
        </section>
        <section className="results-section">
          <ResultsTable />
        </section>
      </main>
    </div>
  );
}

export default App;
