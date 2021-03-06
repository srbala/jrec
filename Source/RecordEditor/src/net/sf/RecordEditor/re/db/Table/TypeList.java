/*
 * @Author Bruce Martin
 * Created on 27/03/2007 for version 0.61
 *
 * Purpose:
 */
package net.sf.RecordEditor.re.db.Table;

import java.util.ArrayList;

import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.params.Parameters;

/**
 *
 *
 * @author Bruce Martin
 *
 */
public class TypeList extends TableList {

    /**
     * Define List of Types
     * @param connectionId DB connection
     * @param sort wether thew list should be sorted
     * @param nullFirstRow wether the first row should be null
     */
    public TypeList(final int connectionId,
            final boolean sort, final boolean nullFirstRow) {
        this(connectionId, sort, nullFirstRow, true);
    }

    /**
     * Define List of Types
     * @param connectionId DB connection
     * @param sort wether thew list should be sorted
     * @param nullFirstRow wether the first row should be null
     */
    public TypeList(final int connectionId,
            final boolean sort, final boolean nullFirstRow, boolean foriegnTranslation) {
        super(connectionId, Common.TI_FIELD_TYPE, sort, nullFirstRow,
              Parameters.TYPE_NUMBER_PREFIX, Parameters.TYPE_NAME_PREFIX,
	          Parameters.NUMBER_OF_TYPES, foriegnTranslation);
        
//
//  Code to compare types in BasicConversion with those in the DB
//
//        BasicConversion b = new BasicConversion();
//        for (int i = 0; i < super.getSize(); i++) {
//        	try {
//				int key = Integer.parseInt(super.getKeyAt(i).toString());
//				System.out.println(i + "\t" + key + "\t" + super.getFieldAt(i, 1) + "\t - \t" + b.getTypeAsString(0, key));
//			} catch (NumberFormatException e) {
//				System.out.println(i + "\t" + super.getKeyAt(i) + "\t" +  super.getFieldAt(i, 1));
//				e.printStackTrace();
//			}
//        	
//        }
    }

	/**
	 * Load the list from DB / properties file
	 */

	public void loadData() {
		ArrayList<TableRec> list = getPropertiesAndDB();
		String name;
		int j = Parameters.FIRST_USER_DATE_TYPE;

		for (int i = 0; i < Parameters.DATE_TYPE_TABLE_SIZE; i++) {
		    name = Parameters.getString(Parameters.PROPERTY_DATE_TYPE_NAME + i);
		    if (name != null && ! "".equals(name)) {
                list.add(new TableRec(j, name));
		    }
		    j += 1;
		}
        //list.add(new ArrayRow(new Object[]{new Integer(115), "CSV array"}));

		loadData(list);
	}

}
