import { useState } from 'react';

export default function SqlTuning() {
  const [query, setQuery] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:8000/tune', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
      });
      const data = await response.json();
      setResult(data.optimized_query || JSON.stringify(data));
    } catch (error) {
      setResult('Error: ' + error.message);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>SQL Tuning Tool</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          rows="5"
          cols="60"
          placeholder="Enter your SQL Query..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <br />
        <button type="submit" disabled={loading}>
          {loading ? 'Tuning...' : 'Tune Query'}
        </button>
      </form>
      <div>
        <h3>Optimized Query:</h3>
        <pre>{result}</pre>
      </div>
    </div>
  );
}
