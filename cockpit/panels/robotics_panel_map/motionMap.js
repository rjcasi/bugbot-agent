// motionMap.js

export const motionMap = [
  {
    pattern: "Spiral",
    robotics: "rotational_motion",
    rule: v => v.angular_velocity > 0.5
  },
  {
    pattern: "Crest",
    robotics: "peak_torque",
    rule: v => v.torque > 0.8
  },
  {
    pattern: "Flux",
    robotics: "adaptive_smoothing",
    rule: v => v.vibration > 0.4
  },
  {
    pattern: "Anchorfield",
    robotics: "posture_stabilization",
    rule: v => v.balance_error < 0.2
  },
  {
    pattern: "Bridge",
    robotics: "coordinate_transform",
    rule: v => v.frame_shift === true
  }
];