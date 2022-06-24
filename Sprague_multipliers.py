# -*- coding: utf-8 -*-

"""
/***************************************************************************
 SpragueMultipliers
                                 A QGIS plugin
 This plugin generates school-aged population for any polygon layer
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-04-01
        copyright            : (C) 2021 by IIEP-UNESCO
        email                : development@iiep.unesco.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'IIEP-UNESCO'
__date__ = '2021-04-01'
__copyright__ = '(C) 2021 by IIEP-UNESCO'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon

import processing

from qgis.core import QgsProcessingAlgorithm, QgsApplication
from .Sprague_multipliers_provider import SpragueMultipliersProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class SpragueMultipliersPlugin(object):

    def __init__(self, iface):
        self.provider = None
        self.iface = iface

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = SpragueMultipliersProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
      self.initProcessing()

      icon = os.path.join(os.path.join(cmd_folder, 'sprague_logo.svg'))
      self.action = QAction(
          QIcon(icon),
          u"Sprague multipliers", self.iface.mainWindow())
      self.action.triggered.connect(self.run)
      self.iface.addPluginToMenu(u"&SpragueMultipliersAlgorithm", self.action)
      self.iface.addToolBarIcon(self.action)

    def unload(self):
      QgsApplication.processingRegistry().removeProvider(self.provider)
      self.iface.removePluginMenu(u"&SpragueMultipliersAlgorithm", self.action)
      self.iface.removeToolBarIcon(self.action)

    def run(self):
      processing.execAlgorithmDialog("IIEP-UNESCO:Sprague Multipliers")
