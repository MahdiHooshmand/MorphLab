# ADR-003: Multi-Source Time Synchronization and Manual Alignment

| Field         | Value                                                  |
| ------------- | ------------------------------------------------------ |
| ADR           | ADR-003                                                |
| Title         | Multi-Source Time Synchronization and Manual Alignment |
| Project       | MorphLab                                               |
| Status        | Accepted                                               |
| Date          | 2026-07-25                                             |
| Authors       | Mahdi Hooshmand                                        |
| RFC Reference | RFC-005 (Section 2.7)                                  |

---

# 1. Context

MorphLab gathers data from disparate hardware devices (e.g., USB-connected ESP32 and WiFi-connected smartphone) operating on independent system clocks. To evaluate kinematics, dynamics, and kinematic errors accurately, data streams must be temporally synchronized.

---

# 2. Decision

1. **Online Execution:** The platform includes automated event-driven synchronization logic for real-time processing. This logic detects distinctive excitation events (such as motion onset or physical impact spikes in IMU and potentiometer data) to dynamically align timeline origins.
2. **Offline Analysis:** Post-experiment workflows provide interactive manual time-shift tools. Researchers can manually adjust temporal offsets across multi-sensor datasets to refine synchronization prior to scientific reporting and model fitting.

---

# 3. Consequences

### Positive
- Eliminates the requirement for complex hardware clock-sync lines (like IEEE 1588 PTP) across heterogeneous experimental setups.
- Grants researchers full manual authority over data alignment for publication-grade precision.

### Negative / Trade-offs
- Automated online alignment requires a distinct excitation signal or movement phase at the start of an experiment session.
