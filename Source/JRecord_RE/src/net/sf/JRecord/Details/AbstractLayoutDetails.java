/*  -------------------------------------------------------------------------
 *
 *            Sub-Project: RecordEditor's version of JRecord 
 *    
 *    Sub-Project purpose: Low-level IO and record translation  
 *                        code + Cobol Copybook Translation
 *    
 *                 Author: Bruce Martin
 *    
 *                License: GPL 2.1 or later
 *                
 *    Copyright (c) 2016, Bruce Martin, All Rights Reserved.
 *   
 *    This library is free software; you can redistribute it and/or
 *    modify it under the terms of the GNU General Public License
 *    as published by the Free Software Foundation; either
 *    version 2.1 of the License, or (at your option) any later version.
 *   
 *    This library is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU General Public License for more details.
 *
 * ------------------------------------------------------------------------ */
      
package net.sf.JRecord.Details;

import java.util.List;

import net.sf.JRecord.Common.IFieldDetail;

/**
 * Description of a Schema (or file definition)
 *
 * @author Bruce Martin
 *
 */
public interface AbstractLayoutDetails extends IBasicLayout {

//	/**
//	 * wether it is a binary record
//	 *
//	 * @return wether it is a binary record
//	 */
//	public abstract boolean isBinary();
//
//	public abstract boolean isBinCSV();
//
//	/**
//	 * Get the record Seperator bytes
//	 *
//	 * @return Record Seperator
//	 */
//	public abstract byte[] getRecordSep();
//
//
//	/**
//	 * Get the Canonical Name (ie Font name)
//	 *
//	 * @return Canonical Name (ie Font name)
//	 */
//	public abstract String getFontName();
//
//	/**
//	 * get the field delimiter
//	 * @return the field delimeter
//	 */
//	public abstract String getDelimiter();
//
//
//	/**
//	 * get the field delimiter
//	 * @return the field delimeter
//	 */
//	public abstract byte[] getDelimiterBytes();


	/**
	 * get a specified field
	 *
	 * @param layoutIdx the specific record layout to be used
	 * @param fieldIdx field index required
	 * @return the required field
	 */
	public abstract IFieldDetail getField(final int layoutIdx, final int fieldIdx);

	/**
	 * Get the field Description array
	 *
	 * @param layoutIdx layout that we want the description for
	 * @return all the descriptions
	 */
	public abstract String[] getFieldDescriptions(final int layoutIdx,
			int columnsToSkip);

	/**
	 * Get the records Description.
	 *
	 * @return The description
	 */
	public abstract String getDescription();

	/**
	 * Get the record-layout name
	 *
	 * @return record layout name
	 */
	public abstract String getLayoutName();

//	/**
//	 * Add a record to the layout
//	 * @param record new record
//	 */
//	public abstract void addRecord(AbstractRecordDetail record);

	/**
	 * get a specific field number
	 *
	 * @param recordNum record number to retrieve
	 *
	 * @return a specific record layout
	 */
	public abstract AbstractRecordDetail getRecord(int recordNum);

	/**
	 * get number of records in the layout
	 *
	 *
	 * @return the number of records in the layout
	 */
	public abstract int getRecordCount();

	/**
	 * get record type
	 *
	 * @return the Record Type
	 */
	public abstract int getLayoutType();


	/**
	 * Get the seperator String
	 *
	 * @return end of line string
	 */
	public abstract String getEolString();

//  Moved to IBasicFileSchema
//
//	/**
//	 * Get the maximum length of the Layout
//	 *
//	 * @return the maximum length
//	 */
//	public abstract int getMaximumRecordLength();


	/**
	 * Get the Index of a specific record (base on name)
	 *
	 * @param recordName record name being searched for
	 *
	 * @return index of the record
	 */
	public abstract int getRecordIndex(String recordName);

	/**
	 * Get the Record Decider class (if present)
	 * @return Returns the record layout decider.
	 */
	public abstract RecordDecider getDecider();

	/**
	 * Get a fields value
	 *
	 * @param record record containg the field
	 * @param type type to use when getting the field
	 * @param field field to retrieve
	 *
	 * @return fields Value
	 */
	public abstract Object getField(final byte[] record, int type, IFieldDetail field);

	/**
	 * Get a field for a supplied field-name
	 *
	 * @param fieldName name of the field being requested
	 *
	 * @return field definition for the supplied name
	 */
	public abstract IFieldDetail getFieldFromName(String fieldName);

	/**
	 /**
	 * This is a function used by the RecordEditor to get a field using
	 * recalculated columns. Basically for XML copybooks,
	 * the End and FollowingText columns
	 * are moved from from 2 and 3 to  the end of the record.
	 * Function probably does not belong here but as good as any spot.
	 *
	 * @param layoutIdx  record index
	 * @param fieldIdx field index
	 * @return requested field
	 */
	public abstract IFieldDetail getAdjField(int layoutIdx, int fieldIdx);

	/**
	 * This is a function used by the RecordEditor to recalculate
	 * columns. Basically for XML copybooks, the End and FollowingText
	 * columns are moved from from 2 and 3 to  the end of the record.
	 * Function probably does not belong here but as good as any spot.
	 *
	 * @param recordIndex record index
	 * @param inColumn input column
	 * @return adjusted column
	 */
	public abstract int getAdjFieldNumber(int recordIndex, int inColumn);

	public abstract int getUnAdjFieldNumber(int recordIndex, int inColumn);

	/**
	 * Wether this is an XML Layout
	 * @return is it an XML layout
	 */
	public abstract boolean isXml();

	/**
	 * Wether it is ok to add Attributes to this layout
	 * @return Wether it is ok to add Attributes to this layout
	 */
	public abstract boolean isOkToAddAttributes();

	/**
	 * determine wether the layout is built or not
	 * @return determine wether the layout is built or not
	 */
	public abstract boolean isBuildLayout();

	/**
	 * check if a Tree Structure has been defined for the layout
	 * i.e. is there a hierarchy between the various layouts
	 * @return wether there is a Tree Structure defined
	 */
	public abstract boolean hasTreeStructure();


	/**
	 * @return the allowChildren
	 */
	public abstract boolean hasChildren();

	/**
	 * Whether layout has Maps (Key / Data sets);
	 * @return Whether layout has Maps (Key / Data sets);
	 */
	public abstract boolean isMapPresent();

	/**
	 * @param allowChildren the allowChildren to set
	 */
	public abstract void setAllowChildren(boolean allowChildren);

	/**
	 * Get Filtered Layout
	 * @param filter layout filter
	 * @return Filtered (Cut down) Layout
	 */
	public AbstractLayoutDetails getFilteredLayout(List<? extends RecordFilter> filter);

	/**
	 * Get Option value
	 * @param option
	 * @return
	 */
	public int getOption(int option);

	/**
	 * Get the value of an attribute
	 * @param attr attribute to get
	 * @return requested attribute value
	 */
	public Object getAttribute(IAttribute attr);


	/**
	 * Set the value of an attribute
	 * @param attr to set
	 * @param value new value for the attribute
	 */
	public void setAttribute(IAttribute attr, Object value);
}