"""Creation must complete before drawing updates or deletion reach the server."""
from unittest.mock import MagicMock
from gns3.qt import QtCore
from canvas_fixtures import canvas, drawing


def test_creation_acknowledgment_flushes_latest_drawing_state(canvas):
    shape = drawing(canvas)
    project = shape._project = MagicMock()
    shape.create()
    posted = project.post.call_args.kwargs['body']
    acknowledge = project.post.call_args.args[1]
    shape.setPos(123, 456)
    shape.setWidthAndHeight(350, 240)
    shape.updateDrawing()
    shape.updateDrawing()
    assert project.post.call_count == 1
    project.put.assert_not_called()
    acknowledge(posted)
    project.put.assert_called_once()
    latest = project.put.call_args.kwargs['body']
    assert (latest['x'], latest['y']) == (123, 456)
    assert 'svg' in latest
    assert shape.scenePos() == QtCore.QPointF(123, 456)


def test_pending_drawing_delete_waits_for_create_acknowledgment(canvas):
    shape = drawing(canvas)
    project = shape._project = MagicMock()
    shape.create()
    acknowledge = project.post.call_args.args[1]
    posted = project.post.call_args.kwargs['body']
    shape.delete()
    project.delete.assert_not_called()
    acknowledge(posted)
    project.delete.assert_called_once_with('/drawings/' + shape.drawing_id(), None)
