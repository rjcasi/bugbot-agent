// RoboticsPatternMapPanel.jsx
import React, { useState, useEffect } from "react";
import { motionMap } from "./motionMap";
import "./styles.css";

export default function RoboticsPatternMapPanel() {
  const [robot, setRobot] = useState({});

  useEffect(() => {
    const interval = setInterval(() => {
      setRobot({
        angular_velocity: Math.random(),
        torque: Math.random(),
        vibration: Math.random(),
        balance_error: Math.random(),
        frame_shift: Math.random() > 0.7
      });
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="robotics-panel">
      <h2 className="panel-title">Pattern → Robotics Arena Mapping</h2>

      {motionMap.map((link, i) => {
        const triggered = link.rule(robot);

        return (
          <div key={i} className="robotics-card">
            <div className="pattern">{link.pattern}</div>
            <div className="robotics">{link.robotics}</div>

            {triggered ? (
              <div className="active">ACTIVE</div>
            ) : (
              <div className="inactive">inactive</div>
            )}
          </div>
        );
      })}
    </div>
  );
}