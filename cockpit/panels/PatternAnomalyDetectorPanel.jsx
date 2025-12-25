// PatternAnomalyDetectorPanel.jsx
import React, { useState, useEffect } from "react";
import { anomalyRules } from "./anomalyRules";
import "./styles.css";

export default function PatternAnomalyDetectorPanel() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    // Replace with your Cyber Arena event stream
    const interval = setInterval(() => {
      const mockEvent = {
        id: Date.now(),
        type: ["divergence", "timing", "entropy"][Math.floor(Math.random() * 3)],
        entropy_delta: Math.random(),
        timing_jitter: Math.random() * 100,
        branches: Math.floor(Math.random() * 3),
        hidden_fields: Math.random() > 0.7 ? ["x"] : [],
        anchor_loss: Math.random() > 0.9
      };
      setEvents(prev => [mockEvent, ...prev].slice(0, 20));
    }, 1500);

    return () => clearInterval(interval);
  }, []);

  function classify(event) {
    for (const rule of anomalyRules) {
      if (rule.match(event)) return rule;
    }
    return null;
  }

  return (
    <div className="anomaly-panel">
      <h2 className="panel-title">Pattern‑Driven Anomaly Detector</h2>

      {events.map(event => {
        const rule = classify(event);
        return (
          <div key={event.id} className="anomaly-card">
            <div className="event-id">Event {event.id}</div>
            {rule ? (
              <>
                <div className="pattern-hit">{rule.pattern}</div>
                <div className="explanation">{rule.explanation}</div>
              </>
            ) : (
              <div className="no-match">No symbolic match</div>
            )}
          </div>
        );
      })}
    </div>
  );
}