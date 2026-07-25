# RFC-004: System Context

| Field | Value |
|-------|-------|
| RFC | RFC-004 |
| Title | System Context |
| Project | MorphLab |
| Status | Draft |
| Version | 0.2 |
| Author | Mahdi Hooshmand |
| Created | YYYY-MM-DD |

---

# 1. Abstract

This document defines the system boundary of MorphLab and identifies external actors, hardware devices, and ecosystem interactions.

---

# 2. System Boundary

MorphLab is responsible for:

- Experiment orchestration and configuration management
- Device driver management and sensor abstraction
- Control algorithm execution and dispatching
- Time-synchronized data logging and dataset recording
- Live visualization and offline analysis execution
- Asset Registry management (packaging, driver management, certification tiers)

MorphLab is **not** responsible for manufacturing hardware, providing hard real-time execution environments inside microcontrollers, or replacing CAD/physics engines.

---

# 3. External Actors & Systems

## Researcher / Contributor
Interacts with MorphLab to run experiments, analyze data, write papers, and publish new drivers or algorithms to the ecosystem.

## Controllers & Microcontrollers
External hardware (e.g., ESP32, STM32, Arduino) running dedicated firmware (e.g., MicroPython, C/C++) that interfaces directly with physical sensors and motor driver circuits.

## External Measurement Systems & Smart Devices
Independent hardware (e.g., Android smartphones, IMU units, motion tracking cameras) providing observations via standard transport protocols (USB, WiFi, Sockets).

## External Analysis & Publication Tools
Scientific suites (e.g., Jupyter, MATLAB, SciPy) consuming exported MorphLab Datasets.

---

# 4. Context Diagram

```
 +------------------------+                  +-------------------------+
 |       Researcher       |<---------------->|   MorphLab Ecosystem    |
 | (User & Contributor)   |                  | (Core & Asset Registry) |
 +------------------------+                  +------------+------------+
                                                          |
                                      +-------------------+-------------------+
                                      |                   |                   |
                                      v                   v                   v
                             +-----------------+ +-----------------+ +-----------------+
                             |   Controllers   | | External Smart  | | Data Consumers  |
                             | (e.g. ESP32 USB)| | Devices (WiFi)  | | (Jupyter/MATLAB)|
                             +--------+--------+ +--------+--------+ +-----------------+
                                      |                   |
                                      +---------+---------+
                                                |
                                                v
                                     +---------------------+
                                     | Physical Mechanism  |
                                     | (e.g., 3-DOF Robot) |
                                     +---------------------+
```

---

# 5. Summary

MorphLab acts as the central orchestration software and driver library repository, interfacing cleanly with external hardware controllers, smart devices, and analysis suites.
