# MorphLab

MorphLab is an experimental software platform for developing, evaluating, and validating mechatronic mechanisms and control algorithms.

## Documentation

The complete documentation is available through GitHub Pages.

## Repository Layout

- `docs/` — RFCs and ADRs (platform-level architecture decisions).
- `registry/` — Asset Registry (RFC-002/ADR-004): reusable drivers and joint
  compositions shared across experiments. See `registry/drivers/esp32_micropython/`
  (atomic drivers) and `registry/components/` (composed joints, e.g. `DCJoint`).
- `experiments/` — one folder per experiment (RFC-003 "Experiment"). The first is
  `experiments/project-001/`, which binds pins/config to drivers from `registry/`.

## License

MIT
