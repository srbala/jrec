package net.sf.RecordEditor.re.util.csv;

import javax.swing.JButton;

import net.sf.JRecord.Details.LayoutDetail;
import net.sf.RecordEditor.utils.swing.BaseHelpPanel;

public interface FilePreview {

	public static final String SCHEMA_ID = "SCHEMA";
	public static final int NO = 1;
	public static final int LIKELY = 3;
	public static final int YES = 5;
	
	public static final String SEP = "~";
	public static final String NULL_STR = "Empty";

	public abstract BaseHelpPanel getPanel();
	public abstract JButton getGoButton();

	public abstract boolean setData(String filename, byte[] data, boolean checkCharset, String layoutId);

	/**
	 * Get The field seperator
	 * @return field seperator
	 */
	public abstract String getSeperator();

	/**
	 * Get The Quote
	 * @return Quote
	 */
	public abstract String getQuote();

	/**
	 * @param newLines the lines to set
	 * @param numberOfLines the actual number of lines used
	 */
	public abstract boolean setLines(byte[][] newLines, String font,
			int numberOfLines);


	/**
	 * @param newLines the lines to set
	 * @param numberOfLines the actual number of lines used
	 */
	public abstract void setLines(String[] newLines, String font,
			int numberOfLines);


	public abstract LayoutDetail getLayout(String font, byte[] recordSep);

	public abstract String getFileDescription();

	public abstract void setFileDescription(String val);

	public abstract String getFontName();

	public abstract int isMyLayout(String layout, String filename, byte[] data);
	
	public abstract int getSchemaCheckType();
}