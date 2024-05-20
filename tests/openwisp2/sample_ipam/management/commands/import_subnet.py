import swapper

from immunity_ipam.management.commands import BaseImportSubnetCommand


class Command(BaseImportSubnetCommand):
    subnet_model = swapper.load_model('sample_ipam', 'Subnet')
