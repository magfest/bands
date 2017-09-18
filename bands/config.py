from bands import *

bands_config = parse_config(__file__)
c.include_plugin_config(bands_config)

# Add the access levels we defined to c.ACCESS* (this will go away if/when we implement enum merging)
c.ACCESS.update(c.BAND_ACCESS_LEVELS)
c.ACCESS_OPTS.extend(c.BAND_ACCESS_LEVEL_OPTS)
c.ACCESS_VARS.extend(c.BAND_ACCESS_LEVEL_VARS)

# A list of checklist items for display on the band admin page
c.CHECKLIST_ITEMS = [
    {'name': 'panel', 'header': 'Panel'},
    {'name': 'bio', 'header': 'Bio Provided'},
    {'name': 'info', 'header': 'Agreement Completed'},
    {'name': 'taxes', 'header': 'W9 Uploaded', 'is_link': True},
    {'name': 'merch', 'header': 'Merch'},
    {'name': 'charity', 'header': 'Charity'},
    {'name': 'badges', 'header': 'Badges Claimed'},
    {'name': 'stage_plot', 'header': 'Stage Plans', 'is_link': True},
]

# Generate the possible template prefixes per step
for item in c.CHECKLIST_ITEMS:
    item['deadline_template'] = ['checklist/', item['name'] + '_deadline.html']
