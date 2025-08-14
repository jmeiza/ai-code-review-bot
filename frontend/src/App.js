import { useState } from "react";
import './App.css';

const App = () => {
  const [code, setCode] = useState("");
  const [review, setReview] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/review", {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify({ code })
      });
      const data = await res.json();
      setReview(data);
    }
    catch (err) {
      console.error(err)
      setReview({ error: "Something went wrong" });
    }
    setLoading(false);
  };

  return (
    <div className="app-container">
      <h1>AI Code Review</h1>
      <textarea
        className="code-input"
        value={code} 
        onChange={(e) => setCode(e.target.value)}
        placeholder="Paste your Python code here..."
      ></textarea>
      <button className="submit-btn" onClick={handleSubmit} disabled={loading}>
        {loading ? "Reviewing..." : "Review Code"}
      </button>

      {review && (
        <div className="review-container">
          {["bugs", "optimizations", "style", "suggestions"].map((category) => (
            <div className="review-category" key={category}>
              <h2>{category.charAt(0).toUpperCase() + category.slice(1)}</h2>
              {review[category]?.length ? (
                review[category].map((item, idx) => (
                  <div className="review-item" key={idx}>
                    <p><strong>Issue:</strong> {item.issue}</p>
                    <p>
                      <strong>Severity:</strong>{" "}
                      <span className={
                        item.severity === "high"
                        ? "severity-high"
                        : item.severity === "medium"
                        ? "severity-medium"
                        : "severity-low"
                      }>
                        {item.severity}
                      </span> 
                    </p>
                    <p><strong>suggestions:</strong> {item.suggestions}</p>
                  </div>
                ))
              ) : (
                <p>No items</p>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;