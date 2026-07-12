import React, { useState } from "react";
import "./App.css";

function App() {
  const API_BASE = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [domainAge, setDomainAge] = useState(null);

  const checkUrl = async () => {
    if (!url) return;
    setLoading(true);
    setResult(null);
    setDomainAge(null);

    try {
      const response = await fetch(`${API_BASE}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();
      setResult(data.prediction);

      // Dummy domain age feature (replace later with real API call)
      const randomAge = Math.floor(Math.random() * 10) + 1; // 1–10 years
      setDomainAge(`${randomAge} years`);
    } catch (error) {
      setResult("Error connecting to backend ❌");
    }
    setLoading(false);
  };

  return (
    <div className="awwwards-container">
      {/* Navbar */}
      <nav className="navbar">
        <div className="logo">
          <span className="glow">URL</span>Detector
        </div>
        <div className="nav-links">
          <a href="#">Docs</a>
          <a href="#">API</a>
        </div>
      </nav>

      {/* Hero Section */}
      <header className="hero">
        <h1>
          Is your <span className="highlight">link</span> safe?
        </h1>
        <p className="subtitle">
          Real-time scam detection powered by AI. Identify phishing, fake
          stores, and malware before you click.
        </p>
      </header>

      {/* Scanner Box */}
      <div className="scanner-card">
        <div className="scanner">
          <input
            type="text"
            placeholder="Paste your URL here..."
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />
          <button onClick={checkUrl} disabled={loading}>
            {loading ? "Analyzing..." : "Check URL"}
          </button>
        </div>
      </div>

      {/* Result Section */}
      {result && (
        <div
          className={`result-box ${
            result.toLowerCase().includes("phish") ? "phish" : "legit"
          }`}
        >
          {result.toLowerCase().includes("phish") ? (
            <p>🚨 Scam / Phishing Detected</p>
          ) : result === "Error connecting to backend ❌" ? (
            <p>{result}</p>
          ) : (
            <p>✅ Legitimate Website</p>
          )}
        </div>
      )}

      {/* Footer */}
      <footer className="footer">
        <p>© 2025 URL Detector⚡</p>
      </footer>
    </div>
  );
}

export default App;
