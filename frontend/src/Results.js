import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Results() {
  const [results, setResults] = useState([]);

  useEffect(() => {
    const stored = JSON.parse(localStorage.getItem("results")) || [];
    setResults(stored);
  }, []);

  return (
    <div className="awwwards-container">
      {/* Navbar */}
      <nav className="navbar">
        <div className="logo">URL<span>Detector</span></div>
        <div className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/analytics">Analytics</Link>
        </div>
      </nav>

      <header className="hero">
        <h1>Scan Results</h1>
      </header>

      <div className="results-table">
        <table>
          <thead>
            <tr>
              <th>URL</th>
              <th>Prediction</th>
              <th>Timestamp</th>
            </tr>
          </thead>
          <tbody>
            {results.length === 0 ? (
              <tr>
                <td colSpan="3">No results yet</td>
              </tr>
            ) : (
              results.map((r, index) => (
                <tr key={index}>
                  <td>{r.url}</td>
                  <td>{r.prediction}</td>
                  <td>{new Date(r.timestamp).toLocaleString()}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      <footer className="footer">
        <p>© 2025 URL Detector.</p>
      </footer>
    </div>
  );
}

export default Results;
