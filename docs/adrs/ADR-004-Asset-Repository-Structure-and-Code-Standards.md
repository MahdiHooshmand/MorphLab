# ADR-004: Asset Repository Structure and Code Standards

| Field         | Value                                         |
| ------------- | --------------------------------------------- |
| ADR           | ADR-004                                       |
| Title         | Asset Repository Structure and Code Standards |
| Project       | MorphLab                                      |
| Status        | Accepted                                      |
| Date          | 2026-07-25                                    |
| Authors       | Mahdi Hooshmand                               |
| RFC Reference | RFC-001, RFC-002                              |

---

# 1. Context

To fulfill MorphLab's vision as an accumulating ecosystem, code created during experiments (drivers, control algorithms, templates) must be structured for long-term maintainability without creating high barriers to entry for non-software engineers.

---

# 2. Decision

1. **Initial Repository Strategy (Project 001):** Drivers, algorithms, and example workflows for Project 001 are organized in separate, modular repositories/packages (Polyrepo approach) from day one to enforce clean separation of concerns.
2. **Ecosystem Evolution Flexibility:** For future experiments, repository layout choices (Monorepo vs. Polyrepo) remain at the researcher's discretion based on project scope.
3. **Software Architecture Standards:** Development should adhere to clean software design principles (e.g., SOLID) where feasible. However, strict compliance is optional for early-stage experiments and is enforced progressively through the certification tier system defined in RFC-002 (Tier 1: Experimental, Tier 2: Standardized, Tier 3: Certified).

---

# 3. Consequences

### Positive
- Enforces modular driver and algorithm design from the first experiment.
- Lowers entry barriers for researchers while providing a structured path toward code standardization.

### Negative / Trade-offs
- Managing multiple repositories requires clear dependency tracking across packages.
