# RFC-002: Terminology

| Field | Value |
|-------|-------|
| RFC | RFC-002 |
| Title | Terminology |
| Project | MorphLab |
| Status | Draft |
| Version | 0.1 |
| Author | Mahdi Hooshmand |
| Created | YYYY-MM-DD |

---

# 1. Abstract

This document defines the official terminology used throughout the MorphLab project.

The purpose of this RFC is to establish a common vocabulary for documentation, software architecture, implementation, and future research.

Unless explicitly stated otherwise, all subsequent RFCs, ADRs, Standards, and Specifications shall use the terminology defined in this document.

---

# 2. Platform

The complete software environment that supports the development, execution, monitoring, recording, and analysis of experiments.

The Platform represents the entire MorphLab ecosystem.

---

## 3. Experiment

The primary research entity within MorphLab.

An Experiment represents a reproducible scientific investigation conducted to evaluate one or more hypotheses.

An Experiment defines the context in which research activities are performed.

The conceptual composition of an Experiment is defined in RFC-003 (Domain Model).

---

# 4. Mechanism

A physical or virtual mechanical system under investigation.

A Mechanism may contain moving structures, joints, transmissions, or any other mechanical elements.

A Mechanism does not include controllers or software.

Examples:

- Three-axis experimental platform
- Robotic arm
- Stewart platform
- Gimbal
- Inverted pendulum

---

# 5. Device

Any hardware component capable of interacting with the platform.

Devices may provide sensing, actuation, communication, computation, or auxiliary functionality.

Examples:

- Microcontroller
- IMU
- Motor Driver
- Camera
- Mobile Phone
- Force Sensor

---

# 6. Controller

A Device responsible for executing low-level control logic and directly interacting with hardware.

Typical responsibilities include:

- Reading sensors
- Driving actuators
- Executing deterministic control loops
- Reporting measurements

A Controller does not perform high-level experiment management.

---

# 7. Sensor

A Device that measures physical quantities.

Examples include:

- Encoder
- Potentiometer
- IMU
- Camera
- Force Sensor
- Temperature Sensor

Sensors generate observations but do not modify the physical system.

---

# 8. Actuator

A Device capable of modifying the physical state of a mechanism.

Examples include:

- DC Motor
- Stepper Motor
- Servo Motor
- Hydraulic Actuator
- Pneumatic Cylinder

---

# 9. Data Source

Any provider of observable data.

A Data Source may be:

- Physical Sensor
- Software Module
- External Application
- Simulation
- Remote System

Every Sensor is a Data Source.

Not every Data Source is a Sensor.

---

# 10. Observation

A single measured value produced by a Data Source.

Examples:

- Position
- Velocity
- Roll
- Pitch
- Yaw
- Acceleration
- Angular Velocity

Observations always represent measurements.

---

# 11. State

A collection of observations describing the current condition of a system at a particular instant.

State represents the best available knowledge about the system.

State may contain measured, estimated, or calculated values.

---

# 12. Control Algorithm

An algorithm responsible for determining actuator commands based on available state information.

Examples:

- PID
- LQR
- MPC
- Adaptive Control
- Reinforcement Learning

The platform imposes no restrictions on algorithm implementation.

---

# 13. Command

A requested action issued to a Device or Controller.

Examples include:

- Set Motor Velocity
- Set Position
- Enable Output
- Disable Output

Commands describe desired behavior rather than measured state.

---

# 14. Session

A continuous period during which the platform operates.

A Session may contain one or more Experiments.

---

# 15. Dataset

A structured collection of recorded experimental data.

Datasets may contain:

- Measurements
- Commands
- Events
- Metadata
- Configuration

Datasets are intended for offline analysis and publication.

---

# 16. Logger

A software component responsible for recording information generated during a Session or Experiment.

Logging is independent of analysis.

---

# 17. Analysis

The process of extracting information from experimental data.

Analysis may include:

- Statistical processing
- Error estimation
- Performance evaluation
- Model validation
- Visualization

Analysis does not modify recorded data.

---

# 18. Visualization

The graphical presentation of experimental information.

Visualization may include:

- Live monitoring
- Charts
- Time-series plots
- Three-dimensional views
- Dashboards

Visualization is independent of data acquisition.

---

# 19. Configuration

A collection of parameters describing how an Experiment is executed.

Configuration may include:

- Hardware selection
- Control parameters
- Sampling rates
- Calibration values
- Experiment settings

Configuration should be reproducible.

---

# 20. Digital Twin

A virtual representation of a physical system synchronized with experimental data.

Digital Twin support is considered a long-term capability of MorphLab and is outside the scope of the initial implementation.

---

# 21. Simulation

A computational model that emulates the behavior of a mechanism or subsystem.

Simulation may replace physical hardware during development or validation.

Simulation is not required for every Experiment.

---

# 22. Plugin

A software component that extends the platform without modifying its core.

Plugins may introduce:

- Devices
- Mechanisms
- Visualizations
- Analysis tools
- Communication interfaces

---

# 23. Future Terms

Additional terminology shall be introduced only through new RFCs or revisions to this document.

---

# 24. Summary

The terminology defined in this RFC establishes the common language of MorphLab.

Future documentation and software should consistently use these definitions to ensure architectural clarity and long-term maintainability.

---

## Relationship to Other RFCs

This document defines the official terminology of MorphLab.

Definitions provided here intentionally avoid describing relationships between entities.

The conceptual relationships between these terms are specified in RFC-003 (Domain Model).