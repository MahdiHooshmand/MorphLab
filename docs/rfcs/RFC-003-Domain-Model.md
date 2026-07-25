# RFC-003: Domain Model

| Field | Value |
|-------|-------|
| RFC | RFC-003 |
| Title | Domain Model |
| Project | MorphLab |
| Status | Draft |
| Version | 0.2 |
| Author | Mahdi Hooshmand |
| Created | YYYY-MM-DD |

---

# 1. Abstract

This document defines the conceptual domain model of MorphLab.

It specifies the primary domain entities, their relationships, and the lifecycle of reusable libraries within the ecosystem.

---

# 2. Domain Entities

The domain model consists of the following core entities:

- Asset Registry / Library (Driver Library, Algorithm Library, Example Templates)
- Certification Tier
- Experiment
- Mechanism
- Device (Controller, Sensor, Actuator)
- Driver
- Data Source
- Observation
- State
- Control Algorithm
- Command
- Dataset
- Logger
- Analysis & Visualization
- Configuration

---

# 3. Domain Relationships & Lifecycle

## Asset Consumption & Contribution Cycle

1. **Instantiation:** An `Experiment` is configured using an `Experiment Template` or built customly by importing `Drivers` and `Control Algorithms` from the `Asset Registry`.
2. **Hardware Binding:** `Sensors` and `Actuators` are connected to `Controllers` using their corresponding `Drivers`.
3. **Execution:** The `Control Algorithm` reads `State` (derived from `Observations`) and outputs `Commands`.
4. **Data Capture:** The `Logger` collects `Observations` and `Commands` into a `Dataset` for `Analysis`.
5. **Asset Feedback:** New hardware drivers or control algorithms created during the experiment are packaged, assigned an initial `Certification Tier` (Tier 1: Experimental), and published back to the `Asset Registry`.

---

# 4. Conceptual View

```
                   +--------------------------------+
                   |   Asset Registry / Libraries   |
                   | (Drivers, Algorithms, Examples)|
                   +---------------+----------------+
                                   |
                          Imports / Contributes
                                   |
                                   v
+-------------------------------------------------------------------+
|                            Experiment                             |
|                                                                   |
|  +------------------+     +-------------------+   +------------+  |
|  |  Configuration   |     | Control Algorithm |-->|  Command   |  |
|  +------------------+     +---------^---------+   +-----+------+  |
|                                     |                   |         |
|  +------------------+         +-----+-----+             |         |
|  |    Mechanism     |         |   State   |             |         |
|  +--------+---------+         +-----^-----+             |         |
|           |                         |                   |         |
|  +--------v---------+     +---------+---------+         |         |
|  | Devices & Drivers|<--->| Observations /    |<--------+         |
|  | (Sensors/Motors) |     | Data Sources      |                   |
|  +------------------+     +---------+---------+                   |
|                                     |                             |
|                           +---------v---------+                   |
|                           | Dataset & Logger  |                   |
|                           +---------+---------+                   |
|                                     |                             |
|                           +---------v---------+                   |
|                           | Analysis & Viz    |                   |
|                           +-------------------+                   |
+-------------------------------------------------------------------+
```

---

# 5. Summary

The Domain Model establishes both the execution relationships during an experiment and the continuous asset accumulation cycle that drives the platform's long-term growth.
