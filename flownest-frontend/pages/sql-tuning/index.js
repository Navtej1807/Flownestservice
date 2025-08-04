import React, { useState } from 'react';
import axios from 'axios';

export default function SqlTuning() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await axios.post('https://flownestservice.onrender.com/tune', { query });

      setResponse(res.data);
    } catch (error) {
      console.error('Error:', error);
      setResponse({ optimized_query: 'Error tuning SQL. Please try again.' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>SQL Tuning Tool</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          rows="6"
          cols="80"
          placeholder="Enter SQL Query here..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        ></textarea>
        <br />
        <button type="submit" disabled={loading}>
          {loading ? 'Tuning...' : 'Tune Query'}
        </button>
      </form>

      {response && response.optimized_query && (
        <div style={{ marginTop: '20px' }}>
          <h3>Optimized Query:</h3>
          <pre>{response.optimized_query}</pre>
        </div>
      )}
    </div>
  );
}
