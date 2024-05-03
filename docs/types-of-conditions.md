# Types of Conditions

## Definitions
| Term | Definition |
| --- | --- |
| SSRF | The Solution Space Restriction Factor, i.e. how much the condition restricts the solution space. |

## Base Condition Templates
All conditions can be boiled down to a template, containing three components:

1. Constraint
2. Target
3. Scope

Below are the basic building blocks for these conditions. This is not all possible conditions, but is a nice set that we can work with

### Constraints
| ID | Constraint |
| --- | --- |
| NumOf-0/1/2/3 | There must be 0/1/2/3/4 of ? |
| AnyOf | There must be at least one of ? |
| AtMostOneOf | There can be at most one of ? |
| NumComp-More/Equal* | There must be more/equal ? than ? |

\* Only to be used with House scope

### Targets
| ID | Target |
| --- | --- |
| SpecificObject | A specific object |
| SpecificWallColour | A specific wall colour |
| Type | A specific object type |
| Style | A specific object style |
| Colour | A specific colour |
| AnyStyle* | At least one of the styles |
| AnyColour* | At least one of the colours |

\* Only to be used with NumOf-0 constraint

### Scopes
| ID | Scope |
| --- | --- |
| House | The whole House |
| Floor | A specific floor of the house |
| Side | A specific side of the house |
| Room | A specific Room of the house |

### Special Scopes
| ID | Scope |
| --- | --- |
| RoomsWith | Rooms that meet a specific Constraint |

## Enumerated Basic Condition Templates
See [spreadsheet](enumerated-basic-condition-templates.xlsx)
