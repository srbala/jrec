package net.sf.RecordEditor.utils.swing;

import java.awt.Component;
import java.awt.Font;

import javax.swing.JTable;
import javax.swing.table.DefaultTableCellRenderer;

import net.sf.RecordEditor.utils.common.Common;

@SuppressWarnings("serial")
public class StandardRendor extends DefaultTableCellRenderer implements IExternalTableCellColoring {

	private ITableColoringAgent tableCellColoring = null;

	private Font font = null;
	public StandardRendor() {
		this(false);
	}


	public StandardRendor(boolean bold) {
		if (bold) {
			Font currFont = super.getFont();
			font = new Font(currFont.getFamily(), Font.BOLD, currFont.getSize());
		}
	}


	/* (non-Javadoc)
	 * @see javax.swing.table.DefaultTableCellRenderer#getTableCellRendererComponent(javax.swing.JTable, java.lang.Object, boolean, boolean, int, int)
	 */
	@Override
	public Component getTableCellRendererComponent(JTable tbl, Object value,
			boolean isSelected, boolean hasFocus, int row, int col) {

		Component ret =  super.getTableCellRendererComponent(tbl, value, isSelected, hasFocus, row, col);

		boolean higlight = Common.OPTIONS.highlightEmpty.isSelected();
		if (higlight && value == Common.MISSING_VALUE) {
			ret.setBackground(Common.EMPTY_COLOR);
		} else if (value == Common.MISSING_REQUIRED_VALUE) {
			ret.setBackground(Common.MISSING_COLOR);
//		} else  {
//			CommonSwingCode.setTableCellBackGround(this, tbl, row, isSelected);
		} else if (tableCellColoring != null) {
			tableCellColoring.setTableCellColors(ret, tbl, row, col, isSelected);
		}

		if (font != null) {
			super.setFont(font);
		}

		return ret;
	}


	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.swing.IExternalTableCellColoring#setTableCellColoring(net.sf.RecordEditor.utils.swing.ISetTableColor)
	 */
	@Override
	public void setTableCellColoring(ITableColoringAgent tableCellColoring) {
		this.tableCellColoring = tableCellColoring;
	}

}
