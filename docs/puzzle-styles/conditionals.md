# Conditionals
## If X in room
| ID | Description |
| --- | --- |
| X-SWC | Specific Wall Colour |
| X-SO | Specific Object |
| X-SOO | Style of Object |
| X-COO | Colour of Object |
| X-HES | Has empty slot |
| X-DS | Duplicate Styles |
| X-DC | Duplicate Colours |

## Then Y
| ID | Description |
| --- | --- |
| Y-2CO | At least 2 of colour of object |
| Y-2SO | At least 2 of style of object |
| Y-M1O | At most one object |
| Y-NSS | Each object must not have the same style as any other object in that room |
| Y-NSC | Each object must not have the same colour as any other object in that room |
| Y-WMT | Wall colour must match the colour of a type of object in the room |
| Y-WMS | Wall colour must match the colour of a style of object in the room |

## Allowed combinations
| X ID | Y IDs |
| --- | --- |
| X-SWC | Y-2CO, Y-2SO, Y-M1O, Y-NSS, Y-NSC  |
| X-SO | Y-2CO, Y-2SO, Y-M1O, Y-NSS, Y-NSC |
| X-SOO | Y-2CO, Y-M1O, Y-NSC, Y-WMT |
| X-COO | Y-2SO, Y-M1O, Y-NSS, Y-WMT, Y-WMS |
| X-DS | Y-WMT, Y-WMS |
| X-DC | Y-WMT, Y-WMS |
