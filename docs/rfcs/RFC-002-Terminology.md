# RFC-002: Terminology

| Field | Value |
|-------|-------|
| RFC | RFC-002 |
| Title | Terminology |
| Project | MorphLab |
| Status | Draft |
| Version | 0.2 |
| Author | Mahdi Hooshmand |
| Created | YYYY-MM-DD |

---

# 1. Abstract

This document defines the official terminology used throughout the MorphLab project.

The purpose of this RFC is to establish a common vocabulary for documentation, software architecture, implementation, libraries, and future research.

Subsequent RFCs, ADRs, Standards, and Specifications shall use the terminology defined in this document.

---

# 2. Platform & Ecosystem

## Platform
The complete software environment that supports the development, execution, monitoring, recording, and analysis of experiments.

## Asset Registry / Library Ecosystem
The structured collection of reusable code, drivers, control algorithms, configuration files, and experiment templates maintained across experiments.

---

# 3. Experiment & Templates

## Experiment
The primary research entity within MorphLab representing a reproducible scientific investigation.

## Example / Experiment Template
A pre-configured, reproducible experiment setup (including mechanism configuration, drivers, algorithms, and analysis scripts) serving as a starting point, tutorial, or research benchmark.

---

# 4. Physical Entities & Hardware Abstractions

## Mechanism
A physical or virtual mechanical structure under investigation (e.g., a 3-DOF robot, Stewart platform, inverted pendulum). It excludes software and high-level controllers.

## Device
Any hardware component interacting with the platform (e.g., microcontroller, IMU, smartphone, driver board).

## Controller
A Device executing low-level, deterministic control logic and directly interfacing with sensors/actuators (e.g., ESP32 running MicroPython).

## Sensor
A Device that measures physical quantities (e.g., encoder, potentiometer, smartphone IMU).

## Actuator
A Device capable of modifying the physical state of a mechanism (e.g., DC motor, stepper motor).

---

# 5. Data & Control Entities

## Data Source
Any provider of observable data (Physical Sensor, Software Module, Mobile App, Simulation).

## Observation
A single measured value produced by a Data Source accompanied by temporal information.

## State
A collection of observations describing the current condition of a system at a particular instant.

## Command
A requested action issued to a Device or Controller (e.g., PWM duty cycle, desired velocity).

## Control Algorithm
A mathematical or computational procedure responsible for determining Commands based on State information (e.g., PID, LQR, MPC).

---

# 6. Library Components

## Driver
A software module providing a standardized abstraction for interacting with a specific Device, Sensor, or Actuator (e.g., potentiometer driver, Android IMU receiver).

## Algorithm Library
A structured repository of generic, hardware-independent Control Algorithms.

## Driver Library
A structured repository of reusable hardware Drivers.

## Certification Tier (Badge)
A standard classification indicating the maturity, quality, test coverage, and specification compliance of a Library asset:
- **Tier 1 (Experimental):** Proof-of-concept code created during a specific experiment.
- **Tier 2 (Standardized):** Refactored library complying with MorphLab standard interfaces.
- **Tier 3 (Certified / Core):** Fully tested, documented, and maintained asset integrated into core releases.

---

# 7. Workflow & Operations

## Session
A continuous period during which the platform operates.

## Dataset
A structured collection of recorded experimental observations, commands, events, and metadata.

## Logger
A software component responsible for capturing and storing runtime experimental data.

## Analysis
The process of processing datasets to extract metrics, evaluate errors, or validate models.

## Visualization
The graphical presentation of live or recorded experimental information.

## Configuration
Structured parameter sets defining how an Experiment, Mechanism, Device, or Algorithm executes.

## Plugin
An external module extending platform capabilities without modifying core code.

---

# 8. Summary

This terminology forms the shared vocabulary of MorphLab. Subsequent documents must adhere to these definitions.
