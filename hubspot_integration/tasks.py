import  hubspot_integration.hubspot_integration.doctype.hubspot_configuration.hubspot_configuration


def all():
    pass

def hourly():
    pass

def daily():
    hubspot_integration.hubspot_integration.doctype.hubspot_configuration.hubspot_configuration.fetch_won_deals()
    hubspot_integration.hubspot_integration.doctype.hubspot_configuration.hubspot_configuration.fetch_companies()

def weekly():
    pass

def monthly():
    pass
