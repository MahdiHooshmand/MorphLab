# ADR-006: Reusable Component Layer Between Drivers and Experiments

| Field         | Value                                                    |
| ------------- | --------------------------------------------------------- |
| ADR           | ADR-006                                                    |
| Title         | Reusable Component Layer Between Drivers and Experiments  |
| Project       | MorphLab                                                   |
| Status        | Accepted                                                   |
| Date          | 2026-08-01                                                 |
| Authors       | Mahdi Hooshmand                                            |
| RFC Reference | RFC-002 (Driver, Driver Library), ADR-004                  |

---

# 1. Context

ADR-004 defines a single reusable-code tier: the Driver Library (`registry/drivers/`),
one file per atomic device capability. During Project 001's implementation, a second,
distinct pattern emerged: several atomic drivers are habitually combined into a fixed,
still-generic (pins/ratios passed in by the caller) higher-level object representing
"one degree of freedom" — e.g. `Encoder` + `DCMotor` + one `L298NDriver` channel +
`Gearbox` together form a drivable, readable joint. This composition is reusable
across future experiments, but it is not itself an atomic hardware driver, so it does
not fit ADR-004's "one file per device capability" rule for the Driver Library.

---

# 2. Decision

Introduce a second Asset Registry tier, `registry/components/`, sitting between
`registry/drivers/` (atomic) and `experiments/<name>/` (assembly-specific, bound to a
concrete mechanism):

- `registry/drivers/<platform>/` — one atomic hardware capability per file
  (unchanged, per ADR-004).
- `registry/components/` — composes 2+ drivers into a reusable, still-generic object
  (e.g. `DCJoint`, `StepperJoint`). Pins, ratios, and driver instances are passed in
  by the caller; nothing here is specific to one mechanism.
- `experiments/<name>/mechanism/` — combines components into the specific mechanism
  under study (e.g. `AnkleMechanism`), including any mechanism-specific kinematics.

---

# 3. Consequences

- The Asset Registry now has two reusable sub-tiers instead of one. Future ADRs/STDs
  referencing "the Driver Library" should distinguish atomic drivers from components.
- RFC-002 §6 ("Library Components") is extended with a `Component` definition
  (see RFC-002 v0.3) to keep terminology and code in sync.
- Certification tiers (RFC-002) apply per-file at both levels: a component can reach
  Tier 2 independently of the drivers it composes, provided its own interface is
  standardized (see STD-001).

---

# 4. Alternatives Considered

- **Keep joint composition inline in each experiment.** Rejected — the same
  encoder+motor+driver+gearbox pattern is expected to recur in future experiments;
  inlining it would duplicate logic instead of reusing it.
- **Put composed objects inside `registry/drivers/`.** Rejected — conflates atomic
  device capability (ADR-004's unit of reuse) with multi-device composition, and
  breaks the "one file, one device capability" rule.
