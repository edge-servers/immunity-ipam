import swapper

from immunity_ipam.management.commands import BaseExportSubnetCommand


class Command(BaseExportSubnetCommand):
    subnet_model = swapper.load_model('sample_ipam', 'Subnet')
