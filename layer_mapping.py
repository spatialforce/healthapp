import os
from django.contrib.gis.utils import LayerMapping  
from .models import Hospitals

hospitals_mapping = {
    'name':'Name',
    'tessellate': 'tessellate',
    'visibility': 'visibility',
    'geom': 'MULTIPOINT25D',
}


hos= os.path.abspath(os.path.join(os.path.dirname(__file__), 'hospitals', 'hospitals.shp'))

def run(verbose=True):
    lm = LayerMapping(Hospitals,hos,hospitals_mapping, transform=False) 
    lm.save(strict=True)  
    if verbose:
        print("data imported successfully.")





