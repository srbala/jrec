package net.sf.RecordEditor.re.db.Combo;

//import java.util.ArrayList;

import net.sf.JRecord.Common.Constants;
import net.sf.RecordEditor.utils.jdbc.AbsRecord;
import net.sf.RecordEditor.utils.swing.AbstractRowList;

/**
 *   This class holds the fields extracted from a SQL statement:
 *
 *   <pre>
 *       Select Combo_Id,
 *              System,
 *              Combo_Name,
 *              Column_Type
 *       From   Tbl_C_Combos
 *
 *   </pre>
 * This class also provides both specific field access methods
 * and Generic (based on Field number) access
 *
 * @Author Generated by BuildJava.Rexx by Bruce Martin
 *
 */
public class ComboRec extends AbsRecord {

	public static final int SINGLE_COLUMN = 1;
	private int comboId;
	protected int initCombo_Id ;
	private int system;
	private String comboName;
	private int columnType;
	private AbstractRowList rows = null;
	//private DBtableModel children;

//	private Connection con;

//	private ComboValuesDB valuesDB = null;




	public ComboRec() {
		super();

		comboId = 0;
		system = 0;
		comboName = "";
		columnType = 0;
		//con = dbConnection;

		setKeys();
	}

	public ComboRec(int pCombo_Id, int pSystem, String pCombo_Name, int pColumn_Type) {
		super(false);

		comboId = pCombo_Id;
		system = pSystem;
		comboName = pCombo_Name;
		columnType = pColumn_Type;
		//con = dbConnection;

		setKeys();
	}

	/**
	 * This method copies the key fields to the Init* fields
	 */
	public void setKeys() {

		initCombo_Id = comboId;
	}

	/**
	 * This method returns clones the current record
	 *
	 * @return a duplicate of the current record
	 */
	public Object clone() {

		Object r = super.clone();
		if (r instanceof ComboRec) {
			return r;
		}

		ComboRec ret = new ComboRec(Constants.NULL_INTEGER, system, comboName, columnType);
		ret.setNew(true);
		ret.setUpdateStatus(ComboRec.UPDATED);

		return ret;
	}

	/**
	 * This method returns clones the current record
	 */
	public int getFieldCount() {
		return 2;
	}

	/**
	 * This method returns a field (specified by field number)
	 *
	 * @param fieldNum
	 *            the field number (in the record)
	 * @return the request field
	 */
	public Object getField(int fieldNum) {

		if (updateStatus == NULL_INT_VALUE)
			return "";

		switch (fieldNum) {
			// case (0) : return new Integer(Combo_Id);
			case (0):
				return Integer.valueOf(system);
			case (1):
				return comboName;
			default:
				return "";
		}
	}

	/**
	 * This method sets a field (specified by field number) with a string value
	 *
	 * @param fieldNum
	 *            the field number (in the record)
	 * @param val
	 *            the value to be assigned to the field
	 */
	protected void setFieldWithString(int fieldNum, String val) {

		switch (fieldNum) {
			// case (0) : setCombo_Id(cnvToInt(Combo_Id, val, "Combo_Id" ));
			// break;
			case (0):
				setSystem(cnvToInt(system, val, "System"));
			break;
			case (1):
				setComboName(val);
			break;
			default:
				;
		}
	}

	/**
	 * This method sets a field (specified by field number) with an object value
	 *
	 * @param fieldNum
	 *            the field number (in the record)
	 * @param val
	 *            the value to be assigned to the field
	 */
	protected void setFieldWithObject(int fieldNum, Object val) {

		switch (fieldNum) {
			// case (0) : setCombo_Id(((Integer) val).intValue());
			// break;
			case (0):
				setSystem(((Integer) val).intValue());
			break;
			default:
				setFieldWithString(fieldNum, (String) val);
		}
	}

	/**
	 * This method gets the vaule of Combo_Id
	 */
	public int getComboId() {
		return comboId;
	}

	/**
	 * This method sets the vaule of Combo_Id
	 *
	 * @param val
	 *            value to be assigned to Combo_Id
	 */
	public void setComboId(int val) {

		if ((val != comboId) || (updateStatus == NULL_INT_VALUE)) {
			comboId = val;
			updateStatus = UPDATED;
		}
	}

	/**
	 * This method gets the vaule of System
	 */
	public int getSystem() {
		return system;
	}

	/**
	 * This method sets the vaule of System
	 *
	 * @param val
	 *            value to be assigned to System
	 */
	public void setSystem(int val) {

		if ((val != system) || (updateStatus == NULL_INT_VALUE)) {
			system = val;
			updateStatus = UPDATED;
		}
	}

	/**
	 * This method gets the vaule of Combo_Name
	 */
	public String getComboName() {
		return comboName;
	}

	/**
	 * This method sets the vaule of Combo_Name
	 *
	 * @param val
	 *            value to be assigned to Combo_Name
	 */
	public void setComboName(String val) {

		if ((val == null || "".equals(val))
				&& (comboName == null || "".equals(comboName))) {
			return;
		}

		if ((val == null) || (!val.equals(comboName))
				|| (updateStatus == NULL_INT_VALUE)) {
			comboName = val;
			updateStatus = UPDATED;
		}
	}


	/**
	 * @return the column_Type
	 */
	public int getColumnType() {
		return columnType;
	}

	/**
	 * @param newColumnType the column_Type to set
	 */
	public void setColumnType(int newColumnType) {

		if (columnType != newColumnType) {
			columnType = newColumnType;
			updateStatus = UPDATED;
		}
	}

	/**
	 * @return the rows
	 */
	public AbstractRowList getRows() {
		return rows;
	}

	/**
	 * @param rows the rows to set
	 */
	public void setRows(AbstractRowList rows) {
		this.rows = rows;
	}
}
