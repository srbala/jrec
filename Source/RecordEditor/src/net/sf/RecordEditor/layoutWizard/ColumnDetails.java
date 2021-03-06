/*
 * @Author Bruce Martin
 * Created on 10/01/2007
 *
 * Purpose:
 * Column details record
 *
 * Changes
 * # Version 0.61b Bruce Martin 2007/05/05
 *  - Changes o support user selecting the default type
 */
package net.sf.RecordEditor.layoutWizard;

import net.sf.RecordEditor.utils.lang.LangConversion;
import net.sf.RecordEditor.utils.swing.treeCombo.TreeComboItem;

/**
 * Column details record
 *
 * @author Bruce Martin
 *
 */
public class ColumnDetails {

    public static final int NAME_IDX    = 0;
    public static final int START_IDX   = 1;
    public static final int LENGTH_IDX  = 2;
    public static final int TYPE_IDX    = 3;
    public static final int DECIMAL_IDX    = 4;
    public static final int INCLUDE_IDX = 5;
    public static final int NUMBER_OF_COLUMNS = 6;

    private static final String[] COLUMN_NAMES = LangConversion.convertColHeading(
			"LayoutWizard Field definition",
			new String[] {
            "Field Name", "Start", "Length", "Type", "Decimal", "Include"
    });

    public String name = "";
    protected int start  = 0;
    public int length = 0;
    public int type;
    public int decimal = 0;
    public boolean include = true;

    /**
     * Column details record
     *
     * @param colStart where the field starts
     * @param defaultType the initial field type to use
     */
    public ColumnDetails(final int colStart, final int defaultType) {
        super();
        start = colStart;
        type  = defaultType;
    }

    /**
     * get the value by column number
     * @param columnIdx column index to acces
     * @return column value
     */
    public Object getValue(int columnIdx) {
        Object o;

        switch (columnIdx) {
        	case(1): o = Integer.valueOf(start);   break;
        	case(2): o = Integer.valueOf(length);  break;
        	case(3): o = Integer.valueOf(type);    break;
        	case(4): o = Integer.valueOf(decimal); break;
        	case(5): o = Boolean.valueOf(include); break;
        	default: o = name;
        }

        return o;
    }


    /**
     * get the value by column number
     * @param columnIdx column index to access
     * @param o new column value
     */
    public void setValue(int columnIdx, Object o) {

        switch (columnIdx) {
        	case(1): start = getInt(o);       break;
        	case(2): length = getInt(o);      break;
        	case(3): type = getInt(o);        break;
        	case(4): decimal = getInt(o);     break;
        	case(5): include = (Boolean) o;   break;
        	default: name = o.toString();
        }
    }

    /**
	 * @return the start
	 */
	public final int getStart() {
		return start;
	}

	/**
	 * @return the length
	 */
	public final int getLength() {
		return length;
	}

	/**
	 * @return the type
	 */
	public final int getType() {
		return type;
	}

	/**
     * conver object to int
     * @param o object to convert
     * @return int value
     */
    private int getInt(Object o) {
        int i = 0;
        if (o != null) {
        	if (o instanceof Integer) {
        		i = ((Integer) o).intValue();
        	} else if (o instanceof TreeComboItem){
        		i = ((TreeComboItem) o).key;
        	} else {
       		i = Integer.parseInt(o.toString());
        	}
        }
        return i;
    }


    /**
     * gets a column name
     * @param column column to get the name of
     * @return Returns the Column name.
     */
    public static String getColumnName(int column) {
        return COLUMN_NAMES[column];
    }
}
