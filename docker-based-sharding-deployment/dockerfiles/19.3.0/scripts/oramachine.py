#!/usr/bin/python
# LICENSE UPL 1.0
#
# Copyright (c) 2020,2021 Oracle and/or its affiliates.
#
# Since: January, 2020
# Author: sanjay.singh@oracle.com, paramdeep.saini@oracle.com

from oralogger import *
from oraenv import *
from oracommon import *
from oramachine import *

import os
import sys

class OraMachine:
    """
     This calss setup the compute before starting the installation.
    """
    def __init__(self,oralogger,orahandler,oraenv,oracommon):
        """
        This constructor of OraMachine class to setup the compute 

        Attributes:
           oralogger (object): object of OraLogger Class.
           ohandler (object): object of Handler class.
           oenv (object): object of singleton OraEnv class.
           ocommon(object): object of OraCommon class.
           ora_env_dict(dict): Dict of env variable populated based on env variable for the setup.
           file_name(string): Filename from where logging message is populated.
        """
        self.ologger             = oralogger
        self.ohandler            = orahandler
        self.oenv                = oraenv.get_instance()
        self.ocommon             = oracommon
        self.ora_env_dict        = oraenv.get_env_vars()
        self.file_name           = os.path.basename(__file__)

    def setup(self):
        """
          This function setup the compute before starting the installation
        """
        msg="Machine setup completed sucessfully!"
        self.ocommon.log_info_message(msg,self.file_name)
