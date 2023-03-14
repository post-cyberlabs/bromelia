# -*- coding: utf-8 -*-
"""
    bromelia.avps
    ~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library 
    that are used to create Diameter messages.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from .etsi_3gpp.ts_129_061 import *
from .etsi_3gpp.ts_129_212 import *
from .etsi_3gpp.ts_129_214 import *
from .etsi_3gpp.ts_129_229 import *
from .etsi_3gpp.ts_129_272 import *
from .etsi_3gpp.ts_129_273 import *
from .etsi_3gpp.ts_129_329 import *
from .etsi_3gpp.ts_183_017 import *
from .etsi_3gpp.ts_129_172 import *

from .ietf.rfc4006 import *
from .ietf.rfc4072 import *
from .ietf.rfc5447 import *
from .ietf.rfc6733 import *
from .ietf.rfc7155 import *
from .ietf.rfc8506 import *
