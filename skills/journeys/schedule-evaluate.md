---
name: schedule-evaluate
description: >
  Evaluate the national immunization schedule over the child's imported doses and propose what is due (journey J3).
---

# schedule-evaluate

Evaluate the national immunization schedule over the child's imported doses and propose what is due (journey J3).

## What it does

`PlanDefinition/$apply` of the OHS KMP workflow library over the child's `Immunization`s, the schedule's applicability conditions in FHIRPath (CQL is not yet available there); the result is a `CarePlan`/`RequestGroup` of due doses, e.g. birth-dose OPV.
