package net.sf.RecordEditor.re.util.csv;

import javax.swing.table.TableModel;

public interface AbstractCsvTblMdl extends TableModel {

	public static final int DERIVE_SEPERATOR = 1;
	public static final int USE_CURRENT_SEPERATOR = 2;

	/**
	 * Set up the column details
	 */
	public abstract void setupColumnCount();

	public abstract int getLines2display();
	/**
	 * @param lines2display the lines2display to set
	 */
	public abstract void setLines2display(int lines2display);

	public abstract String getLine(int idx);

	public abstract String[] getLinesString();

	public abstract byte[][] getLines();

	public abstract int getParserType();

	public abstract void setParserType(int parserType);

	/**
	 * @param quote the quote to set
	 */
	public abstract void setQuote(String quote);

	/**
	 * @param newSeperator the seperator to set
	 */
	public abstract void setSeperator(String newSeperator);

	/**
	 * change wether the first line is hidden
	 * @param hide wether to hide first line
	 */
	public abstract void setHideFirstLine(boolean hide);

	/**
	 * Set the line number where fields are
	 * @param lineNo where the fields are
	 */
	public abstract void setFieldLineNo(int lineNo);

	/* (non-Javadoc)
	 * @see javax.swing.table.AbstractTableModel#fireTableDataChanged()
	 */
	public abstract void fireTableDataChanged();
	/* (non-Javadoc)
	 * @see javax.swing.table.AbstractTableModel#fireTableStructureChanged()
	 */
	public abstract void fireTableStructureChanged();

	public abstract void setLines(byte[][] lines, String font);

	public void setLines(String[] lines);

	public void setFont(String font);

	public CsvAnalyser getAnalyser(int opt);

	public abstract void setDataFont(byte[] data, String font, boolean embeddedCr);

	public void setEmbedded(boolean newEmbedded);
}