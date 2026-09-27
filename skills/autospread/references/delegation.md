# Delegation

Delegate only when the work is sufficiently independent, the host supports it, and the handoff is cheaper or safer than doing it in the current session. Roles do not require separate sessions.

Every handoff states:

- objective and business constraint;
- relevant product files, URLs, data, and experiment ID;
- role method/skill to apply;
- allowed tools and explicit forbidden actions;
- autonomy-policy decision for material actions;
- expected artifact and evidence standard;
- dependencies, observation window, deadline, and failure condition;
- where results must be returned.

Parallelize research or production only when workstreams do not mutate the same external state or depend on each other's results. Sequence dependent work such as research -> landing change -> publish -> measurement.

The Lead checks returned work against the evidence standard. A queued request, child-agent acknowledgement, generated draft, successful command exit, or browser click is not a completed external task without the required observable result.
