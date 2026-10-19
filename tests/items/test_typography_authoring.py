from unittest.mock import patch
import pytest
from PyQt6.QtTest import QTest
from gns3.qt import QtCore, QtWidgets
from canvas_fixtures import canvas, drawing


@pytest.mark.parametrize('accept', [False, True])
def test_note_creation_dialog_confirms_or_discards(canvas, accept):
    from gns3.items.text_item import TextItem
    canvas._adding_note = True
    result = QtWidgets.QDialog.DialogCode.Accepted if accept else QtWidgets.QDialog.DialogCode.Rejected
    with patch('gns3.graphics_view.TextEditorDialog.exec', return_value=result) as dialog:
        QTest.mouseClick(canvas.viewport(), QtCore.Qt.MouseButton.LeftButton, pos=QtCore.QPoint(160, 140))
        dialog.assert_called_once()
    assert len([item for item in canvas.scene().items() if isinstance(item, TextItem)]) == int(accept)


def test_note_typography_defaults_project_fonts_and_svg_roundtrip(canvas):
    from gns3.dialogs.text_editor_dialog import TextEditorDialog
    from gns3.items.text_item import TextItem
    note = drawing(canvas, 'text')
    initial = note.font()
    dialog = TextEditorDialog(canvas, [note])
    assert dialog.fontFamily.currentText() == initial.family()
    assert dialog.fontSize.value() == initial.pointSizeF()
    dialog.fontSize.setValue(32)
    dialog.underline.setChecked(True)
    dialog.uiPlainTextEdit.setPlainText('Network LAN')
    dialog.accept()
    copy = TextItem(svg=note.toSvg())
    assert copy.font().underline() and copy.font().pointSizeF() == 32
    assert copy.toPlainText() == 'Network LAN'
