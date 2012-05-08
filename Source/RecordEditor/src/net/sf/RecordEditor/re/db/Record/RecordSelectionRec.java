package net.sf.RecordEditor.re.db.Record;

//import java.util.ArrayList;

import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.jdbc.AbsRecord;


/**
 *   This class holds the fields extracted from a SQL statement:
 *
 *   <pre>
 *       Select RECORDID,
 *              Child_Key,
 *              Field_No,
 *              Boolean_Operator,
 *              Field_Name,
 *              Operator,
 *              Field_Value
 *       From   Tbl_RFS_FieldSelection
 *
 *   </pre>
 * This class also provides both specific field access methods
 * and Generic (based on Field number) access
 *
 * @Author Generated by BuildJava.Rexx by Bruce Martin
 *
 */
public class RecordSelectionRec extends AbsRecord {

//	public static final int OPERATOR_OR  = 0;
//	public static final int OPERATOR_AND = 1;

	private static final String[] OR_LIST  = {"Or", ""};
	private static final String[] AND_LIST = {"", "And"};

	protected int init_FieldNo;
	private int recordId,
	            childKey,
	            fieldNo,
	            booleanOperator;
	private String testField,
	               operator,
	               fieldValue;


	public RecordSelectionRec() {
		super();

		recordId=0;
        childKey=0;
        fieldNo=-1;
        booleanOperator=Common.BOOLEAN_OPERATOR_AND;
		testField="";
        operator="=";
        fieldValue="";

        setNew(true);

		setKeys();
	}



	public RecordSelectionRec(int recordId, int childKey, int fieldNo,
			int booleanOperator, String field, String operator,
			String fieldValue) {
		super();
		this.recordId = recordId;
		this.childKey = childKey;
		this.fieldNo = fieldNo;
		this.booleanOperator = booleanOperator;
		this.testField = field;
		this.operator = trimField(operator);
		this.fieldValue = fieldValue;

		setKeys();
	}



	/**
	 * This method copies the key fields to the Init* fields
	 */
	public void setKeys() {

		init_FieldNo = fieldNo;
	}

	/**
	 * This method returns clones the current record
	 *
	 * @return a duplicate of the current record
	 */
	public Object clone() {

		Object r = super.clone();
		if (r instanceof RecordSelectionRec) {
			return r;
		}

		RecordSelectionRec ret = new RecordSelectionRec(recordId, childKey, fieldNo, booleanOperator, testField, operator, fieldValue);
		ret.setNew(true);
		ret.setUpdateStatus(UPDATED);

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

//		if (updateStatus == NULL_INT_VALUE)
//			return "";

		switch (fieldNum) {
			case 0: return OR_LIST[booleanOperator];
			case 1: return AND_LIST[booleanOperator];
			case 2: return testField;
			case 3: return trimField(operator);
			case 4: return fieldValue;

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

		//System.out.println("setFieldWithString " + fieldNum + " " + val);
		switch (fieldNum) {
			case 0: setBooleanOperator(searchArray(val, OR_LIST));	break;
			case 1: setBooleanOperator(searchArray(val, AND_LIST));	break;
			case 2: setTestField(val);			break;
			case 3: setOperator(val);			break;
			case 4: setFieldValue(val);			break;
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

		System.out.println("setFieldWithObject " + fieldNum + " " + val);
		if (val == null) {
			setFieldWithString(fieldNum, "");
		} else {
			setFieldWithString(fieldNum, val.toString());
		}
//		switch (fieldNum) {
//		//case 0: setBooleanOperator(1 - ((Integer) val).intValue());	break;
//		//case 1: setBooleanOperator(((Integer) val).intValue());		break;
//
//		default:
//		}
	}


	private int searchArray(String val, String[] array) {
		if (fieldNo == 0) return 0;

		for (int i = 0; i < array.length; i++) {
			if (array[i].equalsIgnoreCase(val)) {
				return i;
			}
		}
		return 0;
	}


	/**
	 * @return the recordId
	 */
	public int getRecordId() {
		return recordId;
	}



	/**
	 * @param recordId the recordId to set
	 */
	public void setRecordId(int recordId) {
		this.recordId = recordId;
	}



	/**
	 * @return the childKey
	 */
	public int getChildKey() {
		return childKey;
	}



	/**
	 * @param childKey the childKey to set
	 */
	public void setChildKey(int childKey) {
		if (this.childKey != childKey) {
			this.childKey = childKey;
			updateStatus = UPDATED;
		}
	}



	/**
	 * @return the fieldNo
	 */
	public int getFieldNo() {
		return fieldNo;
	}



	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.re.db.Record.FieldNumberRecord#setFieldNo(int)
	 */
	public void setFieldNo(int fieldNo) {
		if (this.fieldNo != fieldNo) {
			this.fieldNo = fieldNo;
			updateStatus = UPDATED;
		}
	}



	/**
	 * @return the booleanOperator
	 */
	public int getBooleanOperator() {
		return booleanOperator;
	}



	/**
	 * @param booleanOperator the booleanOperator to set
	 */
	public void setBooleanOperator(int booleanOperator) {
		if (this.booleanOperator != booleanOperator) {
			this.booleanOperator = booleanOperator;
			updateStatus = UPDATED;
		}
	}



	/**
	 * @return the testField
	 */
	public String getFieldName() {
		return testField;
	}



	/**
	 * @param testField the testField to set
	 */
	public void setTestField(String testField) {
		if (! equals(this.testField , testField)) {
			this.testField = testField;
		}
	}



	/**
	 * @return the operator
	 */
	public String getOperator() {
		return trimField(operator);
	}



	/**
	 * @param operator the operator to set
	 */
	public void setOperator(String operator) {

		System.out.println("setOperator: " + operator + "< >" + trimField(operator) + "<");
		operator = trimField(operator);
		if (! equals(this.operator , operator)) {
			this.operator = operator;
		}
	}



	protected String trimField(String s) {
		if (s != null) {
			s = s.trim();
		}

		return s;
	}

	/**
	 * @return the fieldValue
	 */
	public String getFieldValue() {
		return fieldValue;
	}



	/**
	 * @param fieldValue the fieldValue to set
	 */
	public void setFieldValue(String fieldValue) {
		if (! equals(this.fieldValue , fieldValue)) {
			this.fieldValue = fieldValue;
		}
	}



}
