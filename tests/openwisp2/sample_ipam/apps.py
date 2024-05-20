from immunity_ipam.apps import OpenWispIpamConfig


class SampleIpamConfig(OpenWispIpamConfig):
    name = 'immunity2.sample_ipam'
    label = 'sample_ipam'


del OpenWispIpamConfig
