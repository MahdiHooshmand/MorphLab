# ADR-001: JSON Messaging Protocol and Transport Strategy

| Field         | Value                                          |
| ------------- | ---------------------------------------------- |
| ADR           | ADR-001                                        |
| Title         | JSON Messaging Protocol and Transport Strategy |
| Project       | MorphLab                                       |
| Status        | Accepted                                       |
| Date          | 2026-07-25                                     |
| Authors       | Mahdi Hooshmand                                |
| RFC Reference | RFC-005 (Section 2.5 & 2.6)                    |

---

# 1. Context

MorphLab requires a flexible, decoupled, and human-readable messaging protocol to exchange data between heterogeneous hardware nodes (e.g., Linux Laptop host, ESP32 microcontrollers, and Android smartphones).

The platform requires minimal mandatory overhead to allow rapid integration of low-resource devices while maintaining structured data exchange across different device categories.

---

# 2. Decision

1. **Format:** All telemetry, commands, and observations exchanged over IP and Serial networks shall use JSON-encoded text packets.
2. **Minimal Schema Requirements:**
   - **Base Packet (All Nodes):** Must contain only two mandatory fields:
     - `id`: String identifier for the source device or module.
     - `timestamp`: Numeric timestamp (local hardware tick or epoch).
   - **Sensor Observations:** Must include a `value` field containing numerical data, arrays, or structured sensor readings.
   - **Actuator Commands:** Payload fields are dynamic and customized based on the target actuator type (e.g., PWM duty cycles, desired position, step counts). All additional metadata fields remain optional.
3. **Transport Protocol:**
   - **IP-Based Nodes (WiFi/Network):** **WebSockets** is selected as the primary transport protocol. The host system (Laptop) operates as the high-capacity WebSocket Server, while smart devices (Android) and microcontrollers (ESP32) act as lightweight WebSocket Clients. Standard TCP/UDP sockets remain supported as secondary fallbacks for ultra-constrained hardware.
   - **Direct Hardware (USB/Serial):** Standard framing over UART/Serial is used for microcontrollers connected directly via USB.

---

# 3. Consequences

### Positive
- High developer accessibility, ease of debugging, and human readability.
- Minimal mandatory payload size ensures rapid driver implementation.
- WebSocket provides bi-directional, full-duplex communication with low overhead for WiFi-connected devices.

### Negative / Trade-offs
- Text-based JSON incurs slightly higher network bandwidth compared to packed binary protocols, which is acceptable for the laboratory bandwidth in scope.
