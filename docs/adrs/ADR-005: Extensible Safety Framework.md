# ADR-005: Extensible Safety Framework

| Field         | Value                       |
| ------------- | --------------------------- |
| ADR           | ADR-005                     |
| Title         | Extensible Safety Framework |
| Project       | MorphLab                    |
| Status        | Accepted                    |
| Date          | 2026-07-25                  |
| Authors       | Mahdi Hooshmand             |
| Created       | 2026-07-25                  |
| RFC Reference | RFC-004                     |

---

# 1. Context

Experimental mechatronics setups range from low-power benchtop setups to high-power robotic mechanisms. Software safety requirements (such as emergency stops and heartbeat signals) vary greatly depending on physical risk.

---

# 2. Decision

1. **Baseline Strategy (Project 001):** No mandatory software safety subsystems or heartbeat enforcement are imposed for Project 001. The physical hardware consists of low-power actuators with direct manual power disconnects, posing negligible risk.
2. **Extensible Architecture Provision:** The core architecture reserves hooks for optional safety modules (e.g., connection heartbeat timeouts, velocity limits, soft emergency-stop triggers) that can be enabled and configured in future high-risk experiments without architectural changes.

---

# 3. Consequences

### Positive
- Zero software overhead and rapid prototyping setup for low-power laboratory experiments.
- Architecture remains ready to adopt safety subsystems when required by future hardware.

### Negative / Trade-offs
- Safety enforcement relies entirely on physical manual switches for early low-power experiments.
