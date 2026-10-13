---
name: remotion-maps
description: Remotion Map animation knowledge
version: 4.0.506
---

# Remotion Maps

Choose exactly one technique from the intended shot, then load only that technique's `TECHNIQUE.md`.
Techniques are organized separately; check the selected technique's resource availability before using it.

**Source resource gap:** this snapshot omits the MapTiler `assets/RiverReveal.tsx`,
`assets/CountryLabel.tsx`, and `assets/example-Root.tsx`, plus the Cesium
`assets/CesiumFlythrough.tsx` and `assets/example-Root.tsx`. For those branches, obtain
user-provided implementations or implement project-local components from the technique's
architecture and rendering requirements within the authorized task. Verify actual files and
imports, then inspect a rendered still and short sequence before claiming the branch is ready.
Until these prerequisites are met, report the missing implementation; do not copy or import
these filenames as though they were bundled. The available MapTiler provider-vector helper
and other techniques can be used when they fit the requested shot.

## [Static map](techniques/static-map/TECHNIQUE.md)

- Requires you grab a satellite image and mount it in a `<Img>` tag, and animate on top

## [Mapbox](techniques/mapbox/TECHNIQUE.md)

- Requires a Mapbox key
- Nicer styles by default
- Map can display a round globe when zoomed out
- Includes nice 3D buildings such as the Eiffel tower

## [MapLibre](techniques/maplibre/TECHNIQUE.md)

- Requires no API key, fully free
- Does not include 3D building

## [MapTiler](techniques/maptiler/TECHNIQUE.md)

- Uses MapTiler
- Annotations can be drawn on top of geographic features: borders, rivers, labels

## [CesiumJS](techniques/cesium/TECHNIQUE.md)

- Flythroughs through terrain and mountains
- "Flight simulator" perspective
