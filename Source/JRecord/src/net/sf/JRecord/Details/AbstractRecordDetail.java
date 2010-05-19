package net.sf.JRecord.Details;

import net.sf.JRecord.Common.AbstractRecord;
import net.sf.JRecord.Common.FieldDetail;


public interface AbstractRecordDetail<FieldDefinition extends FieldDetail> 
extends AbstractRecord {

	/**
	 * Add a record to the layout
	 * @param field new field
	 */
	public abstract void addField(FieldDefinition field);

	/**
	 * Get the Record Name
	 *
	 * @return Record Name
	 */
	public abstract String getRecordName();

	/**
	 * Get Selection Field
	 * @return Selection field
	 */
	public abstract FieldDefinition getSelectionField();

	/**
	 * @param newSelectionField the selectionFld to set
	 */
	public abstract void setSelectionField(FieldDefinition newSelectionField);

	/**
	 * This method returns a value to be compared with the selection field.
	 * If the Selection field is equals this value, it is assumed that this
	 * record Layout should be used to display the line
	 *
	 * @return Selection Value
	 */
	public abstract String getSelectionValue();

	/**
	 * Get the Record Type
	 *
	 * @return Record - Return the record layout
	 */
	public abstract int getRecordType();

	/**
	 * Gets the records length
	 *
	 * @return the records length
	 */
	public abstract int getLength();

	/**
	 * Get the font name to use when viewing string fields
	 *
	 * @return font Name
	 */
	public abstract String getFontName();

	/**
	 * wether it is a binary field or not
	 *
	 * @param fldNum fldNum Field Number
	 *
	 * @return wether it is a binary field
	 */
	public abstract boolean isBinary(int fldNum);

//	/**
//	 * Check if field is numeric 
//	 * @param fldNum field to check
//	 * @return wether it is numeric or not
//	 */
//	public abstract boolean isNumericField(int fldNum);

	/**
	 * Get the Index of a specific record (base on name)
	 *
	 * @param fieldName record name being searched for
	 *
	 * @return index of the record
	 */
	public abstract int getFieldIndex(String fieldName);

	/**
	 * Get a specific field definition
	 * @param idx index of the required field
	 * @return requested field
	 */
	public abstract FieldDefinition getField(int idx);

	/**
	 * Get the numeric Type of field
	 * @param idx field index
	 * @return numeric type (if it is numeric)
	 */
	public abstract int getFieldsNumericType(int idx);

	/**
	 * Get a specific field definition (using the field name)
	 *
	 * @param fieldName record name being searched for
	 *
	 * @return index of the record
	 */
	public abstract FieldDefinition getField(String fieldName);

	/**
	 * get the number of fields in the record
	 *
	 * @return the number of fields in the record
	 */
	public abstract int getFieldCount();

	/**
	 * Get the maximum width of the fields (a value < 0 means
	 * use the default width).
	 *
	 * @return Returns the widths.
	 */
	public abstract int[] getWidths();

	/**
	 * Get the Field Delimiter (ie Tab / Comma etc in CSV files)
	 *
	 * @return Returns the delimiter.
	 */
	public abstract String getDelimiter();

	/**
	 * @see net.sf.JRecord.Common.AbstractRecord#getQuote()
	 */
	public abstract String getQuote();

	/**
	 * @see net.sf.JRecord.Common.AbstractRecord#getParentRecordIndex()
	 */
	public abstract int getParentRecordIndex();

	/**
	 * @param parentRecordIndex the parentRecordIndex to set
	 */
	public abstract void setParentRecordIndex(int parentRecordIndex);

	/**
	 * @see net.sf.JRecord.Common.AbstractRecord#getRecordStyle()
	 */
	public abstract int getRecordStyle();

	/**
	 * get the count of childRecords
	 * @return
	 */
	public int getChildRecordCount();
	
	/**
	 * Get Child Record Definition
	 * @param idx Child Index
	 * @return Child record Definition
	 */
	public AbstractChildDetails<? extends AbstractRecordDetail<FieldDefinition>> getChildRecord(int idx);
	
//	/**
//	 * @return the sourceIndex
//	 * 
//	 *  @see net.sf.JRecord.Common.AbstractRecord#getSourceIndex()
//	 */
//	public abstract int getSourceIndex();
//
//	/**
//	 * @param sourceIndex the sourceIndex to set
//	 */
//	public abstract void setSourceIndex(int sourceIndex);

}