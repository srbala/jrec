/*
 * @Author Bruce Martin
 * Created on 9/02/2007 version 0.60
 *
 * Purpose:
 * A String based check box format with supplied yes / no strings
 */
package net.sf.RecordEditor.re.jrecord.format;

import javax.swing.DefaultCellEditor;
import javax.swing.table.TableCellEditor;
import javax.swing.table.TableCellRenderer;

import net.sf.JRecord.Common.IFieldDetail;
import net.sf.RecordEditor.utils.swing.CheckBoxTableRender;
import net.sf.RecordEditor.utils.swing.SwingUtils;


/**
 * A String based check box format with supplied yes / no strings
 *
 * @author Bruce Martin
 *
 */
public class CheckBoxBooleanFormat implements CellFormat {

    private CheckBoxTableRender render = new CheckBoxTableRender();




    /**
     * @see net.sf.RecordEditor.re.jrecord.format.CellFormat#getFieldHeight()
     */
    public int getFieldHeight() {
        return SwingUtils.CHECK_BOX_HEIGHT;
    }

    /**
     * @see net.sf.RecordEditor.re.jrecord.format.CellFormat#getFieldWidth()
     */
    public int getFieldWidth() {
        return SwingUtils.CHECK_BOX_WIDTH;
    }

    /**
     * @see net.sf.RecordEditor.re.jrecord.format.CellFormat#getTableCellEditor(net.sf.RecordEditor.record.types.FieldDetail)
     */
    @Override
    public TableCellEditor getTableCellEditor(IFieldDetail fld) {
        return new DefaultCellEditor(new CheckBoxTableRender());
    }

    /**
     * @see net.sf.RecordEditor.re.jrecord.format.CellFormat#getTableCellRenderer(net.sf.RecordEditor.record.types.FieldDetail)
     */
    @Override
    public TableCellRenderer getTableCellRenderer(IFieldDetail fld) {
        return render;
    }
}
