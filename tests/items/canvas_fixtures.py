"""Shared real-Qt fixtures for independently reviewable canvas features."""
import uuid
from unittest.mock import MagicMock
import pytest
from gns3.qt import QtCore, QtWidgets
from gns3.graphics_view import GraphicsView
from gns3.items.node_item import NodeItem


@pytest.fixture
def canvas(main_window):
    main_window.uiSnapToGridAction.isChecked.return_value = False
    window = QtWidgets.QMainWindow()
    central = QtWidgets.QWidget(window)
    window.setCentralWidget(central)
    view = GraphicsView(central)
    view._main_window = main_window
    view.toggleUiDeviceMenu = MagicMock()
    main_window.uiGraphicsView = view
    view._topology = MagicMock()
    view._topology.project.return_value = None
    view._topology.links.return_value = []
    view.resize(800, 600)
    view.show()
    yield view
    window.close()


def device(view, x=0, y=0):
    node = MagicMock()
    node.x.return_value, node.y.return_value = x, y
    node.z.return_value = 1
    node.locked.return_value = False
    node.initialized.return_value = False
    node.node_id.return_value = str(uuid.uuid4())
    node.name.return_value = "Device-" + node.node_id.return_value
    item = NodeItem(node)
    view.scene().addItem(item)
    return item


def drawing(view, kind="rect", x=0, y=0):
    svg = '<svg width="80" height="40"><rect width="80" height="40" /></svg>'
    if kind == "text":
        svg = '<svg width="80" height="40"><text x="0" y="16">hello</text></svg>'
    return view.createDrawingItem(kind, x, y, 0, svg=svg)
