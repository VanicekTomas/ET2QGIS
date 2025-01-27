# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ET2QGIS
                                 A QGIS plugin
 This plugin creates analyses and visualizations from ET2Spatial data.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-08-02
        copyright            : (C) 2023 by Tomas Vanicek (Palacky University)
        email                : tomas.vanicek@upol.cz
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ET2QGIS class from file ET2QGIS.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .et2qgis import ET2QGIS
    return ET2QGIS(iface)
