## Scratch entries for the member-list probe (12 November 2026) — not dictionary entries

### [P1] net-force-material-object

```text
For one material-object, its haze-material-object plus its contribution-material-object.
```

### [P2] contribution-material-object

```text
For one material-object and a remaining interaction-set that is not empty, the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member.
```

### [P3] contribution-material-object

```text
For one material-object and an empty remaining interaction-set, the zero vector.
```

### [P4] impressed-force

```text
For a member that is the action of an acting-object, the action-force of that acting-object.
```

### [P5] impressed-force

```text
For a member that is the reaction of an acting-object, the reaction-force of that acting-object.
```

### [P6] reaction-force

```text
For one acting-object, the negative of its action-force.
```

### [P7] action-force_spring

```text
For a spring acting-object, the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis.
```

### [P8] action-force_near-surface-gravity

```text
For the near-surface gravity acting-object of the Earth, the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis.
```
