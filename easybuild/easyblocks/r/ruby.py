##
# Copyright 2009-2013 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
EasyBuild support for Ruby, implemented as an easyblock

@author: Robert Schmidt (OHRI)
"""

from easybuild.easyblocks.generic.configuremake import ConfigureMake

#Seems like the quickest test for whether a gem is installed
EXTS_FILTER_GEMS = ("gem list %(ext_name)s -i", "")

class EB_Ruby(ConfigureMake):
    
    def prepare_for_extensions(self):
        self.cfg['exts_defaultclass'] = "RubyGem"
        self.cfg['exts_filter'] = EXTS_FILTER_GEMS

