DASHBOARD_TEMPLATE = """
title: Beem Energy
views:
  - title: Flux d'énergie
    path: energy
    theme: default
    badges: []
    cards:
      - type: custom:power-flow-card-plus
        title: Flux énergétique Beem
        entities:
          battery:
            entity: sensor.soc
            state_of_charge_unit: '%'
          grid:
            entity: sensor.meter_power
          solar:
            entity: sensor.solar_power
          home:
            entity: sensor.active_power
        battery:
          show_soc: true
        display_zero_lines: true
        watt_threshold: 20
        clickable_entities: true
        display_missing_entities: false
"""
