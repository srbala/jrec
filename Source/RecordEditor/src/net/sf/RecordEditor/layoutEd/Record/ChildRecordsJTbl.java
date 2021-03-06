/*
 * Created on 19/09/2004
 *
 * Changes
 * # Version 0.56 Bruce Martin 2007/01/16
 *   - Added new Child Record Popup
 *   - ensure all Child Record layout are in the Combo Box
 *     (even those in other Systems)
 */
package net.sf.RecordEditor.layoutEd.Record;

/**
 * This class implements a JTable to display Child Records of a parent
 * record
 *
 * @author Bruce Martin
 *
 */



import javax.swing.DefaultCellEditor;
import javax.swing.JComboBox;
import javax.swing.table.TableColumnModel;

import net.sf.RecordEditor.re.db.Record.RecordDB;
import net.sf.RecordEditor.re.db.Record.RecordRec;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.common.ReConnection;
import net.sf.RecordEditor.utils.jdbc.AbsDB;
import net.sf.RecordEditor.utils.swing.AbsJTable;
import net.sf.RecordEditor.utils.swing.ButtonTableRendor;
import net.sf.RecordEditor.utils.swing.ComboBoxRender;
import net.sf.RecordEditor.utils.swing.ComboBoxs.KeyedComboMdl;



/**
 * Child record Table
 *
 *
 * @author Bruce Martin
 *
 */
@SuppressWarnings("serial")
public class ChildRecordsJTbl extends AbsJTable {

    private final RecordDB childRecordRecords   = new RecordDB();

    private final KeyedComboMdl<Integer> childRecordModel;

	private ButtonTableRendor tableBtn = new ButtonTableRendor();

	private final ChildRecordsTblMdl model;


//    /**
//     * Create the Child record Table
//     *
//     * @param dbIdx Database Index
//     */
//    public ChildRecordsJTbl(final int dbIdx) {
//        super();
//
//        commonInit(dbIdx);
//    }


  /**
   * Create the Child record Table
   *
   * @param mdl Table model
   * @param dbIdx Database Index
   */
  public ChildRecordsJTbl(final ChildRecordsTblMdl mdl, final int dbIdx) {
      super(mdl);
      model = mdl;

      //super.setName("ChildRecordsJTbl");

      childRecordModel = new KeyedComboMdl<Integer>(model.recordKeys.nullItem);

      childRecordRecords.setConnection(new ReConnection(dbIdx));
      childRecordRecords.resetSearch();
      childRecordRecords.setSearchRecordType(AbsDB.opLT, Common.rtGroupOfRecords);

      setColumnSizes();
  }


  	/**
  	 * Set the column sizes
  	 */
	public void setColumnSizes() {
		//ParentList = new ParentList()
		//ParentList list = new ParentList();
		//BmKeyedComboBox parentCombo = new BmKeyedComboBox(list, false);

		TableColumnModel tcm = this.getColumnModel();

		tcm.getColumn(0).setCellRenderer(tableBtn);
		tcm.getColumn(0).setMaxWidth(5);
		tcm.getColumn(1).setCellRenderer(tableBtn);
		tcm.getColumn(1).setMaxWidth(5);

		tcm.getColumn(ChildRecordsTblMdl.RECORD_COLUMN).setCellRenderer(
				new ComboBoxRender(model.recordKeys));
		tcm.getColumn(ChildRecordsTblMdl.RECORD_COLUMN).setCellEditor(
				new DefaultCellEditor(
						new ComboBoxRender(childRecordModel)));
		childRecordModel.trace = true;

		tcm.getColumn(ChildRecordsTblMdl.PARENT_COLUMN).setCellRenderer(
				new ComboBoxRender(model.getParentModel()));
		tcm.getColumn(ChildRecordsTblMdl.PARENT_COLUMN).setCellEditor(
				new DefaultCellEditor(
						new JComboBox(model.getParentModel())));

		tcm.moveColumn(1, 5);

}


	/**
	 * Set the System id
	 *
	 * @param system new system
	 */
	public void setSystem(int system) {

		boolean doFree = childRecordRecords.isSetDoFree(false);

		KeyedComboMdl<Integer> childRecordModel1 = model.recordKeys;

		childRecordModel.removeAllElements();
		childRecordModel1.removeAllElements();
	    childRecordRecords.resetSearch();
	    childRecordRecords.setSearchRecordType(AbsDB.opLT, Common.rtGroupOfRecords);

	    if (system != Common.UNKNOWN_SYSTEM) {
	        StringBuffer b = new StringBuffer();
	        char sep = '(';
        	boolean foundRec = false;

	        if (model.getRowCount() > 0) {
	            for (int i = model.getRowCount() - 1; i >= 0; i--) {
	            	if (model.getRecord(i).getChildRecordId() >= 0) {
	            		b.append(sep).append(model.getRecord(i).getChildRecordId());
	            		foundRec = true;
		                sep = ',';
	            	}
	            }
	        }
            if (foundRec) {
	            b.append(')').append(')');
	            childRecordRecords.setSqlOperator(" And (");
	            childRecordRecords.setSearchSystem(AbsDB.opEquals, system);
	            childRecordRecords.setSqlOperator(" Or ");
	            childRecordRecords.setSearchArg("RecordId", AbsDB.opIn, b.toString());
            } else {
            	childRecordRecords.setSearchSystem(AbsDB.opEquals, system);
            }
		}

	    //System.out.println();
	    //System.out.println(" --------------------------------------------------------------");
	    childRecordRecords.setOrderBy(" Order by RecordName");
	    childRecordRecords.open();
	    RecordRec rec ;

		while ((rec = childRecordRecords.fetch()) != null) {
			//System.out.println(" ==> " + rec.getRecordId() + " "+ rec.getRecordName());


			childRecordModel1.addElement(
					childRecordModel.addElement(
							Integer.valueOf(rec.getRecordId()),
							rec.getRecordName()));
		}
	    //System.out.println(" --------------------------------------------------------------");

		childRecordRecords.close();
		childRecordRecords.setDoFree(doFree);

		//setColumnSizes();
		//model.fireTableDataChanged();
	}
}
