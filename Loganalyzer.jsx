import { useState } from "react";

const COLORS = [
  "#00FF94", "#00D4FF", "#FF6B35", "#FFD700", "#FF3CAC", "#A8FF3E"
];

function analyzeLog(text) {
  if (!text.trim()) return [];
  const words = text
    .split(/\s+/)
    .map(w => w.replace(/[^a-zA-Z0-9_:.-]/g, ""))
    .filter(w => w.length > 0);
  const freq = {};
  words.forEach(w => { freq[w] = (freq[w] || 0) + 1; });
  return Object.entries(freq)
    .sort((a, b) => b[1] - a[1])
    .map(([pattern, count], i) => ({ pattern, count, color: COLORS[i % COLORS.length] }));
}

export default function LogAnalyzer() {
  const [input, setInput] = useState("");
  const [results, setResults] = useState([]);
  const [analyzed, setAnalyzed] = useState(false);

  const handleAnalyze = () => {
    const r = analyzeLog(input);
    setResults(r);
    setAnalyzed(true);
  };

  const maxCount = results[0]?.count || 1;

  return (
    <div style={{
      minHeight: "100vh",
      background: "#0a0a0f",
      color: "#e8e8f0",
      fontFamily: "'Courier New', 'Lucida Console', monospace",
      padding: "0",
      margin: "0",
    }}>
      {/* Header */}
      <div style={{
        borderBottom: "1px solid #1e1e2e",
        padding: "24px 40px",
        display: "flex",
        alignItems: "center",
        gap: "16px",
        background: "#0d0d16",
      }}>
        <div style={{
          width: 10, height: 10, borderRadius: "50%",
          background: "#00FF94", boxShadow: "0 0 12px #00FF94",
        }} />
        <span style={{ fontSize: 11, letterSpacing: 4, color: "#555", textTransform: "uppercase" }}>
          SRE-1
        </span>
        <span style={{ fontSize: 11, letterSpacing: 4, color: "#333", marginLeft: "auto" }}>
          LOG PATTERN ANALYZER
        </span>
      </div>

      <div style={{ padding: "40px", maxWidth: 960, margin: "0 auto" }}>
        {/* Title */}
        <div style={{ marginBottom: 40 }}>
          <h1 style={{
            fontSize: "clamp(28px, 5vw, 52px)",
            fontWeight: 900,
            letterSpacing: -1,
            margin: 0,
            lineHeight: 1,
            color: "#fff",
          }}>
            LOG<span style={{ color: "#00FF94" }}>.</span>PATTERN
            <span style={{ display: "block", color: "#333", fontSize: "0.55em", letterSpacing: 6, fontWeight: 400, marginTop: 4 }}>
              FREQUENCY ANALYZER ──────────────────
            </span>
          </h1>
        </div>

        {/* Input area */}
        <div style={{ marginBottom: 24 }}>
          <label style={{
            display: "block", fontSize: 10, letterSpacing: 3,
            color: "#555", marginBottom: 10, textTransform: "uppercase"
          }}>
            ▸ Paste Log Content
          </label>
          <textarea
            value={input}
            onChange={e => setInput(e.target.value)}
            placeholder={`INFO   read_physical_table: message 1  This is test mail\nINFO   read_physical_data: message 2  Lets plan outdoor trip\nINFO   read_physical_memory: message 3 : Goa is the best`}
            style={{
              width: "100%",
              minHeight: 180,
              background: "#0d0d16",
              border: "1px solid #1e1e2e",
              borderLeft: "3px solid #00FF94",
              color: "#a0ffc0",
              fontFamily: "inherit",
              fontSize: 13,
              padding: "16px 20px",
              resize: "vertical",
              outline: "none",
              lineHeight: 1.7,
              boxSizing: "border-box",
              caretColor: "#00FF94",
            }}
            spellCheck={false}
          />
        </div>

        <button
          onClick={handleAnalyze}
          style={{
            background: "transparent",
            border: "1px solid #00FF94",
            color: "#00FF94",
            fontFamily: "inherit",
            fontSize: 11,
            letterSpacing: 4,
            textTransform: "uppercase",
            padding: "12px 32px",
            cursor: "pointer",
            marginBottom: 48,
            transition: "all 0.2s",
            position: "relative",
          }}
          onMouseEnter={e => {
            e.target.style.background = "#00FF94";
            e.target.style.color = "#000";
          }}
          onMouseLeave={e => {
            e.target.style.background = "transparent";
            e.target.style.color = "#00FF94";
          }}
        >
          ▶ Analyze Patterns
        </button>

        {/* Results */}
        {analyzed && (
          <div>
            <div style={{
              display: "flex", justifyContent: "space-between",
              alignItems: "baseline", marginBottom: 20
            }}>
              <span style={{ fontSize: 10, letterSpacing: 3, color: "#555", textTransform: "uppercase" }}>
                ▸ Pattern Frequency — Descending
              </span>
              <span style={{ fontSize: 10, color: "#333" }}>
                {results.length} unique patterns
              </span>
            </div>

            {results.length === 0 ? (
              <div style={{ color: "#333", fontSize: 13 }}>No patterns found.</div>
            ) : (
              <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                {results.map(({ pattern, count, color }, i) => (
                  <div key={pattern} style={{
                    display: "flex", alignItems: "center", gap: 16,
                    padding: "10px 0",
                    borderBottom: "1px solid #111",
                    animation: `fadeIn 0.3s ease ${i * 0.02}s both`,
                  }}>
                    {/* Rank */}
                    <span style={{
                      width: 28, textAlign: "right",
                      fontSize: 10, color: "#333", flexShrink: 0
                    }}>
                      {String(i + 1).padStart(2, "0")}
                    </span>

                    {/* Pattern name */}
                    <span style={{
                      width: 200, fontSize: 13, color: "#ccc",
                      overflow: "hidden", textOverflow: "ellipsis",
                      whiteSpace: "nowrap", flexShrink: 0,
                    }}>
                      {pattern}
                    </span>

                    {/* Bar */}
                    <div style={{
                      flex: 1, height: 6,
                      background: "#111", borderRadius: 2, overflow: "hidden"
                    }}>
                      <div style={{
                        height: "100%",
                        width: `${(count / maxCount) * 100}%`,
                        background: color,
                        boxShadow: `0 0 8px ${color}88`,
                        borderRadius: 2,
                        transition: "width 0.6s cubic-bezier(.4,0,.2,1)",
                      }} />
                    </div>

                    {/* Count */}
                    <span style={{
                      width: 80, textAlign: "right",
                      fontSize: 12, color: color,
                      flexShrink: 0,
                    }}>
                      {count}× {count === 1 ? "time" : "times"}
                    </span>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}
      </div>

      <style>{`
        @keyframes fadeIn {
          from { opacity: 0; transform: translateX(-8px); }
          to { opacity: 1; transform: translateX(0); }
        }
        * { box-sizing: border-box; }
        textarea::placeholder { color: #2a2a3a; }
        scrollbar-width: thin;
        scrollbar-color: #1e1e2e #0a0a0f;
      `}</style>
    </div>
  );
}
