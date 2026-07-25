# ADR-002: Execution Frequency and Missing Data Strategy

| Field         | Value                                         |
| ------------- | --------------------------------------------- |
| ADR           | ADR-002                                       |
| Title         | Execution Frequency and Missing Data Strategy |
| Project       | MorphLab                                      |
| Status        | Accepted                                      |
| Date          | 2026-07-25                                    |
| Authors       | Mahdi Hooshmand                               |
| RFC Reference | RFC-003, RFC-005                              |

---

# 1. Context

In mechatronic experimentation, control loops and sensor sampling rates vary widely depending on sensor hardware, processing bandwidth, and physical mechanism dynamics. Furthermore, network communication or hardware glitches can result in dropped packets or transmission delays.

---

# 2. Decision

1. **Execution Rate Freedom:** The core platform does not impose artificial rate caps on data streams or control loop frequencies. Sampling and command dispatch operate at the maximum achievable rate dictated by hardware constraints.
2. **Missing/Delayed Data Handling Strategy:**
   - When incoming observations are delayed or dropped, the platform applies data estimation algorithms to maintain execution continuity.
   - **Project 001 Baseline:** Linear extrapolation based on the last two valid data points is adopted as the primary estimation method.
   - **Future Flexibility:** The platform architecture supports configurable estimation modules (e.g., zero-order hold, higher-order polynomial fitting, or Kalman state estimation) selectable per experiment.

---

# 3. Consequences

### Positive
- Platform runtime maximizes hardware capability without arbitrary software bottlenecks.
- Control loops remain stable during transient communication drops due to deterministic extrapolation.

### Negative / Trade-offs
- Extrapolation introduces estimation error during high-frequency physical transients if packet loss spans multiple consecutive cycles.
