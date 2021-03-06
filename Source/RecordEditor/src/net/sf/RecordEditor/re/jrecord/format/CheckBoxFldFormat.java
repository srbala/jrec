/*
 * @Author Bruce Martin
 * Created on 9/02/2007 version 0.60
 *
 * Purpose:
 * A String based check box format with supplied yes / no strings
 */
package net.sf.RecordEditor.re.jrecord.format;

import javax.swing.table.TableCellEditor;
import javax.swing.table.TableCellRenderer;

import net.sf.JRecord.Common.IFieldDetail;
import net.sf.JRecord.CsvParser.BasicCsvLineParser;
import net.sf.JRecord.CsvParser.CsvDefinition;
import net.sf.RecordEditor.utils.swing.CheckboxTableRenderStringBased;
import net.sf.RecordEditor.utils.swing.SwingUtils;


/**
 * A check box format with supplied yes / no strings
 * coming from the field
 *
 * @author Bruce Martin
 *
 */
public class CheckBoxFldFormat implements CellFormat {

    private CheckboxTableRenderStringBased render = null;
    //render = new StringCheckBoxTableRender(yesStr, noStr, defaultVal);


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
        return getCheckbox(fld);
    }

    /**
     * @see net.sf.RecordEditor.re.jrecord.format.CellFormat#getTableCellRenderer(net.sf.RecordEditor.record.types.FieldDetail)
     */
    @Override
    public TableCellRenderer getTableCellRenderer(IFieldDetail fld) {
        if (render == null) {
            render = getCheckbox(fld);
        }
        return render;
    }

    /**
     * Get the Swing checkbox
     * @param fld field definition
     * @return Swing checkbox
     */
    private CheckboxTableRenderStringBased getCheckbox(IFieldDetail fld) {
        String s = fld.getParamater();
        CheckboxTableRenderStringBased ret = null;

        if (s != null) {
            try {
            	BasicCsvLineParser parser = BasicCsvLineParser.getInstance();
            	String line = s.substring(1);
            	String delim = s.substring(0, 1);

            	CsvDefinition csvDef = new CsvDefinition(delim, "");
                String yesStr = parser.getField(0, line, csvDef);
                String noStr  = parser.getField(1, line, csvDef);
                String defaultValue  = parser.getField(2, line, csvDef);
                //System.out.println("Case Sensitive ~~> " + parser.getField(3, line, delim, ""));
                boolean caseSensitive = "Y".equalsIgnoreCase(parser.getField(3, line, csvDef)) ;

                ret = new CheckboxTableRenderStringBased(yesStr, noStr,
                		yesStr.equals(defaultValue), caseSensitive);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return ret;
    }
}
