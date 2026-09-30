---
tags:
  - machinery
chart_type: 
chart_name: 
exact_datetime_utc: 
exact_datetime_local: 
location: Washington, D.C.
house_system: Whole Sign
sign: 
degree: 
window_start: 
window_end: 
key_aspects: []
astro_gold_file: 
status: 
---

# {{chart_name}}

## Chart data

| Field | Value |
|---|---|
| Type | |
| Exact moment (UTC) | |
| Exact moment (D.C. local) | |
| Sign | |
| Degree | |
| Key aspects | |
| Window of influence | |

## Astro Gold chart

*Open chart file in Astro Gold to view the wheel. Export as PDF or PNG and embed below for in-vault viewing.*

## My interpretation


## Themes / questions to watch


## Linked events (by transit tag)

```dataview
TABLE date, primary_plotline
FROM "01 - Events"
WHERE contains(transits_active, this.chart_name)
SORT date ASC
```

## Linked events (by date window)

```dataview
TABLE WITHOUT ID
  file.link AS "Event",
  date AS "Date",
  primary_plotline AS "Primary plotline"
FROM "01 - Events"
WHERE date >= this.window_start AND date <= this.window_end
SORT date ASC
```

## Related charts and transits

